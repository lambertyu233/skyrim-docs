---
id: clipping
title: 穿模 / 破皮（身形与衣服不匹配）
category: 06-troubleshooting
kind: tutorial
version: 1.0.0
updated: 2026-09-22
tags: [排错, 穿模, 破皮, BodySlide, 预设]
aliases: [衣服穿模, 身形不符, 跟随从穿模, 3bav2 兼容]
source: https://forums.nexusmods.com/topic/13536754-body-clips-through-clothes-but-only-on-followers/
summary: 穿模的四类成因（未构建、家族不匹配、预设不一致、3BAv2 版本断代）与修法，并解释"为什么只有随从穿模"。
---

# 穿模 / 破皮

## 症状

身体从衣服里穿出来，或衣服像纸片一样被撑破。

## 根因：构建是烘焙，滑块是运行时

先建立这个模型，下面的成因才有意义：

| | 离线烘焙（BodySlide Build） | 运行时 morph（RaceMenu） |
|---|---|---|
| 何时算 | 点 Build 的那一刻 | 游戏运行中，每帧 |
| 改不改文件 | **改**：数值写进 `.nif` 顶点坐标，成静态模型 | 不改，只是临时形变 |
| 影响谁 | 所有用这个网格的人（含全部 NPC） | **只影响玩家** |

> **换预设只重新烘焙了身体，衣服的 nif 还停在上一个预设的形状** ——
> 顶点对不上，于是破皮、穿模、塌陷。

所以「穿模」本质上永远是同一句话：**某些网格的起点形状与你的身体不一致**。

机制展开见 [`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md)。

## 成因

### ① 服装没有在 BodySlide 里构建

**最常见。** 装了服装 mod 但没跑 Batch Build → 服装还是那个服装的原始形状，
和你的身形对不上。

→ **修**：在 BodySlide 里用**与身形相同的预设**对全部服装做 Batch Build。

### ② 身形家族不匹配

CBBE 身形穿 BHUNP 服装（或反之）。两族网格结构不同，必然穿模。

→ **修**：确认服装写明 for CBBE 3BA 还是 for BHUNP，只装同族。

### ③ 预设不一致

裸身用 Curvy、衣服用 Slim → 穿模。

→ **修**：裸身与服装用**同一个预设**构建。

### ④ 3BAv2 的版本断代（隐蔽但重要）

**3BAv2（2021 年底）之后**为 3BAv2 制作的服装才与 3BAv2 兼容。
更老的 CBBE / 3BBB 服装需要转换。

→ **修**：用 **Outfit Studio** 把老服装 Conform / 转换到你的身形。

### ⑤ 只有手/脚/内衣穿模

slot 32（身体）被替换了，但手（33）/ 脚（37）/ 内衣没有同步构建。

→ **修**：Batch Build 时把全套部件都包含进去。

## ⭐ 为什么"只有随从穿模"

这是社区里反复出现的问题，成因有两类：

1. **随从用了不同的身形**（见 [`../05-distribution/`](../05-distribution/obody-ng.md) 的分配设置）——
   分配工具按预设分发身形，如果随从拿到的预设与你为服装构建的预设不同，就会穿模；
2. **3BAv2 兼容性问题**：随从身上的服装来自更老的包。

所以遇到"只有随从穿模"，先查**分配工具给它的预设**，再查服装年代。

## 排查顺序

```
1. 这件服装构建过吗？（Batch Build）
2. 服装的身形家族 == 身形的家族吗？
3. 构建用的预设 == 裸身用的预设吗？
4. 服装是 3BAv2 前还是后？
5. 是随从专属问题吗？（→ 查分配工具的预设）
6. 手/脚/内衣是否同步构建？
```

## 正解：Zeroed Sliders + Build Morphs + Batch Build

与其「每换一次预设就把所有衣服重刷一遍」，更省心的做法是**把起点统一到零**：

1. **Outfit/Body** 选你的主身体（CBBE 3BA → `CBBE 3BBB Body Amazing`）；
2. **Preset** 选 **`Zeroed Sliders`**（用身体 mod 自带的那份；
   里面有滑块是 100% 属正常设计，**不要改**）；
3. 勾上 **`Build Morphs`**；
4. **Batch Build** 所有服装（记得在 Group Filter 里勾上 `Unassigned` 组，很多服装在那儿）；
5. 出现冲突列表时**统一选第 1 步的那个身体**。

这样所有网格起点一致，之后在游戏里用 RaceMenu 那一栏调什么都生效、不穿模。

六步详细版见 [`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md)。

## 来源

- 成因与修法（未构建 / 家族不匹配 / 预设不一致 / slot 未同步）：
  LoversLab 与 Nexus 论坛穿模帖 —— **社区经验（多帖一致）**
- 3BAv2 兼容断代：Nexus 论坛随从穿模帖 —— **社区经验**
- Conform / 用 Outfit Studio 转换：BodySlide 官方 wiki（Outfit Studio 职责）—— **一手**
- "只有随从穿模"与分配工具的关系：**社区经验 + 机制推论**
