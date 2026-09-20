import re, os

def strings(path, minlen=6):
    data = open(path, 'rb').read()
    return [m.group().decode('ascii') for m in re.finditer(rb'[\x20-\x7e]{%d,}' % minlen, data)]

def dump(path, rx=None, limit=1000):
    print('=' * 72)
    print('FILE:', os.path.basename(path), os.path.getsize(path), 'bytes')
    ss = strings(path)
    print('total strings:', len(ss))
    if rx:
        r = re.compile(rx, re.I)
        out = [(i, s) for i, s in enumerate(ss) if r.search(s)]
        print('matched:', len(out))
        for i, s in out[:limit]:
            print('%5d  %s' % (i, s))
    else:
        for i, s in enumerate(ss[:limit]):
            print('%5d  %s' % (i, s))

beh = r'E:\game\JIZIYU Y5.0\mods\Nemesis Engine 数据\meshes\actors\character\behaviors'
fn = r'E:\game\JIZIYU Y5.0\mods\FNIS SE 7.6 XXL\Meshes\actors\character\characters'

dump(os.path.join(beh, 'bow_direction_behavior.hkx'))
dump(os.path.join(fn, 'defaultmale.hkx'), r'sneakbow|bow_idle|bowdrawn|bow_draw|bow_release|bowidle', 120)
