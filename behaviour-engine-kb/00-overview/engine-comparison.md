---
id: engine-comparison
title: 官方三引擎对比表（附解读）
category: 00-overview
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [对比, 表格, FNIS, Nemesis, Pandora, 选型]
source: https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/wiki
summary: Pandora 官方 wiki 首页的三引擎对比表（原表直录 + 逐项解读），是本领域唯一成体系的官方对比文档。
---

# 官方三引擎对比表（附解读）

## 原表（Pandora 官方 Wiki 直录）

| 项目 | **Pandora** | **Nemesis** | **FNIS** |
| --- | --- | --- | --- |
| **OS** | Windows / Linux / MacOS | Windows / Linux | Windows |
| **Game** | Skyrim SE / AE | Skyrim SE / AE | Skyrim SE / AE / LE |
| **Support（支持对象）** | Humans & creatures | Humans & some creatures | Humans & creatures |
| **Patching（打补丁方式）** | Behavior, Imperative | Behavior, Imperative | Behavior, Declarative |
| **Export（导出工具）** | HKX2E | HKXCMD | HKXCMD |
| **Cross-Compatibility（交叉兼容）** | 大多数 FNIS mods & 全部 Nemesis mods* | 几乎所有 FNIS mods | 仅自家格式 |
| **Source（开源）** | Open Source (GPL v3) | Open Source (GPL v3) | Closed Source |
| **Animations（加动画方式）** | 经 behavior 或 animlist | 经 behavior 或 animlist | 仅经 animlist |

> \* Pandora 不支持那些**已有现代替代方案**的 FNIS/Nemesis 特性，例如：Sexy Move、PCEA（已被 **OAR** 取代）、baked motion data（已被 **AMR** 取代）。

> 来源：Pandora 官方 Wiki https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/wiki

## 逐项解读

- **OS / Game**：Pandora 跨三平台且覆盖 SE/AE；Nemesis 无 MacOS；只有 FNIS 还在支持 **LE（传奇版）**。LE 玩家基本只能留在 FNIS 或旧 Nemesis。
- **Support**：注意此处**三家写法不同**。Pandora 与 FNIS 是"人形 + 生物"；Nemesis 是"人形 + **部分**生物"。中文社区常简化成"FNIS 支持生物、Nemesis 不支持生物"，严格来说 Nemesis 是**部分支持**，生物动画不完整。
- **Patching**：FNIS 是**声明式**（你声明要什么，它按固定方式拼）；Nemesis/Pandora 是**命令式**（提交具体编辑指令），后者才支撑得起任意新动画类型。
- **Cross-Compatibility**：Nemesis 能吃"几乎所有 FNIS mod"；Pandora 能吃"大多数 FNIS mod + 全部 Nemesis mod"。迁移到 Pandora 时，Nemesis 侧几乎无损。
- **Source**：FNIS 闭源，这是它无法被社区接手、最终被淘汰的根本原因；Nemesis/Pandora 都是 GPLv3。
- **Animations**：FNIS 只能靠 animlist；后两代既能靠 behavior（补丁）也能靠 animlist。

## 表里没说的三件事（社区补充）

1. **文档完备度**：Nemesis 中级以上用法**没有公开文档**，官方描述页原话是"请直接通过 Discord 联系 Shikyo Kira"。Pandora 有官方 Wiki（就是本文来源）。
2. **大 modlist 下的稳定性**：社区普遍反馈 Nemesis 在动画数量极大时易崩溃/需反复重跑，Pandora 更快更稳（但仍有零星小 bug）。详见 [Nemesis 的局限](../03-nemesis/nemesis-limitations.md)。
3. **FNIS 已停更**：7.6 版、2020-02-21 最后一次更新，见 [FNIS 概览](../02-fnis/fnis-overview.md)。

## ⚠️ 使用本表的注意

社区二手文章（含部分中文站与 AI 站点）常把 Pandora 说成"Nemesis 的 fork（分支）"——**这是错的**。Pandora 是一套独立实现的新引擎，只是**兼容** Nemesis/FNIS 的补丁格式。以官方 wiki 的表述为准。
