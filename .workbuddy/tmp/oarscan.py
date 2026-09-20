import re, os, glob

def strings(path, minlen=4):
    data = open(path, 'rb').read()
    return [m.group().decode('ascii') for m in re.finditer(rb'[\x20-\x7e]{%d,}' % minlen, data)]

dlls = glob.glob(r'E:\game\JIZIYU Y5.0\mods\**\OpenAnimationReplacer.dll', recursive=True)
print('DLL:', dlls)
if dlls:
    s2 = strings(dlls[0])
    for kw in ['Attacking', 'WeaponDrawn', 'Sneaking', 'GraphVariable', 'ActionActive', 'IsBashing', 'IsBlocking', 'IsCasting', 'BowDrawn', 'EquippedType', 'Movement', 'IsMoving', 'Sprinting']:
        hits = sorted({s for s in s2 if kw.lower() in s.lower() and len(s) < 60})
        print('--- %s ---' % kw)
        print('   ', ' | '.join(hits[:25]))
    print()
    print('--- 所有 Is* 形式的字符串 ---')
    print(', '.join(sorted({s for s in s2 if re.fullmatch(r'Is[A-Za-z0-9_]{3,30}', s)})))
    print()
    print('--- 版本信息 ---')
    print(', '.join(sorted({s for s in s2 if re.fullmatch(r'\d+\.\d+\.\d+', s)})[:20]))
    p = os.path.dirname(dlls[0])
    print('OAR 目录:', p)
    for f in os.listdir(p):
        print('   ', f)
