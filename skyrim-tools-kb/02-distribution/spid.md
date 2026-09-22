---
id: spid
title: Spell Perk Item Distributor (SPID)
category: 02-distribution
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [分发, SKSE, 免冲突, 配置文件, powerofthree]
aliases: [Spell Perk Item Distributor, DISTR, distr ini, 分发法术, 给NPC发东西, 36869]
source: https://github.com/powerof3/Spell-Perk-Item-Distributor
summary: 用纯文本配置把法术/技能/物品/喊话/服装/关键词/派系分发给 NPC——不建插件、不碰记录，从根上消灭了「两个 mod 改同一个 NPC」的冲突。
---

# Spell Perk Item Distributor (SPID)

## 它消解的是什么问题

传统做法：想给所有强盗加一个新能力 → 编辑强盗的记录 → 建插件 →
**你的 mod 就与所有改过这些 NPC 的 mod 冲突了**，还得为每种组合做补丁，败者全盘失效。

SPID 改成**运行时分发**：写一行配置（分发什么 + 谁能拿到），游戏加载时应用。
**不编辑任何记录**，所以不存在数据冲突，基于 SPID 的 mod 是**叠加**而不是互相覆盖。

## 配置长什么样（社区教程口径）

配置文件放在 `Data/` 下，文件名以 `_DISTR.ini` 结尾。行格式（示意）：

```
Type = <FormID>~<Mod.esp> | <String 过滤> | <Form 过滤> | <需求:等级/技能> | <特征:性别/唯一/召唤物/儿童> | <数量> | <百分比几率>
```

可分发的 Type 覆盖 spells / perks / items / shouts / packages / outfits / keywords / factions。
过滤维度包括关键词、派系、种族、职业、战斗风格、等级、性别、是否 unique、EditorID 模式，
并且支持 `ALL` 组合（`X+Y+Z`）与 `NOT` 取反。
（来源：官方仓库 README + 社区教程；**具体语法以官方 README 为准，本文不复述全部字段**）

## 三条操作要点

1. **改 `_DISTR.ini` 要重新加载存档才生效**——分发发生在加载时，不是即时。
2. **移除"已经分发过的"东西不一定生效**：NPC 已经拿到的东西不会因为删掉配置就消失。
3. **它本身不产生任何内容**。单独装它毫无作用——它出现在你的下载列表里，
   只是因为你装的某个 NPC 类 mod 把它写进了 Requirements。

## 前置（官方 Requirements）

- **SKSE**（必需）
- **Address Library for SKSE Plugins**
- **powerofthree's Tweaks**（用于 EditorID 解析）

> ⚠️ 注意区分：**Tweaks** 是引擎修复（[powerofthree's Tweaks（引擎修复与调整）](../09-diagnostics/po3-tweaks.md)），
> **Papyrus Extender** 是脚本函数扩展（[powerofthree's Papyrus Extender](../01-frameworks/po3-papyrus-extender.md)）——
> 三个 po3 项目名字都带 po3，用途完全不同。

## 相关

- [Keyword Item Distributor (KID)](../02-distribution/kid.md)（同作者，把关键词分发给物品）
- [Base Object Swapper (BOS)](../02-distribution/bos.md)（同作者，运行时替换 base form）
- [SKSE64（Skyrim Script Extender）](../01-frameworks/skse64.md)、[Address Library for SKSE Plugins](../01-frameworks/address-library.md)
- [More Informative Console](../09-diagnostics/more-informative-console.md)（确认某个东西到底来自哪个 mod）
