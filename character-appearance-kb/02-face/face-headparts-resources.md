---
id: face-headparts-resources
title: 眼、眉、发、须资源现状
category: 02-face
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [捏脸, 眼睛, 眉毛, 头发, 胡须, 资源]
aliases: [eyes of beauty, brows, ks hairdos, apachii, beards, 发型包, 眼睛 mod]
source: https://www.nexusmods.com/skyrimspecialedition/mods/16185
summary: 捏脸最常用的四类外观资源（眼/眉/发/须）的代表 mod、Nexus ID、版本口径与 HPH 兼容补丁，并澄清 SE 版与 LE 版的版本号体系差异。
---

# 眼、眉、发、须资源现状

这些是"脸的配件"：不装也能捏脸，但装了才好看。它们的共同坑是
**与 High Poly Head 的适配**——HPH 换了头型，眉毛和胡须要专门的补丁。

## 眼睛

| mod | Nexus | 作者 | 说明 |
|---|---|---|---|
| **The Eyes of Beauty SSE** | 16185 | LogRaam（Gabriel Mailhot），docteure 上传 | 官方授权 SE 移植，**版本 1.2**（2020-08） |
| Mikan Eyes | 18780 | nerune | 常见预设软依赖 |
| The Witcher 3 Eyes | — | Oaristys | — |
| Improved Eyes Skyrim | — | — | — |

**The Eyes of Beauty 的版本号陷阱**：

> 中文镜像站上看到的 **"version 10.0.1" 是 LE 原版的版本号体系**。
> **SE 官方移植是 1.2。** 这两个数字不是一回事，别混。

它按 Player 包 / NPC 包 / Dawnguard（吸血鬼眼）包分开，可单装可组合，
含人类、亚龙人、精灵、虎人、兽人的异色瞳。

## 眉毛

**Hvergelmir's Aesthetic 系列**（作者 Hvergelmir，上传 lthot）：

- Nexus SE **1062**；LE 版 30411。
- 版本口径有 **4.0.1 / 4.1.0** 两种记录（**未确认唯一最新值**）。
- 提供 Ultra(2048×1024) / High(1024×512) / Low(512×256) 三档。
- 可选 `.esp` 增加更多手绘眉型（含深浅色匹配发色）。

**HPH 兼容**：Brows 与 HPH 属"半兼容"——不崩溃但眉形略歪，需要补丁：

| 补丁 | Nexus |
|---|---|
| Brows by Hvergelmir for High Poly Head | 38493 |
| 同款 - COTR - UBE 版（v2.1.0，含 Headpart Whitelist 与隐藏原版眉的 `Brows - Non-playable.esp`） | 63777 |

其它：Maevan2's Eyebrows（SE 26881，Shiva182 移植）、Kalilies Brows。

## 头发

| mod | Nexus | 作者 | 说明 |
|---|---|---|---|
| **KS Hairdos SSE** | 6817 | Kalilies & Stealthic | 老牌大型发型包，**约 980+ 款**（约 876 女 / 107 男） |
| **ApachiiSkyHair SSE** | 2014 | apachii | 量最大，含 Males / Females 分文件；纹理偏旧，常有重纹理补丁 |
| Vanilla Hair Replacer (VHR) | — | preeum | 替换原版发型；与 Face Discoloration Fix 有协同 |

KS Hairdos 生态衍生：**KS Hairdos - HDT SMP**（物理版，SE 31300）、
KS Hairdos 1.7 Salt and Wind（重纹理）、SC - KS Hairdos Retextured、
KS Hairdos Male Scalp Fix、LDD - KS Male Hairstyle Tweaks。

> **KS 发型数量的口径差异**：983（876F/107M）与 883（792F/91M）两种说法都存在，
> 取决于版本。写入笔记时统一说"**约 980+**"更稳。

## 胡须

| mod | Nexus | 作者 | 说明 |
|---|---|---|---|
| **Beards（Aesthetic 系列）** | 1067 | Hvergelmir（上传 lthot） | 版本 **5.0.1**；5.0 用 BC7 `.dds` 重做全部纹理与法线，5.0.1 修 FOMOD 路径错误 |
| Beards of Power | 42635 | Mharlek1 | 另一套胡须美化 |

APACHII 与 Beards 系列的取向不同：前者补量，后者补质（并复原了 Bethesda 砍掉的辫/串珠款）。

## 使用建议

1. **先确定身形家族**（见 [`../03-body/`](../03-body/cbbe.md)），再统一挑选配套皮肤；
2. 装了 HPH 就**同时装对应的眉毛/胡须补丁**，否则会出现"眉歪""须悬空"；
3. 资源装得越多，**FaceGen 缓存与头部件索引的负担越重** —— 装到上百个发型时，
   留意是否有专门的 FaceGen 缓存处理需求。

## 来源

- The Eyes of Beauty SSE：`https://www.nexusmods.com/skyrimspecialedition/mods/16185`，版本 1.2 为 SE 移植 —— **一手**
- Brows：`https://www.nexusmods.com/skyrimspecialedition/mods/1062`；
  补丁 38493 / 63777 —— **一手（Nexus 页面）**
- KS Hairdos SSE：`https://www.nexusmods.com/skyrimspecialedition/mods/6817` —— **一手**
- ApachiiSkyHair SSE：`https://www.nexusmods.com/skyrimspecialedition/mods/2014` —— **一手**
- Beards：`https://www.nexusmods.com/skyrimspecialedition/mods/1067` —— **一手**
- 版本号的多口径（Brows 4.0.1/4.1.0、KS 983/883）：**多来源口径不一致，已标注"未确认唯一最新值"**
- "SE 1.2 vs LE 10.x 版本体系不同"：**本工作区在撰条目时交叉核对得出，属辨析结论**
