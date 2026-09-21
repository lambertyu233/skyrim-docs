---
id: basic-quest-scripting
title: 教程：基础任务脚本
category: 06-tutorials
version: 1.0.0
updated: 2026-09-20
tags: [tutorial, quest, papyrus, scripting, beginner, fragment]
source: https://ck.uesp.net/wiki/Bethesda_Tutorial_Basic_Quest_Scripting
summary: 官方教程——创建一个简单任务，并用 Papyrus 片段（Fragment）驱动阶段推进与目标完成。
status: stable
kind: tutorial
---

# 教程：基础任务脚本

本教程（Bethesda 官方）演示如何创建一个**简单任务**，并用 **Papyrus 片段（Fragment）** 驱动其阶段与目标的推进。是连接[任务系统](../03-game-systems/quests.md)与[Papyrus](../04-scripting/papyrus-overview.md)的实操桥梁。

## 你会学到

- 新建 Quest 记录并设置 ID / 类型。
- 添加 **Stage（阶段）** 与 **Objective（目标）**。
- 编写 **Stage Fragment**，在进入阶段时执行脚本。
- 在脚本中标记目标完成、推进任务。

## 步骤概要

1. 在 Object Window 新建 `Quest`，命名（如 `MQDemo`）。
2. 在 **Quest → Stages** 添加阶段 `10`、`20`、`100`。
3. 在 **Objectives** 添加可见目标，并关联到阶段。
4. 为阶段 `10` 写 Fragment：激活目标 NPC 的对话或给予物品。
5. 为阶段 `100` 写 Fragment：标记目标完成、结束任务（`CompleteQuest`）。
6. 保存并测试：在游戏中触发，确认阶段按预期流转。

## 关键 API（片段中常用）

- `CompleteAllObjectives` / `CompleteQuest`（来自 [Quest 脚本对象](https://ck.uesp.net/wiki/Quest_Script)）。
- 通过**别名（Alias）**读写任务绑定对象，避免硬编码。

## 延伸

- 想进一步控制脚本生命周期，见 [Papyrus 语言要素](../04-scripting/papyrus-language.md)。
- 想做动态生成内容，见 [Radiant Story](../03-game-systems/radiant-story.md)。

> 来源：[UESP Bethesda Tutorial Basic Quest Scripting](https://ck.uesp.net/wiki/Bethesda_Tutorial_Basic_Quest_Scripting)
