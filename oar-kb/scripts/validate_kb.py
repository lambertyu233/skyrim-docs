#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_kb.py — 资料库机械校验（结构 + 索引 + 索引页模板）

检查项：
1. 每个条目 id == 文件名；category 与所在目录名**严格相等**（如 02-features）；
2. 必填字段非空（id/title/category/version/updated/tags/source/summary）；
3. updated 形如 YYYY-MM-DD；
4. 每个有条目的目录都在 manifest.categories 里声明过（否则页面分类标签会渲染成空）；
5. index.json 条目数与磁盘一致；若该库内联正文，则每条 content 非空；
6. index.html 无残留占位符，<title> 与 manifest 的 kb.name 一致；
7. index.html 含升级后的侧栏结构（id="navbox" / id="navtoggle"），且不含已删除的冗余说明；
8. 可选字段 aliases（检索别名）：必须是数组、无重复、不与自身 tags/id 重复
   —— 别名是 agent/用户提问词与条目标题之间的桥梁，写脏了会让检索悄悄失准。

历史教训：早期本脚本允许 category 写成省略 `NN-` 前缀的短名（如 `features`），
结果某个库的 47 个条目真的写成 `category: features`，而 build_index.py 会采用
frontmatter 的值去查分类标签 → 页面上分类名与标签变空，却一路绿灯通过校验。
现改为严格相等 + manifest 目录交叉校验，两头都堵住。

兼容说明：不同时期生成的资料库 index.json 结构略有差异
（新版含 total / by_category / 内联 content；旧版为 meta + entries 且不内联正文），
本脚本按实际存在的字段决定检查范围，避免对旧库误报。

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
# 索引页模板必须包含的结构（缺失说明模板被改坏/回退到了出问题的旧版）
REQUIRED_PAGE_IDS = ["navbox", "navtoggle"]
# 可选字段 aliases（检索别名）：不填合法，填了就要干净
OPTIONAL_FM_LIST = ["aliases"]
# 各库必须存在的 stock 脚本副本由 scripts/sync_scripts.py 统一核对指纹；
# 这里只做「存在性」层面的把关（脚本本身不属于条目，不查内容）
STOCK_SCRIPTS = ["build_index.py", "validate_kb.py", "check_index_ui.py", "check_links.py", "fix_links.py"]
# 已在 1.0.1 删除的冗余文案，不应再出现
REMOVED_TEXTS = ["正文已渲染为排版好的文章"]
# 库根层的非条目文件（文档性文件，不参与条目校验；与 build_index.py 的 IGNORE_FILES 对齐）
ROOT_NON_ENTRY_FILES = {
    "README.md", "CHANGELOG.md", "CONTRIBUTING.md", "AGENTS.md", "LICENSE.md",
}


def parse_fm_list(raw_value):
    """把 frontmatter 里的数组值解析成列表。

    兼容两种写法：
      tags: [a, b, c]
      tags: [a, b,
             c]
    （折行数组需要按行累积才能拿到完整内容）
    """
    v = (raw_value or "").strip()
    if not v.startswith("["):
        return []
    v = v.replace("\n", " ")
    if "]" in v:
        v = v[:v.rindex("]")]
    v = v[1:]
    return [x.strip().strip('"').strip("'") for x in v.split(",") if x.strip()]


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


def category_matches(fm_cat, top):
    """category 必须与所在目录名严格相同（如 02-features）。

    不要把这里放宽成「允许省略 NN- 前缀」。build_index.py 是拿 frontmatter 的
    值去查分类标签的，写成 `features` 就查不到 `02-features` 的标签，
    页面上分类名会变空、列表按分类过滤后也找不到对应按钮，且这种错误
    在页面上只是「空标签」，很容易长期不被发现。
    """
    return fm_cat == top


def declared_category_dirs(mdata):
    """manifest.categories 里声明过的分类目录名。"""
    return {c.get("dir") for c in (mdata or {}).get("categories", []) if c.get("dir")}


def main():
    errs = []
    notes = []
    count = 0
    cats_seen = set()
    mdata = {}
    _man = os.path.join(ROOT, "manifest.json")
    if os.path.isfile(_man):
        try:
            with open(_man, encoding="utf-8") as f:
                mdata = json.load(f)
        except Exception:
            mdata = {}  # 后面的 manifest 检查块会给出明确报错

    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in {"scripts", "_raw", ".git", "node_modules"}]
        rel = os.path.relpath(dirpath, ROOT)
        top = rel.split(os.sep)[0]
        is_root = (rel == ".")
        # 分类目录一律 `NN-` 前缀；库根层只允许「自身声明了 category 的条目」，
        # 其余根层 md（README/CHANGELOG/…) 不参与条目校验。
        # 这条规则必须与 build_index.py 的收集规则一致，否则会出现
        # 「构建收入了 N 条、校验却数出 0 条」的假报错。
        if not is_root and not re.match(r"^\d\d-", top):
            continue
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            if is_root and fn in ROOT_NON_ENTRY_FILES:
                continue
            full = os.path.join(dirpath, fn)
            with open(full, encoding="utf-8") as f:
                fm = parse_frontmatter(f.read())
            if fm is None:
                if is_root:
                    continue  # 根层的非条目 md 可以没有 frontmatter
                errs.append("%s: 缺少 frontmatter" % full)
                continue
            count += 1
            cats_seen.add(top if not is_root else fm.get("category", top))
            stem = os.path.splitext(fn)[0]
            if fm.get("id") != stem:
                errs.append("%s: id=%r != 文件名 %r" % (full, fm.get("id"), stem))
            if is_root:
                # 库根层条目没有目录可对照，改为要求 category 必须在
                # manifest.categories[].dir 里声明过（否则页面标签仍是空的，
                # 只是换了个地方兜住）。
                declared_dirs = declared_category_dirs(mdata)
                if fm.get("category") not in declared_dirs:
                    errs.append("%s: 根层条目的 category=%r 未在 manifest.categories 中声明"
                                % (full, fm.get("category")))
            elif not category_matches(fm.get("category"), top):
                errs.append("%s: category=%r 与目录 %r 不符" % (full, fm.get("category"), top))
            for k in REQUIRED:
                if not fm.get(k) or fm.get(k) == "[]":
                    errs.append("%s: 必填字段 %s 为空" % (full, k))
            upd = fm.get("updated", "")
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", upd):
                errs.append("%s: updated 格式异常 %r" % (full, upd))
            # ---- 可选字段 aliases：不填合法，填了必须是干净的数组 ----
            for key in OPTIONAL_FM_LIST:
                raw_v = fm.get(key)
                if raw_v is None or not raw_v.strip():
                    continue
                if not raw_v.lstrip().startswith("["):
                    errs.append("%s: %s 必须是 [] 数组形式（当前 %r）" % (full, key, raw_v[:40]))
                    continue
                items = parse_fm_list(raw_v)
                if not items:
                    errs.append("%s: %s 解析为空数组" % (full, key))
                low = [x.lower() for x in items]
                dup = sorted({x for x in low if low.count(x) > 1})
                if dup:
                    errs.append("%s: %s 有重复项 %s" % (full, key, ", ".join(dup)))
                if len(items) > 16:
                    errs.append("%s: %s 条目过多(%d)，别名应聚焦" % (full, key, len(items)))
                tags_low = {x.lower() for x in parse_fm_list(fm.get("tags", ""))}
                overlap = sorted(set(low) & tags_low)
                if overlap:
                    notes.append("%s: %s 与 tags 重复 %s（可删）" % (os.path.relpath(full, ROOT), key, ", ".join(overlap)))
                if (fm.get("id", "").lower()) in low:
                    notes.append("%s: %s 含自身 id，无检索价值" % (os.path.relpath(full, ROOT), key))

    print("扫描条目: %d" % count)

    # ---------- index.json ----------
    idx_path = os.path.join(ROOT, "index.json")
    if os.path.exists(idx_path):
        with open(idx_path, encoding="utf-8") as f:
            data = json.load(f)
        entries = data.get("entries") or []
        declared = data.get("total")
        if declared is None:
            declared = len(entries)
            notes.append("该库 index.json 无 total 字段（旧版结构），改用 entries 长度比对")
        print("index.json entries: %d | declared total: %s | by_category: %s"
              % (len(entries), declared, data.get("by_category")))
        if declared != count:
            errs.append("index.json 条目数(%s) != 磁盘条目数(%d)" % (declared, count))
        if entries and all("content" not in e for e in entries):
            notes.append("该库 index.json 不内联正文（旧版结构），跳过 content 检查")
        else:
            empty = [e.get("id") for e in entries if not (e.get("content") or "").strip()]
            if empty:
                errs.append("index.json 正文为空: %s" % ", ".join(empty))
    else:
        errs.append("缺少 index.json（请先运行 build_index.py）")

    # ---------- index.html ----------
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
        # 模板结构：缺 id 说明回退到了「全部按钮漏绑」的旧版模板
        for eid in REQUIRED_PAGE_IDS:
            if ('id="%s"' % eid) not in html:
                errs.append("index.html 缺少 id=\"%s\"：索引页模板未升级，侧栏交互会有问题" % eid)
        for t in REMOVED_TEXTS:
            if t in html:
                errs.append("index.html 仍含已删除的冗余文案：%s" % t)
        # 「全部」按钮必须落在 #navbox 内，否则统一绑定的选择器选不到它
        navbox = re.search(r'<div id="navbox">(.*?)</aside>', html, re.S)
        if navbox and not re.search(r'data-cat="all"', navbox.group(1)):
            errs.append('index.html 的「data-cat="all"」按钮不在 #navbox 内，会被漏绑')
        elif not navbox:
            errs.append("index.html 未找到 #navbox 容器")
    else:
        errs.append("缺少 index.html（请先运行 build_index.py）")

    # ---------- manifest 分类声明 vs 实际目录 ----------
    man_path = os.path.join(ROOT, "manifest.json")
    if not os.path.exists(man_path):
        errs.append("缺少 manifest.json（索引页标题与分类标签都从这里读）")
    else:
        try:
            with open(man_path, encoding="utf-8") as f:
                mdata = json.load(f)
        except Exception as ex:
            mdata = {}
            errs.append("manifest.json 解析失败：%s" % ex)
        if not mdata.get("kb", {}).get("name"):
            errs.append("manifest.json 缺少 kb.name（索引页标题会退回默认值）")
        declared = [c.get("dir") for c in mdata.get("categories", []) if c.get("dir")]
        if not declared:
            errs.append("manifest.json 缺少 categories[].dir（索引页分类标签会全部为空）")
        missing = sorted(cats_seen - set(declared))
        if missing:
            errs.append("manifest.categories 未声明这些目录，页面分类标签会渲染成空: %s"
                        % ", ".join(missing))
        extra = sorted(set(declared) - cats_seen)
        if extra:
            notes.append("manifest.categories 声明了但没有条目的目录: %s" % ", ".join(extra))

    # ---------- stock 脚本副本存在性 ----------
    for fn in STOCK_SCRIPTS:
        p = os.path.join(ROOT, "scripts", fn)
        if not os.path.isfile(p):
            errs.append("缺少 stock 脚本 scripts/%s（跑 scripts/sync_scripts.py 同步）" % fn)

    print("---")
    for n in notes:
        print("NOTE: %s" % n)
    print("ERRORS: %d" % len(errs))
    for e in errs:
        print(" -", e)
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
