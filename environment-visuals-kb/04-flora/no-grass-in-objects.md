---
id: no-grass-in-objects
title: No Grass In Objects（meh321）
category: 04-flora
version: 1.0.0
updated: 2026-10-22
tags: [NGIO, 草, 性能, meh321, SKSE]
kind: reference
source: https://www.nexusmods.com/skyrimspecialedition/mods/42161
summary: SKSE 插件：阻止草从岩石/地板/木箱/路面里长出来，可扩展草的绘制距离并生成草 LOD 缓存；v1.6.14 已支持游戏 1.7.99/1.7.104。
aliases: [No Grass In Objects, 草穿模, 草缓存, grass cache]
---

# No Grass In Objects（meh321）

- **作者**：meh321（一手源：Nexus 42161）
- **Nexus**：skyrimspecialedition/mods/42161；当前 **v1.6.14**
  （2026-10-19 更新），26,077 endorsements
- **依赖**：SKSE64 + Address Library；需 VC++ 2022 x64 运行库

## 功能（一手源：发布页）

1. **阻止草从物体里长出**：岩石、地板、床卷、木箱、路面等——
   用射线检测判断草该不该长。
2. **Extended Grass Distance**：允许草在已加载单元之外绘制。
3. **草缓存（grass cache）**：为 DynDOLOD 的草 LOD 生成提供基础。

## 版本与 1.7.x 适配（一手源：changelog）

- v1.6.11-1.6.14：连续修复 **1.7.99/1.7.104** 的启动报错与崩溃
  （"Fixed crash while loading a save with extended grass with game
  versions 1.7.99/104"）——**是环境类 mod 中较早适配 1.7.x 的**。
- v1.6.3：射线检测优化，草生成平均快 60%，减少切区卡顿。
- v1.6.4：新增 `_NGIO` 后缀 ini 做**按 trishape 的过滤**
  （如只允许山崖平面长草、忽略路面泥土部分）。

## 与 LOD 的关系（一手源：Nolvus 指南）

- NGIO 设置变更（除两个距离值）→ **重建草缓存**（删 Grass Cache mod 重跑）。
- 顺序上：先 NGIO 出缓存 → DynDOLOD 用它生成草 LOD。

## 相关

- [草类生态](../04-flora/grass-mods-overview.md)、[草地 INI 设置](../04-flora/grass-ini-settings.md)
- [LOD 生成完整流程](../08-practices/lod-generation-workflow.md)
- 游戏版本矩阵见 `character-appearance-kb/00-overview/game-version-1-7-x.md`
