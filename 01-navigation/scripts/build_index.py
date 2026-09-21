#!/usr/bin/env python3
# 通用：扫描全部条目 frontmatter → index.json + 离线浏览器 index.html（两栏布局 + 内联全文）。
# 用法：把本文件放到资料库的 scripts/ 下，运行 `python scripts/build_index.py`
# 说明：标题/副标题从 manifest.json 的 kb.name / kb.description 注入；分类中文名从 manifest 的 categories 读取。
import os, re, json, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IGNORE_DIRS = {"scripts", "_raw"}
IGNORE_FILES = {
    "README.md", "CHANGELOG.md", "CONTRIBUTING.md",
    "manifest.json", "index.json", "index.html",
}
FM_RE = re.compile(r"^---\s*$(.*?)^---\s*$", re.DOTALL | re.MULTILINE)


def parse_frontmatter(text):
    m = FM_RE.match(text)
    if not m:
        return None
    block = m.group(1)
    fm = {}
    for line in block.splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        k = k.strip()
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            inner = v[1:-1].strip()
            arr = [x.strip().strip('"').strip("'") for x in inner.split(",") if x.strip()]
            fm[k] = arr
        elif v.startswith("[") and "]" not in v:
            # YAML 数组折行：从本行起累积，直到出现 ']'
            buf = [v]
            while "]" not in buf[-1]:
                nxt = f.readline()
                if not nxt:
                    break
                buf.append(nxt.strip())
            inner = " ".join(buf)
            inner = inner[1:inner.rindex("]")]
            arr = [x.strip().strip('"').strip("'") for x in inner.split(",") if x.strip()]
            fm[k] = arr
        else:
            fm[k] = v.strip('"').strip("'")
    return fm


def _esc_html(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _inline(text):
    """行内元素：代码、链接、删除线、粗体、斜体。"""
    text = _esc_html(text)
    stash = []
    def _code(m):
        stash.append(m.group(1))
        return "\x00%d\x00" % (len(stash) - 1)
    text = re.sub(r"`([^`]+)`", _code, text)
    def _link(m):
        url = m.group(2).replace('"', "%22")
        return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (url, m.group(1))
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", _link, text)
    text = re.sub(r"~~([^~]+)~~", r"<del>\1</del>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"__([^_]+)__", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"(?<!_)_([^_]+)_(?!_)", r"<em>\1</em>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: "<code>%s</code>" % stash[int(m.group(1))], text)
    return text


def _build_list(items, i, base_indent):
    """把同级列表项递归渲染为 <ul>/<ol>，支持任意层级嵌套。"""
    ordered = items[i][1]
    parts = []
    n = len(items)
    while i < n and items[i][0] == base_indent:
        _, _, content = items[i]
        li = [_inline(content)]
        i += 1
        if i < n and items[i][0] > base_indent:
            sub_html, i = _build_list(items, i, items[i][0])
            li.append(sub_html)
        parts.append("<li>%s</li>" % "".join(li))
    tag = "ol" if ordered else "ul"
    return "<%s>%s</%s>" % (tag, "".join(parts), tag), i


def _is_block_start(line):
    if re.match(r"^#{1,6}\s", line): return True
    if re.match(r"^\s*[-*+]\s+", line) or re.match(r"^\s*\d+\.\s+", line): return True
    if line.lstrip().startswith(">"): return True
    if re.match(r"^```", line): return True
    if re.match(r"^(---|\*\*\*|___)\s*$", line): return True
    if "|" in line: return True
    return False


def md_to_html(md):
    """极简 Markdown -> HTML（纯标准库，覆盖标题/列表/表格/代码块/引用/段落）。"""
    lines = md.split("\n")
    n = len(lines)
    out = []
    i = 0
    while i < n:
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        m = re.match(r"^```(\w*)\s*$", line)
        if m:
            i += 1
            code = []
            while i < n and not lines[i].startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            out.append('<pre class="code"><code>%s</code></pre>' % _esc_html("\n".join(code)))
            continue
        if stripped.startswith(">"):
            quote = []
            while i < n and lines[i].lstrip().startswith(">"):
                quote.append(lines[i].lstrip()[1:].strip())
                i += 1
            out.append("<blockquote>%s</blockquote>" % _inline(" ".join(quote)))
            continue
        if "|" in line and i + 1 < n and re.match(r"^\s*\|?[\s:\-|]+\|?\s*$", lines[i+1]) and "-" in lines[i+1]:
            header_cells = [c.strip() for c in stripped.strip("|").split("|")]
            aligns = []
            for c in lines[i+1].strip().strip("|").split("|"):
                c = c.strip()
                lft, rgt = c.startswith(":"), c.endswith(":")
                aligns.append("center" if lft and rgt else "right" if rgt else "left" if lft else "")
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            th = "".join('<th style="text-align:%s">%s</th>' % (a or "left", _inline(c)) for c, a in zip(header_cells, aligns))
            body = "".join(
                "<tr>%s</tr>" % "".join('<td style="text-align:%s">%s</td>' % (a or "left", _inline(c)) for c, a in zip(r, aligns))
                for r in rows
            )
            out.append('<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (th, body))
            continue
        if re.match(r"^\s*[-*+]\s+", line) or re.match(r"^\s*\d+\.\s+", line):
            items = []
            base_ordered = None
            while i < n:
                l = lines[i]
                if not l.strip():
                    j = i + 1
                    while j < n and not lines[j].strip():
                        j += 1
                    if j < n:
                        nxt = lines[j]
                        nxt_list = bool(re.match(r"^\s*[-*+]\s+", nxt) or re.match(r"^\s*\d+\.\s+", nxt))
                        nxt_ord = bool(re.match(r"^\s*\d+\.\s+", nxt))
                        if nxt_list and base_ordered is not None and nxt_ord == base_ordered:
                            i = j
                            continue
                    break
                if re.match(r"^\s*[-*+]\s+", l) or re.match(r"^\s*\d+\.\s+", l):
                    indent = len(l) - len(l.lstrip(" "))
                    ordered = bool(re.match(r"^\s*\d+\.\s+", l))
                    if base_ordered is None:
                        base_ordered = ordered
                    content = re.sub(r"^\s*([-*+]|\d+\.)\s+", "", l)
                    items.append((indent, ordered, content))
                    i += 1
                else:
                    break
            html_list, _ = _build_list(items, 0, items[0][0])
            out.append(html_list)
            continue
        hm = re.match(r"^(#{1,6})\s+(.*)$", line)
        if hm:
            lvl = len(hm.group(1))
            out.append("<h%d>%s</h%d>" % (lvl, _inline(hm.group(2).rstrip("#").strip()), lvl))
            i += 1
            continue
        if re.match(r"^(---|\*\*\*|___)\s*$", line):
            out.append("<hr>")
            i += 1
            continue
        para = [line]
        i += 1
        while i < n and lines[i].strip() and not _is_block_start(lines[i]):
            para.append(lines[i])
            i += 1
        out.append("<p>%s</p>" % _inline(" ".join(s.strip() for s in para)))
    return "\n".join(out)


def _strip_leading_h1(html):
    """剥掉正文开头的 # 标题 H1（详情面板已单独显示标题，避免重复）。"""
    html = html.strip()
    m = re.match(r"^<h1>(.*?)</h1>\s*", html, re.DOTALL)
    if m:
        return html[m.end():].strip()
    return html


def main():
    entries = []
    cats = {}
    cat_labels = {}
    title = "资料库"
    subtitle = "可维护 · 分层 · 版本化 · 协作更新"

    manifest_path = os.path.join(ROOT, "manifest.json")
    if os.path.exists(manifest_path):
        try:
            with open(manifest_path, encoding="utf-8") as f:
                mdata = json.load(f)
            kb = mdata.get("kb", {})
            title = kb.get("name", title)
            src = kb.get("source_name", "")
            desc = kb.get("description", "")
            subtitle = (("基于 " + src + " 整理 · " if src else "") + desc) or subtitle
            for c in mdata.get("categories", []):
                cat_labels[c.get("dir")] = c.get("title", c.get("dir"))
        except Exception:
            pass

    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel = os.path.relpath(dirpath, ROOT)
        top = rel.split(os.sep)[0]
        if top in IGNORE_DIRS:
            continue
        # 根目录只放 manifest / index / README 这类文件；条目一律进分类子目录。
        # 这里用「正好等于库根」来判定，而不是隐式依赖 rel == "." 之后才切 top，
        # 否则一旦有人把条目写在库根层，会被静默丢掉（构建显示 0 entries 也不报错）。
        is_root = (rel == ".")
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            if fn in IGNORE_FILES:
                continue
            full = os.path.join(dirpath, fn)
            with open(full, encoding="utf-8") as f:
                text = f.read()
            fm = parse_frontmatter(text)
            if not fm:
                continue
            # 抽取 frontmatter 之后的正文，渲染为排版好的 HTML 内联进详情面板
            m = FM_RE.match(text)
            body = text[m.end():].strip() if m else text.strip()
            fm["content"] = _strip_leading_h1(md_to_html(body))
            category = fm.get("category", "" if is_root else top)
            if not category:
                # 根层条目必须自己声明 category，否则分类标签会变空
                continue
            fm["_file"] = os.path.relpath(full, ROOT).replace("\\", "/")
            fm["_chars"] = len(text)
            entries.append(fm)
            cats[category] = cats.get(category, 0) + 1

    entries.sort(key=lambda e: (e.get("category", ""), e.get("title", "")))
    data = {
        "generated": datetime.date.today().isoformat(),
        "total": len(entries),
        "by_category": dict(sorted(cats.items())),
        "entries": entries,
    }
    # newline="" 必须显式传：默认文本模式在 Windows 上会把 "\n" 静默转成 "\r\n"，
    # 导致同一份产物在不同平台字节不同，且与 check_links.py 的「全部为 LF」断言冲突。
    with open(os.path.join(ROOT, "index.json"), "w", encoding="utf-8", newline="") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    html = HTML_TEMPLATE
    html = html.replace("__ENTRIES__", json.dumps(entries, ensure_ascii=False).replace("</", "<\\/"))
    html = html.replace("__CATS__", json.dumps(data["by_category"], ensure_ascii=False))
    html = html.replace("__CAT_LABELS__", json.dumps(cat_labels, ensure_ascii=False))
    html = html.replace("__TITLE__", title)
    html = html.replace("__SUBTITLE__", subtitle)
    html = html.replace("__GENERATED__", data["generated"])
    html = html.replace("__TOTAL__", str(len(entries)))
    assert "__ENTRIES__" not in html and "__CATS__" not in html and "__CAT_LABELS__" not in html, "占位符未替换！"
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8", newline="") as f:
        f.write(html)

    print(f"Built: {len(entries)} entries, categories={data['by_category']}")


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>
  :root{
    --bg:#f7f8fa; --panel:#ffffff; --ink:#1f2329; --muted:#6b7280;
    --line:#e5e7eb; --accent:#2563eb; --accent2:#0ea5e9; --chip:#eef2ff;
    --green:#16a34a; --amber:#d97706; --gray:#9ca3af; --blue:#2563eb;
  }
  *{box-sizing:border-box}
  body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"PingFang SC","Microsoft YaHei",sans-serif;
       background:var(--bg);color:var(--ink);font-size:14px;line-height:1.6}
  header{background:linear-gradient(135deg,#1e3a8a,#2563eb);color:#fff;padding:20px 24px}
  header h1{margin:0;font-size:20px}
  header p{margin:6px 0 0;opacity:.9;font-size:13px}
  .stats{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
  .stat{background:rgba(255,255,255,.15);padding:4px 10px;border-radius:20px;font-size:12px}
  .wrap{display:flex;min-height:calc(100vh - 116px)}
  aside{width:230px;flex:0 0 230px;background:var(--panel);border-right:1px solid var(--line);padding:16px;overflow:auto;
        transition:width .16s ease,flex-basis .16s ease}
  aside.collapsed{width:78px;flex:0 0 78px;padding:14px 10px}
  aside.collapsed .sidehead{flex-direction:column;gap:8px;align-items:stretch;margin:0}
  aside.collapsed .sidehead-title{display:none}
  aside.collapsed .navtoggle{padding:6px 4px;width:100%}
  .sidehead{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:8px}
  .sidehead-title{font-size:12px;color:var(--muted);white-space:nowrap}
  .navtoggle{background:none;border:1px solid var(--line);border-radius:6px;color:var(--muted);
             font-size:11px;padding:2px 8px;cursor:pointer;line-height:1.5;white-space:nowrap}
  .navtoggle:hover{color:var(--accent);border-color:var(--accent)}
  #navbox.hidden{display:none}
  main{flex:1;padding:20px 24px;overflow:auto}
  .toolbar{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-bottom:14px}
  input[type=search]{flex:1;min-width:200px;padding:9px 12px;border:1px solid var(--line);border-radius:8px;font-size:14px}
  select{padding:9px 10px;border:1px solid var(--line);border-radius:8px;background:#fff}
  .navbtn{display:block;width:100%;text-align:left;padding:8px 10px;margin-bottom:4px;border:1px solid transparent;
          background:none;border-radius:8px;cursor:pointer;color:var(--ink);font-size:13px}
  .navbtn:hover{background:var(--chip)}
  .navbtn.active{background:var(--accent);color:#fff}
  .navbtn .cnt{float:right;opacity:.7;font-size:12px}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px}
  .card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px;cursor:pointer;transition:.15s}
  .card:hover{box-shadow:0 4px 16px rgba(0,0,0,.08);transform:translateY(-1px)}
  .card h3{margin:0 0 6px;font-size:15px}
  .card .sum{color:var(--muted);font-size:13px;margin:0 0 8px}
  .card .why{display:inline-block;font-size:11px;color:var(--accent);background:#eff6ff;
    border:1px solid #bfdbfe;border-radius:20px;padding:1px 8px;margin:0 0 8px}
  .chips{display:flex;gap:6px;flex-wrap:wrap}
  .chip{background:var(--chip);color:#3730a3;font-size:11px;padding:2px 8px;border-radius:20px}
  .chip.muted{background:#f3f4f6;color:var(--muted)}
  .detail{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:22px;max-width:880px}
  .detail h2{margin-top:0}
  .back{background:none;border:1px solid var(--line);border-radius:8px;padding:6px 12px;cursor:pointer;margin-bottom:12px}
  .actions{display:flex;gap:10px;flex-wrap:wrap;margin:16px 0}
  .btn{display:inline-block;padding:9px 14px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:600}
  .btn-primary{background:var(--accent);color:#fff}
  .btn-ghost{border:1px solid var(--line);color:var(--accent)}
  a{color:var(--accent)}
  .empty{color:var(--muted);padding:30px;text-align:center}
  .tip{font-size:12px;color:var(--muted);margin-top:8px}
  .article{background:#fff;border:1px solid var(--line);border-radius:10px;padding:8px 22px 18px;
    font-size:14.5px;line-height:1.8;color:var(--ink);max-width:860px}
  .article h1,.article h2,.article h3,.article h4{line-height:1.35;margin:1.1em 0 .5em}
  .article h1{font-size:1.55em;border-bottom:2px solid var(--line);padding-bottom:.3em}
  .article h2{font-size:1.3em;border-bottom:1px solid var(--line);padding-bottom:.25em}
  .article h3{font-size:1.12em}
  .article p{margin:.6em 0}
  .article ul,.article ol{margin:.5em 0;padding-left:1.6em}
  .article li{margin:.25em 0}
  .article a{color:var(--accent);text-decoration:underline}
  .article code{background:#f1f5f9;border:1px solid var(--line);border-radius:4px;padding:1px 5px;
    font-family:"SFMono-Regular",Consolas,Menlo,monospace;font-size:.92em;color:#be123c}
  .article pre.code{background:#0f172a;color:#e2e8f0;border-radius:10px;padding:14px 16px;overflow:auto;
    font-family:"SFMono-Regular",Consolas,Menlo,monospace;font-size:13px;line-height:1.6}
  .article pre.code code{background:none;border:none;color:inherit;padding:0}
  .article blockquote{margin:.7em 0;padding:.5em 1em;border-left:4px solid var(--accent);
    background:#f8fafc;color:#374151;border-radius:0 8px 8px 0}
  .article table{border-collapse:collapse;width:100%;margin:.8em 0;font-size:13.5px}
  .article th,.article td{border:1px solid var(--line);padding:7px 10px}
  .article thead th{background:#f1f5f9;font-weight:600}
  .article tbody tr:nth-child(even){background:#fafafa}
  .article hr{border:none;border-top:1px solid var(--line);margin:1.2em 0}
</style>
</head>
<body>
<header>
  <h1>__TITLE__</h1>
  <p>__SUBTITLE__</p>
  <div class="stats" id="stats"></div>
</header>
<div class="wrap">
  <aside>
    <div class="sidehead">
      <span class="sidehead-title">分类过滤</span>
      <button id="navtoggle" class="navtoggle" type="button" aria-expanded="true"
              aria-controls="navbox" title="收起/展开分类过滤">‹ 收起</button>
    </div>
    <div id="navbox">
      <button class="navbtn active" data-cat="all" type="button">全部 <span class="cnt" id="allcnt"></span></button>
      <div id="catnav"></div>
    </div>
  </aside>
  <main>
    <div class="toolbar">
      <input type="search" id="q" placeholder="搜索标题、摘要、标签、分类…">
      <select id="sort">
        <option value="cat">按分类</option>
        <option value="title">按标题</option>
        <option value="updated">按更新时间</option>
      </select>
    </div>
    <div id="view"></div>
  </main>
</div>
<script>
const ENTRIES = __ENTRIES__;
const CATS = __CATS__;
const CAT_LABELS = __CAT_LABELS__;
let curCat='all', curQ='', sortBy='cat';

function label(cat){ return CAT_LABELS[cat] || cat; }
function esc(s){return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}

function filtered(){
  const q=curQ.toLowerCase();
  return ENTRIES.filter(e=>{
    if(curCat!=='all' && e.category!==curCat) return false;
    if(q){
      const hay=(e.title+' '+(e.summary||'')+' '+(e.tags||[]).join(' ')+' '+
        (e.aliases||[]).join(' ')+' '+(e.category||'')+' '+label(e.category)).toLowerCase();
      if(!hay.includes(q)) return false;
    }
    return true;
  });
}
// 记录每条命中的原因：优先展示比标题更具体的匹配证据（别名 / 标签 / 正文）
function showWhy(e){
  const q=curQ.toLowerCase(); if(!q) return '';
  if((e.aliases||[]).some(a=>a.toLowerCase().includes(q))) return '别名命中';
  if((e.tags||[]).some(t=>t.toLowerCase().includes(q))) return '标签命中';
  const t=(e.title||'').toLowerCase();
  if(t.includes(q)) return '标题命中';
  if((e.summary||'').toLowerCase().includes(q)) return '摘要命中';
  return '正文提及';
}
function sortEntries(list){
  if(sortBy==='title') return list.sort((a,b)=>(a.title||'').localeCompare(b.title||'','zh'));
  if(sortBy==='updated') return list.sort((a,b)=>(b.updated||'').localeCompare(a.updated||''));
  return list; // cat：本已按 category 预排序
}
function renderGrid(){
  const list=sortEntries(filtered());
  const view=document.getElementById('view');
  if(!list.length){view.innerHTML='<div class="empty">没有匹配的条目</div>';return;}
  let html='<div class="grid">';
  for(const e of list){
    const why=showWhy(e);
    html+='<div class="card" data-id="'+esc(e.id)+'"><h3>'+esc(e.title)+'</h3>'+
      (why?'<div><span class="why">'+esc(why)+'</span></div>':'')+
      '<div class="chips" style="margin-bottom:6px">'+
      '<span class="chip">'+esc(label(e.category))+'</span>'+
      (e.kind?'<span class="chip muted">'+esc(e.kind)+'</span>':'')+'</div>'+
      '<p class="sum">'+esc(e.summary||'')+'</p>'+
      '<div class="chips">'+((e.tags||[]).slice(0,4).map(t=>'<span class="chip">'+esc(t)+'</span>').join(''))+'</div></div>';
  }
  html+='</div>';
  view.innerHTML=html;
  view.querySelectorAll('.card').forEach(c=>c.onclick=()=>showDetail(c.dataset.id));
}
function showDetail(id){
  const e=ENTRIES.find(x=>x.id===id); if(!e) return;
  const view=document.getElementById('view');
  const src=e.source?'<a class="btn btn-ghost" href="'+esc(e.source)+'" target="_blank" rel="noopener">官方来源 ↗</a>':'';
  const file=e._file?'<a class="btn btn-primary" href="'+esc(e._file)+'" target="_blank" rel="noopener">打开本地 .md →</a>':'';
  const tags=((e.tags||[]).map(t=>'<span class="chip">'+esc(t)+'</span>').join(''));
  const als=((e.aliases||[]).length?
    '<div class="chips" style="margin:6px 0 0">'+
    (e.aliases||[]).map(a=>'<span class="chip muted">'+esc(a)+'</span>').join('')+'</div>':'');
  view.innerHTML='<button class="back" onclick="renderGrid()">← 返回列表</button>'+
    '<div class="detail"><h2>'+esc(e.title)+'</h2>'+
    '<div class="chips" style="margin-bottom:4px">'+
    '<span class="chip">'+esc(label(e.category))+'</span>'+
    (e.kind?'<span class="chip muted">'+esc(e.kind)+'</span>':'')+
    (e.version?'<span class="chip muted">v'+esc(e.version)+'</span>':'')+
    (e.updated?'<span class="chip muted">'+esc(e.updated)+'</span>':'')+'</div>'+
    '<div class="chips" style="margin:6px 0 10px">'+tags+'</div>'+
    '<div class="article">'+(e.content||'<p>(暂无正文)</p>')+'</div>'+
    '<div class="actions">'+file+src+'</div>'+
    als+
    '<p class="tip">源文件：'+esc(e._file||'')+'</p></div>';
  document.querySelector('main').scrollTop=0;
}
function selectCat(cat,btn){
  curCat=cat;
  document.querySelectorAll('[data-cat]').forEach(x=>x.classList.remove('active'));
  const target=btn||document.querySelector('#navbox .navbtn[data-cat="'+cat+'"]');
  if(target) target.classList.add('active');
  renderGrid();
}
function setNavCollapsed(collapsed){
  const box=document.getElementById('navbox'), btn=document.getElementById('navtoggle'), side=document.querySelector('aside');
  box.classList.toggle('hidden',collapsed);
  if(side) side.classList.toggle('collapsed',collapsed);
  btn.textContent=collapsed?'展开 ›':'‹ 收起';
  btn.setAttribute('aria-expanded',String(!collapsed));
  try{localStorage.setItem('kb-nav-collapsed',collapsed?'1':'0');}catch(e){}
}
function toggleNav(){
  setNavCollapsed(document.getElementById('navbox').classList.contains('hidden')===false);
}
function renderNav(){
  const nav=document.getElementById('catnav');
  nav.innerHTML=Object.keys(CATS).map(c=>'<button class="navbtn" data-cat="'+c+'">'+esc(label(c))+' <span class="cnt">'+CATS[c]+'</span></button>').join('');
  // 注意：侧栏「全部」按钮和分类按钮必须在这里统一绑定。
  // 只选 [data-cat]（即分类按钮），避开同处 #navbox 内的状态过滤按钮，
  // 否则「全部」按钮会漏绑 → 选中某分类后切不回全部（历史 bug）。
  document.querySelectorAll('#navbox .navbtn[data-cat]').forEach(b=>b.onclick=()=>selectCat(b.dataset.cat,b));
}
function renderStats(){
  const s=document.getElementById('stats');
  const total=ENTRIES.length;
  document.getElementById('allcnt').textContent=total;
  let h='<span class="stat">共 '+total+' 条</span>';
  for(const c in CATS) h+='<span class="stat">'+esc(label(c))+': '+CATS[c]+'</span>';
  s.innerHTML=h;
}
document.getElementById('q').oninput=e=>{curQ=e.target.value;renderGrid();};
document.getElementById('sort').onchange=e=>{sortBy=e.target.value;renderGrid();};
document.getElementById('navtoggle').onclick=toggleNav;
renderStats();renderNav();renderGrid();
// 恢复上次的收起/展开状态
(function(){
  let collapsed=false;
  try{collapsed=localStorage.getItem('kb-nav-collapsed')==='1';}catch(e){}
  if(collapsed) setNavCollapsed(true);
})();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    main()
