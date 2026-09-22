---
id: morph-and-nif-basics
title: 底层机制：NIF、morph 与 .tri
category: 00-overview
kind: concept
version: 1.0.0
updated: 2026-09-22
tags: [总览, 机制, NIF, morph, tri, 原理]
aliases: [morph 原理, tri 文件, nif 格式, bodytri, 滑块原理, 网格机制]
source: https://github.com/ousnius/BodySlide-and-Outfit-Studio
summary: 讲清"滑块为什么能改变体型"：NIF 网格容器、BSTriShape、morph 顶点位移、.tri 与 BODYTRI 的配合，以及 RaceMenu 如何在运行时应用。
---

# 底层机制：NIF、morph 与 .tri

不懂这一层，就只能"照着教程点"，出了偏差也不知道错在哪一步。

## 一、NIF 是网格容器

**NIF（NetImmerse Format）** 是 Creation Engine 的 3D 资产格式，
可包含网格、着色器、骨骼、动画与物理信息。身体/头部/服装都是 NIF。

关键差异：

| 游戏 | 身体网格的形状节点 |
|---|---|
| Skyrim LE | `NiTriShape` + 挂一个 `NiTriShapeData`（几何数据分开） |
| **Skyrim SE / AE** | **`BSTriShape`**（把形状与几何数据合并成单块） |

> 这个差异有实际后果。RaceMenu 作者记录过：某个游戏版本更新后，
> **`NiTriShape` 不带 `NiTriShapeData` 会导致崩溃**，因此新版 overlay NIF 被重新打包。
> 也就是说，"网格格式的细节"是会直接影响能否进游戏的。

### 蒙皮网格还要一个东西

可被骨骼摆动的网格（身体、衣服）额外挂 **`BSDismemberSkinInstance`**，
它包含两件事：

1. **顶点权重**（每个顶点受哪些骨骼影响、权重多少）—— 这就是"`Bone Weight Fix`"在修的东西；
2. **Partitions（身体部位分区）**：裸体 = `SBP_32_Body`，手 = `33`，脚 = `37`。
   **分区号必须与 ARMO / ARMA 记录里的 biped 槽一致，否则该部分不显示。**

## 二、morph：滑块的数学本质

**morph 就是一组顶点位移向量。** 一个 morph 描述"当这个滑块 = 100 时，每个顶点要移动多少"。

运行时实际显示的网格 = **基础网格 + Σ(各 morph × 该滑块权重)**。

所以：

- 基础网格 + 滑块值 = 你最终看到的体型；
- 这也解释了为什么"手动把滑块拉到 200 会破网格"—— 位移是线性叠加的，超出设计范围就会自交。

## 三、`.tri` 与 BODYTRI：morph 怎么被游戏找到

| 环节 | 谁产生 | 谁消费 |
|---|---|---|
| `.tri` 文件（morph 目标数据） | **BodySlide**（勾 `Build Morphs` 时生成） | RaceMenu 的 NiOverride / 游戏引擎 |
| NIF 里的 **`BODYTRI` extra data** | **BodySlide**（同一次构建写入） | 引擎（据此找到对应 `.tri`） |

**因此**：

- 不勾 `Build Morphs` → 没有 `.tri` → **RaceMenu 里看不到身形滑块**；
- 只生成了 `.tri` 但 NIF 没有 `BODYTRI` → 引擎找不到 → 同样无效；
- 构建被另一个 mod 的 NIF 覆盖 → 你的 `BODYTRI` 也没了（**这是"滑块突然消失"的常见真因**）。

BodySlide 仓库的提交记录里有一条 "Write only a single BODYTRI extra data when building"，
正是这条机制的佐证。

## 四、RaceMenu 在运行时做什么

RaceMenu 的核心是 **`skee64.dll`**，它内含 **NiOverride** 与 **CharGen** 两个模块：

- **NiOverride**：运行时往网格上叠加 morph / 纹理覆盖（overlay）/ 着色；
- **CharGen**：角色创建界面本身（也就是"滑块界面"）。

因为 NiOverride 能在**运行时**改网格，所以：

- 滑块能即时预览；
- 预设能在游戏内应用、能发给 NPC；
- **但也意味着 morph 状态是存在存档（SKSE co-save）里的** —— 换 mod 后旧档的 morph 可能对不上。

## 五、FaceGen 是另一套机制（别混）

脸不是靠 morph 实时生成的：

- **FaceGen** 是引擎**预生成**的头部数据，来自 Creation Kit 的 `Ctrl+F4` 导出；
- 玩家角色在 RaceMenu 里可以临时用 morph 调整并导出成 FaceGen；
- **NPC 的脸永远是预生成的**（这也是 EFM 只影响玩家、不影响 NPC 的根本原因）。

详见 [`../02-face/facegen-pipeline.md`](../02-face/facegen-pipeline.md)。

## 六、装备网格替换裸体网格

一条容易被忽略、但决定了整个身型问题的机制：

> **Skyrim 里「穿衣服」不是给身体套一层布，而是用装备网格直接替换裸体网格。**
> 装备本身就是「一具穿好衣服的身体」。

推论只有一个：**所有网格（裸体 + 每一件衣服）的顶点形状必须一致**。谁不一致，谁穿模。

而「形状」由两条互相独立的路径决定：

| 路径 | 何时算 | 改不改文件 | 影响谁 |
|---|---|---|---|
| **离线烘焙**（BodySlide Build） | 你点 Build 的那一刻 | **改**：数值写进 `.nif` 的顶点坐标，成静态模型 | 所有用这个网格的人（含全部 NPC） |
| **运行时 morph**（RaceMenu / NiOverride） | 游戏运行中，每一帧 | 不改，只是临时形变 | **只影响玩家** |

**两者是叠加的**：先烘出一个「起点形状」，再在运行时往它上面叠 morph。
所以只要起点不一致，运行时怎么调都会错位 —— 这就是「换了预设衣服就穿模」的根源。

展开见 [`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md)。

## 来源

- NIF / BSTriShape / `BSDismemberSkinInstance` / SBP 分区号：Beyond Skyrim「Arcane University」NIF 技术文档 —— **社区权威技术文档**
  （原文另见：`https://wiki.beyondskyrim.org/wiki/Arcane_University:NetImmerse_Format`）
- `.tri` + `BODYTRI` + Build Morphs：BodySlide 官方仓库提交记录与 wiki —— **一手**
- NiTriShape / NiTriShapeData 崩溃与 overlay NIF：RaceMenu 作者 Nexus 帖 —— **一手（作者本人）**
- morph = 顶点位移、基础网格 + Σ(morph × 权重)：由 BodySlide wiki 的滑块机制说明与 NiOverride 行为归纳 —— **一手机制 + 合理归纳**
- NPC 脸是预生成、EFM 只影响玩家：EFM Nexus 发布页描述 —— **一手**
