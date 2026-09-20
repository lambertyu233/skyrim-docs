import re, os, glob
cands = glob.glob(r"D:/game/JIZIYU J5.0/mods/OAR动作框架-Open Animation Replacer/**/*.dll", recursive=True) \
      + glob.glob(r"D:/game/JIZIYU J5.0/mods/OAR动作框架-Open Animation Replacer/**/*.ini", recursive=True)
for p in cands:
    data = open(p,'rb').read()
    strs = [m.group().decode('ascii') for m in re.finditer(rb"[\x20-\x7e]{3,}", data)]
    hits = [s for s in strs if re.search(r"bow|draw|release|attack state|attackState", s, re.I)]
    if hits:
        print("="*70); print(p)
        seen=set()
        for s in hits:
            if s not in seen:
                seen.add(s); print("   ", s)
