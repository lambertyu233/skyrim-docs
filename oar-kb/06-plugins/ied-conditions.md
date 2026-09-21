---
id: ied-conditions
title: IED Conditions（Immersive Equipment Displays 联动条件）
category: 06-plugins
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [OAR, IED, Simple Dual Sheath, 插件, 拔收武器]
source: https://www.nexusmods.com/skyrimspecialedition/mods/98308
summary: SlavicPotato 做的 SKSE64 插件，让 OAR 能读到 Immersive Equipment Displays 与 Simple Dual Sheath 的数据；主用途是"按装备挂在哪里播不同的拔/收武器动画"。
---

# IED Conditions（Immersive Equipment Displays 联动条件）

> **Open Animation Replacer - IED Conditions**
> 作者：**SlavicPotato** ｜ 当前版本 **1.0.2**（2023-09-02）
> Nexus mod **98308** ｜ 源码在 GitHub：`SlavicPotato/OpenAnimationReplacer-IEDConditionExtensions`

## 它做什么

> 一个 SKSE64 插件，给 Open Animation Replacer 添加新条件，供 **Immersive Equipment Displays** 和 **Simple Dual Sheath** 使用。
> **目前的主要用例是：根据装备（武器）挂在哪里，播放不同的拔/收武器动画**（即"风格匹配的动画"）。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/98308>

## 前置需求（作者给 mod 用户的直白提示）

> - 安装 **Open Animation Replacer** 及其前置，然后通过 mod 管理器（或手动丢进 `Data`）安装本插件。它应该能在 **OAR 支持的任何游戏版本**上工作。
> - 按你所用动画替换器的要求，安装 **Immersive Equipment Displays（≥ 1.7.1）** 或 **Simple Dual Sheath（≥ 1.5.3）**。
> - **技术上它并不依赖 IED 或 SDS 任何一个**，但如果某个插件没找到，**它那组条件就不会提供给 OAR**。有些条件不绑定任何插件，始终可用。

作者还给 mod **用户**留了一段很实在的话：

> 如果你是因为某个 OAR mod 把它列为前置才来的，看上面。**如果你是偶然点进来的，就退出去吧，这个不是给你的。**

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/98308>

## 提供的条件

### 绑定 IED 的

| 条件 | 说明 |
| --- | --- |
| **`IED_GearNodePlacementHint`** | 检查装备节点的当前 placement hint 是否匹配 **'Weapon placement ID'** 参数（按所选 `Comparison` 运算符）。装备节点由 **'Gear node ID'** 参数指定 |
| **`IED_GearNodeEquippedPlacementHint`** | 同上，但**装备节点由已装备的武器类型决定** |
| **`IED_GearNodeParentName`** | 检查装备节点当前**父节点名**是否等于 'Node name' 参数（**不区分大小写**）。装备节点由 'Gear node ID' 指定 |
| **`IED_PluginOption`** | 检查 IED 的各种设置 |

### 绑定 SDS 的

| 条件 | 说明 |
| --- | --- |
| **`SDS_IsShieldOnBackEnabled`** | 检查目标 ref 在 Simple Dual Sheath 里是否启用了**盾牌背在背上** |

### 通用（官方原话：尽管带前缀，**不绑定 IED 或 SDS 任何一个**）

| 条件 | 说明 |
| --- | --- |
| **`IED_HasEquipSlot`** | 检查目标 ref **手上装备的物品**是否配置了指定装备槽 |
| **`IED_IsBoundWeaponEquipped`** | 检查目标 ref **手上装备的物品**是否是**召唤武器**（1.0.1 新增） |

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/98308>

> 提示：`IED_IsBoundWeaponEquipped` 与 **OAR 本体 3.2.0 新增的 `HasBoundWeaponEquipped`** 功能重叠。装了新版 OAR 时，优先用本体条件，少一个依赖。

## 页面里给的辅助资料

官方描述里给了三类查表链接（原文指向社区维护的 ID 表）：

- **gear node IDs** 列表
- **Weapon placement IDs** 列表
- 某个具体 **MOV 节点**被分配了哪个 ID

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/98308>

## 版本与迭代

| 版本 | 变更 |
| --- | --- |
| 1.0.2 | 修复了一个**与旧版 IED/SDS 交互时可能崩溃**的问题 |
| 1.0.1 | 新增 `IED_IsBoundWeaponEquipped` 条件 |

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/98308>（Changelogs）

## 作者与致敬

> 致谢：SKSE 团队、Ryan（CommonLib）、**ersh（OAR）**、GiraPomba 催我做点这样的东西并在开发过程中提供帮助。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/98308>

## 相关

- [插件 API 概览](plugin-api.md)
- [条件全清单](../03-conditions/conditions-list.md)
- [实战：给特定武器绑特定动作](../08-practices/editor-workflow-weapon.md)
