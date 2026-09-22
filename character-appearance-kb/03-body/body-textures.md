---
id: body-textures
title: 身体皮肤材质
category: 03-body
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [身形, 皮肤, 材质, 贴图, UV]
aliases: [身体皮肤, 皮肤材质, skin, 男性皮肤, cbbe 皮肤, unp 皮肤]
source: https://www.nexusmods.com/skyrimspecialedition/mods/798
summary: 身体皮肤与身形家族的绑定关系、常见皮肤 mod、以及"换皮肤后出现接缝"的判断顺序。
---

# 身体皮肤材质

## 核心规则：皮肤必须与身形家族同族

| 身形家族 | 可选皮肤 |
|---|---|
| **CBBE / 3BA** | 仅 CBBE 系皮肤（CBBE UV） |
| **UNP / BHUNP** | 仅 UNP 系皮肤（UNP UV） |

原因：CBBE 与 UNP 使用**不同的 UV 映射**，贴图无法互换。
错配的表现是手 / 颈 / 脚接缝、纹理错位。

## 常见皮肤 mod

| mod | Nexus | 覆盖 | 备注 |
|---|---|---|---|
| **Fair Skin Complexion** | 798 | 女性（脸+身） | 提供 **CBBE 与 UNP 两种选项**；CBBE 装完后的常见推荐 |
| **Tempered Skins for Males** | — | 男性 | 男性皮肤的代表作 |
| BnP (Female / Male Skin) | — | 双向 | 社区常用 |
| Mature / Leyenda / Diamond / The Pure / Demoniac | — | 女性为主 | 社区点名较多 |

> 上表中除 Fair Skin 与 Tempered Skins 外的一批名字来自 Nexus 论坛的皮肤讨论帖 ——
> **社区经验，且清单随时期变化**。写文档时不要把它当成"权威排行"。

## 男性与女性是两条独立链

- 女性身形（CBBE 系 / UNP 系）**二选一**；
- 男性身形（如 **HIMBO**）是**另一条**链，可与女性身形**同时启用**；
- 男性皮肤（Tempered Skins for Males 等）也自成一套 UV。

## 排查顺序：出现接缝时

1. **头 / 手 / 身体是否来自同一套皮肤的同一种选项？**（一支 FOMOD 里的 12 个选项要全选同一档）
2. **皮肤与身形是否同族？**
3. 是否装了自定义头网格（HPH / CITRUS 等）而没做配套？
4. FaceGen 的 tint 是否与 CK 里 NPC 的 Face Tinting Color 一致？
5. **最后**才考虑"脖缝修补 mod" —— 它是创可贴，不解决根因。

完整排查见 [`../06-troubleshooting/neck-seam.md`](../06-troubleshooting/neck-seam.md)。

## 来源

- Fair Skin Complexion：`https://www.nexusmods.com/skyrimspecialedition/mods/798` —— **一手**
- "CBBE / UNP 的 UV 不通用"：Nexus 发布页描述 + 社区一致确认 —— **一手 + 社区经验**
- 皮肤清单中的非 Fair Skin / Tempered Skins 项：Nexus 论坛皮肤讨论 —— **社区经验（随时间变化）**
- 接缝排查顺序：综合脖子接缝帖（Nexus 论坛 / LoversLab）归纳 —— **社区经验**
