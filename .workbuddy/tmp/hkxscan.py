import re, sys, os

def strings(path, minlen=6):
    data = open(path, 'rb').read()
    return [m.group().decode('ascii') for m in re.finditer(rb'[\x20-\x7e]{%d,}' % minlen, data)]

def scan(path, patterns, minlen=6, limit=400):
    if not os.path.exists(path):
        print('!! MISSING:', path); return
    ss = strings(path, minlen)
    print('=' * 70)
    print('FILE:', path)
    print('size:', os.path.getsize(path), ' strings:', len(ss))
    rx = re.compile(patterns, re.I)
    hit = 0
    for i, s in enumerate(ss):
        if rx.search(s):
            hit += 1
            if hit <= limit:
                print('%6d  %s' % (i, s))
    print('--- total matched:', hit)

base_beh = r'E:\game\JIZIYU Y5.0\mods\Nemesis Engine 数据\meshes\actors\character\behaviors'
fn = r'E:\game\JIZIYU Y5.0\mods\FNIS SE 7.6 XXL\Meshes\actors\character\characters'

scan(os.path.join(base_beh, 'bow_direction_behavior.hkx'), r'sneak|bow', 6)
scan(os.path.join(fn, 'defaultmale.hkx'), r'sneakbow|bowdrawn|sneakwalk|sneakrun|sneak_turn|sneakmt', 6)
