---
id: conditions-overview
title: 条件系统总览
category: 03-conditions
kind: concept
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 条件, 语法, 嵌套, EditorID, 数值来源]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: 条件决定"什么时候用这套替换动画"；外层列表本身就是一个 AND，OR/AND 等可无限嵌套；数值可来自静态值/全局变量/Actor Value/行为图变量；关键字可写 EditorID。
---

# 条件系统总览

## 条件在干什么

条件决定"**什么时候**用这套替换动画"。每个 submod 有一份条件列表，OAR 在游戏请求某动画时逐个求值，全部满足才把请求重定向到这个 submod 的动画。

## 四条语法要点（官方）

> - 所有用于比较的**数值**都可以是：**静态值**、**全局变量引用**、**Actor Value**、或**行为图变量（behavior graph variable）**。
> - **关键字**可以直接写它的 **EditorID**（例如 `WeaponKatana`）来代替。如果多个关键字共享同一个 EditorID，它们会**全部匹配**。
> - 带子条件列表的条件（**OR**、**AND**）可以**无限嵌套**。
> - **所有条件和它们的组件在 UI 里悬停时都有 tooltip 说明。**

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## 外层条件列表 = 一个 AND

> 外层条件列表本身**就是一个 AND 条件**。

> 来源：<https://bakemono.app/p/patreon/25643772/80271137>（0.5.1 开发日志）

所以你**不需要**在最外层写 `AND`。只有需要嵌套组合逻辑时才显式用容器条件。

## 真实 `config.json` 的形状

```json
{
  "name": "Sneak Bow Pose",
  "priority": 1750000000,
  "interruptible": true,
  "conditions": [
    { "condition": "IsActorBase", "requiredVersion": "1.0.0.0",
      "Actor base": { "pluginName": "Skyrim.esm", "formID": "7" } },
    { "condition": "IsSneaking", "requiredVersion": "1.0.0.0" }
  ]
}
```

几个**反直觉**的点（本工作区实测，均被社区配置样本印证）：

- **字段名是英文可读名**（`"Actor base"`、`"Left hand"`、`"Attack state"`），不是变量名。
- **数值要包成对象**：`"Type": { "value": 7.0 }`，不是 `"Type": 7`。
- **取反**用 `"negated": true`（编辑器里是 `Negate` 勾选框）。
- **组合条件用条件的形式写**：`{"condition": "OR", "Conditions": [ … ]}`——注意子数组的键是**大写 `C` 的 `Conditions`**。
- **`formID` 在 JSON 里写插件内的 FormID**，不带 `0x` 前缀（实测写成字符串 `"7"` 可用）；对应文本语法的 `0x00000007`。
- 关键字可以用 `{ "editorID": "ElderNPC" }` 这种形式，不必查 formID。

> 来源：本工作区实测记录 `OAR/OAR-补充文档.md`；`negated` / `editorID` 的形态见社区配置样本 <https://www.loverslab.com/topic/245858-how-to-have-both-follower-and-pc-play-idle-animations-with-oar-conditions>

## 两个必知的坑

### 坑 1：`HasGraphVariable` 只能判断变量「存在」，不能读值

想要读行为图变量的**值**做判断，要用 **`CompareValues`**（它的取值来源支持行为图变量），不能指望 `HasGraphVariable`。

> 补充：OAR 注册的 `HasGraphVariable` 只有一个，早期 0.5.0 曾有 `HasGraphVariable[Float/Int/Bool]` 与 `GraphVariable*EqualTo/LessThan` 这一族条件；到发布版最终收敛为 `HasGraphVariable` + `CompareValues` 的组合。写法以你所用版本的编辑器显示为准。

> 来源：本工作区实测记录 `OAR/OAR-补充文档.md`；0.5.0 条件清单见 <https://bakemono.app/p/patreon/25643772/80271137>

### 坑 2：抄别人的条件时要连 `requiredVersion` 一起抄

带版本号的条件（如 `AttackState` 是 `1.3.0.0`）如果**没写 `requiredVersion`**，或写的版本**高于你的 OAR**，编辑器会报「需要更高版本/缺少插件」。

**最安全的做法**：别手写，直接在 `Shift+O` 的**作者模式**里加条件，编辑器会自动填好所有字段。

> 来源：本工作区实测记录 `OAR/OAR-补充文档.md`。

## 三级来源的可靠性排序

写条件时，遇到不确定的地方按这个顺序找答案：

1. **游戏内编辑器**（`Shift+O`）——它显示的条件名、组件名、当前值、tooltip **就是你这一版的真相**；选中目标后还能看到每条条件是否命中。
2. **Nexus 描述页的条件清单**（本库 [条件全清单](conditions-list.md) 就是它的结构化版本）——与源码逐条核对过。
3. **别人的 `config.json`**——最直观，但可能属于旧版本、可能写错。

## 相关

- [条件全清单](conditions-list.md)
- [容器条件](condition-containers.md)
- [DAR 旧条件改名/合并对照](dar-condition-renames.md)
- [编辑器与调试](../05-editor/in-game-editor.md)
