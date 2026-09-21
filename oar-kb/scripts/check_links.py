#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_links.py — 站内相对链接校验（附带换行一致性检查）

资料库条目大量互相交叉引用（`../../02-features/core/sky-sync.md` 这类）。
相对链接的 `../` 层数由**目录深度**决定，手写极易错；而 validate_kb.py
只校验 frontmatter 与索引，**完全不看正文链接**，所以坏链能长期潜伏。

本脚本是资料库的"链接 lint"：任何目录调整、批量写条目、移动分类之后都该跑一次。

检查两项：
1. **站内相对链接**：解析不到实际文件即报错（计入退出码）。
2. **换行一致性**：报告 CRLF / 混合换行的文件（仅提示，不影响退出码）。
   资料库约定用 LF；混用换行会让 diff 噪音变大。

用法：managed python scripts/check_links.py
退出码：0 = 链接全部有效；1 = 存在失效链接。
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"scripts", "_raw", ".git", "node_modules"}
# markdown 链接 + 图片；http(s)/mailto/纯锚点不参与
LINK_RE = re.compile(r"\]\(([^)]+)\)")


def wiki_links():
    """产出 (文件绝对路径, 原始文本) —— 文本未做换行翻译，便于同时判断换行。"""
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue
            full = os.path.join(dirpath, fn)
            with open(full, "rb") as f:
                raw = f.read()
            yield full, raw.decode("utf-8", errors="replace"), raw


def main():
    bad = []
    total = 0
    endings = []

    for full, text, raw in wiki_links():
        dirpath = os.path.dirname(full)

        # ---- 1. 链接 ----
        for m in LINK_RE.finditer(text):
            target = m.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#", "//")):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            total += 1
            resolved = os.path.normpath(os.path.join(dirpath, path_part))
            if not os.path.exists(resolved):
                bad.append((os.path.relpath(full, ROOT), target))

        # ---- 2. 换行 ----
        crlf = raw.count(b"\r\n")
        lf_only = raw.count(b"\n") - crlf
        if crlf and lf_only:
            endings.append((os.path.relpath(full, ROOT), "MIXED"))
        elif crlf:
            endings.append((os.path.relpath(full, ROOT), "CRLF"))

    print("检查站内相对链接: %d" % total)
    if bad:
        print("失效链接: %d" % len(bad))
        for src, tgt in bad:
            print(" - %s -> %s" % (src, tgt))
    else:
        print("链接全部有效。")

    if endings:
        print("")
        print("NOTE: 以下 %d 个文件不是 LF 换行（资料库约定统一 LF）：" % len(endings))
        for src, kind in endings:
            print(" - [%s] %s" % (kind, src))
    else:
        print("换行一致：全部为 LF。")

    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
