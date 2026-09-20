import re, os, struct

def blob(p): return open(p,'rb').read() if os.path.exists(p) else None

files = {
 "obito Bow_IdleDrawn (我用了21次)": r"F:\download\BaiduNetdiskDownload\obito定制拉弓动作\_备份_原DAR结构\DynamicAnimationReplacer\_CustomConditions\1750000000\Bow_IdleDrawn.HKX",
 "obito Bow_DrawLight":             r"F:\download\BaiduNetdiskDownload\obito定制拉弓动作\_备份_原DAR结构\DynamicAnimationReplacer\_CustomConditions\1750000000\Bow_DrawLight.HKX",
 "obito Bow_Release":               r"F:\download\BaiduNetdiskDownload\obito定制拉弓动作\_备份_原DAR结构\DynamicAnimationReplacer\_CustomConditions\1750000000\Bow_Release.HKX",
 "Gunslicer Bow/bow_idledrawn":     r"D:\game\JIZIYU J5.0\mods\女性动作补充包Gunslicer OAR Animations Pack\Meshes\actors\character\animations\OpenAnimationReplacer\Gunslicer Animations OAR\Bow\bow_idledrawn.hkx",
 "Gunslicer Bow_Sneak/sneakbow_idledrawn": r"D:\game\JIZIYU J5.0\mods\女性动作补充包Gunslicer OAR Animations Pack\Meshes\actors\character\animations\OpenAnimationReplacer\Gunslicer Animations OAR\Bow_Sneak\sneakbow_idledrawn.hkx",
 "Gunslicer Bow_Sneak/sneakwalk_forward":  r"D:\game\JIZIYU J5.0\mods\女性动作补充包Gunslicer OAR Animations Pack\Meshes\actors\character\animations\OpenAnimationReplacer\Gunslicer Animations OAR\Bow_Sneak\sneakwalk_forward.hkx",
 "速射弓 sneakbow_idledrawn":       r"D:\game\JIZIYU J5.0\mods\速射弓Bow Rapid Combo v3\meshes\Actors\Character\animations\OpenAnimationReplacer\Bow Rapid Combo V3\Professional Skill\sneakbow_idledrawn.hkx",
}

print("### 关键特征位检查 ###")
for n,p in files.items():
    d = blob(p)
    if d is None: print(n, "NOT FOUND"); continue
    feats = {}
    for k in (b'hkaSkeleton', b'hkaBone', b'hkaMeshBinding', b'ADDITIVE', b'BlendHint',
              b'originalSkeletonName', b'hkaBoneAttachment', b'BONE_QUALITY', b'rootBoneIndex'):
        feats[k.decode()] = d.count(k)
    # 找动画时长 / 轨道数（heuristic: u32 type, f32 dur, u32 tracks, u32 floats）
    cands = []
    for off in range(0xa0, len(d)-16, 4):
        t, dur, trk, flt = struct.unpack_from('<IfII', d, off)
        if t <= 4 and 0.05 <= dur <= 60.0 and 3 <= trk <= 400 and flt <= 32:
            cands.append((off, t, round(dur,3), trk, flt))
    print(f"\n{n}  size={len(d)}")
    print("   ", {k:v for k,v in feats.items() if v})
    print("    时长/轨道候选:", cands[:6])

print("\n### 骨骼名字符串（判断是否内嵌完整骨架） ###")
for n,p in list(files.items())[:1] + list(files.items())[3:4]:
    d = blob(p)
    strs = sorted(set(s.decode('ascii','ignore') for s in re.findall(rb"[\x20-\x7e]{4,}", d)))
    bones = [s for s in strs if re.match(r'^(NPC |AnimObject|Camera|Weapon|Bow|Quiver|Arrow|Skeleton|R Hand|L Hand|Head|Neck|Spine|Pelvis|Clavicle|UpperArm|Forearm|Hand|Thigh|Calf|Foot|Toe|Tail|Skirt|HDT)', s)]
    print(f"\n{n}: 疑似骨骼名 {len(bones)} 个")
    print("   ", bones[:40])
