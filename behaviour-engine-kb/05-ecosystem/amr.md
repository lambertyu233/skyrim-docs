---
id: amr
title: AMR 动画运动革命（Animation Motion Revolution）
category: 05-ecosystem
kind: concept
version: 1.0.0
updated: 2026-09-21
tags: [AMR, 位移, motion data, 注释, MCO, 生态]
aliases: [Animation Motion Revolution, 动画运动, 滑步修复, motion revolution]
source: https://www.nexusmods.com/skyrimspecialedition/mods/50258
summary: AMR 让每条动画都能携带自定义位移/旋转数据，解决"滑步"问题；Pandora 官方点名它取代了旧的 baked motion data 方案。
---

# AMR 动画运动革命（Animation Motion Revolution）

## 它解决什么问题

官方描述（大意）：

> 原版里"动画只是门面"——移动由一堆预设值驱动，动画动作与实际位移脱节。
> AMR 让玩家第一次能**为每条动画单独定义角色的真实位移**，实现"每个武器/每个敌人甚至每个生物都有独一无二的移动"。动画与位移可被完美匹配，战斗手感更接近现代动作游戏。

**技术手段：动画注释（annotation）**。插件读取动画里携带的 motion 数据注释，注入游戏引擎来移动角色。注释正确则位移与动画完美同步。

> 来源：AMR Nexus 描述 https://www.nexusmods.com/skyrimspecialedition/mods/50258

## 注释格式（作者向）

用 `hkanno64` 工具往动画里加注释。

- 位移：`[time] animmotion [x] [y] [z]`（time 单位为秒，与 Bethesda 在 animationdatasinglefile.txt 里的数值同尺度、同格式）
- 旋转：`[time] animrotation [degrees]`（例：1.5 秒内转 360° → `0.5 animrotation 90` / `0.9 animrotation 180` / `1.2 animrotation 270` / `1.5 animrotation 360`）

位移与旋转注释可混用。

## 生效条件

AMR 对**任何关联到开启了 `bAllowRotation` 或 `bAnimationDriven` 的 behavior** 的动画生效——这会强制游戏依据 motion data 移动角色（原版的重击、踉跄、部分杂物交互默认就开了）。用 **Skyrim Behavior Tool** 可改行为修饰符，给更多动画类型开启位移驱动。

## 生态配套

| 配套 | 作用 |
| --- | --- |
| **MCO**（Modern Combat Overhaul） | 基于 AMR 开发，让**普通攻击**（而非仅重击）也由 motion data 驱动；用同一套注释系统进一步扩展 |
| **SCAR**（Skyrim Combos AI Revolution） | 让 NPC 智能调用带自定义位移的攻击动画 |
| **DAR/OAR** | 变体动画按条件替换 |

## 与 Pandora 的关系

Pandora 官方对比表脚注把 **baked motion data**（把位移"烘焙"进动画的旧做法）列为**已被 AMR 淘汰**的特性，因此 Pandora **不再支持那套旧机制**：

> baked motion data obsolete by AMR

也就是说：现代方案是"动画 + AMR 注释"，而不是旧式烘焙。这就是为什么 Pandora 允许自己"不支持旧特性"——因为有更好的替代。

> 来源：Pandora 官方 Wiki https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/wiki

## 相关

- [OAR / DAR](oar-dar.md)
- [相关工具链](related-tools.md)
- [官方三引擎对比表](../00-overview/engine-comparison.md)
