---
id: script-object-actor
title: Actor 脚本对象
category: 04-scripting
version: 1.0.0
updated: 2026-09-20
tags: [papyrus, script-object, actor, native]
aliases: [Actor 脚本, 脚本对象 Actor, actor 引用, GetActorReference]
source: https://ck.uesp.net/wiki/Actor_Script
summary: 代表游戏中可活动角色（NPC / 生物）的脚本基类，提供属性、装备、战斗、法术等原生函数。
status: stable
kind: reference
---

# Actor 脚本对象

代表游戏中可活动角色（NPC / 生物）的脚本基类，提供属性、装备、战斗、法术等原生函数。

> 来源：https://ck.uesp.net/wiki/Actor_Script

## 概述

本条目汇总该 Papyrus 脚本对象最常用的原生（native）函数。所有函数均来自游戏引擎暴露，无法在脚本中重写其实现。完整列表与参数请以官方页面为准。

## 常用函数

| 函数 | 说明 |
| --- | --- |
| `GetActorValue - Actor` | 读取某项 Actor Value（如 Health、Magicka）的当前值。 |
| `SetActorValue - Actor` | 直接设置某项 Actor Value 的当前值。 |
| `DamageActorValue - Actor` | 对某项 Actor Value 造成扣减（不触发永久修改）。 |
| `RestoreActorValue - Actor` | 恢复某项 Actor Value 的已损失部分。 |
| `EquipItem - Actor` | 将指定物品装备到角色身上。 |
| `UnequipItem - Actor` | 卸下角色身上指定物品。 |
| `AddItem - ObjectReference` | 向角色库存添加物品（定义在 ObjectReference，Actor 继承）。 |
| `AddSpell - Actor` | 为角色添加法术或能力（Ability）。 |
| `RemoveSpell - Actor` | 移除角色的法术或能力。 |
| `StartCombat - Actor` | 命令角色与指定目标进入战斗。 |
| `StopCombat - Actor` | 停止角色当前战斗。 |
| `GetEquippedItemType - Actor` | 返回当前右手装备物品的类型枚举。 |
| `IsDead - Actor` | 判断角色是否已死亡。 |
| `GetLevel - Actor` | 返回角色等级。 |

## 使用提示

- 脚本对象即「类」，运行于具体实例（如某个 Actor 或某个箱子）。
- `Self` 指向调用函数的当前实例；全局对象（Game / Debug）无 Self。
- 编译与连接请参见同板块的「编译脚本」条目。

