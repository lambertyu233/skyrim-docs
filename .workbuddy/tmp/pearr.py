import struct, re
p = r"D:/game/JIZIYU J5.0/mods/OAR动作框架-Open Animation Replacer/SKSE/Plugins/OpenAnimationReplacer.dll"
data = open(p,'rb').read()

# ---- parse PE ----
e_lfanew = struct.unpack_from('<I', data, 0x3C)[0]
assert data[e_lfanew:e_lfanew+4] == b'PE\0\0'
coff = e_lfanew + 4
nsec, = struct.unpack_from('<H', data, coff+2)
opt = coff + 20
magic, = struct.unpack_from('<H', data, opt)
is64 = magic == 0x20b
imgbase = struct.unpack_from('<Q', data, opt+24)[0] if is64 else struct.unpack_from('<I', data, opt+28)[0]
print(f"nsec={nsec} is64={is64} imagebase={imgbase:#x}")
secs=[]
so = opt + (240 if is64 else 224)
for i in range(nsec):
    o = so + i*40
    name = data[o:o+8].rstrip(b'\0').decode('ascii','ignore')
    vsize, va, rsize, rptr = struct.unpack_from('<IIII', data, o+8)
    secs.append((name, va, vsize, rptr, rsize))
    print(f"  {name:8s} VA={va:#010x} VS={vsize:#x} RAW={rptr:#010x} RS={rsize:#x}")

def rva_to_off(rva):
    for name, va, vs, rptr, rsize in secs:
        if va <= rva < va + max(vs, rsize):
            return rptr + (rva - va)
    return None

target = b"Bow draw"
toff = data.find(target)
# find which section & rva
t_rva = None
for name, va, vs, rptr, rsize in secs:
    if rptr <= toff < rptr + rsize:
        t_rva = va + (toff - rptr); t_sec = name
print(f"\n'Bow draw' fileoff={toff:#x} rva={t_rva:#x} sec={t_sec} VA={imgbase+t_rva:#x}")

t_va = imgbase + t_rva
packed = struct.pack('<Q', t_va)
hits = [m.start() for m in re.finditer(re.escape(packed), data)]
print(f"指向它的 8 字节指针出现 {len(hits)} 次:", [hex(h) for h in hits[:10]])

# walk backwards/forwards collecting pointers that resolve to printable strings
def ptr_str(va):
    off = rva_to_off(va - imgbase)
    if off is None: return None
    end = data.find(b'\0', off, off+80)
    if end < 0: return None
    s = data[off:end]
    if not s or not all(0x20 <= c < 0x7f for c in s): return None
    return s.decode('ascii')

for h in hits[:3]:
    print(f"\n===== 指针表 @ {h:#x} =====")
    base = h
    # walk back
    start = base
    while start-8 >= 0:
        v, = struct.unpack_from('<Q', data, start-8)
        s = ptr_str(v)
        if s is None: break
        start -= 8
    out=[]
    i = start
    while i < min(len(data)-8, base + 8*30):
        v, = struct.unpack_from('<Q', data, i)
        s = ptr_str(v)
        if s is None: break
        out.append((i, s)); i += 8
    for j,(offv,s) in enumerate(out):
        print(f"   [{j:2d}] {s!r}")
