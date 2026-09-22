---
id: physics-overview
title: 物理方案总览与选型
category: 04-physics
kind: concept
version: 1.0.0
updated: 2026-09-22
tags: [物理, 总览, 选型, SMP, CBPC, HDT-PE]
aliases: [物理方案, 选哪个物理, smp 还是 cbpc, 物理总览, hdt, 抖动原理]
source: https://www.nexusmods.com/skyrimspecialedition/mods/57339
summary: 三代物理方案（HDT-PE / HDT-SMP / CBPC）的原理差异与适用场景，以及"SMP 与 CBPC 争同一插槽"这个必踩的坑和它的解法。
---

# 物理方案总览与选型

## 三代方案

| 方案 | 原理层 | 精度 | 性能 | 状态 |
|---|---|---|---|---|
| **HDT-PE**（Physics Extension） | 用游戏内建 **Havok** 做**骨骼级**碰撞 | 粗 | 一般 | 已被 SMP 取代；旧身形仍可用 |
| **HDT-SMP**（Skinned Mesh Physics） | 用 **Bullet** 做**逐顶点蒙皮网格**物理 | 高 | 重 | 当代主选（实际用其 fork **FSMP**） |
| **CBPC**（CBP Physics with Collisions） | **球体 / 胶囊近似**的逐帧模拟 | 中 | 轻（对 CPU 友好） | 当代主选（身体部位） |

**一句话选型**：

> **身体用 CBPC，头发和衣服用 HDT-SMP。**

这条经验来自机制差异，不是玄学：

- CBPC 用近似体，跑大量 NPC 时开销可控，适合"每个 NPC 都有的身体"；
- SMP 逐顶点计算精确，适合网格不大但需要精细摆动的东西（头发、斗篷、裙子）；
- **CBPC 完全无法处理头发和衣服物理**（它没有对应网格的蒙皮信息）。

## SMP 与 CBPC 的关键区别再展开

| | HDT-SMP / FSMP | CBPC |
|---|---|---|
| 模拟对象 | 网格顶点（蒙皮） | 骨骼挂的球/胶囊体 |
| 配置文件 | `hdtSkinnedMeshConfigs/*.xml`（FSMP 4.x 起全局配置改用 JSON） | 预设 XML / `cbp.dll` 配置 |
| 前置 | SKSE64 + Address Library；早期需 **OpenCL 2.0**（可切 CPU 模拟） | SKSE64、XPMSE、FNIS |
| 作用于 | 只附加到 **XPMSE 的 human skeleton** | XPMSE 骨骼 |
| 能管头发/衣服 | **能** | **不能** |

## 必踩的坑：两个 dll 争 body 插槽

SMP 与 CBPC **想挂的是同一批骨骼**，同时启用会互相覆盖。要"身体用 CBPC、衣服头发用 SMP"，
必须做下面两件事之一：

1. **编辑 `defaultBBPs.xml`**，让 SMP 忽略身体、只管头发/衣服；
2. **把 `cbp.dll` 改名为 `zcbp.dll`**，让 SMP 的 dll 先加载（利用加载顺序），
   或用 Engine Fixes 的 preload 机制。

> 这条是社区经验，但在多个帖子里被反复给出同一解法，可信度较高。

## 与身形的耦合

物理**不是独立层**，它依赖身形的两个条件：

1. 身形必须选 **physics 变体**（如 3BA 的物理版本、BHUNP 的 3BBB）；
2. 必须在 **BodySlide 构建带物理的身形**。

所以"装了 FSMP 还是不抖"的第一检查点不是物理 mod，而是**身形装的是不是物理版**。

## 与骨骼的耦合

所有现代身形与物理都**依赖 XPMSE 提供的额外骨骼节点**
（如 `HDT LBreasts`、`HDT Belly`、`NPC L/R Breast` 等）。
没有 XPMSE 就没有"可挂物理的骨"。详见 [`xpmse-skeleton.md`](xpmse-skeleton.md)。

## 诊断入口

物理不生效的完整排查见 [`../06-troubleshooting/physics-not-working.md`](../06-troubleshooting/physics-not-working.md)。

## 来源

- HDT-SMP 原理（Bullet、蒙皮网格）与"只附加 XPMSE human skeleton"：
  HDT-SMP Nexus 页描述 + 原始仓库 —— **一手**
  `https://www.nexusmods.com/skyrimspecialedition/mods/30872`
- CBPC 基于 polygonhell 的 CBP、球体近似、依赖：CBPC 页描述经转述 —— **一手（经转述）**
- "SMP 适合衣服、CBPC 适合身体"、"CBPC 不能管头发和衣服"：**社区经验（LoversLab 多帖一致）**
- `cbp.dll → zcbp.dll` 改名 / `defaultBBPs.xml` 调整：**社区经验（LoversLab 帖，多帖一致）**
- HDT-PE 用游戏内建 Havok：HDT-PE 原作者描述 —— **一手**
