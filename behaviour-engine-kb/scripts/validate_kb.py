#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_kb.py — 资料库机械校验

检查项：
1. 每个条目 id == 文件名、category == 所在目录名；
2. 必填字段非空（id/title/category/version/updated/tags/source/summary）；
3. updated 形如 YYYY-MM-DD；
4. index.json 中每条 content 非空；
5. index.html 无残留占位符，且 <title> 与 manifest 的 kb.name 一致。

用法：托管 python validate_kb.py
退出码：0 = 全部通过；1 = 发现问题。
"""
import os
import re
import sys
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED = ["id", "title", "category", "version", "updated", "tags", "source", "summary"]
FM_RE = re.compile(r"^---\s*$(.*?)^---\s*$", re.DOTALL | re.MULTILINE)
PLACEHOLDERS = ["__ENTRIES__", "__CATS__", "__CAT_LABELS__", "__TITLE__", "__SUBTITLE__", "__GENERATED__", "__TOTAL__"]


def parse_frontmatter(text):
    m = FM_RE.match(text)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    return fm


def main():
    errs = []
    count = 0

    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in {"scripts", "_raw", ".git"}]
        rel = os.path.relpath(dirpath, ROOT)
        top = rel.split(os.sep)[0]
        if not re.match(r"^\d\d-", top):
            continue
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            full = os.path.join(dirpath, fn)
            with open(full, encoding="utf-8") as f:
                fm = parse_frontmatter(f.read())
            if fm is None:
                errs.append("%s: 缺少 frontmatter" % full)
                continue
            count += 1
            stem = os.path.splitext(fn)[0]
            if fm.get("id") != stem:
                errs.append("%s: id=%r != 文件名 %r" % (full, fm.get("id"), stem))
            if fm.get("category") != top:
                errs.append("%s: category=%r != 目录 %r" % (full, fm.get("category"), top))
            for k in REQUIRED:
                if not fm.get(k) or fm.get(k) == "[]":
                    errs.append("%s: 必填字段 %s 为空" % (full, k))
            upd = fm.get("updated", "")
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", upd):
                errs.append("%s: updated 格式异常 %r" % (full, upd))

    print("扫描条目: %d" % count)

    # index.json
    idx_path = os.path.join(ROOT, "index.json")
    if os.path.exists(idx_path):
        with open(idx_path, encoding="utf-8") as f:
            data = json.load(f)
        print("index.json total: %s | by_category: %s" % (data.get("total"), data.get("by_category")))
        if data.get("total") != count:
            errs.append("index.json total(%s) != 实际条目数(%d)" % (data.get("total"), count))
        empty = [e.get("id") for e in data.get("entries", []) if not (e.get("content") or "").strip()]
        if empty:
            errs.append("index.json 正文为空: %s" % ", ".join(empty))
    else:
        errs.append("缺少 index.json（请先运行 build_index.py）")

    # index.html
    html_path = os.path.join(ROOT, "index.html")
    if os.path.exists(html_path):
        with open(html_path, encoding="utf-8") as f:
            html = f.read()
        m = re.search(r"<title>(.*?)</title>", html)
        print("index.html <title>: %s" % (m.group(1) if m else "MISSING"))
        for ph in PLACEHOLDERS:
            if ph in html:
                errs.append("index.html 残留占位符 %s" % ph)
        man = os.path.join(ROOT, "manifest.json")
        if os.path.exists(man):
            with open(man, encoding="utf-8") as f:
                want = json.load(f).get("kb", {}).get("name")
            if want and (not m or m.group(1).strip() != want):
                errs.append("index.html <title> 与 manifest.kb.name 不一致（期望 %r）" % want)
    else:
        errs.append("缺少 index.html（请先运行 build_index.py）")

    print("---")
    print("ERRORS: %d" % len(errs))
    for e in errs:
        print(" -", e)
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
