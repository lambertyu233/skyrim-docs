---
id: quests
title: 任务系统（Quests）
category: 03-game-systems
version: 1.0.0
updated: 2026-09-20
tags: [quest, quest-system, stages, objectives, aliases]
source: https://ck.uesp.net/wiki/CreationKit:Quests
summary: 任务是 CK 的核心系统，由阶段（Stage）、目标（Objective）、别名（Alias）与脚本片段（Fragment）构成。
status: stable
kind: reference
---

# 任务系统（Quests）

**Quest（任务）** 是 CK 中组织游戏流程的核心记录类型。一个任务把对话、场景、奖励、脚本逻辑与可追踪目标组合成一个完整体验。

## 核心组成

| 组成 | 作用 |
| --- | --- |
| **Stage（阶段）** | 任务进度由整数阶段标识；阶段可设置「阶段结果脚本（Stage Fragment）」，在进入时执行。 |
| **Objective（目标）** | 玩家可见的任务目标，可显示/隐藏、标记完成。 |
| **Alias（别名）** | 在任务运行时动态绑定的引用（如「任务给予者」「目标物品」），使任务与具体实例解耦。 |
| **Quest Fragment（任务片段）** | 在任务启动、阶段变更等时机自动执行的 Papyrus 片段。 |
| **Dialogue / Scene** | 任务常配合对话主题与场景演出。 |

## 典型工作流

1. 在 Object Window 新建 `Quest` 记录，设置 ID 与类型。
2. 规划 **Stages** 与 **Objectives**，定义进度节点。
3. 用 **Aliases** 绑定动态引用，避免硬编码具体物体。
4. 编写 **Stage / Quest Fragment** 脚本（见 [基础任务脚本教程](06-tutorials/basic-quest-scripting.md)）。
5. 连接对话与场景，测试各阶段跳转。

## 相关条目

- [对话系统](dialogue.md)
- [AI 包](packages.md)
- [Radiant Story](radiant-story.md)
- [Papyrus 脚本概览](04-scripting/papyrus-overview.md)

> 来源：[UESP CreationKit:Quests](https://ck.uesp.net/wiki/CreationKit:Quests)
