import json, glob, os
base = r"F:/download/BaiduNetdiskDownload/obito定制拉弓动作-倒立拉弓-潜行版/meshes/actors/character/animations/OpenAnimationReplacer/ObitoSneakBow"
print("=== JSON 校验 ===")
def cond_brief(c, ind="    "):
    n = c.get("condition")
    if n in ("OR","AND","XOR"):
        subs = ", ".join(cond_brief(x, ind+"  ") for x in c.get("Conditions", []))
        return f"{n}({subs})"
    if n == "AttackState":
        return f"AttackState {c.get('Comparison')} {int(c['Attack state']['value'])}"
    if n == "IsActorBase":
        return f"IsActorBase({c['Actor base']['pluginName']}/{c['Actor base']['formID']})"
    return n
ok = True
for p in sorted(glob.glob(base + r"\**\config.json", recursive=True)):
    raw = open(p,'rb').read()
    rel = os.path.relpath(p, base)
    if raw.startswith(b'\xef\xbb\xbf'):
        print("  BOM! ->", rel); ok = False; continue
    try:
        d = json.loads(raw.decode('utf-8'))
    except Exception as e:
        print("  JSON ERROR", rel, e); ok = False; continue
    if 'conditions' not in d:
        print(f"  [mod级] {rel}  name={d.get('name')!r}"); continue
    print(f"  OK  {rel}")
    print(f"        name     = {d.get('name')!r}")
    print(f"        priority = {d.get('priority')}   interruptible = {d.get('interruptible')}")
    for c in d['conditions']:
        print(f"        + {cond_brief(c)}")
print("\n=== 文件数 ===")
for sub in ("Pose","DrawMove","ReleaseMove","HoldMove"):
    n = len(glob.glob(os.path.join(base, sub, "*.hkx")))
    print(f"  {sub:12s} {n} 个 hkx")
print("\n结果:", "全部通过" if ok else "有问题")
