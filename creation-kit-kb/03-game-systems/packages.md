---
id: packages
title: AI 包（Packages）
category: 03-game-systems
version: 1.0.0
updated: 2026-09-20
tags: [ai, packages, behavior, sandbox, ai-package]
source: https://ck.uesp.net/wiki/Packages
summary: AI 包是定义 NPC 行为的模板，控制其日程、移动与互动，如 Sandbox、跟随、巡逻等。
status: stable
kind: reference
---

# AI 包（Packages）

**Package（AI 包）** 是定义 Actor 行为的模板。通过组合不同的包，可让 NPC 拥有日程、巡逻、战斗、社交等丰富表现。

## 工作方式

- 每个 Actor 可分配一个或多个包；引擎按**优先级**与**条件**选择当前生效的包。
- 包内包含一系列**程序化动作（Procedure）**，如移动到某处、使用某物品、与某人互动。
- 条件（如时间、地点、任务阶段）决定包是否启用。

## 常见包类型

| 包类型 | 用途 |
| --- | --- |
| **Sandbox** | 让 NPC 在其居所/区域内自由活动（生火、坐下、打扫等）。 |
| **Follow / Escort** | 跟随或护送目标。 |
| **Patrol / Travel** | 沿路线巡逻或前往指定地点。 |
| **Guard / Combat** | 守卫站位与战斗行为。 |
| **Use Item At / Acquire** | 使用或获取物品。 |

## 设计要点

- 用 **Sandbox** 作为默认包，叠加特定情境包覆盖。
- 避免多个高优先级包冲突导致 NPC「卡住」——注意条件互斥。
- 自定义复杂行为可参考 [Hold Position Packages](https://ck.uesp.net/wiki/Hold_Position_Packages) 等社区范例。

## 相关条目

- [任务系统](quests.md)
- [Radiant Story](radiant-story.md)
- [术语表](../02-features/glossary.md)

> 来源：[UESP Packages](https://ck.uesp.net/wiki/Packages)
