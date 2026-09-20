---
id: dialogue
title: 对话系统（Dialogue）
category: 03-game-systems
version: 1.0.0
updated: 2026-09-20
tags: [dialogue, topic, response, conversation, conditions]
source: https://ck.uesp.net/wiki/Dialogue
summary: 对话由主题（Topic）、回应（Response）与条件（Condition）构成，可绑定脚本片段驱动剧情。
status: stable
kind: reference
---

# 对话系统（Dialogue）

《天际》的对话系统让 NPC 与玩家通过**主题（Topic）**与**回应（Response）**交互，并由**条件（Condition）**控制何时出现。

## 核心概念

- **Topic（主题 / 对话主题）**：一条可说的对话分支，如问候、任务询问、闲聊。
- **Response（回应）**：玩家选择某主题后，NPC 说出的具体台词，可带配音与字幕。
- **Branch / Subtopic**：主题可包含子分支，形成对话树。
- **Condition（条件）**：决定某回应是否出现的判定（如任务阶段、玩家等级、变量值）。
- **Dialogue Fragment（对话片段）**：可在进入主题 / 选择回应时执行 Papyrus 脚本，驱动任务或世界状态改变。

## 与任务的关系

- 任务对话通常通过**任务别名（Alias）**引用 NPC，使同一套对话可绑定不同实例。
- 在 Quest 编辑器的 Dialogue 视图中把 Topic 挂到具体任务，便于按任务管理。

## 设计要点

- 用 **条件** 控制分支，避免「所有人都说同一句话」。
- 关键剧情节点用 **Fragment** 推进任务阶段，而非硬编码。
- 口语检查（Speech Check）等机制通过条件 + 分支实现（见 [对话口语检查教程](https://ck.uesp.net/wiki/Tutorial:_Dialogue_Speech_Checks)）。

## 相关条目

- [任务系统](quests.md)
- [Papyrus 事件与属性教程](https://ck.uesp.net/wiki/Bethesda_Tutorial_Papyrus_Events_and_Properties)

> 来源：[UESP Dialogue](https://ck.uesp.net/wiki/Dialogue)
