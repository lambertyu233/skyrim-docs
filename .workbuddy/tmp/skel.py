import re, os
files = {
 "obito Bow_IdleDrawn (我复制了21次)": r"F:\download\BaiduNetdiskDownload\obito定制拉弓动作\_备份_原DAR结构\DynamicAnimationReplacer\_CustomConditions\1750000000\Bow_IdleDrawn.HKX",
 "obito Bow_DrawLight":   r"F:\download\BaiduNetdiskDownload\obito定制拉弓动作\_备份_原DAR结构\DynamicAnimationReplacer\_CustomConditions\1750000000\Bow_DrawLight.HKX",
 "obito Bow_Release":     r"F:\download\BaiduNetdiskDownload\obito定制拉弓动作\_备份_原DAR结构\DynamicAnimationReplacer\_CustomConditions\1750000000\Bow_Release.HKX",
 "Gunslicer Bow/bow_idledrawn": r"D:\game\JIZIYU J5.0\mods\女性动作补充包Gunslicer OAR Animations Pack\Meshes\actors\character\animations\OpenAnimationReplacer\Gunslicer Animations OAR\Bow\bow_idledrawn.hkx",
 "Gunslicer Bow_Sneak/sneakbow_idledrawn": r"D:\game\JIZIYU J5.0\mods\女性动作补充包Gunslicer OAR Animations Pack\Meshes\actors\character\animations\OpenAnimationReplacer\Gunslicer Animations OAR\Bow_Sneak\sneakbow_idledrawn.hkx",
 "Gunslicer Bow_Sneak/sneakwalk_forward": r"D:\game\JIZIYU J5.0\mods\女性动作补充包Gunslicer OAR Animations Pack\Meshes\actors\character\animations\OpenAnimationReplacer\Gunslicer Animations OAR\Bow_Sneak\sneakwalk_forward.hkx",
 "速射弓 sneakbow_idledrawn": r"D:\game\JIZIYU J5.0\mods\速射弓Bow Rapid Combo v3\meshes\Actors\Character\animations\OpenAnimationReplacer\Bow Rapid Combo V3\Professional Skill\sneakbow_idledrawn.hkx",
}
pat_nif  = re.compile(rb"[\x20-\x7e]{2,80}?\.nif")
pat_skel = re.compile(rb"[\x20-\x7e]{0,40}[Ss]keleton[\x20-\x7e]{0,40}")
for n,p in files.items():
    if not os.path.exists(p): print(n,"NOT FOUND"); continue
    d = open(p,'rb').read()
    nif = sorted(set(m.group().decode('ascii','ignore') for m in pat_nif.finditer(d)))
    sk  = sorted(set(m.group().decode('ascii','ignore') for m in pat_skel.finditer(d)))
    print(f"\n### {n}  ({len(d)} bytes)")
    print("   .nif 相关:", [s for s in nif if len(s) < 90][:8])
    print("   skeleton 相关:", [s for s in sk if len(s) < 90][:8])
