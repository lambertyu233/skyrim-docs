---
id: detection-plugin
title: Detection Plugin（检测条件扩展）
category: 06-plugins
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [OAR, Detection, 插件, DETECTS, DETECTED_BY, 潜行]
source: https://www.nexusmods.com/skyrimspecialedition/mods/104806
summary: Nonameron 用 OAR 插件 API 实现的检测条件扩展，提供 DETECTS / DETECTED_BY 两个容器条件与距离/关系/角度三个子条件；页面示例里的 IsPlayer 实为笔误，OAR 与本体均无此条件。
---

# Detection Plugin（检测条件扩展）

> **Open Animation Replacer - Detection Plugin**
> 作者：**Nonameron** ｜ 首次发布 2023-11-15 ｜ 当前版本 **2.1.5**（2026-09-03）
> Nexus mod **104806** ｜ 前置：**OAR 本体**（无需行为补丁、无需 Nemesis/Pandora）

## 它做什么

官方原话：

> 给 Open Animation Replacer 添加两个可用于触发动画的条件。它们是：
> **DETECTED_BY**、**DETECTS**
> 另外还有三个**只能与（且仅与）这两个条件配合使用**的子条件：
> **DetectionDistance**、**DetectionRelationship**、**DetectionAngle**

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/104806>

一句话：它把游戏**潜行侦测系统**的结果暴露成动画条件，让动画能对"**谁看见了谁**"做出反应。

## 两个容器条件

| 条件 | 语义（官方示例） |
| --- | --- |
| **DETECTED_BY** | 当**存在一个满足子条件的 actor 侦测到本 actor（或玩家）**时触发 |
| **DETECTS** | 当**本 actor（或玩家）看见一个满足子条件的 actor**时触发 |

官方示例（原文）：

```
DETECTED_BY
    IsFemale
    IsInFaction 00086EEE (GuardFaction)
```
→ 玩家（或 NPC）**被一个女守卫侦测到**时触发。

```
DETECTS
    IsPlayer
```
→ **有一个 actor 看见了玩家**时触发。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/104806>

## 三个子条件

### DetectionDistance

> **按距离限制检测。必须直接放在 `DETECTS` 或 `DETECTED_BY` 下面，否则什么都不做。**

示例（原文）：

```
DETECTS
    IsFemale
    DetectionDistance < 500
```
→ 玩家（或 NPC）**看见 5 米内的一个女性**时触发。

```
DETECTED_BY
    IsInFaction 00086EEE (GuardFaction)
    DetectionDistance > 1000
```
→ 玩家（或 NPC）**被 10 米之外的一个守卫看见**时触发。

**单位是"游戏单位"**，示例里 `< 500` 对应"5 米"、`> 1000` 对应"10 米"。

### DetectionRelationship

> **按关系限制检测。必须直接放在 `DETECTS` 或 `DETECTED_BY` 下面，否则什么都不做。**

数值表（官方原文）：

| 值 | 关系 |
| --- | --- |
| **-4** | Archnemesis（死敌） |
| **-3** | Enemy（敌人） |
| **-2** | Foe（敌对者） |
| **-1** | Rival（对手） |
| **0** | Acquaintance（泛泛之交） |
| **1** | Friend（朋友） |
| **2** | Confidant（密友） |
| **3** | Ally（盟友） |
| **4** | Lover（恋人） |

示例：

```
DETECTS
    DetectionRelationship() = 4.0
```
→ 看见自己的恋人时触发。

### DetectionAngle

> **按角度限制检测。** 角度是**在 `DETECTS` 里**"侦测者朝向"的偏差，**在 `DETECTED_BY` 里**则是"被侦测者朝向"的偏差。
> 可以用 **"Swap actor"** 这个 flag 把角度改成从**另一个 actor** 出发（`DETECTED_BY` 里的侦测者，或 `DETECTS` 里的被侦测者）。
> **必须直接放在 `DETECTS` 或 `DETECTED_BY` 下面，否则什么都不做。**

官方举例：

> 如果检测角度设成 `< 45`，而玩家正朝东看，那么这个条件会在玩家看到**位于他东北到东南之间**的 actor 时触发。

示例：

```
DETECTED_BY
    IsInFaction 00086EEE (GuardFaction)
    DetectionAngle < 30
```
→ 玩家（或 NPC）**被一个位于其朝向 ±30 度内的守卫看见**时触发。

配套的组件还有 **"Limit detection to right side"** / **"Limit detection to left side"** 两个方向开关（源码里确认存在）。

## ⚠️ 勘误：页面示例里的 `IsPlayer` 不存在

官方页面里 `DETECTS` 的示例写的是：

```
DETECTS
    IsPlayer
```

**但 `IsPlayer` 并不是 OAR 的条件。** 本库做了两处源码核对：

1. **OAR 本体**：`src/Conditions.h` 中注册的条件名**共 125 个**，包含 `IsPlayerTeammate`，**但不含 `IsPlayer`**。
2. **Detection Plugin**：其源码中注册的条件名只有 **`DETECTED_BY`、`DETECTS`、`DetectionDistance`、`DetectionRelationship`、`DetectionAngle`** 五个，**也不含 `IsPlayer`**。

> 来源（核对）：`github.com/ersh1/OpenAnimationReplacer` 的 `src/Conditions.h`；`github.com/matiasmakipelto/OpenAnimationReplacer-DetectionConditions` 的 `src/Conditions.h` / `src/Conditions.cpp`（2026-09-21）

**正确写法**：

| 想要的效果 | 写法 |
| --- | --- |
| 判"是玩家" | `IsForm` + Player（`Skyrim.esm` 的 `0x00000007`），或 `IsActorBase` + Player |
| 判"是玩家的随从" | `IsInFaction` 或 `IsPlayerTeammate` |
| 换求值对象为玩家 | 容器条件 [`PLAYER`](../03-conditions/condition-containers.md) |

> 这个笔误在社区里被反复传播（连 LoversLab 的求助帖里也照着抄了 `IsPlayer`）。遇到"照文档写却怎么都不触发"的情况，先怀疑这里。

## 工作原理与判定规则

官方页面没展开讲底层，但社区与源码侧能确认几点：

- 判定基于游戏原生**侦测等级**；天然受**视线（LOS）、光照、潜行技能、距离、角度**等原版潜行机制影响。
- 以下对象**被排除**：**自己**（target == actor）、**已删除/已禁用**的 actor、**`ManakinRace`**（人偶/展示用种族）。
- 求值成功时，条件会显示**侦测者的名字**作为"当前值"，便于在编辑器里调试。

> 来源：`matiasmakipelto/OpenAnimationReplacer-DetectionConditions` 源码中出现 `ManakinRace` 排除逻辑；`Sources` 说明见 <https://www.nexusmods.com/skyrimspecialedition/mods/104806>
> （"排除自己/已删除/ManakinRace"与"显示侦测者名字"这两条来自社区与源码侧整理，非官方描述原文，标记为**社区/源码事实**。）

## 典型用法（官方用例清单）

官方给的"你能做什么"：

> - 玩家看到守卫时**竖中指**
> - 玩家看到生物时**走得更猥琐**
> - 玩家看到 **Nazeem** 时表现出**厌恶**
> - NPC 看到玩家时**移开视线**
> - 玩家看到**远处的人**时**望向远方**——或者如果你的角色近视，就**凑近看**
> - 想让玩家对你的**自定义 NPC** 有独特反应时也特别合适：在 ta 附近**走得更娇羞**之类

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/104806>

## 怎么拿到它（社区补充）

LoversLab 上的求助帖里，有人想区分"随从和玩家用不同 idle"时，得到的第一条建议就是：

> 你可以试试 Detection Plugin。你的随从应该在某个人 "followers" 派系里……所以你可以在里面用 `IsInFaction`，而你自己有 …… 对玩家用相应的条件。

> 来源：<https://www.loverslab.com/topic/245858-how-to-have-both-follower-and-pc-play-idle-animations-with-oar-conditions>

## 相关

- [插件 API 概览](plugin-api.md)
- [容器条件与子条件的挂载规则](../03-conditions/condition-containers.md)
- [条件全清单](../03-conditions/conditions-list.md)
