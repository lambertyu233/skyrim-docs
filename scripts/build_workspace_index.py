#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_workspace_index.py — 生成工作区统一 HTML 预览入口（根目录 index.html）

动机：各资料库各有一个 index.html（内嵌本库全文的离线浏览器），但工作区层面缺少
统一入口——想先看"有哪些库、各库多大"、或跨库搜一个概念时没有落点。

与各库 build_index.py 的分工（刻意不重复造轮子）：
  - 本页只内联**元数据**（标题/摘要/标签/别名/分类/所属库），**不含正文**；
    正文预览与库内检索仍在各库 index.html，本页负责"总览 + 跨库检索 + 跳转"。
    这样本页只有百 KB 级，不会变成第二个"全库正文inline"。
  - 跨库检索命中后跳 `<库>/index.html#id=<条目id>`：各库页面自 2026-10-23 起支持
    该深链（打开即落在条目上，见各库 build_index.py 的 _hashId）。
  - 库发现规则与 sync_scripts.py 一致：工作区下「含 manifest.json 的一级目录」。
  - 条目数据复用 scripts/kb.py 的 load_kbs()（直接读各条目 frontmatter，
    不额外维护清单——清单一多必腐化）。

用法：
  managed python scripts/build_workspace_index.py

新增/删除资料库、或条目增删后都应重跑，否则计数与检索结果是旧快照。
退出码：0 = 成功；1 = 有库缺少 index.html（深链目标缺失）。
"""
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE).replace(os.sep, "/")
sys.path.insert(0, HERE)

import kb as kbmod  # noqa: E402  同目录的工作区检索工具，复用其扫描结果

TITLE = "上古卷轴5 MOD知识库"
# 症状排错索引的深链落点（01-navigation 库的 troubleshooting-index 条目）
TROUBLE_HREF = "01-navigation/index.html#id=troubleshooting-index"


def build_data():
    """扫描全部库 → (库卡片数据, 跨库检索用的条目元数据, 缺失 index.html 的库)。"""
    kbs = kbmod.load_kbs()
    libs, entries, missing = [], [], []
    for name in sorted(kbs):
        k = kbs[name]
        cats = k.get("categories", {})
        used = sorted({e["category"] for e in k["entries"]})
        cat_rows = [{
            "dir": c,
            "title": cats.get(c, {}).get("title", c),
            "n": sum(1 for e in k["entries"] if e["category"] == c),
        } for c in used]
        if not os.path.isfile(os.path.join(ROOT, name, "index.html")):
            missing.append(name)
        libs.append({
            "name": name,
            "title": k["title"],
            "desc": k["desc"],
            "version": k.get("version", ""),
            "entries": len(k["entries"]),
            "cats": cat_rows,
            "href": name + "/index.html",
        })
        for e in k["entries"]:
            entries.append({
                "kb": name,
                "kbTitle": k["title"],
                "id": e["id"],
                "title": e["title"],
                "category": e["category"],
                "catLabel": cats.get(e["category"], {}).get("title", e["category"]),
                "kind": e.get("kind", ""),
                "summary": e.get("summary", ""),
                "tags": e.get("tags", []) or [],
                "aliases": e.get("aliases", []) or [],
                "href": "%s/index.html#id=%s" % (name, e["id"]),
            })
    entries.sort(key=lambda x: (x["kb"], x["category"], x["title"]))
    return libs, entries, missing


def main():
    libs, entries, missing = build_data()
    total = len(entries)
    ncats = sum(len(l["cats"]) for l in libs)
    subtitle = ("%d 个资料库 · %d 条目 · 统一预览与跨库检索："
                "命中后直达对应资料库的条目页" % (len(libs), total))
    # 症状入口只在目标条目真实存在时才渲染（库被删/改名时不留死链）
    trouble = ('<a class="enter" href="%s">遇到问题？从症状查起 →</a>' % TROUBLE_HREF
               if any(e["href"] == TROUBLE_HREF for e in entries) else "")

    html = HTML_TEMPLATE
    html = html.replace("__TITLE__", TITLE)
    html = html.replace("__SUBTITLE__", subtitle)
    html = html.replace("__GENERATED__", datetime.date.today().isoformat())
    html = html.replace("__TROUBLE_LINK__", trouble)
    html = html.replace("__KBS__", json.dumps(libs, ensure_ascii=False).replace("</", "<\\/"))
    html = html.replace("__ENTRIES__", json.dumps(entries, ensure_ascii=False).replace("</", "<\\/"))
    for token in ("__TITLE__", "__SUBTITLE__", "__GENERATED__", "__TROUBLE_LINK__",
                  "__KBS__", "__ENTRIES__"):
        assert token not in html, "占位符未替换：%s" % token

    # newline="" 与各库 build_index 一致：Windows 文本模式会把 \n 写成 \r\n，
    # 与 .gitattributes 的 eol=lf 及 check_links 的「全部为 LF」断言冲突。
    out = os.path.join(ROOT, "index.html")
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(html)

    print("Built workspace index: %d libs / %d entries / %d categories -> %s"
          % (len(libs), total, ncats, out))
    for m in missing:
        print("[warn] %s/index.html 不存在（深链目标缺失），请先跑该库 build_index.py" % m,
              file=sys.stderr)
    return 1 if missing else 0


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>
  :root{
    --bg:#f7f8fa; --panel:#ffffff; --ink:#1f2329; --muted:#6b7280;
    --line:#e5e7eb; --accent:#2563eb; --chip:#eef2ff;
  }
  *{box-sizing:border-box}
  body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"PingFang SC","Microsoft YaHei",sans-serif;
       background:var(--bg);color:var(--ink);font-size:14px;line-height:1.6}
  header{background:linear-gradient(135deg,#1e3a8a,#2563eb);color:#fff;padding:22px 24px}
  header h1{margin:0;font-size:22px}
  header p{margin:6px 0 0;opacity:.9;font-size:13px}
  .stats{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px;align-items:center}
  .stat{background:rgba(255,255,255,.15);padding:4px 10px;border-radius:20px;font-size:12px}
  a.enter{display:inline-block;margin-top:12px;background:#fff;color:#1e3a8a;font-weight:600;
          padding:7px 14px;border-radius:8px;text-decoration:none;font-size:13px}
  a.enter:hover{background:#eff6ff}
  main{max-width:1080px;margin:0 auto;padding:20px 24px 44px}
  .toolbar{margin:18px 0 4px}
  input[type=search]{width:100%;padding:11px 14px;border:1px solid var(--line);border-radius:10px;
                     font-size:14px;background:#fff}
  input[type=search]:focus{outline:2px solid #bfdbfe;border-color:var(--accent)}
  h2.sec{font-size:15px;margin:22px 0 12px}
  h2.sec .n{color:var(--muted);font-weight:400;font-size:12px;margin-left:8px}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
  a.card{display:block;background:var(--panel);border:1px solid var(--line);border-radius:12px;
         padding:14px 16px;text-decoration:none;color:inherit;transition:.15s}
  a.card:hover{box-shadow:0 4px 16px rgba(0,0,0,.08);transform:translateY(-1px);border-color:#bfdbfe}
  a.card h3{margin:0 0 6px;font-size:15px}
  a.card .sum{color:var(--muted);font-size:13px;margin:0 0 8px}
  .chips{display:flex;gap:6px;flex-wrap:wrap}
  .chip{background:var(--chip);color:#3730a3;font-size:11px;padding:2px 8px;border-radius:20px}
  .chip.muted{background:#f3f4f6;color:var(--muted)}
  .chip.kb{background:#ecfdf5;color:#065f46}
  .why{display:inline-block;font-size:11px;color:var(--accent);background:#eff6ff;
       border:1px solid #bfdbfe;border-radius:20px;padding:1px 8px;margin:0 0 8px}
  a.chip.link{text-decoration:none;cursor:pointer}
  a.chip.link:hover{background:#dbeafe;color:#1e3a8a}
  .bridge{margin:0 0 16px;padding:10px 14px;background:#fffbeb;border:1px solid #fde68a;
          border-radius:10px;font-size:12px;color:#92400e}
  .empty{color:var(--muted);padding:30px;text-align:center;background:var(--panel);
         border:1px dashed var(--line);border-radius:12px;grid-column:1/-1}
  .tip{font-size:12px;color:var(--muted);margin-top:26px;line-height:1.9}
  .tip code{background:#f1f5f9;border:1px solid var(--line);border-radius:4px;padding:1px 5px;font-size:11px}
  #results{display:none}
  #results.on{display:block}
  #libs.off{display:none}
</style>
</head>
<body>
<header>
  <h1>__TITLE__</h1>
  <p>__SUBTITLE__</p>
  <div class="stats" id="stats"></div>
  __TROUBLE_LINK__
</header>
<main>
  <div class="toolbar">
    <input type="search" id="q" placeholder="跨库搜索：标题 / 摘要 / 标签 / 别名 / 库名（如：视差、拉弓、DynDOLOD、爆显存）… 回车打开第一个结果；连正文一起搜见结果区的各库入口">
  </div>
  <div id="results">
    <h2 class="sec">跨库检索结果<span class="n" id="rcount"></span></h2>
    <div id="bridge"></div>
    <div class="grid" id="resgrid"></div>
  </div>
  <div id="libs">
    <h2 class="sec">资料库<span class="n" id="libnote"></span></h2>
    <div class="grid" id="libgrid"></div>
    <p class="tip">
      各库页面由各库 <code>scripts/build_index.py</code> 生成，正文预览与库内检索在那里；<br>
      本页由 <code>scripts/build_workspace_index.py</code> 生成于 __GENERATED__，只内联元数据、不含正文。<br>
      命令行跨库检索：<code>python scripts/kb.py find 关键词</code>；
      agent 入口契约见 <a href="AGENTS.md" target="_blank" rel="noopener">AGENTS.md</a>。
    </p>
  </div>
</main>
<script>
const KBS=__KBS__;
const ENTRIES=__ENTRIES__;
const q=document.getElementById('q'), res=document.getElementById('results'),
      libs=document.getElementById('libs'), resgrid=document.getElementById('resgrid'),
      libgrid=document.getElementById('libgrid'), bridge=document.getElementById('bridge');
function esc(s){return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function renderStats(){
  const ncat=KBS.reduce((a,l)=>a+l.cats.length,0);
  document.getElementById('stats').innerHTML=
    '<span class="stat">资料库 '+KBS.length+'</span>'+
    '<span class="stat">条目 '+ENTRIES.length+'</span>'+
    '<span class="stat">分类 '+ncat+'</span>';
  document.getElementById('libnote').textContent=
    '（'+KBS.length+' 个库，点击卡片进入该库的完整索引页）';
}
function renderLibs(){
  let h='';
  for(const l of KBS){
    h+='<a class="card" href="'+esc(l.href)+'"><h3>'+esc(l.title)+'</h3>'+
       '<p class="sum">'+esc(l.desc||'')+'</p>'+
       '<div class="chips" style="margin-bottom:6px">'+
       '<span class="chip">'+l.entries+' 条目</span>'+
       '<span class="chip muted">'+l.cats.length+' 分类</span>'+
       (l.version?'<span class="chip muted">v'+esc(l.version)+'</span>':'')+'</div>'+
       '<div class="chips">'+
       l.cats.map(c=>'<span class="chip muted">'+esc(c.title)+' '+c.n+'</span>').join('')+
       '</div></a>';
  }
  libgrid.innerHTML=h;
}
function scoreOf(e,qq){
  let sc=0;
  if((e.title||'').toLowerCase().includes(qq)) sc+=100;
  if((e.aliases||[]).some(a=>a.toLowerCase().includes(qq))) sc+=60;
  if((e.tags||[]).some(t=>t.toLowerCase().includes(qq))) sc+=40;
  if(e.kbTitle.toLowerCase().includes(qq)||e.kb.toLowerCase().includes(qq)) sc+=30;
  if((e.summary||'').toLowerCase().includes(qq)) sc+=20;
  if((e.catLabel||'').includes(qq)||(e.category||'').includes(qq)) sc+=15;
  return sc;
}
function whyOf(e,qq){
  if((e.aliases||[]).some(a=>a.toLowerCase().includes(qq))) return '别名命中';
  if((e.tags||[]).some(t=>t.toLowerCase().includes(qq))) return '标签命中';
  if((e.title||'').toLowerCase().includes(qq)) return '标题命中';
  if(e.kbTitle.toLowerCase().includes(qq)||e.kb.toLowerCase().includes(qq)) return '库名命中';
  if((e.catLabel||'').includes(qq)||(e.category||'').includes(qq)) return '分类命中';
  return '摘要命中';
}
// 元数据未含正文的兜底桥：本页只内联元数据，「拉弓」这类只出现在正文里的词
// 在这里搜不到——给每个库一条 #q= 预填深链，一键进去做全文检索。
function renderBridge(qq){
  let h='<div class="bridge">上面的命中只来自标题 / 摘要 / 标签 / 别名（本页不内联正文）。'+
        '要连条目正文一起搜，进各库全文检索：<div class="chips" style="margin-top:6px">';
  for(const l of KBS){
    h+='<a class="chip link" href="'+esc(l.href)+'#q='+encodeURIComponent(qq)+'">'+esc(l.name)+'</a>';
  }
  bridge.innerHTML=h+'</div></div>';
}
function search(){
  const qq=q.value.trim().toLowerCase();
  if(!qq){ res.classList.remove('on'); libs.classList.remove('off'); bridge.innerHTML=''; return; }
  renderBridge(qq);
  const hits=ENTRIES.map(e=>({e:e,s:scoreOf(e,qq)})).filter(x=>x.s>0)
    .sort((a,b)=>b.s-a.s||(a.e.kb+a.e.title).localeCompare(b.e.kb+b.e.title,'zh'));
  document.getElementById('rcount').textContent='（'+hits.length+' 条，回车打开第一条）';
  if(!hits.length){
    resgrid.innerHTML='<div class="empty">没有匹配的条目——换个说法（支持别名，如「拉弓」「爆显存」），或直接进下面的资料库页面检索。</div>';
  }else{
    let h='';
    for(const x of hits){
      const e=x.e;
      h+='<a class="card" href="'+esc(e.href)+'">'+
         '<div><span class="why">'+esc(whyOf(e,qq))+'</span></div>'+
         '<h3>'+esc(e.title)+'</h3>'+
         '<div class="chips" style="margin-bottom:6px">'+
         '<span class="chip kb">'+esc(e.kb)+'</span>'+
         '<span class="chip">'+esc(e.catLabel)+'</span>'+
         (e.kind?'<span class="chip muted">'+esc(e.kind)+'</span>':'')+'</div>'+
         '<p class="sum">'+esc(e.summary||'')+'</p>'+
         '<div class="chips">'+
         ((e.tags||[]).slice(0,4).map(t=>'<span class="chip muted">'+esc(t)+'</span>').join(''))+
         '</div></a>';
    }
    resgrid.innerHTML=h;
  }
  res.classList.add('on'); libs.classList.add('off');
}
q.oninput=search;
q.onkeydown=function(ev){
  if(ev.key==='Enter'){ const f=resgrid.querySelector('a.card'); if(f) location.href=f.getAttribute('href'); }
};
renderStats();renderLibs();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    sys.exit(main())
