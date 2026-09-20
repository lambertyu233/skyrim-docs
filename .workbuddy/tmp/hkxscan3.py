import re, os, glob

def strings(path, minlen=6):
    data = open(path, 'rb').read()
    return [m.group().decode('ascii') for m in re.finditer(rb'[\x20-\x7e]{%d,}' % minlen, data)]

fn = r'E:\game\JIZIYU Y5.0\mods\FNIS SE 7.6 XXL\Meshes\actors\character\characters\defaultmale.hkx'
ss = strings(fn)
print('===== vanilla 潜行(sneak)动画路径 =====')
for i, s in enumerate(ss):
    if s.startswith('Animations') and 'sneak' in s.lower():
        print('%6d  %s' % (i, s))

print()
print('===== vanilla 弓(非潜行)动画路径 =====')
for i, s in enumerate(ss):
    if s.startswith('Animations') and ('bow' in s.lower()) and 'sneak' not in s.lower():
        print('%6d  %s' % (i, s))

print()
dlls = glob.glob(r'E:\game\JIZIYU Y5.0\mods\**\OpenAnimationReplacer.dll', recursive=True)
print('===== OpenAnimationReplacer.dll =====')
print(dlls)
if dlls:
    d = dlls[0]
    s2 = strings(d, 4)
    cond = sorted({s for s in s2 if re.fullmatch(r'Is[A-Z][A-Za-z0-9]*', s)})
    print('--- Is* 条件名 ---')
    print(', '.join(cond))
    other = sorted({s for s in s2 if re.fullmatch(r'(Has|Is|Get|RandomOrder|Current|Compare|Graph|Actor)[A-Za-z0-9]*', s)})
    print('--- 其他候选条件名 ---')
    print(', '.join(other))
