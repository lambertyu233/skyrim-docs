---
id: overlay-nif-ctd
title: 启动/捏脸崩溃：RaceMenu overlay NIF
category: 06-troubleshooting
kind: reference
version: 1.0.0
updated: 2026-09-30
tags: [排错, 崩溃, CTD, RaceMenu, overlay, 1.7]
aliases: [overlay nif, 启动崩溃, 捏脸崩溃, nif 解析, 八个 nif]
source: https://www.nexusmods.com/skyrimspecialedition/mods/19080?tab=posts
summary: 1.7.x 更新后，磁盘上残留的旧版 RaceMenu overlay nif 会让游戏直接崩溃——八个具体文件名与处理方式。
---

# 崩溃：RaceMenu overlay NIF

## 症状

更新到 **1.7.x** 之后，游戏**启动或进捏脸界面时崩溃**。可能伴随 RaceMenu 相关报错，
也可能什么都不报直接退出。

## 根因（作者原文，一手）

Bethesda 在 1.7.x 里改坏了 Nif 解析的一个边界情况：

> "Bethesda broke a very edge case in their Nif parsing code, meshes with `NiTriShape`
> but no `NiTriShapeData` crash the game, these happen to be all of the 'overlay' nifs
> used by RaceMenu."

也就是说：**带 `NiTriShape` 却没有 `NiTriShapeData` 的网格会让游戏崩**，
而 RaceMenu 的 overlay 网格全都是这种结构。

## 处理：删掉这 8 个文件

作者明确要求：如果**本地磁盘上存在旧版本**的下列文件，**必须删掉**。
新版已经打包进 BSA，不再需要散文件。

```
Data\Meshes\Actors\Character\Character Assets\face_overlay.nif
Data\Meshes\Actors\Character\Character Assets\body_overlay.nif
Data\Meshes\Actors\Character\Character Assets\hands_overlay.nif
Data\Meshes\Actors\Character\Character Assets\feet_overlay.nif
Data\Meshes\Actors\Character\Character Assets\face_magicoverlay.nif
Data\Meshes\Actors\Character\Character Assets\body_magicoverlay.nif
Data\Meshes\Actors\Character\Character Assets\hands_magicoverlay.nif
Data\Meshes\Actors\Character\Character Assets\feet_magicoverlay.nif
```

> 作者原话：**"If you have older versions of these files locally, your game WILL crash."**

### 在 MO2 里怎么找

这类文件最常见的藏身之处是 **Overwrite 目录**，或者某个早期版本的 RaceMenu / 皮肤 mod。
用 MO2 的"数据" tab 或右键 mod → 搜索文件名定位，也可以在
`Data\Meshes\Actors\Character\Character Assets\` 下直接看。

## 判断分叉点（别误诊）

| 看起来像 | 其实 |
|---|---|
| "RaceMenu 没更新所以崩了" | 部分是，但**即使不装新 RaceMenu，残留旧 overlay nif 也会崩** |
| "某个皮肤/妆容 mod 坏了" | 先确认是不是这 8 个文件被某个 mod 带进来了 |
| "SKSE 插件版本不对" | 版本不对通常是**静默失效**（功能消失）而不是崩溃；崩溃优先查 NIF |

## 更一般的排错动作

SKSE 官网给了一条通用建议，在本场景同样适用：

> "Having crashes on startup after a game patch? **Remove the files from `Data/SKSE/Plugins` and try again.**
> Mods using plugins probably need to be updated."

也就是：**游戏大版本更新后崩，先把 `Data/SKSE/Plugins` 清空一次做二分**，再逐个加回。

## 来源

- 8 个 overlay nif 文件名、"NiTriShape 无 NiTriShapeData 会崩"、"旧版本残留必崩"、新版已打进 BSA：
  RaceMenu 作者帖（2026-08-23）—— **一手（作者本人）**
- "更新后启动崩溃先清空 `Data/SKSE/Plugins`"：SKSE 官网 Contact 段 —— **一手（SKSE 团队）**
- 1.7.x 的背景与适配现状：见 [`../00-overview/game-version-1-7-x.md`](../00-overview/game-version-1-7-x.md)
