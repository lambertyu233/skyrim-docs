import re, os, glob

def strings(path, minlen=4):
    data = open(path, 'rb').read()
    return [m.group().decode('ascii') for m in re.finditer(rb'[\x20-\x7e]{%d,}' % minlen, data)]

dll = r'E:\game\JIZIYU Y5.0\mods\OAR动作框架-Open Animation Replacer\SKSE\Plugins\OpenAnimationReplacer.dll'
ss = set(strings(dll))
print('=== OAR DLL 中的 AttackState 枚举名 ===')
for s in sorted(ss):
    if re.fullmatch(r'(Bow drawn|Bow attached|Bow draw|Bow releasing|Bow released|Bow next attack|Bow follow through|Fire|Firing|Fired|Draw|Swing|Follow through|Bash|Hit|Next attack|None)', s):
        print('   ', s)

print()
print('=== 用 IsAttacking 的示例 config ===')
ex = r'E:\game\JIZIYU Y5.0\mods\动态闪避Dynamic Dodge Animation\meshes\actors\character\animations\OpenAnimationReplacer\Dynamic Dodge - TK Dodge RE-0.55-rc3\70210\config.json'
print(open(ex, encoding='utf-8', errors='replace').read()[:1200])

print()
print('=== MO2 配置里是否已装 obito / 拉弓 ===')
for p in glob.glob(r'E:\game\JIZIYU Y5.0\profiles\**\modlist.txt', recursive=True):
    txt = open(p, encoding='utf-8', errors='replace').read()
    hits = [l for l in txt.split('\n') if 'obito' in l.lower() or '拉弓' in l]
    print(' ', p, '->', hits if hits else '(无)')
