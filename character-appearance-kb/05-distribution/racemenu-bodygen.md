---
id: racemenu-bodygen
title: RaceMenu BodyGen（内置身形随机化）
category: 05-distribution
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [分配, BodyGen, RaceMenu, morph, NPC 身形]
aliases: [racemenu morphs, 随机身形, npc 身形随机, morphs.ini, templates.ini]
source: https://www.nexusmods.com/skyrimspecialedition/mods/19080
summary: BodyGen 的配置目录与两份 ini 的语法（templates.ini 定义模板、morphs.ini 映射 Actor）、它的硬前提（BodySlide 必须勾 Build Morphs），以及状态存在 co-save 这件事的后果。
---

# RaceMenu BodyGen

**BodyGen 不是独立 mod** —— 它是 RaceMenu 内置的身形随机化功能，作者就是
RaceMenu 的作者 **expired6978**。

## 它做什么

把 **morph 组合**随机/按规则分配给 NPC 与玩家，让每个 NPC 的身材不完全一样。

## 配置目录

```
meshes/actors/character/BodyGenData/<插件名含扩展名>/
├── templates.ini     定义"模板"（一组 morph 取值）
└── morphs.ini        把 ActorBase 映射到模板
```

注意目录名是 **`<插件文件名含扩展名>`**（例如 `MyMod.esp`）。

## 语法

### `templates.ini`

```
模板名=morph@值 | morph@区间
```

- **逗号 = AND**（同时应用）；
- **`|` = OR**（随机取一个）；
- `@` 后可以是固定值，也可以是 `a:b` 的随机区间。

例：

```
Breasts=Breast@1.0 | BreastCleavage@0.1:1.0
```

### `morphs.ini`

```
Skyrim.esm|F62F0=模板名
All|Female=模板名
```

- 左边是 **插件名 | FormID**，或 **`All|Female`** 这类批量写法；
- 多个模板可用逗号组合（如 `Sevenbase,Random` 之类的用法）。

> **`ini` 末尾需留一个空行**（社区经验）。

## 硬前提

1. **BodySlide 必须勾 `Build Morphs`** —— 否则没有 `.tri`，RaceMenu 无从应用 morph；
2. 运行时由 RaceMenu 的 **NiOverride（`skee64.dll`）** 应用；
3. **morph 状态会写入 SKSE co-save**。

## 第 3 条的后果（重要）

因为 morph 状态存在 **co-save** 里：

- 中途增删身形/皮肤/预设类 mod，**旧档可能对不上**（脸/身材回到默认，或出现异常）；
- 调整 BodyGen 配置后，**已有 NPC 的状态可能不会自动刷新**（需要新档或让游戏重新生成）。

这与"预设不生效"类问题高度相关，见
[`../06-troubleshooting/preset-not-applied.md`](../06-troubleshooting/preset-not-applied.md)。

## 与其它分配工具的关系

| 工具 | 配置形态 | 说明 |
|---|---|---|
| **BodyGen** | `.ini`（含在 RaceMenu 里） | 语法最原始，无 GUI |
| **OBody NG** | `.json` | 有 MCM，支持预设分发 |
| **AutoBody** | `.ini`（**仿 BodyGen 语法**） | 额外支持 faction / 男性 / 权重随机 |

**注意**：AutoBody 的 `morphs.ini` 语法是**有意仿照 BodyGen** 的，
所以见过 BodyGen 写法的人能直接上手 —— 但两者是**不同的 mod**，不要混装。

## 来源

- BodyGen 配置目录、两份 ini、语法、co-save 存储：LoversLab 的非官方 BodyGen 文档
  （基于 expired6978 原话整理）—— **社区文档，引作者原话**
  `https://www.loverslab.com/topic/53531-unofficial-bodygen-docs`
- 硬前提需 BodySlide `Build Morphs` + NiOverride 应用：BodySlide 机制 + BodyGen 文档 —— **一手（机制）+ 社区**
- "ini 末尾需空行"：**社区经验**
- AutoBody 语法仿 BodyGen：AutoBody 官方仓库 README —— **一手**
