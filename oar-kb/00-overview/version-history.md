---
id: version-history
title: 版本迭代史与关键节点
category: 00-overview
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 版本, 历史, 更新日志, Patreon]
aliases: [OAR 更新日志, OAR 版本, 新增了什么条件, changelog, oar 0.5.0, 版本变化]
source: https://bakemono.app/p/patreon/25643772/79535580
summary: OAR 的机制解释大量只存在于作者 Ersh 的 Patreon 开发日志里；本页把 0.3 → 0.8 → 1.0 → 3.2 的关键节点按时间线整理，并给出各版本新增的条件与函数。
---

# 版本迭代史与关键节点

## 为什么需要这一页

OAR **没有 wiki**。它很多机制的设计动机和"为什么是这个形状"，只出现在作者 **Ersh 的 Patreon 开发日志**里。这些帖子是公开可读的一手资料，但散落且不好检索——本页把它们按时间线收拢。

> 来源（Patron 帖）：<https://bakemono.app/p/patreon/25643772/79535580>（status update）、`/80271137`（0.5.1）、`/80648390`（0.6.1）、`/81916525`（0.8.0）、`/86003539`（Paired Annotation Fix test）、`/83900406`（Released）

## 时间线

| 阶段 | 版本 | 关键节点 |
| --- | --- | --- |
| 测试期 | 0.3 | 作者在尝试翻倍 32k 动画上限时，**偶然发现一个极简改动能几乎完全绕过动画队列**——不再需要手动加载所有替换动画、不再等队列、不再 T-Pose。改动"只是一个 bool"，但当时极不稳定（0.3.1 被撤下、0.3.2 加互斥量回退）。 |
| 测试期 | 0.5.x | **新结构首发**：replacer mod → submod 两级结构、编辑器大改（可增删改条件、改顺序、改优先级）、multicondition 可嵌套。0.5.0 引入 `IsEquippedShout`（并**纠正**了 DAR 里它其实检查的是 Power 这一历史误解）、图变量条件、**必需项目名**、**忽略 No Triggers 标记**。 |
| 测试期 | 0.6.1 | 修掉一个**自 OAR 诞生起就存在的重大 bug**：同步动画（killmove、上马）会因 `DefaultMale` / `DefaultFemale` 项目动画数量不同而失败——这是 Bethesda 的一个游戏 bug/假设；DAR 因为总是把整个动画数组填满空字符串所以不会触发。同时新增"为用户配置面向 legacy mod 保存"的能力，以及默认开启的 `Hook Animation Manager` 实验设置。 |
| 测试期 | 0.8.0 | **破坏性变更**：条件系统又一次大重构（这次是为了让插件 API 能注册新条件），**所有 `.json` 作废需重建**。同版新增：动画日志 overlay、**动画文件夹覆盖**、**重复动画过滤（内容哈希去重）**、**SKSE 插件 API**、**Echo 上也能触发替换**。 |
| 发布前 | 实验版 | `Paired Annotation Fix`（独立的配对动画注释修复插件）：作者搞清楚了配对动画的工作原理，并发现原版一个 issue——配对动画里的 annotation 触发器（动画事件）不会执行。 |
| 1.0 | 发布 | 正式上架 Nexus。部分条件与组件在发布前被**再次改名**（`.json` 又坏一次，作者承诺此后保持兼容）。 |
| 2.x 系列 | 2.0.0 / 2.1.0 / 2.2.0 / 2.3.x | 2.0.0：replacer mod 可放在 `Data\Meshes` 内**任意位置**。2.1.0：`XOR` 条件、动画**事件**日志。2.2.0：**PRESET**、`MOUNT`、**变体顺序模式（Sequential）**、附魔/攻击类型类条件。2.3.0：楼梯/材质/超负重/非法闯入/守卫等条件。 |
| 3.x 系列 | 3.0.0 – 3.2.1 | 3.0.0：**FUNCTIONS（函数）** 系统上线、`OAR` 虚拟动画事件、动画日志 **"show trace"**、`CurrentPackageProcedureType` → `CurrentPackageType` 改名、修 `IdleTime` 计时器 bug、修配对动画失同步。3.1.0：条件/函数支持**注释**、修 3.0.0 引入的 `IsEquippedShout` 被运行时改成 `IsEquippedPower` 的 bug、条件/函数 API 更新。3.2.0：`HasBoundWeaponEquipped`、`SetPlaybackSpeedMultiplier`。3.2.1：当前版本。 |

> 来源（发布后的版本变更）：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（描述页与 Changes 区）

## 当前版本（截至 2026-09）

- **本体**：**3.2.1**，最后更新 2026-09-01。
- **配套插件**：Detection Plugin **2.1.5**（2026-09-03）、Math Plugin **1.0.5**（2026-08-31）、IED Conditions **1.0.2**。

> 来源：各 mod 的 Nexus 页面（见 [官方来源清单](../09-sources/official-sources.md)）

## 需要留意的两点

1. **`.json` 曾经坏过好几次**（0.5.1、0.8.0、1.0 发布前）。作者说 1.0 之后会保持兼容。因此如果你看到"0.5.1 的压缩包里有 readme"这类老说法——**那是 2023 年测试版的情形，对现在的 3.x 不适用**。
2. **插件 API 有版本要求**：自定义条件的插件（Detection 等）在 OAR 大版本更新后往往需要重新编译或更新。3.0.0 与 3.1.0 都注明"已有自定义条件插件必须用新的 API 重新编译"。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（3.0.0 / 3.1.0 变更条目）

## 相关

- [OAR 是什么](what-is-oar.md)
- [插件 API 概览](../06-plugins/plugin-api.md)
- [Detection Plugin](../06-plugins/detection-plugin.md)
