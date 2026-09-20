---
id: radiant-story
title: Radiant Story（故事管理器）
category: 03-game-systems
version: 1.0.0
updated: 2026-09-20
tags: [radiant, story-manager, procedural, quests, encounters]
source: https://ck.uesp.net/wiki/Bethesda_Tutorial_Story_Manager
summary: Radiant Story / 故事管理器按条件在运行时动态生成任务与遭遇，实现程序化、可重复的内容。
status: stable
kind: tutorial
---

# Radiant Story（故事管理器）

**Radiant Story** 通过 **Story Manager（故事管理器）** 在运行时**动态生成**任务与遭遇，让内容随玩家行为、地点、阵营等因素程序化变化。它是《天际》大量「 radiant 任务」与随机遭遇背后的系统。

## 核心思想

- 传统任务在编辑器中写死；Radiant 任务则定义**规则**，由引擎在合适时机「填空」生成实例。
- 例如：NPC 向玩家求助 → 系统动态选取一个地点、一组敌人、一份奖励来拼出一个可重复完成的任务。

## 关键构件

| 构件 | 作用 |
| --- | --- |
| **Story Manager Node** | 规则节点，定义触发条件与生成逻辑。 |
| **Quest（模板任务）** | 提供 Radiant 任务的结构，运行时由节点填充别名与参数。 |
| **Alias（别名）** | 在生成时动态绑定地点 / NPC / 物品等。 |
| **Conditions** | 控制节点是否触发（声望、地点、随机概率等）。 |

## 工作流（以教程为例）

1. 新建模板 Quest，预留 Alias（如「目标地点」「目标角色」）。
2. 在 Story Manager 新建节点，设置触发条件与引用的模板任务。
3. 通过节点把运行时选中的 Form 写入任务别名。
4. 测试：在不同地点/情境下确认任务能动态生成且可完成。

## 提示

- Radiant 任务要小心**循环刷取**与**别名未绑定**导致的崩溃。
- 与 [AI 包](packages.md) 配合，可让生成的 NPC 有合理行为。

## 相关条目

- [任务系统](quests.md)
- [基础任务脚本教程](06-tutorials/basic-quest-scripting.md)

> 来源：[UESP Bethesda Tutorial Story Manager](https://ck.uesp.net/wiki/Bethesda_Tutorial_Story_Manager)
