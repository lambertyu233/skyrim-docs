---
id: himbo
title: HIMBO（男性身形）与男性皮肤生态
category: 03-body
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [身形, 男性, HIMBO, 皮肤, 男性美化]
aliases: [男性身形, 男体, male body, 男性皮肤, vitruvia, 男角色]
source: https://www.nexusmods.com/skyrimspecialedition/mods/143045
summary: 女性有 CBBE/3BA，男性的对应位是 HIMBO（作者 Kreiste）——它是什么、需要什么配套皮肤、以及"要装 SOS-Lite 版纹理"这条反直觉的经验。
---

# HIMBO（男性身形）

## 定位

**HIMBO = Highly Improved Male Body Overhaul**，作者 **Kreiste**。

它在男性身上的生态位，等价于女性侧的 **CBBE / 3BA**：

| | 女性 | 男性 |
|---|---|---|
| 基础身形 | CBBE | **HIMBO** |
| 带物理的进阶版 | CBBE 3BA | HIMBO（自带 Bodyslide 体系） |
| 构建工具 | BodySlide and Outfit Studio | 同一个 BodySlide |

> 本库 [`cbbe.md`](cbbe.md) / [`cbbe-3ba.md`](cbbe-3ba.md) 讲女性侧；本条补上男性侧。
> **只装女性身形不装男性身形，是"男性角色还是原版方块手"的最常见原因。**

## 它提供什么

- 男性身体网格 + **BodySlide 滑块体系**（可在 BodySlide 里用预设批量构建）；
- 与女性侧一样，**盔甲/衣服需要对应的 Bodyslide 文件**才能跟着身形走，否则穿模；
- 新出的盔甲 mod 现在普遍同时提供 **3BA / HIMBO / UBE** 三套 Bodyslide 文件
  （见 [`ube.md`](ube.md)）。

## BodySlide 里的操作差异

一个容易忽略的点：**男女用不同的骨骼文件**。社区指南给的做法是——
打开 BodySlide 设置确认当前选的是对应骨骼：

- 女性 → `skeleton_female_sse.nif`
- 男性（HIMBO）→ `skeleton_male_sse.nif`

然后像女性侧一样选身形、选预设、**Batch Build**。

## 男性皮肤纹理生态

男性皮肤的选择逻辑和女性不同，有几个高频组合（均见于社区指南的推荐清单）：

| 用途 | mod | 作者 |
|---|---|---|
| 人类男性皮肤 | **Vitruvia - Skin texture overhaul for males** | mandragorasprouts |
| 亚龙人（Argonian）男性皮肤 | Masculine Argonian Textures (Chameleon and Lizard) | MONSTERaider |
| 虎人（Khajiit）男性皮肤 | Masculine Khajiit Textures (Grey Cat and Leopard) | MONSTERaider |
| HIMBO 预设 | Norse God -- HIMBO Bodyslide Preset | M4ruko |

### ⚠️ 反直觉但很重要：男性皮肤要下 **SOS-Lite 版**

社区指南里反复强调一句经验：

> "We need the **SOS version** even though we're not getting SOS,
> because it **meshes with HIMBO better**."

即：**即使你不装 SOS（Schlongs of Skyrim），皮肤纹理也要选 SOS-Lite / SOS 版本**，
因为它的 UV 与 HIMBO 更贴合。装了原版（非 SOS）版本的皮肤会出现接缝或错位。

> 这条是**社区经验**（多个指南一致表述），不是某条官方说明。但它被重复得足够多，
> 且解释了"男性皮肤为什么总有缝"这一类问题，值得一试。

## 与 SOS 的关系

**SOS（Schlongs of Skyrim）是另一套东西**，来自 VectorPlexus，是独立的男性生殖器模组体系，
**不是 HIMBO 的前置**。两者关系是"共用 UV 规范"，不是依赖。

## 已知未确认项

| 事项 | 状态 |
|---|---|
| **HIMBO 的 Nexus mod ID 与当前版本号** | **未确认**（发布页在成人内容墙后，本轮未取得） |
| HIMBO 是否需要 XPMSSE 或特定骨骼 | **未确认**（社区指南默认已装骨骼类前置） |

> 需要 ID 时请在 Nexus 站内按 **"Highly Improved Male Body Overhaul"** 或作者名
> **Kreiste** 搜索；它在大量盔甲 mod 的 Requirements 列表里以
> `Highly Improved Male Body Overhaul -HIMBO-` 的形式作为**可选前置**出现。

## 来源

- HIMBO 全称 **Highly Improved Male Body Overhaul** 与作者 **Kreiste**：
  多个盔甲 mod 发布页的 Requirements 列表与 credits —— **一手（Nexus 发布页）**
- "盔甲同时提供 3BA / HIMBO / UBE 三套 Bodyslide 文件"：Iron Rose Armor 发布页 —— **一手**
- 男女骨骼文件不同（`skeleton_female_sse.nif` / `skeleton_male_sse.nif`）与 Batch Build 流程：
  Return to Skyrim（Nexus 指南） —— **社区经验（指南）**
- 男性皮肤清单（Vitruvia / Masculine Argonian / Masculine Khajiit）与作者：**一手（发布页署名）**；
  "HIMBO 更适合 SOS 版纹理"：Return to Skyrim 指南原文 —— **社区经验**
- HIMBO 预设 Norse God（M4ruko）：指南推荐清单 —— **一手（署名）**
