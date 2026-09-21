---
id: script-object-objectreference
title: ObjectReference 脚本对象
category: 04-scripting
version: 1.0.0
updated: 2026-09-20
tags: [papyrus, script-object, objectreference, native]
aliases: [对象引用, 物件脚本, reference 对象]
source: https://ck.uesp.net/wiki/ObjectReference_Script
summary: 游戏世界中所有可放置对象的基类，提供激活、启停、移动、物品、约束等最常用原生函数。
status: stable
kind: reference
---

# ObjectReference 脚本对象

游戏世界中所有可放置对象的基类，提供激活、启停、移动、物品、约束等最常用原生函数。

> 来源：https://ck.uesp.net/wiki/ObjectReference_Script

## 概述

本条目汇总该 Papyrus 脚本对象最常用的原生（native）函数。所有函数均来自游戏引擎暴露，无法在脚本中重写其实现。完整列表与参数请以官方页面为准。

## 常用函数

| 函数 | 说明 |
| --- | --- |
| `Activate - ObjectReference` | 以指定触发者激活该引用对象。 |
| `Enable - ObjectReference` | 启用（显示）对象引用。 |
| `Disable - ObjectReference` | 禁用（隐藏）对象引用。 |
| `Delete - ObjectReference` | 立即删除对象引用。 |
| `DisableNoWait - ObjectReference` | 异步禁用，不等待动画完成。 |
| `MoveTo - ObjectReference` | 将对象移动到另一引用位置。 |
| `SetPosition - ObjectReference` | 直接设置对象的 X/Y/Z 坐标。 |
| `SetAngle - ObjectReference` | 设置对象的旋转角度。 |
| `AddItem - ObjectReference` | 向容器 / 角色添加物品。 |
| `RemoveItem - ObjectReference` | 从容器 / 角色移除物品。 |
| `GetDistance - ObjectReference` | 返回与另一引用的距离。 |
| `PlayAnimation - ObjectReference` | 播放指定动画事件。 |
| `ApplyHavokImpulse - ObjectReference` | 对对象施加物理冲量。 |
| `BlockActivation - ObjectReference` | 暂时阻止对象的激活行为。 |

## 使用提示

- 脚本对象即「类」，运行于具体实例（如某个 Actor 或某个箱子）。
- `Self` 指向调用函数的当前实例；全局对象（Game / Debug）无 Self。
- 编译与连接请参见同板块的「编译脚本」条目。

