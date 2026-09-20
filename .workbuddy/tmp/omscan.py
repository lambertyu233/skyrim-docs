import re, os

def strings(path, minlen=4):
    data = open(path, 'rb').read()
    return [m.group().decode('ascii') for m in re.finditer(rb'[\x20-\x7e]{%d,}' % minlen, data)]

p = r'E:\game\JIZIYU Y5.0\mods\FNIS SE 7.6 XXL\Meshes\actors\character\behaviors\0_master.hkx'
print('FILE:', p, os.path.getsize(p))
ss = strings(p)
print('total:', len(ss))
print()
print('--- 含 bow 的字符串 ---')
for i, s in enumerate(ss):
    if 'bow' in s.lower():
        print('%6d  %s' % (i, s))
print()
print('--- 含 sneak 的字符串 ---')
for i, s in enumerate(ss):
    if 'sneak' in s.lower():
        print('%6d  %s' % (i, s))
print()
print('--- 变量名形式的字符串 (i/b/f 开头驼峰) ---')
vars_ = sorted({s for s in ss if re.fullmatch(r'[ibf][A-Z][A-Za-z0-9_]{2,30}', s)})
print(', '.join(vars_))
