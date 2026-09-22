#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""linkify_refs.py — 把条目正文里的"反引号纯文本路径引用"批量转成 markdown 相对链接。

为什么需要它
------------
`check_links.py` **只认 markdown 链接 `](...)`**。如果交叉引用写成反引号纯文本：

    详见 `09-diagnostics/crash-log-analyzer.md`

那么 ① 渲染出来不可点击；② `check_links.py` 完全看不到它，会打印
"检查站内相对链接: 0 / 链接全部有效" —— **看起来通过，实际是空跑**。
一旦之后调整目录结构，这些引用全都会静默失效。

解析策略（**命中即用；解析不到就原样保留**）
------------------------------------------
依次尝试：
  1. `entry_dir/../<token>`      → 同库其它分类      href = `../<token>`
  2. `entry_dir/../../<token>`   → 工作区根（其它库） href = `../../<token>`
  3. `entry_dir/<token>`         → 同目录            href = `<token>`
三者都不存在 → 不动它。因此 `github.com/xxx`、`x.osmenoga.com/xxx` 这类 URL 片段
**不会被误转成链接**。

只有"首段是真实存在的库目录或本库分类目录"的 token 才进入候选，进一步避免误伤。

链接文字：`.md` 目标取该文件 frontmatter 的 `title`；目录目标取所属库
`manifest.json` 里该分类的 title，退化到目录名。

安全纪律（血泪）
----------------
- **必须按围栏代码块 ``` 切段**，只对代码块外的片段做替换。
  不要用"等长占位盖住围栏、替换后按位还原"的方案 —— 替换本身会改变字符串长度，
  按位还原随之失效（本脚本第一版就是这么翻车的，靠自身的长度断言才中止）。
- 每文件断言：行数不变、反引号总数恰减少 `2 × 替换数`、围栏数量不变。
- 读写 `newline=""` 保留原换行（Windows 上文本模式会静默把 `\n` 变 `\r\n`）。
- 结束后**必须重跑 `build_index.py` 并用条目数做端到端校验**，再跑 `check_links.py`。

用法
----
  python linkify_refs.py <kb-dir>             # dry-run，报告替换数与样例
  python linkify_refs.py <kb-dir> --apply     # 实际写盘
退出码 0 = 正常；1 = 有文件不满足断言（未写盘）。
"""
import json
import os
import re
import sys

FENCE_RE = re.compile(r"^```.*?^```\s*$", re.S | re.M)
# 反引号内、含斜杠的候选（首段合法性在 resolve 前单独判定）
TOKEN_RE = re.compile(r"`([A-Za-z0-9._-]+/[A-Za-z0-9._/-]+)`")
FM_TITLE_RE = re.compile(r"^---\n.*?^title:\s*(.+?)\s*$.*?^---\n", re.S | re.M)


def read_title(path):
    try:
        with open(path, "r", encoding="utf-8", newline="") as f:
            head = f.read(4000)
    except OSError:
        return None
    m = FM_TITLE_RE.match(head)
    return m.group(1).strip() if m else None


_CAT_CACHE = {}


def dir_title(path):
    """目录 → 所属库 manifest 里该分类的 title，退化到目录名。"""
    path = path.rstrip("/\\")
    parent = os.path.dirname(path)
    if parent not in _CAT_CACHE:
        mp = os.path.join(parent, "manifest.json")
        titles = {}
        if os.path.exists(mp):
            try:
                mf = json.load(open(mp, encoding="utf-8"))
                for c in mf.get("categories", []):
                    titles[c["dir"]] = c.get("title", c["dir"])
            except Exception:
                pass
        _CAT_CACHE[parent] = titles
    return _CAT_CACHE[parent].get(os.path.basename(path))


def load_targets(root):
    """返回 (库目录集合, 条目文件列表)。与 build_index.py 的收集口径保持一致。"""
    ws = os.path.dirname(root)
    libs = set()
    for d in sorted(os.listdir(ws)):
        p = os.path.join(ws, d)
        if os.path.isdir(p) and os.path.exists(os.path.join(p, "manifest.json")):
            libs.add(d)

    manifests = []
    if os.path.exists(os.path.join(root, "manifest.json")):
        manifests.append(os.path.join(root, "manifest.json"))
    for d in sorted(os.listdir(root)):
        p = os.path.join(root, d, "manifest.json")
        if os.path.isdir(os.path.join(root, d)) and os.path.exists(p):
            manifests.append(p)
    if not manifests:
        raise SystemExit("未找到 manifest.json：%s" % root)

    files = []
    for mp in manifests:
        mf = json.load(open(mp, encoding="utf-8"))
        base = os.path.dirname(mp)
        for c in mf.get("categories", []):
            dp = os.path.join(base, c["dir"])
            libs.add(c["dir"])
            if not os.path.isdir(dp):
                continue
            for fn in sorted(os.listdir(dp)):
                if fn.endswith(".md"):
                    files.append(os.path.join(dp, fn))
    return libs, files


def resolve(entry_dir, token):
    for abs_t, href in (
        (os.path.normpath(os.path.join(entry_dir, "..", token)), "../" + token),
        (os.path.normpath(os.path.join(entry_dir, "..", "..", token)), "../../" + token),
        (os.path.normpath(os.path.join(entry_dir, token)), token),
    ):
        if os.path.exists(abs_t):
            return abs_t, href
    return None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    apply_ = "--apply" in sys.argv
    if not args:
        raise SystemExit(__doc__)
    root = os.path.abspath(args[0])
    libs, files = load_targets(root)

    total_rep, touched, skipped, problems = 0, 0, {}, []

    for fp in files:
        entry_dir = os.path.dirname(fp)
        with open(fp, "r", encoding="utf-8", newline="") as f:
            text = f.read()

        reps = []

        def sub(m):
            token = m.group(1)
            head = token.split("/", 1)[0]
            if head not in libs:                     # 首段不是真实库/分类目录 → 不动
                return m.group(0)
            r = resolve(entry_dir, token)
            if not r:
                skipped[token] = skipped.get(token, 0) + 1
                return m.group(0)
            abs_t, href = r
            if os.path.isdir(abs_t):
                label = dir_title(abs_t) or os.path.basename(abs_t.rstrip("/\\"))
            else:
                label = read_title(abs_t) or os.path.basename(abs_t)[:-3]
            rep = "[%s](%s)" % (label, href)
            reps.append((m.group(0), rep))
            return rep

        out, last = [], 0
        for m in FENCE_RE.finditer(text):            # 围栏原样保留
            out.append(TOKEN_RE.sub(sub, text[last:m.start()]))
            out.append(m.group(0))
            last = m.end()
        out.append(TOKEN_RE.sub(sub, text[last:]))
        new_text = "".join(out)

        if not reps:
            continue

        rel = os.path.relpath(fp, root)
        if text.count("\n") != new_text.count("\n"):
            problems.append("%s: 换行数变化" % rel)
            continue
        if new_text.count("`") != text.count("`") - 2 * len(reps):
            problems.append("%s: 反引号数不符" % rel)
            continue
        if len(FENCE_RE.findall(text)) != len(FENCE_RE.findall(new_text)):
            problems.append("%s: 围栏数变化" % rel)
            continue

        total_rep += len(reps)
        touched += 1
        if apply_:
            with open(fp, "w", encoding="utf-8", newline="") as f:
                f.write(new_text)

    print("%s: %d 处替换 / %d 个条目文件" % ("APPLIED" if apply_ else "DRY-RUN", total_rep, touched))
    if skipped:
        print("\n首段合法但解析不到目标（保持原样）：")
        for k, v in sorted(skipped.items(), key=lambda x: -x[1])[:20]:
            print("  %3d  %s" % (v, k))
    if problems:
        print("\n[断言失败，未写盘]：")
        for p in problems:
            print("  - %s" % p)
        return 1
    if not apply_:
        print("\n加 --apply 实际写盘；之后请重跑 build_index.py（核对条目数）与 check_links.py。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
