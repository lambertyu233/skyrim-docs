---
id: face-textures
title: 脸部皮肤与纹理
category: 02-face
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [捏脸, 皮肤, 纹理, 贴图, UV]
aliases: [脸皮, skin texture, fair skin, 皮肤贴图, 脖子接缝原因]
source: https://www.nexusmods.com/skyrimspecialedition/mods/798
summary: 脸部/身体皮肤贴图的选择原则，以及"皮肤必须与身形同族"这条硬约束——它是脖缝与手脚接缝的第一大成因。
---

# 脸部皮肤与纹理

## 一条硬约束：皮肤 UV 必须与身形同族

**这是本领域最容易被忽略、又最容易造成视觉缺陷的一条规则。**

- **CBBE 有自己的 UV 映射**，UNP 系有另一套；
- 为 CBBE 制作的皮肤贴图**不能**直接用在 UNP / BHUNP 上，反之亦然；
- 错配的表现是**手、颈、脚出现接缝**，或者纹理错位。

所以"选皮肤"这件事，在"选身形"之后就已经被限定了一半。

## 头部与身体要用同一套

不只是身形家族内部要一致，**头、手、身体必须来自同一套皮肤的同一种选项**：

- 一个皮肤 mod 的 FOMOD 里如果分了 12 个部件选项，就要**全部选同一档**；
- 混搭不同档位（比如头用 High、身体用 Low，或头用 A 皮肤的 complexion、身体用 B 皮肤的）
  是脖缝的第二大成因。

脖子接缝的完整排查见 [`../06-troubleshooting/neck-seam.md`](../06-troubleshooting/neck-seam.md)。

## 常见皮肤 mod

| mod | Nexus | 备注 |
|---|---|---|
| **Fair Skin Complexion** | 798 | 女性脸/身贴图，提供 **CBBE 与 UNP 两种选项**；CBBE 装完后的常见推荐 |
| **Tempered Skins for Males** | — | 男性皮肤的代表，配男性身形 |
| 其它常被点名的 | — | Mature、Leyenda、Diamond、The Pure、BnP (Female/Male Skin)、Demoniac 等 |

> ⚠️ "最主流的皮肤清单"会随时期变化，**不宜写死**。
> 上面除 Fair Skin 外的一批名字来自 Nexus 论坛的皮肤讨论帖 —— **社区经验**。

## 与其它层的交叉

| 交叉点 | 说明 |
|---|---|
| 与身形 | 必须同族（见上） |
| 与 High Poly Head | HPH **兼容基于原版头部的纹理**，不需要专门为 HPH 找皮肤 |
| 与 tint mask | 皮肤是"底"，tint mask 是"上层着色"。改肤色后要在 CK 里同步 Face Tinting Color |
| 与 RaceMenu 预设 | 预设里的 `skinOverrides` 与皮肤相关，缺失会导致油光类 bug |

## 选择建议

1. 先定身形家族（CBBE 或 UNP 系）；
2. 在该家族里挑皮肤，**CBBE 皮肤配 CBBE 身形，UNP 皮肤配 UNP 身形**；
3. 头/手/身体选项保持同档；
4. 换皮肤后如果出现脖缝，先怀疑是不是头身不同源，而不是去做"脖缝修补 mod"。

> **提醒**：脖缝修补类 mod 是**创可贴**，不解决根因。真正的解法是让头颈贴图同源。

## 来源

- Fair Skin Complexion：`https://www.nexusmods.com/skyrimspecialedition/mods/798` —— **一手**
- "CBBE 与 UNP 的 UV 不通用"：Nexus 发布页描述 + 社区一致确认 —— **一手 + 社区经验（一致）**
- 头/手/身体需同一套同一档：脖子接缝排查帖（Nexus 论坛 / LoversLab）—— **社区经验**
- 皮肤清单中的非 Fair Skin 项：Nexus 论坛 BHUNP 皮肤讨论 —— **社区经验，随时期变化**
- HPH 兼容原版头部纹理：HPH 发布页描述 —— **一手**
