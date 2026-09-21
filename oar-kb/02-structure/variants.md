---
id: variants
title: 动画变体（Variants）
category: 02-structure
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 变体, 随机, 顺序, 权重]
aliases: [OAR 变体, 随机动画, 多个动画随机播, 轮播动画]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: 自 1.2.0 起一个替换动画可有多个变体，做法是建 _variants_<动画名> 子文件夹；不用写随机条件，可在编辑器里配权重；2.2.0 起还有顺序模式与"只播一次"。
---

# 动画变体（Variants）

## 它解决什么问题

自 **1.2.0** 起，一个替换动画可以有**多个变体**。这是做**随机动画**更舒服的方式。

以前做随机变体要：创建**多个条件相同的 submod**，再各自加随机条件。
有变体后：**只需要一个 submod，且不需要任何随机条件**。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## 怎么加（官方步骤）

1. 在**该动画原本应放置的位置**，新建一个子文件夹；
2. 文件夹命名为 **`_variants_[不含扩展名的动画名]`**；
3. 把**所有变体**都放进去。

例：为 `mt_idle.hkx` 做变体 → 新建文件夹 **`_variants_mt_idle`**（放在同一位置），把变体文件放进去。

- **变体文件名随意**。
- 但作者建议用**短名**（甚至 `1.hkx`、`2.hkx`），以**避免长路径带来的问题**。

> 也就是说：原本 `submodFolder/male/mt_idle.hkx`，变成 `submodFolder/male/_variants_mt_idle/1.hkx` 等。

**就这样**——插件会自动识别，并在该替换动画该播放时**随机挑选**一个变体。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## 权重

可在游戏内编辑器的 submod 替换动画里，为**每个变体配置权重**：

> 例：给一个变体设 **权重 2**，它的播放概率就是**权重 1** 变体的**两倍**。

变体随机同样会**遵循**"循环/回声时保留随机结果"与"共享随机结果"这两个 submod 设置，就像随机条件一样。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## 顺序模式（自 2.2.0）

变体新增 **Sequential（顺序）** 模式：不随机，而是**按顺序依次播放**。此模式下可把某个变体标记为 **"Play once"**——它在本轮序列中**不会再播放**，即使序列已经绕回来。

序列数据（下一个变体的索引、"只播一次"的历史）会在该替换动画（或**整个动画剪辑**）**闲置一小段时间后重置**。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## 心智模型（官方原话，值得直接背下来）

> 把事情说清楚、让它更好懂一点：**不要把这东西想复杂了。它只是条件求值之后的一个可选步骤。** 唯一区别是——不再是"选中并播放单个替换动画"，而是"从可能的变体里选一个"。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## 版本相关的两个 bug 修复（说明它在被认真维护）

- **2.3.5**：标记为 Play Once 的变体不再以混合时间偏移开始混合（现在从 0 而不是 `animDuration - blendTime` 开始）；顺序变体在序列末尾的混合问题修复。
- **2.3.6**：修复配对动画变体在参与角色的行为项目不同时播错动画的问题。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（变更条目）

## 与"随机条件"的取舍

| | 变体 | `Random` 条件 |
| --- | --- | --- |
| 需要的 submod 数 | **1 个** | 多个（同条件 + 随机条件） |
| 是否需要随机条件 | **不需要** | 需要 |
| 权重可调 | **可以**（编辑器里） | 只能通过条件里的 min/max 曲线上调 |
| 顺序播放 | **支持**（2.2.0+） | 不支持 |
| 分组随机（共享结果） | 支持（有对应设置） | 支持（有对应设置） |

**结论**：做随机动画优先用变体。`Random` 条件仍有它的位置（比如"以 X% 概率**根本不用**这套替换，落到原版动画"）——那时它是在**决定要不要命中**，而不是"命中哪一个"。

## 相关

- [`config.json`、`user.json` 与优先级](config-and-priority.md)
- [目录结构与路径插入规则](directory-structure.md)
- [条件全清单](../03-conditions/conditions-list.md)
