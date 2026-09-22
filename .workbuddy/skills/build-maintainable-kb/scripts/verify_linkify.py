# -*- coding: utf-8 -*-
"""语义等价核验：证明本次改动「只是把反引号引用换成了 markdown 链接」。

做法：定义一个归一化 h()，把两种写法都折叠成"纯目标路径"：
    h(s) = 把 `[label](href)` 折成 (href)，再把 `code` 折成 (code)
对同一文件的 **HEAD 版本** 与 **工作区版本** 分别求 h()，
若两者逐字节相同，则证明二者除「反引号 <-> 链接」外没有任何差别。

对两侧都施加同样的归一化，所以文件里**本来就存在**的 markdown 链接
（`[a](b)`）在两侧会被同样折叠，不会造成假阴性。
"""
import re
import subprocess
import sys

LINK = re.compile(r"\[([^\]]*)\]\(([^)]*)\)")
CODE = re.compile(r"`([^`\n]*)`")
# 归一化时抹掉目标的 `../` 前缀：原文里的 `oar-kb/08-practices/` 是「给人看的
# 工作区相对路径」，转换后必然变成「能点的 `../../oar-kb/08-practices/`」，
# 两者逻辑目标相同，不该判成差异。两侧同样处理，所以不会掩盖真问题。
LEADUP = re.compile(r"\(((?:\.\./)+)")


def h(s):
    s = LINK.sub(r"(\2)", s)
    s = CODE.sub(r"(\1)", s)
    s = LEADUP.sub("(", s)
    return s


def main():
    files = sys.argv[1:]
    if not files:
        # 默认：本次改动的全部 .md，但排除 .workbuddy/ 下的技能与记忆文件
        # （它们不是资料库条目，改了本来就该不一样）
        out = subprocess.run(["git", "diff", "--name-only", "--", "*.md"],
                             capture_output=True, text=True, encoding="utf-8").stdout
        files = [l for l in out.splitlines()
                 if l.strip() and not l.startswith(".workbuddy/")]

    ok = bad = 0
    for f in files:
        old = subprocess.run(["git", "show", "HEAD:" + f],
                             capture_output=True, encoding="utf-8").stdout
        with open(f, "r", encoding="utf-8", newline="") as fh:
            new = fh.read()
        if h(old) == h(new):
            ok += 1
        else:
            bad += 1
            print("✗ 超出预期的差异: %s" % f)
            # 打印第一处不同的行
            for i, (a, b) in enumerate(zip(h(old).split("\n"), h(new).split("\n"))):
                if a != b:
                    print("    归一化后首个不同行 #%d:" % (i + 1))
                    print("      HEAD : %s" % a)
                    print("      现在 : %s" % b)
                    break

    print("语义等价: %d 个文件通过 / %d 个文件异常（共 %d）" % (ok, bad, len(files)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
