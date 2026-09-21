---
id: math-plugin
title: Math Plugin（数学表达式条件）
category: 06-plugins
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [OAR, Math Plugin, MathStatement, 插件, 示例]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92607
summary: 作者自己把本来内置的数学表达式条件拆成独立插件，主要作为"如何用 OAR API 写复杂条件"的示例；提供 MathStatement 条件，用 exprtk 求值。
---

# Math Plugin（数学表达式条件）

> **Open Animation Replacer - Math Plugin**
> 作者：**Ersh**（OAR 本体作者）｜ 当前版本 **1.0.5**（2026-08-31）
> Nexus mod **92607** ｜ 前置：**SKSE + OAR 本体**

## 它的来历（作者自述，很有意思）

> 这个插件给 OAR 加了一个新条件。**起初它是本体的一部分**，但把数学表达式库（`exprtk`）算进来后，**插件的体积直接翻了四倍**。让整个插件大部分体积来自单独一个功能，感觉很别扭。
> 我决定把这个条件去掉，后来发现它可能是个不错的例子——**演示如何通过 OAR API 添加一个更复杂的条件**。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92607>

作者对它的定位说得很直白：

> 它**主要是给程序员当示例用的**，也是"通过其他插件添加新的、相当复杂的条件确实可行"的证明。条件本身能用，也挺酷，但**我想不出什么真实用例是现有条件覆盖不了的**。也许有人能找到好的用法，值得为此多装一个插件。
> **如果你用的 replacer mod 不需要它，就没有真正的理由装它**——除非你好奇，或者你是 replacer mod 作者、确实用得上这个条件。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92607>

发布时的公告也提到：

> 还有一个可选插件，有些人可能觉得有用。我不想把它放进主 mod，因为**那个数学库的体积大概是 OAR 本身的三倍**。

> 来源：<https://bakemono.app/p/patreon/25643772/83900406>

## 它加的条件：`MathStatement`

> 插件加了一个叫 **`MathStatement`** 的新条件。它让你在编辑器的文本框里**写一个数学表达式**（例如 `x + y > 20`），然后它会**自动为表达式里的每个变量创建一个数值组件**。
> 这些数值的工作方式和所有其他条件里的数值一样，所以可以是**静态值**、**全局变量引用**、**Actor Value**、或**行为图变量**。
> 条件只是对表达式的结果求值，检查它**是否不等于 0**——所以，配上一个真正的数学语句，就意味着**检查该语句是否为真**。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92607>

所用数学库 **`exprtk`** 非常强大，可以写出很复杂的表达式——作者原话是"但我依然很难看到真实用例，不过挺酷的"。

## 为什么它值得收进资料库

它不是一个"玩家应该装"的插件，而是：

1. **插件 API 的官方参考实现**——想写自己的 OAR 扩展插件，先看它；
2. **解释了 OAR 的一个设计取舍**：功能强 ≠ 该内置。作者为了不让主插件体积被单一依赖撑大，宁可把功能拆出去。同样的取舍在 [Detection Plugin](detection-plugin.md)（拆给社区）和 [IED Conditions](ied-conditions.md)（社区自建）上重复出现——**OAR 的体积克制是一种有意的架构决策**。

## 相关

- [插件 API 概览](plugin-api.md)
- [Detection Plugin](detection-plugin.md)
- [IED Conditions](ied-conditions.md)
