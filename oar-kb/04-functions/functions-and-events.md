---
id: functions-and-events
title: 函数系统与 OAR 自定义动画事件
category: 04-functions
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 函数, OnTrigger, 动画事件, OAR 事件]
aliases: [OAR 函数, 自定义动画事件, functions, 发事件, SendAnimationEvent]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: 函数是 submod 触发的游戏行为，可在动画开始/结束/指定动画事件时运行；OAR 还注册了一个不需要行为补丁的虚拟动画事件 "OAR"，可在点号后带任意载荷。
---

# 函数系统与 OAR 自定义动画事件

## 函数是什么

> 函数本质上是 submod 可以触发的**游戏事件**。函数可以在动画**开始**、**结束**，或**在指定的动画事件上**运行。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

用法上与条件很像：

> 函数在很多方面的用法跟条件类似。**有函数集（function sets）**，就像条件集一样；也有可以容纳子函数集的**多元函数（multifunctions）**。
> 还有一个多元函数**内含条件集**，只有条件通过时其子函数才会运行。这应该能让 modder 用这套系统做出挺有意思的东西。
> 和条件一样，**其他插件可以通过 API 添加自定义函数**。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

**函数系统是 3.0.0 才上线的。** 变更日志原文就是干脆的一句「Added FUNCTIONS.」

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（3.0.0 变更）

## 可用函数清单

| 函数 | 引入 | 作用 |
| --- | --- | --- |
| **PlaySound** | 3.0.0 | 在 ref 位置播放声音 |
| **ModActorValue** | 3.0.0 | 修改某个 Actor Value |
| **SetGraphVariable** | 3.0.0 | 设置行为图变量 |
| **ModifyGraphVariable** | 3.1.0 | **修改**行为图变量 |
| **SendAnimEvent** | 3.0.0 | 发送行为图事件 |
| **CastSpell** | 3.0.0 | 施放法术 |
| **DispelSpell** | 3.0.0 | 驱散法术 |
| **SpawnParticle** | 3.0.0 | 生成粒子 |
| **UnequipSlot** | 3.0.0 | 卸下指定槽位的物品 |
| **SetPlaybackSpeedMultiplier** | 3.2.0 | 设置当前动画剪辑的**播放速度倍率** |

### 多元函数（multifunctions）

| 多元函数 | 引入 | 作用 |
| --- | --- | --- |
| **CONDITION** | 3.0.0 | 仅在指定条件为真时，运行其包含的一组函数 |
| **RANDOM** | 3.0.0 | 从包含的函数组中**随机**运行一个 |
| **ONE** | 3.0.0 | 自上而下依次尝试运行函数组中的函数，**直到第一个成功为止**。主要配合 `CONDITION` 使用，或与其他"自带内部检查再运行"的函数搭配 |
| **FILENAME** | 3.1.0 | 仅当当前替换动画**文件名匹配**时，才运行其包含的函数组 |

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

### 3.0.0 已支持注释

**3.1.0** 起条件与函数都支持**注释**：

> Mod 作者可以右键点条件/函数，选择 "Edit comment" 来设置注释。已有实现自定义条件的插件必须用新的 OAR Condition API 版本重新编译才能获得这个功能。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（3.1.0 变更）

## OAR 自定义动画事件（重要）

> OAR 还给游戏加了一个**自定义动画事件**，叫 **"OAR"**。它**不需要行为补丁就能被识别**。这个事件的目的，是让动画 mod 更容易用一个**带载荷（payload）的虚拟事件**去触发函数，而不必去复用某个原版游戏事件。
>
> 想在动画里播两个声音？给你的动画加上 **`OAR.sound1`** 和 **`OAR.sound2`** 两个事件（**点号后面的载荷可以是任意文本**），然后在 OnTrigger 集合里加两个 **PlaySound** 函数：一个触发于 `OAR.sound1`，另一个触发于 `OAR.sound2`。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

### 为什么这条很关键

「**不需要行为补丁**」意味着：**你可以在不做行为文件编辑、不刷任何补丁器的前提下，让动画事件驱动游戏行为**。这是 OAR 从"只能换文件"跨到"能带动逻辑"的关键一步。

命名规律：`OAR.<任意文本>`。点号前的 `OAR` 是固定的，点号后的部分是**你自己定义的载荷**，用来区分同一动画里的不同触发点。

## 触发时机

| 时机 | 说明 |
| --- | --- |
| **动画开始** | 替换动画开始播放时 |
| **动画结束** | 替换动画结束时 |
| **指定动画事件** | 动画里带的注释事件（例如 `OAR.sound1`）触发时 |

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（functions can run when an animation starts, ends, or on a specified animation event）

## 与"忽略 No Triggers 标记"的关系

⚠️ 有个容易踩的坑：**原版某些动画剪辑带着 `No Triggers` 标记**，它会让**带触发器的注释事件被忽略**——包括你的替换动画。所以即使你正确加了 `OAR.xxx` 事件，也可能不触发。

解法是打开 submod 的附加设置 **「忽略 No Triggers 标记」**（作者 0.5.0 引入时的原话）：

> 有些原版动画剪辑上设了一个特定 flag，出于某种原因会导致**任何带触发器的注释都被忽略**。这对**替换动画**同样成立——所以如果你替换的那个原版动画带这个 flag，而你又在注释里加了动画事件，它们**就是不会运行**。启用这个设置后，该 flag 会被忽略，注释里的动画事件就能如期运行了。
>
> 我理论上可以直接全局忽略这个 flag，但我想 Bethesda 设它应该是有原因的。

> 来源：<https://bakemono.app/p/patreon/25643772/80271137>（0.5.1 开发日志）

## 相关

- [子模组附加设置与编辑器](../05-editor/in-game-editor.md)
- [条件系统总览](../03-conditions/conditions-overview.md)
- [插件 API 概览](../06-plugins/plugin-api.md)
