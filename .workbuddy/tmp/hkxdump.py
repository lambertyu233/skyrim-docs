import re, os, struct

files = {
 "obito Bow_IdleDrawn":      r"F:\download\BaiduNetdiskDownload\obito定制拉弓动作\_备份_原DAR结构\DynamicAnimationReplacer\_CustomConditions\1750000000\Bow_IdleDrawn.HKX",
 "obito Bow_Release":        r"F:\download\BaiduNetdiskDownload\obito定制拉弓动作\_备份_原DAR结构\DynamicAnimationReplacer\_CustomConditions\1750000000\Bow_Release.HKX",
 "obito Bow_DrawLight":      r"F:\download\BaiduNetdiskDownload\obito定制拉弓动作\_备份_原DAR结构\DynamicAnimationReplacer\_CustomConditions\1750000000\Bow_DrawLight.HKX",
 "Gunslicer Bow/bow_idledrawn":        r"D:\game\JIZIYU J5.0\mods\女性动作补充包Gunslicer OAR Animations Pack\Meshes\actors\character\animations\OpenAnimationReplacer\Gunslicer Animations OAR\Bow\bow_idledrawn.hkx",
 "Gunslicer Bow_Sneak/sneakbow_idledrawn": r"D:\game\JIZIYU J5.0\mods\女性动作补充包Gunslicer OAR Animations Pack\Meshes\actors\character\animations\OpenAnimationReplacer\Gunslicer Animations OAR\Bow_Sneak\sneakbow_idledrawn.hkx",
 "Gunslicer Bow_Sneak/sneakwalk_forward":  r"D:\game\JIZIYU J5.0\mods\女性动作补充包Gunslicer OAR Animations Pack\Meshes\actors\character\animations\OpenAnimationReplacer\Gunslicer Animations OAR\Bow_Sneak\sneakwalk_forward.hkx",
 "速射弓 sneakbow_idledrawn": r"D:\game\JIZIYU J5.0\mods\速射弓Bow Rapid Combo v3\meshes\Actors\Character\animations\OpenAnimationReplacer\Bow Rapid Combo V3\Professional Skill\sneakbow_idledrawn.hkx",
}

for name, path in files.items():
    print("="*70)
    if not os.path.exists(path):
        print(name, "-> NOT FOUND"); continue
    data = open(path,'rb').read()
    print(f"{name}  size={len(data)}")
    print("  hdr:", data[:0x28].hex(' '))
    # 关键：hkx 的尾部/各段标记
    for mark in (b'__classnames__', b'__types__', b'__data__', b'classnames', b'hk_2010', b'hk_2014'):
        idxs = [m.start() for m in re.finditer(re.escape(mark), data)]
        if idxs:
            print(f"  marker {mark!r}: {idxs[:6]}")
    # 类名/类型名（可打印长串）
    strs = sorted(set(s.decode() for s in re.findall(rb"[\x20-\x7e]{6,}", data)))
    anim = [s for s in strs if 'hka' in s or 'hkb' in s or 'Animation' in s or 'Skeleton' in s or 'Track' in s or 'Binding' in s]
    print(f"  strings total={len(strs)}  hka/hkb相关({len(anim)}):")
    for s in anim[:25]: print("     ", s)
    other = [s for s in strs if s not in anim][:12]
    print("  其他样例:", other)
