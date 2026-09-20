---
id: warnings-and-order-problems
title: 警告面板与潜在 mod 顺序问题
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 警告, mod 顺序, 排错]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 工具栏警告图标提示"潜在 mod 顺序问题"，可点 Fix 让 MO 重排；它管资源（贴图/网格）顺序，与 LOOT 管的插件顺序不同。
kind: tutorial
---

# 警告面板与潜在 mod 顺序问题

## 警告图标

- 工具栏有时会亮起 **warning 图标**，表示左窗格的 mod 顺序存在**潜在问题**。
- 点击它 → 显示需要处理的 `Problems`；选中上方面板里的 `Potential Mod order Problem`，下方会给出**所需调整的说明**。

## 怎么处理

- 最好的做法通常是直接点 **`Fix`**，让 MO 帮你重排这些 mod。
- 若你做了大量改动、甚至**整体重装了所有 mod**，可以先**手动排序**再 Fix。
- 手动排序的技巧：**从列表底部往上调**，这样在处理高位 mod 时，可能某些冲突已经被顺带解决了。

## "潜在"是什么意思

- 正如对话框标题所说，这些是**潜在**问题。
- 通常游戏**仍能跑起来**、未必会 CTD，但**很可能出现贴图/网格（或其它资源）缺失，或至少是错的那一份**。
- 这个功能相当于对"作者页面上关于该 mod 应装在哪个位置、与谁先后顺序"的提醒做了一次自动复核。
- 原理：所有 mod 都被"装"进 MO 的**虚拟游戏数据目录**，所以**游戏引擎实际的加载顺序**可以通过在左窗格重排这些 mod 来改变。

## 与 LOOT / Sort 的区别（重要）

| | 管什么 |
| --- | --- |
| **本警告面板 / 左窗格顺序** | **资源**（textures / meshes / menus 等）的覆盖关系 |
| **Plugins 页的 `Sort`、LOOT、BOSS** | **插件**（esp/esm）的加载顺序 |

> 二者性质不同：mod 顺序问题不是 LOOT 或 BOSS 能处理的范畴。

> 相关：[冲突解决与优先级](conflict-resolution.md)、[启用 mod 与激活插件](enable-and-activate.md)、[界面总览](ui-layout.md)（warning 图标）。
