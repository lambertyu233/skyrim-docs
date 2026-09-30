#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fix_links.py — 一次性修复站内相对链接的深度错误

背景：条目分布在 `00-overview/`、`02-features/core/` 等**不同深度**的目录里，
手写 `../` 层数极易出错（例如 `02-features/core/x.md` 引根目录要 `../../`，
而 `01-installation/x.md` 只要 `../`）。这类错误不会让构建失败，能长期潜伏。

策略：**不信人写的层数**。把目标路径的前导 `../` 全部剥掉得到"尾部路径"，
在资料库根目录下反查实际文件，再用 os.path.relpath 反算正确的相对路径。
这样无论条目在几层深都成立。

换行：以 text + newline="" 读写，**原样保留**每个文件既有的换行符
（CRLF 不会因为修一个链接就被改成 LF，反之亦然）。

会保持原样的链接：
- http(s) / mailto / 纯锚点；
- 本来就能解析到的链接；
- 反查不到实际文件的链接（交回 check_links.py 报告，不猜）。

用法：managed python scripts/fix_links.py
退出码：0 = 全部可解析（含"无需修改"）；1 = 有链接的目标文件不存在。
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"scripts", "_raw", ".git", "node_modules"}
LINK_RE = re.compile(r"\]\(([^)]+)\)")


def find_real_path(tail):
    """在 ROOT 下按"尾部路径"寻找实际文件/目录。"""
    candidate = os.path.normpath(os.path.join(ROOT, tail))
    if os.path.exists(candidate):
        return candidate
    # 兜底：层级写错但文件名正确时，按文件名在库内搜索
    base = os.path.basename(tail)
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        if base in filenames:
            return os.path.join(dirpath, base)
    return None


def main():
    fixed = 0
    touched = 0
    unfixable = []

    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue
            full = os.path.join(dirpath, fn)
            # newline="" —— 读写都不做换行翻译，原样保留 CRLF / LF
            with open(full, encoding="utf-8", newline="") as f:
                text = f.read()

            changes = []

            def repl(m):
                target = m.group(1).strip()
                if target.startswith(("http://", "https://", "mailto:", "#", "//")):
                    return m.group(0)
                path_part, sep, anchor = target.partition("#")
                if not path_part:
                    return m.group(0)
                if os.path.exists(os.path.normpath(os.path.join(dirpath, path_part))):
                    return m.group(0)  # 本来就对
                tail = path_part
                while tail.startswith("../"):
                    tail = tail[3:]
                if tail.startswith("./"):
                    tail = tail[2:]
                real = find_real_path(tail)
                if real is None:
                    unfixable.append((os.path.relpath(full, ROOT), target))
                    return m.group(0)
                new_rel = os.path.relpath(real, dirpath).replace(os.sep, "/")
                if not new_rel.startswith("."):
                    new_rel = "./" + new_rel
                new_target = new_rel + sep + anchor
                changes.append((target, new_target))
                return "](%s)" % new_target

            new_text = LINK_RE.sub(repl, text)
            if new_text != text:
                with open(full, "w", encoding="utf-8", newline="") as f:
                    f.write(new_text)
                touched += 1
                print("修正 %s：" % os.path.relpath(full, ROOT))
                for a, b in changes:
                    print("   %s -> %s" % (a, b))
                fixed += len(changes)

    print("\n共修正 %d 处链接（涉及 %d 个文件）。" % (fixed, touched))
    if unfixable:
        print("无法自动修正（目标不存在，请人工判断）: %d" % len(unfixable))
        for src, tgt in unfixable:
            print(" - %s -> %s" % (src, tgt))
        return 1
    print("全部可达。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
