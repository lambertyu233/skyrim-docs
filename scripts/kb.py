#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kb.py — 工作区知识库检索入口（给 agent / 人用的最小工具）

设计目标：agent 不该为了找一句话读完 296KB 的 index.json。
本工具只返回「定位信息」（路径 / id / 标题 / 摘要 / 大纲），
由调用方自行决定读哪一篇的正文。

用法：
  kb.py list                          # 5 个库的概览
  kb.py toc <kb> [--long]             # 某库的分类地图（--long 带摘要）
  kb.py find <关键词...> [--kb X] [-n 10]   # 跨库检索条目
  kb.py grep <正则> [--kb X] [-n 20]        # 正文精确检索，返回 路径:行号:内容
  kb.py show <id|路径片段>            # 解析到唯一条目：元数据 + 标题大纲
  kb.py read <id|路径片段> [--max 4000]     # 直接打印正文（省一步 Read 工具调用）
  kb.py check                         # 校验 AGENTS.md 是否覆盖了所有库

  ← 任意命令追加 --json 输出结构化结果

零依赖（仅标准库）。数据源始终是各条目的 frontmatter，不额外维护清单。
"""

import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace(os.sep, "/")
SKIP_DIRS = {".workbuddy", "scripts", "_raw", ".git", "OAR"}


# ---------------------------------------------------------------- frontmatter

def parse_frontmatter(text):
    """极简 YAML 子集解析：只认 key: value，值支持 [a, b] 与 'x' / "x"。"""
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        k, v = k.strip(), v.strip()
        if v.startswith("[") and v.endswith("]"):
            meta[k] = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
        else:
            meta[k] = v.strip("'\"")
    return meta, text[m.end():]


def outline(body, levels=(2, 3)):
    """抽 ``` 外的一级/二级标题，给 agent 当目录用。"""
    heads, in_code = [], False
    for line in body.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^(#{2,3})\s+(.*)$", line)
        if m and len(m.group(1)) in levels:
            heads.append(("  " * (len(m.group(1)) - 2)) + m.group(2).strip())
    return heads


# ---------------------------------------------------------------- 扫描

def load_kbs():
    kbs = {}
    for name in sorted(os.listdir(ROOT)):
        mpath = os.path.join(ROOT, name, "manifest.json")
        if not os.path.isfile(mpath):
            continue
        try:
            with open(mpath, encoding="utf-8") as f:
                man = json.load(f)
        except Exception as e:
            print(f"[warn] {name}/manifest.json 解析失败: {e}", file=sys.stderr)
            continue
        cats = {c["dir"]: c for c in man.get("categories", [])}
        if isinstance(man.get("kb"), dict):
            kb_meta = man["kb"]
        else:
            kb_meta = man if isinstance(man, dict) else {}
        entries = []
        for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, name)):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for fn in filenames:
                if not fn.endswith(".md"):
                    continue
                full = os.path.join(dirpath, fn)
                rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
                try:
                    with open(full, encoding="utf-8-sig") as f:
                        raw = f.read()
                except Exception:
                    continue
                meta, body = parse_frontmatter(raw)
                if not meta.get("id"):
                    continue  # 非条目文件（如 CONTRIBUTING.md）
                entries.append({
                    "id": meta.get("id", fn[:-3]),
                    "title": meta.get("title", fn[:-3]),
                    "category": meta.get("category", os.path.basename(dirpath)),
                    "kind": meta.get("kind", ""),
                    "version": meta.get("version", ""),
                    "updated": meta.get("updated", ""),
                    "tags": meta.get("tags", []) or [],
                    "aliases": meta.get("aliases", []) or [],
                    "source": meta.get("source", ""),
                    "summary": meta.get("summary", ""),
                    "path": rel,
                    "body": body,
                })
        entries.sort(key=lambda e: (e["category"], e["id"]))
        kbs[name] = {
            "name": name,
            "title": kb_meta.get("name", name),
            "desc": kb_meta.get("description", ""),
            "version": man.get("version", ""),
            "generated_at": man.get("generated_at", ""),
            "categories": cats,
            "entries": entries,
        }
    return kbs


def all_entries(kbs, only=None):
    for kb_name, kb in kbs.items():
        if only and kb_name != only:
            continue
        for e in kb["entries"]:
            yield kb_name, kb, e


# ---------------------------------------------------------------- 检索

def _squeeze(text):
    """去掉所有空白并转小写。

    中文查询里空格是随意的：「怎么装 mod」「怎么装mod」「怎么装 Mod」是同一句话。
    不归一化的话，别名写成带空格的形式就会漏掉用户的连写输入（实测踩过）。
    """
    return re.sub(r"\s+", "", text.lower())


def _cjk_ngrams(query, lo=2, hi=6):
    """"无空格的中文长查询"切 gram 兜底。

    中文不像英文有词边界：用户输入「光源太多闪烁」是一个 term，
    而条目的别名多半写成更短的「光太多闪烁」——精确相等与"整串作为子串"
    都命中不了。这里把查询切成 2~6 字的滑窗，让库里较短的别名能被包含进来，
    再由下方 score() 按"别名片段命中"给一个较低权重（26 分级），
    既有召回，又不会盖过精确命中。
    """
    q = _squeeze(query)
    grams = set()
    for n in range(lo, hi + 1):
        for i in range(len(q) - n + 1):
            grams.add(q[i:i + n])
    return grams


def score(kb_name, e, terms, query):
    """命中理由可解释：返回 (分数, 理由列表)。

    权重设计：id 精确 > 别名精确 > tag 精确 > 别名模糊 > tag 模糊 > 标题 > 摘要 > 正文。
    别名的存在就是为了兜住"用户/agent 的口头说法与条目标题不一致"——
    例如问 `submod priority`，标题写的是「优先级」，只有别名能命中。
    """
    s, why = 0, []
    tags_l = [t.lower() for t in e["tags"]]
    tags_sq = [_squeeze(t) for t in e["tags"]]
    alias_l = [a.lower() for a in e.get("aliases", [])]
    alias_sq = [_squeeze(a) for a in e.get("aliases", [])]
    title = e["title"].lower()
    title_sq = _squeeze(e["title"])
    idl = e["id"].lower()
    summ = e["summary"].lower()
    summ_sq = _squeeze(e["summary"])
    body = e["body"].lower()
    for t in terms:
        tsq = _squeeze(t)
        if t == idl:
            s += 100
            why.append(f"id={e['id']}")
        # ---- 别名：精确（含去空格归一）> 子串 ----
        if t in alias_l or (tsq and tsq in alias_sq):
            s += 60
            why.append(f"alias:{t}")
        elif any(t in x for x in alias_l) or (tsq and any(tsq in x for x in alias_sq)):
            s += 26
            why.append(f"alias~{t}")
        # ---- tag ----
        if t in tags_l or (tsq and tsq in tags_sq):
            s += 40
            why.append(f"tag:{t}")
        elif any(t in x for x in tags_l) or (tsq and any(tsq in x for x in tags_sq)):
            s += 22
            why.append(f"tag~{t}")
        if t in title or (tsq and tsq in title_sq):
            s += 20
            why.append(f"title:{t}")
        if t in summ or (tsq and tsq in summ_sq):
            s += 8
            why.append(f"summary:{t}")
        if t in body:
            s += 3 * min(body.count(t), 5)
            why.append(f"正文×{body.count(t)}")
    # ---- CJK 长串兜底：查询被切成 gram 后，库里较短的别名能否被"容纳" ----
    gram_terms = terms
    if len(gram_terms) == 1 and len(_squeeze(query)) >= 4:
        qsq = _squeeze(query)
        # 反向包含：别名整体是查询的一段（如查询"光源太多闪烁"含别名"光太多闪烁"）
        for a_sq, a_raw in zip(alias_sq, e.get("aliases", [])):
            if len(a_sq) >= 3 and a_sq in qsq:
                s += 26
                why.append(f"alias~{a_raw}")
                break
        else:
            # 再退一步：别名里有 >=3 字的长片段与查询共享
            for a_sq, a_raw in zip(alias_sq, e.get("aliases", [])):
                if len(a_sq) < 3:
                    continue
                overlap = max(
                    (len(qsq[i:i + n]) for n in range(len(a_sq), 2, -1)
                     for i in range(len(qsq) - n + 1) if qsq[i:i + n] in a_sq),
                    default=0,
                )
                if overlap >= 3:
                    s += 14
                    why.append(f"alias≈{a_raw}")
                    break
    if query and (query.lower() in summ or _squeeze(query) in summ_sq):
        s += 6
    return s, why


def do_find(kbs, query, only=None, limit=10, as_json=False):
    terms = [t.lower() for t in query.split() if t.strip()]
    if not terms:
        return
    hits = []
    for kb_name, kb, e in all_entries(kbs, only):
        s, why = score(kb_name, e, terms, query)
        if s > 0:
            hits.append((s, kb_name, e, why))
    hits.sort(key=lambda x: -x[0])
    hits = hits[:limit]
    if as_json:
        print(json.dumps([{
            "score": s, "kb": k, "id": e["id"], "title": e["title"],
            "category": e["category"], "path": e["path"],
            "summary": e["summary"], "aliases": e.get("aliases", []),
            "why": sorted(set(w)),
        } for s, k, e, w in hits], ensure_ascii=False, indent=2))
        return
    if not hits:
        print("无命中。换个说法，或先跑 `kb.py toc <kb>` 看该库怎么分的类。")
        return
    for s, kb_name, e, why in hits:
        print(f"[{s:>3}] {e['path']}")
        print(f"      {e['title']}  ({e['category']})")
        if e.get("aliases"):
            print(f"      别名  {'、'.join(e['aliases'][:8])}")
        if e["summary"]:
            print(f"      {e['summary'][:110]}")
    print(f"\n下一步：kb.py read <id>  或  Read 对应路径")


def do_grep(kbs, pattern, only=None, limit=20, ctx=0):
    try:
        rx = re.compile(pattern, re.I)
    except re.error as exc:
        print(f"正则不合法: {exc}", file=sys.stderr)
        return
    n = 0
    for kb_name, kb, e in all_entries(kbs, only):
        lines = e["body"].splitlines()
        for i, line in enumerate(lines):
            if rx.search(line):
                n += 1
                if n > limit:
                    print(f"...（已截断，仅显示前 {limit} 条）")
                    return
                print(f"{e['path']}:{i + 1}: {line.strip()[:180]}")
                for c in range(1, ctx + 1):
                    for off in (i + c, i - c):
                        if 0 <= off < len(lines) and lines[off].strip():
                            print(f"    | {lines[off].strip()[:160]}")
                            break
    if n == 0:
        print("正文无命中。")


def do_toc(kbs, kb_name, long=False, as_json=False):
    kb = kbs.get(kb_name)
    if not kb:
        print(f"没有这个库：{kb_name}\n可用：" + ", ".join(kbs), file=sys.stderr)
        sys.exit(1)
    if as_json:
        print(json.dumps({
            "kb": kb["name"], "title": kb["title"], "desc": kb["desc"],
            "version": kb["version"], "generated_at": kb["generated_at"],
            "categories": [
                {"dir": c, "title": kb["categories"].get(c, {}).get("title", ""),
                 "entries": [{"id": e["id"], "title": e["title"], "summary": e["summary"],
                              "path": e["path"]}
                             for e in kb["entries"] if e["category"] == c]}
                for c in sorted({e["category"] for e in kb["entries"]})
            ]}, ensure_ascii=False, indent=2))
        return
    print(f"{kb['title']}  [{kb['name']}]  v{kb['version']} · {kb['generated_at']}"
          f" · {len(kb['entries'])} 条目")
    for c in sorted({e["category"] for e in kb["entries"]}):
        label = kb["categories"].get(c, {}).get("title", "")
        rows = [e for e in kb["entries"] if e["category"] == c]
        print(f"\n{c}  {label}  ({len(rows)})")
        for e in rows:
            print(f"  {e['id']:<32} {e['title']}")
            if long and e["summary"]:
                print(f"  {'':<32} └ {e['summary'][:100]}")


def resolve(kbs, needle):
    nl = needle.lower().replace("\\", "/")
    exact, partial = [], []
    for kb_name, kb, e in all_entries(kbs):
        if nl == e["id"].lower():
            exact.append((kb_name, e))
        elif nl in e["id"].lower() or nl in e["path"].lower() or nl in e["title"].lower():
            partial.append((kb_name, e))
    return exact or partial


def do_show(kbs, needle, do_read=False, max_chars=4000, as_json=False):
    hits = resolve(kbs, needle)
    if not hits:
        print(f"解析不到条目：{needle}", file=sys.stderr)
        sys.exit(1)
    if len(hits) > 1:
        ids = {e["id"] for _, e in hits}
        if len(ids) > 1:
            print(f"命中 {len(hits)} 条，请给更精确的 id：")
            for kb_name, e in hits[:15]:
                print(f"  {e['id']:<34} {e['title']}")
            sys.exit(2)
    kb_name, e = hits[0]
    if as_json:
        print(json.dumps({
            "kb": kb_name, "id": e["id"], "title": e["title"], "category": e["category"],
            "kind": e["kind"], "version": e["version"], "updated": e["updated"],
            "tags": e["tags"], "aliases": e.get("aliases", []),
            "source": e["source"], "summary": e["summary"],
            "path": e["path"], "outline": outline(e["body"]),
            "body": e["body"] if do_read else None,
        }, ensure_ascii=False, indent=2))
        return
    full = ROOT + "/" + e["path"]
    print(f"# {e['title']}   (id={e['id']})")
    print(f"路径   {e['path']}")
    print(f"分类   {e['category']} · kind={e['kind']} · v{e['version']} · 更新 {e['updated']}")
    if e["tags"]:
        print(f"标签   {', '.join(e['tags'])}")
    if e.get("aliases"):
        print(f"别名   {', '.join(e['aliases'])}")
    if e["summary"]:
        print(f"摘要   {e['summary']}")
    if e["source"]:
        print(f"来源   {e['source']}")
    heads = outline(e["body"])
    if heads and not do_read:
        print("\n大纲（决定读不读 / 读哪一段）")
        for h in heads:
            print(f"  {h}")
        print(f"\n正文全文：Read {full}")
        return
    body = e["body"]
    if len(body) > max_chars:
        body = body[:max_chars] + f"\n...（截断，完整走 Read {full}）"
    print("\n" + body)


def do_list(kbs, as_json=False):
    if as_json:
        print(json.dumps([{
            "kb": k["name"], "title": k["title"], "desc": k["desc"],
            "version": k["version"], "generated_at": k["generated_at"],
            "entries": len(k["entries"]),
            "categories": len({e["category"] for e in k["entries"]}),
        } for k in kbs.values()], ensure_ascii=False, indent=2))
        return
    total = sum(len(k["entries"]) for k in kbs.values())
    for k in kbs.values():
        cats = len({e["category"] for e in k["entries"]})
        print(f"{k['name']:<22} {len(k['entries']):>3} 条目 / {cats:>2} 分类   v{k['version']}  {k['title']}")
        print(f"{'':<22} {k['desc'][:76]}")
    print(f"\n共 {len(kbs)} 库 / {total} 条目。")


def do_check(kbs):
    """AGENTS.md 必须覆盖所有库，否则 agent 会漏掉整个知识库。"""
    path = os.path.join(ROOT, "AGENTS.md")
    if not os.path.isfile(path):
        print("✗ 缺少根目录 AGENTS.md —— agent 无法自动发现这些知识库")
        return 1
    with open(path, encoding="utf-8") as f:
        text = f.read()
    missing = [n for n in kbs if n not in text]
    if missing:
        print("✗ 以下库未在 AGENTS.md 中被提及：" + ", ".join(missing))
        return 1
    print(f"✓ AGENTS.md 覆盖全部 {len(kbs)} 个库，共 {sum(len(k['entries']) for k in kbs.values())} 条目")
    return 0


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description="工作区知识库检索入口", add_help=True)
    sub = ap.add_subparsers(dest="cmd")

    p = sub.add_parser("list", help="库概览")
    p.add_argument("--json", action="store_true")

    p = sub.add_parser("toc", help="某库的分类地图")
    p.add_argument("kb")
    p.add_argument("--long", action="store_true", help="附摘要")
    p.add_argument("--json", action="store_true")

    p = sub.add_parser("find", help="跨库检索条目")
    p.add_argument("query", nargs="+")
    p.add_argument("--kb")
    p.add_argument("-n", type=int, default=10)
    p.add_argument("--json", action="store_true")

    p = sub.add_parser("grep", help="正文精确检索")
    p.add_argument("pattern")
    p.add_argument("--kb")
    p.add_argument("-n", type=int, default=20)
    p.add_argument("-C", type=int, default=0, help="附上下文行")

    p = sub.add_parser("show", help="元数据 + 大纲")
    p.add_argument("needle")
    p.add_argument("--json", action="store_true")

    p = sub.add_parser("read", help="连正文一起打印")
    p.add_argument("needle")
    p.add_argument("--max", type=int, default=4000)

    p = sub.add_parser("check", help="自检 AGENTS.md 覆盖度")

    args = ap.parse_args()
    if not args.cmd:
        ap.print_help()
        return 0

    kbs = load_kbs()
    if args.cmd == "list":
        do_list(kbs, getattr(args, "json", False))
    elif args.cmd == "toc":
        do_toc(kbs, args.kb, args.long, args.json)
    elif args.cmd == "find":
        do_find(kbs, " ".join(args.query), args.kb, args.n, args.json)
    elif args.cmd == "grep":
        do_grep(kbs, args.pattern, args.kb, args.n, args.C)
    elif args.cmd == "show":
        do_show(kbs, args.needle, False, as_json=args.json)
    elif args.cmd == "read":
        do_show(kbs, args.needle, True, args.max)
    elif args.cmd == "check":
        return do_check(kbs)
    return 0


if __name__ == "__main__":
    sys.exit(main())
