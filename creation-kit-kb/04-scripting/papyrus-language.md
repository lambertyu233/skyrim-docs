---
id: papyrus-language
title: Papyrus 语言要素
category: 04-scripting
version: 1.0.0
updated: 2026-09-20
tags: [papyrus, language, variables, properties, states, arrays, functions]
source: https://ck.uesp.net/wiki/Papyrus_Introduction
summary: Papyrus 的面向对象要素——变量/属性、语句、数组、状态、函数、事件、扩展脚本、线程与持久化。
status: stable
kind: reference
---

# Papyrus 语言要素

Papyrus 是**面向对象**的脚本语言。理解以下核心要素，是编写任何脚本的前提。

## 核心要素一览

| 要素 | 说明 |
| --- | --- |
| **Variables & Properties（变量与属性）** | 变量是脚本内部的存储；属性（Property）是对外暴露、可在编辑器中配置/连接的变量。 |
| **Statement（语句）** | 控制流：`if/elseIf/else`、`while`、`return` 等。 |
| **Arrays（数组）** | 同类型元素的定长集合，如 `int[]`、`ObjectReference[]`。 |
| **States（状态）** | 同名函数可按状态切换实现不同行为，便于状态机式逻辑。 |
| **Functions（函数）** | 可复用的工作单元，可带参数与返回值；支持 `global`/`native` 修饰。 |
| **Events（事件）** | 由游戏运行时触发、脚本可响应的信号（如 `OnActivate`）。 |
| **Extending Scripts（扩展脚本）** | 通过继承父脚本复用并覆盖行为。 |
| **Threading（线程）** | Papyrus 异步执行，需注意竞态与回调。 |
| **Persistence（持久化）** | 标记为持久化的脚本/对象在存档中保留状态。 |
| **Save File Notes（存档笔记）** | 脚本状态如何写入/恢复存档的注意事项。 |

## 面向对象速记

- 脚本定义「类」，运行于具体「实例（对象）」。
- 函数内部通过 **`Self`** 指代调用它的当前实例（类似其它语言的 `this`）。
- 比较两个对象是否同一实例时，用 `== self` 可避免误伤自身（如 `car1.Ram(car2)` 中排除 `car2 == self`）。

## 修饰符

- **Global**：函数不作用于具体实例，无 `Self`。
- **Native**：函数由游戏引擎实现、无函数体；若引用了引擎未暴露的函数，编译不报错但运行会报错。

## 推荐学习顺序

1. [Papyrus 概览](papyrus-overview.md) → 2. 本页语言要素 → 3. [编译脚本](compiling-scripts.md) → 4. [事件/函数参考](events-reference.md)。

> 来源：[UESP Papyrus Introduction](https://ck.uesp.net/wiki/Papyrus_Introduction)
