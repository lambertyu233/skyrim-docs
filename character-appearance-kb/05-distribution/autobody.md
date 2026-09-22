---
id: autobody
title: AutoBody（AE 版身形分发）
category: 05-distribution
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [分配, AutoBody, CBBE, HIMBO, NPC 身形, ini]
aliases: [身形分发, napmouse, 给 npc 分配身形]
source: https://github.com/napmouse/autoBodyAE
summary: AutoBody 的作者与机制、仿 BodyGen 的 morphs.ini 语法、它对 CBBE 与 HIMBO 预设的支持，以及游戏内调整菜单。
---

# AutoBody

- 作者 **napmouse**
- 仓库：`https://github.com/napmouse/autoBodyAE`（**GPL-3.0**）
- Nexus：`mods/61321`（论坛引用处）

## 它做什么

一个 SKSE 插件，把 **CBBE 与 HIMBO 预设**分发给 NPC。
它**重新实现了 OBody 的 ORefit 算法**。

## 配置：`morphs.ini`

**语法有意仿照 RaceMenu BodyGen**，但用 **EditorID** 匹配：

```
All|Female|TownWhiterunFaction=...
```

能力：

- 按 **faction / race** 匹配；
- 支持**男性**（HIMBO 预设）；
- 支持**权重随机**。

## 游戏内工具

| 功能 | 说明 |
|---|---|
| `;` 键 | 打开 actor 调整菜单 |
| **Regenerate Actor 法术** | 让某个 actor 重新生成身形 |

## 依赖

**Address Library for SKSE Plugins。**

（注意它比 OBody NG 的依赖**更少** —— 不需要 MCM Helper / UIExtensions。）

## 与 OBody NG 的对比

| | AutoBody | OBody NG |
|---|---|---|
| 配置 | `.ini`（仿 BodyGen） | `.json` |
| 男性身形支持 | **HIMBO** | 见其配置说明 |
| 界面 | 游戏内菜单 + 法术 | MCM |
| 依赖 | 仅 Address Library | RaceMenu + MCM Helper + UIExtensions |
| 作者 | napmouse | Aietos |

> 社区有"OBody NG 是 AutoBody 的继任者"的说法，但**先后关系未确认**。
> 择一使用即可。

## 来源

- 作者、GPL-3.0、ORefit 算法重实现、`morphs.ini` 语法与 EditorID 匹配、
  faction/男性/权重随机、`;` 键与 Regenerate Actor 法术、依赖 Address Library：
  **GitHub 官方 README** —— **一手**
  `https://github.com/napmouse/autoBodyAE`
- Nexus mod id 61321：Nexus 论坛引用 —— **社区经验**
- 与 OBody NG 的继任关系：**未确认**
