#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fix_aliases.py — 清理条目 frontmatter 中 aliases 的冗余/有害项。

为什么需要它
------------
`kb.py find` 对查询与别名都做 `.lower()` + 去空白归一化，因此**大小写变体与空格变体
在检索端完全冗余**；而 `validate_kb.py` 会对归一化后重复的项**直接报 ERROR**。
手写条目时很容易顺手写下 `DynDOLOD` 与 `dyndolod` 两行，从而让校验失败。

本脚本按同一个归一化键 `re.sub(r"\\s+", "", s.lower())` 清理三类项：
  1. 归一化后**重复**的项（保留首次出现）—— validate_kb 的 ERROR 来源；
  2. 与 `tags` 归一化后**相同**的项 —— tags 精确命中已计 40 分，别名冗余；
  3. 与自身 `id` **相同**的项 —— id 精确命中已计 100 分。

安全纪律（2026-09-22 曾因批量 frontmatter 改写静默破坏 33 个条目）
------------------------------------------------------------------
- **先断言锚点**：frontmatter 必须能匹配到，且 `aliases:` 行唯一；
- 只改 `aliases:` 那一行：把原文与改后文本逐行 diff，**断言恰好 1 行发生变化**；
- 读写一律 `newline=""`，避免 Windows 文本模式把 `\n` 静默转成 `\r\n`；
- 结束后打印清理后**不足 3 条别名**的条目，供人工补写。

用法
----
  python fix_aliases.py <kb-dir>              # dry-run，只报告
  python fix_aliases.py <kb-dir> --apply      # 实际写盘
退出码 0 = 无 ERROR；1 = 有文件不满足断言（未写盘）。
"""
import json
import os
import re
import sys

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
ALIASES_RE = re.compile(r"^aliases: \[(.*)\]\s*$", re.M)
ID_RE = re.compile(r"^id:\s*(\S+)\s*$", re.M)
TAGS_RE = re.compile(r"^tags:\s*\[(.*)\]\s*$", re.M)


def norm(s):
    return re.sub(r"\s+", "", s.lower())


def parse_list(raw):
    return [x.strip() for x in raw.split(",") if x.strip()]


def entry_files(root):
    """按 manifest.json 的 categories 收集条目（与 build_index.py 的收集口径一致）。"""
    manifests = []
    if os.path.exists(os.path.join(root, "manifest.json")):
        manifests.append(os.path.join(root, "manifest.json"))
    for d in sorted(os.listdir(root)):
        p = os.path.join(root, d, "manifest.json")
        if os.path.isdir(os.path.join(root, d)) and os.path.exists(p):
            manifests.append(p)
    if not manifests:
        raise SystemExit("未找到 manifest.json：%s" % root)

    for mp in manifests:
        mf = json.load(open(mp, encoding="utf-8"))
        base = os.path.dirname(mp)
        for c in mf.get("categories", []):
            dp = os.path.join(base, c["dir"])
            if not os.path.isdir(dp):
                continue
            for fn in sorted(os.listdir(dp)):
                if fn.endswith(".md"):
                    yield os.path.join(dp, fn)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    apply_ = "--apply" in sys.argv
    if not args:
        raise SystemExit(__doc__)
    root = os.path.abspath(args[0])

    changed, thin, problems = 0, [], []
    files = list(entry_files(root))

    for fp in files:
        with open(fp, "r", encoding="utf-8", newline="") as f:
            text = f.read()

        m = FM_RE.match(text)
        if not m:
            problems.append("%s: frontmatter 锚点未命中" % os.path.relpath(fp, root))
            continue
        fm = m.group(1)

        am = ALIASES_RE.search(fm)
        if not am:
            continue                                    # 没写 aliases，合法
        if len(ALIASES_RE.findall(fm)) != 1:
            problems.append("%s: aliases 行不唯一" % os.path.relpath(fp, root))
            continue

        raw_items = parse_list(am.group(1))
        idm = ID_RE.search(fm)
        id_key = norm(idm.group(1)) if idm else ""
        tgm = TAGS_RE.search(fm)
        tag_keys = {norm(t) for t in parse_list(tgm.group(1))} if tgm else set()

        seen, kept = set(), []
        for it in raw_items:
            k = norm(it)
            if not k or k in seen:      # 规则 1
                continue
            if k in tag_keys:           # 规则 2
                continue
            if k == id_key:             # 规则 3
                continue
            seen.add(k)
            kept.append(it)

        if kept == raw_items:
            continue

        new_line = "aliases: [%s]" % ", ".join(kept)
        # 拼回完整块，绝不对 group 偏移做切片（会丢掉开头的 ---\n）
        new_fm = fm[:am.start()] + new_line + fm[am.end():]
        new_text = "---\n" + new_fm + "\n---\n" + text[m.end():]

        # 断言：行数不变、恰好 1 行变化
        old_lines, new_lines = text.split("\n"), new_text.split("\n")
        if len(old_lines) != len(new_lines):
            problems.append("%s: 行数变化" % os.path.relpath(fp, root))
            continue
        diffs = [i for i, (a, b) in enumerate(zip(old_lines, new_lines)) if a != b]
        if len(diffs) != 1:
            problems.append("%s: 改动行数 != 1 (%d)" % (os.path.relpath(fp, root), len(diffs)))
            continue

        changed += 1
        if len(kept) < 3:
            thin.append((os.path.relpath(fp, root), len(kept), kept))

        if apply_:
            with open(fp, "w", encoding="utf-8", newline="") as f:
                f.write(new_text)

    print("%s: %d / %d 个文件需要清理" % ("APPLIED" if apply_ else "DRY-RUN", changed, len(files)))
    if thin:
        print("\n[需人工补别名] 清理后不足 3 条：")
        for p, n, k in thin:
            print("  %s -> %d %s" % (p, n, k))
    if problems:
        print("\n[断言失败，未写盘]：")
        for p in problems:
            print("  - %s" % p)
        return 1
    if not apply_:
        print("\n加 --apply 实际写盘；之后请重跑 validate_kb.py（须 0 ERROR / 0 NOTE）与 build_index.py。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
