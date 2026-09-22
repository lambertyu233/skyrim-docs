---
id: neck-seam
title: 脖子接缝 / 手脚接缝
category: 06-troubleshooting
kind: tutorial
version: 1.0.0
updated: 2026-09-22
tags: [排错, 接缝, 脖缝, 皮肤, UV]
aliases: [脖子接缝, neck seam, 手脚接缝, 皮肤接缝, 颈部色差]
source: https://forums.nexusmods.com/topic/13527930-i-cant-get-rid-of-the-neck-seams-in-bhunp-body/
summary: 接缝的四个成因（头身皮肤不同源、UV 错配、自定义头网格未配套、tint 不一致）与按顺序的排查法，并指出脖缝修补 mod 只是创可贴。
---

# 脖子接缝 / 手脚接缝

## 症状

头像"套"在身体上，颈部（或手腕、脚踝）有一圈色差或纹理错位线。

## 成因（按发生频率排序）

### ① 头 / 手 / 身体用了不同套或不同档的皮肤

皮肤 mod 的 FOMOD 里常有多个部件选项（例如 12 个文件）。
**只要有一项选得不一样，就会出现接缝。**

→ **检查**：同一套皮肤、同一档，全部部件一致。

### ② 皮肤与身形家族不匹配

**CBBE 与 UNP 用不同的 UV 映射**，贴图不能互换。
给 CBBE 做的皮肤贴到 BHUNP 身上，接缝是必然的。

→ **检查**：CBBE 皮肤配 CBBE 系身形；UNP 皮肤配 UNP / BHUNP。见
[`../03-body/body-textures.md`](../03-body/body-textures.md)。

### ③ 自定义头网格与身体皮肤不配套

装了 **CITRUS**、**High Poly Head** 之类的自定义头网格，
却没有把头部纹理/法线与身体对齐。

→ **检查**：HPH 兼容"基于原版头部的纹理"，但如果你同时换了皮肤，要确认皮肤提供了 HPH 适配。

### ④ FaceGen 的 tint 与 NPC 记录不一致

改了肤色之后没有同步：

- RaceMenu 里记下肤色 **RGB**；
- 导出头后把 tint mask 放到正确位置、让头网格指过去；
- 在 CK 的 NPC 记录里把 **Face Tinting Color** 设为**相同 RGB**，**Interpolation = 1**；
- 然后 `Ctrl+F4` 重导该 NPC 的 FaceGen。

### ⑤ 旧 mod 残留的 loose 文件覆盖

装了新皮肤，但旧皮肤的松散文件还在覆盖。

→ **检查**：MO2 的 Conflicts 面板。

## 排查顺序（照着走）

```
1. 头/手/身体是否同一套皮肤同一档？
2. 皮肤与身形是否同族？
3. 是否装了自定义头网格而没做配套？
4. FaceGen tint 与 CK 的 Face Tinting Color 是否一致？
5. 是否有旧 mod 的 loose 文件覆盖？
```

## ⚠️ 一条重要认知

> **"脖子接缝修补 mod"是创可贴，不解决根因。**

有一种常见做法是用 **Caliente's Texture Blender** 混合头颈纹理，
或用"接缝修补"类 mod 遮盖。这些在"实在找不到根因"时可以应急，
但只要根因（不同源 / UV 错配）还在，换一套资源接缝就会重新出现。

## 来源

- "头/手/身体必须同源同档"、"必须同族"、"`Ctrl+F4` 重导"：
  Nexus 论坛脖子接缝帖（BHUNP）与 LoversLab 帖 —— **社区经验（多帖一致）**
- CBBE / UNP UV 不通用：Nexus 发布页描述 + 社区一致确认 —— **一手 + 社区经验**
- CITRUS 头网格导致接缝：LoversLab 帖 —— **社区经验**
- CK 的 Face Tinting Color / Interpolation：Creation Kit wiki（NPC 记录）—— **一手**
- "脖缝修补是创可贴"：**机制推论 + 社区共识**
