---
id: xpmse-skeleton
title: XP32 Maximum Skeleton Extended（XPMSE / XPMSSE）
category: 04-physics
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [物理, 骨骼, XPMSE, XPMSSE, 节点]
aliases: [xp32, xpmss, 骨架, skeleton, 骨骼节点, 武器挂点]
source: https://www.nexusmods.com/skyrimspecialedition/mods/1988
summary: XPMSE 解决什么问题、四类骨骼节点前缀（NPC / HDT / MOV / CME）的含义、它与 RaceMenu 的插件关系，以及"绝不删 skeleton_female.hkx"这条警告。
---

# XP32 Maximum Skeleton Extended

全称 **XP32 Maximum Skeleton Special Extended（XPMSSE）**，前身 XPMSE。
原作者 **XP32**，现由 **Team XPMSE** 维护，主要维护者 **Groovtma**、**Skulltyrant**。

Nexus：`https://www.nexusmods.com/skyrimspecialedition/mods/1988`

## 它解决什么

为 **HDT 物理（PE / SMP）** 和游戏内骨架自定义提供**扩展骨骼节点与行为文件**。具体包括：

- 额外骨骼节点（物理需要挂点）；
- 武器位置风格（背挂/腰挂等）；
- 身形缩放；
- 内置 Realistic Ragdolls & Force、Flimsy Ragdolls；
- 兽人尾巴/翅膀等支持。

## 为什么它是"必装"

1. **物理必须挂在 XPMSE 的节点上**：HDT-SMP 明确只把网格附加到
   **XPMSE 的 human skeleton**（这条设计还顺带修掉了 Lurker 等非人骨架被物理破坏的问题）。
2. **身形与物理都假设这些节点存在**：3BA、BHUNP 的物理骨骼都在这套命名下。
3. **无完整替代品**：截至 2026 仍是事实标准前置。Pandora 行为引擎有 XPMSE 补丁，
   但骨架本身仍依赖 XPMSE。

## 四类骨骼节点前缀（重要）

| 前缀 | 含义 | 例子 |
|---|---|---|
| **`NPC`** | 标准网格骨骼 | `NPC L Hand [LHnd]`、`NPC R Hand [RHnd]`、`NPC L/R Breast`、`NPC L/R Breast01`、`NPC Belly`、`NPC Pelvis [Pelv]`、`NPC Spine [Spn0]` |
| **`HDT`** | **HDT 专用运动骨** | `HDT Belly`、`HDT LBreasts` 等 |
| **`MOV`** | 武器插槽节点 | `Weapon Left` / `Weapon Right`、`NPC L/R Item01~03` |
| **`CME`** | 额外 CME / RaceMenu 骨 | 由 RaceMenu / ECE 自定义数据设置 |

两条由此推出的规则：

- **`HDT`/`MOV` 前缀的节点不要改名**（可以改位置/旋转，但名字是接口）；
- **旧版 XML 里用 `NPC PreBelly` 是错的** —— XPMSE 2.0+ 起该骨已改名 `HDT Belly`，
  用旧名会导致低 FPS 甚至 CTD。

**历史变更**：XPMSE 4.72 移除了 `Prebreast` 骨（CBPC 不再需要它）。

## 与 RaceMenu 的关系

XPMSE 附带一个 **RaceMenu 插件（XPMSSE RaceMenu）**，提供：

- 武器风格；
- 缩放 / 位置 / 旋转滑杆；
- 身形相关滑杆；
- SOS / SAM 滑杆；
- 兽人种族滑杆；
- 第一 / 第三人称缩放。

要求 RaceMenu 0.4.2+（LE 旧版 3.4.5+）。

## 版本与前置

| 项 | 值 |
|---|---|
| 最新版本 | **5.06**（2024-02-11，针对 SE/AE）；前有 5.05（2023-12-09）、5.04（2023-08-19） |
| SKSE64 | 需要 |
| 行为补丁 | FNIS SE 7.2+ 或 Nemesis（跑一次以生成行为文件） |
| RaceMenu | 用其 RaceMenu 插件时需要 |

> ⚠️ **版本号来源**：Nexus 页本轮未能直读（描述页受限），5.06 来自镜像站转载的 changelog ——
> **标注为"经转述"，请以 Nexus Files 页为准**。

## ⚠️ 一条硬警告

> **不要删除 `skeleton_female.hkx`。**

它被游戏与多个 mod 假定存在；删掉会引发难以定位的问题。

## 来源

- 全称、维护团队、功能清单、前置、版本：Nexus 发布页（经镜像站转述 changelog）—— **一手（经转述）**
- "SMP 只附加到 XPMSE human skeleton"：HDT-SMP Nexus 页描述 —— **一手**
- 四类节点前缀：XPMSE 官方 FOMOD 说明（经 3DM 与俄站转述）—— **官方说明，经转述**
- `NPC PreBelly` → `HDT Belly`、4.72 移除 `Prebreast`：changelog 经转述 —— **中（经转述）**
- "不要删除 `skeleton_female.hkx`"：官方说明经转述 —— **中（经转述）**
- "无完整替代"：**社区经验（多源一致）**

> ⚠️ 本条目中"经转述"的版本号与 changelog 细节，**建议在能访问 Nexus 时复核一次**。
