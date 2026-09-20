import re
p = r"D:/game/JIZIYU J5.0/mods/OAR动作框架-Open Animation Replacer/SKSE/Plugins/OpenAnimationReplacer.dll"
data = open(p,'rb').read()
# 收集所有可打印串及其偏移（含 null 结尾的连续字面量）
items = [(m.start(), m.group().decode('ascii')) for m in re.finditer(rb"[\x20-\x7e]{3,}", data)]
targets = ["Bow draw","Bow attached","Bow drawn","Bow releasing","Bow released",
           "Bow next attack","Bow follow through"]
idx = {s:i for i,(o,s) in enumerate(items) if s in targets}
print("目标串在串表中的位置:", idx)
if targets[0] in idx:
    i = idx[targets[0]]
    print("\n===== 该串前后各 12 条（按文件偏移顺序）=====")
    for j in range(max(0,i-12), min(len(items), i+14)):
        off, s = items[j]
        mark = "  <<< " if s in targets else ("      " if j!=i else "")
        if len(s) > 60: continue
        print(f"{off:#010x}  [{j:5d}]  {s!r}{'   <<<<<' if s in targets else ''}")
