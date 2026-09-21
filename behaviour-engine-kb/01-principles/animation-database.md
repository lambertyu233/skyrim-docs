---
id: animation-database
title: 动画数据库与事件名：引擎到底往文件里写了什么
category: 01-principles
kind: concept
version: 1.0.0
updated: 2026-09-21
tags: [动画数据库, 事件名, scorrp10, 原理, animation-event]
aliases: [动画数据库在哪, 事件名从哪来, animation database, 行为文件写什么, hkx 里的动画列表]
source: https://forums.nexusmods.com/topic/13497416-open-animation-replacer-a-pose/
summary: 游戏内部有一张"动画字符串 → hkx 文件"的数据库表，新增动画就是往这张表里加新条目——这是动作引擎的核心工作对象。
---

# 动画数据库与事件名：引擎到底往文件里写了什么

## 资深玩家 scorrp10 的解释（社区公认转引）

关于"引擎到底干了什么"，社区里被反复转引的一段解释来自 Nexus 论坛上的资深玩家 **scorrp10**（非官方，但被广泛认可）：

> The game essentially has a database of animations, where a given string ultimately corresponds to an hkx file under `meshes\actors\character\animations`. I.e. "IdleWallLeanStart" animation event plays `meshes\actors\character\animations\wall_idlebackloop.hkx`, which is the vanilla wall lean animation.
>
> However, some mods add **entirely NEW animations** to the game. Such as posers, dance mods, adult mods, etc. These require the **animation database to be updated** in order to add new command strings, corresponding to new animation files (i.e. `"7GOM34"` → `meshes\actors\character\animations\GomaPeroPero1\7GOM34.hkx`) — and then these new animation commands will be invoked via mod scripts as necessary. **Updating of the database is what FNIS/Nemesis/Pandora does.**

翻译要点：

- 游戏里有一张**动画数据库**：一个**字符串（动画事件名）**最终对应到 `meshes\actors\character\animations` 下的某个 hkx 文件。
  - 例：动画事件 `"IdleWallLeanStart"` → 播放 `...\animations\wall_idlebackloop.hkx`（原版靠墙待机）。
- 有些 mod 往游戏里加**全新的动画**（摆姿势、跳舞、成人动画等）。这要求**更新动画数据库**，为新的 hkx 文件加上新的命令字符串（例：`"7GOM34"` → `...\GomaPeroPero1\7GOM34.hkx`），之后由 mod 的脚本按需调用这些新命令。
- **"更新动画数据库"就是 FNIS / Nemesis / Pandora 干的活。**

> 来源（社区）：scorrp10，Nexus 论坛，2024-12-30
> https://forums.nexusmods.com/topic/13497416-open-animation-replacer-a-pose/

## 由此推出的关键结论

1. **"新增动画"= 往数据库里加新行**；"替换动画"= 让已有行指向别的文件（这是 OAR/DAR 的活）。
2. 数据库就在**行为文件**里（上文说 hkx 是包格式、行为文件里含状态机与事件——数据库表也是行为图的一部分）。
3. 这也是为什么**必须按 modlist 现场生成**：每张表都是所有 mod 新加行的并集，别人的表不含你的 mod 的新行。
4. 这也是为什么**FNIS 有硬上限**：早期实现里新事件行的容量是有限的；后续引擎改成软上限/近乎无限，见 [三引擎对比](../00-overview/engine-comparison.md)。

## 名字必须一一对应

任何一个"新增动画"的 mod，都会同时提供两样东西：

- **动画文件**（hkx，放在 `animations` 下）；
- **数据库条目**（告诉引擎"事件名 X → 这个文件"）。

因此当"动画不生效"时，排查顺序通常是：**文件名（事件名）是否对 → 数据库条目是否被引擎读到 → 条件/优先级是否正确**。这与本工作区其他动画改造经验一致。

## 相关

- [Patcher 与 Replacer 的区别](patcher-vs-replacer.md)
- [hkx 其实有两种](hkx-two-kinds.md)
