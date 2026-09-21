---
id: condition-containers
title: 容器条件：OR / AND / XOR / TARGET / PLAYER / MOUNT / PRESET
category: 03-conditions
kind: concept
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 条件, 容器, 嵌套, OR, AND, PLAYER, TARGET]
aliases: [OAR 条件容器, OR AND NOT, 嵌套条件, containers, 条件怎么写多个, TARGET PLAYER 容器]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: 容器条件自身不判断数值，而是"换一个求值对象"或"组合子条件"；外层列表本身就是 AND，容器可无限嵌套，子数组的键名为大写 Conditions。
---

# 容器条件：OR / AND / XOR / TARGET / PLAYER / MOUNT / PRESET

## 两大类容器

容器条件本身**不直接判断任何数值**，它们做两件事之一：

| 类型 | 成员 | 作用 |
| --- | --- | --- |
| **逻辑组合** | `AND`、`OR`、`XOR` | 对**同一批条件**做布尔组合 |
| **切换求值对象** | `TARGET`、`PLAYER`、`MOUNT` | 子条件全为真，但**求值对象换成别人** |
| **间接引用** | `PRESET` | 就地求值 replacer mod 里定义的预设 |

## 逐条说明

### AND / OR / XOR

- `AND`：所有子条件为真。
- `OR`：任一子条件为真。
- `XOR`（2.1.0）：**仅**一个子条件为真（异或）。

**外层条件列表本身就是 AND**，所以只在需要**混合逻辑**时才显式使用它们。

### TARGET / PLAYER / MOUNT

- `TARGET`（1.3.0）：子条件全为真，但**对"当前目标"求值**。
- `PLAYER`（1.3.0）：子条件全为真，但**对玩家求值**。
- `MOUNT`（2.2.0）：子条件全为真，但**对坐骑求值**。

用途举例：让"被玩家骑着的马"用某套动画 → `MOUNT` 里写判定坐骑的条件。

### PRESET

就地求值 replacer mod 里定义的条件预设，详见 [条件预设](../02-structure/presets.md)。

## 嵌套规则（官方）

> 带子条件列表的条件（**OR**、**AND**）可以**无限嵌套**。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## ⚠️ 最经典的踩坑：**子条件必须挂在正确的父条件下面**

这是社区里最高频的困惑。LoversLab 上一位用户想"让随从和玩家都用同一套 idle"，试着把 `IsFemale` 换成 `isactorbase7` / `isform14`，结果随从也不触发了。用户原话：

> 我的"逻辑"告诉我 `isFemale OR isactorbase` 或 `isform` 应该能用，但 **OAR 的 GUI 好像不允许我给 `isFemale` 添加子条件**。

得到的回答一针见血：

> 那是因为**父条件本身就应该是 `OR`**，所有选项都挂在 `OR` 条件下面。

> 来源：<https://www.loverslab.com/topic/245858-how-to-have-both-follower-and-pc-play-idle-animations-with-oar-conditions>

**正确形状**：

```
OR
  ├── IsFemale
  └── IsForm(Player)          ← 两者都是 OR 的子条件
```

**错误形状**（做不到，UI 不会让你这么加）：

```
IsFemale
  └── OR(IsForm(Player))      ← 条件不是容器，没有子条件槽
```

**规律**：**只有容器条件（OR/AND/XOR/TARGET/PLAYER/MOUNT）才有"子条件"槽**。普通判断条件（`IsFemale`、`IsEquipped`…）是叶子节点，不能挂子条件。

同一条规则在 Detection Plugin 上也存在，那里的说法是"**子条件必须紧跟在 `DETECTS`/`DETECTED_BY` 下面，否则什么都不做**"——见 [Detection Plugin](../06-plugins/detection-plugin.md)。

## JSON 写法

组合条件写成"一个条件对象"，子数组的键名是**大写 `C` 的 `Conditions`**：

```json
{
  "condition": "OR",
  "requiredVersion": "1.0.0.0",
  "Conditions": [
    { "condition": "IsEquippedType", "requiredVersion": "1.0.0.0",
      "Type": { "value": 7.0 }, "Left hand": true },
    { "condition": "IsEquippedType", "requiredVersion": "1.0.0.0",
      "Type": { "value": 7.0 }, "Left hand": false }
  ]
}
```

> 来源：本工作区实测记录 `oar-kb/08-practices/`（原 `OAR/` 目录的内容已并入本库）（`Conditions` 大写、`{"value": N}` 包裹、`Left hand` 布尔组件均经实测）。

## 实战建议：为什么"左右手要各写一条 OR"

`IsEquippedType` 这类带"左手"布尔组件的条件，**一条只能判一只手**。要"无论左右手持弓都算"，就得：

```
OR
  ├── IsEquippedType  Type=7(Bow), Left hand = true
  └── IsEquippedType  Type=7(Bow), Left hand = false
```

这是专业动画包和本工作区实测配置里都出现的标准写法——避免"只写一条导致左手持弓不生效"。

`Type` 的取值见 [条件全清单](conditions-list.md) 与编辑器的下拉列表；弓是 **7**（本工作区实测值）。

## 相关

- [条件系统总览](conditions-overview.md)
- [条件全清单](conditions-list.md)
- [Detection Plugin 的子条件规则](../06-plugins/detection-plugin.md)
- [实战：改造别人的动作包](../08-practices/authoring-workflow.md)
