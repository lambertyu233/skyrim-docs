import os, json, re, glob
root = r"D:/game/JIZIYU J5.0/mods"
hits = []
for p in glob.glob(os.path.join(root, "**", "config.json"), recursive=True):
    try:
        d = json.loads(open(p, 'rb').read().decode('utf-8', 'ignore'))
    except Exception:
        continue
    def walk(cs, acc):
        for c in cs:
            if not isinstance(c, dict): continue
            nm = c.get("condition")
            if nm == "AttackState":
                acc.append((c.get("Comparison"), c.get("Attack state", c.get("Attack State"))))
            elif nm in ("OR","AND","XOR"):
                walk(c.get("Conditions", []), acc)
    acc = []
    walk(d.get("conditions", []), acc)
    if acc:
        rel = os.path.relpath(p, root)
        hits.append((rel, d.get("name"), acc))
seen=set()
for rel, name, acc in hits:
    key=(rel,name,str(acc))
    if key in seen: continue
    seen.add(key)
    print(f"--- {name!r}\n    {rel}")
    for cmp_, v in acc:
        print(f"      AttackState {cmp_} {v}")
print()
print("总命中:", len(hits))
