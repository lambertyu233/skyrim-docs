---
id: po3-tweaks
title: powerofthree's Tweaks（引擎修复与调整）
category: 09-diagnostics
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [稳定性, 引擎修复, INI, 配置, powerofthree]
aliases: [po3 Tweaks, powerofthree's Tweaks, po3_Tweaks.ini, 51073, 调整项]
source: https://www.nexusmods.com/skyrimspecialedition/mods/51073
summary: 一堆「别人没覆盖到的」引擎 bug 修复与可选项调整；每项都能在 po3_Tweaks.ini 里单独开关，是 SPID 的官方前置之一。
---

# powerofthree's Tweaks

## 官方定位（发布页）

> **"Collection of engine bug fixes and tweaks. SKSE plugin."**
> —**修复**是 bug fix；**调整**是可选的玩法/沉浸度特性。
> **实验性选项未经测试**，只应在你清楚自己在做什么时启用。

## 安装与配置

- 前置：**SKSE64**（SE 需 2.0.20；AE 需 2.1.5+）、**Address Library**、VC++ 2022 运行库。
- 配置在 **`Data/SKSE/Plugins/po3_Tweaks.ini`**。
- **该 ini 不会随安装生成**——**要先进一次游戏**（不必读档）才会被写出来；
  文件丢失时会自动重建，新版本的选项也会随之出现。

### MO2 特有的坑（社区实测）

首次进游戏后，`po3_Tweaks.ini` 会出现在 **MO2 的 Overwrite 目录**里。
**即使你手动把一份 ini 丢进 `Data/SKSE/Plugins/`，Overwrite 里仍可能被再生成一份。**
正确做法是：进一次游戏 → 把 Overwrite 里的 ini **移回该 mod 的目录**（或建一个配置 mod），
以后就按这个位置改。（来源：中文社区整理帖，属社区经验，但与 MO2 的 Overwrite 机制一致）

## 它修/调什么（发布页 Changelog 举例）

按发布页的 changelog 分类，可见的条目类型包括：

- **Fixes**：远距离引用加载崩溃、地图标记放置、恢复"不可拾取书籍"标志、
  投射物射程、战斗结束对话、加载时重施法术、家具动画类型判定、
  灯光附着崩溃、召唤法术补 NoAbsorb、编辑器 ID 缓存相关的一批修复……
- **Tweaks**：如可选的 `Faction Stealing` 等玩法调整。
- 版本演进的趋势是**性能与缓存优化**（editorID 缓存、语音描述符缓存等）。

> 具体开关名与默认值**以你的 ini 文件与当前发布页为准**——它在持续追加，
> 任何转述的清单都会很快过时。ini 里每项都有注释说明。

## 与同名作者其它项目的关系（这是最常混的一组）

| 项目 | 类别 | 本库条目 |
|---|---|---|
| **powerofthree's Tweaks** | 引擎修复/调整 | 本文 |
| **powerofthree's Papyrus Extender** | 脚本函数扩展 | [powerofthree's Papyrus Extender](../01-frameworks/po3-papyrus-extender.md) |
| **SPID / KID / BOS** | 运行时分发 | `02-distribution/` |
| **Papyrus Tweaks NG** | 脚本调度优化 | [Papyrus Tweaks NG](../09-diagnostics/papyrus-tweaks-ng.md) |

三个名字都带 po3/Tweaks，**用途完全不同，且常常需要同时安装**。

## 相关

- [SKSE64（Skyrim Script Extender）](../01-frameworks/skse64.md)、[Address Library for SKSE Plugins](../01-frameworks/address-library.md)
- [配置文件体系（哪个 ini 在哪、归谁管）](../11-config/settings-files.md)（ini 的落点与归属）
- [Papyrus Tweaks NG](../09-diagnostics/papyrus-tweaks-ng.md)
