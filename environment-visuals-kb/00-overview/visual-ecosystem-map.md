---
id: visual-ecosystem-map
title: 环境美化生态地图与选型总纲
category: 00-overview
version: 1.0.0
updated: 2026-10-22
tags: [总览, 生态, 选型, 环境美化, 画质]
kind: concept
source: https://www.nexusmods.com/skyrimspecialedition/mods/659
summary: 一张图看懂环境美化的六层结构：网格底座→材质替换→地形/植被/水体→天气光照→视差增强→LOD 远景，以及各层怎么选。
aliases: [材质, graphics, visuals, overhaul]
---

# 环境美化生态地图与选型总纲

## 六层结构（自下而上）

环境美化 mod 不是一堆并列的"高清包"，而是**分层的堆叠**。理解层级是排序与排错的前提：

| 层 | 作用 | 代表 mod | 详见 |
|---|---|---|---|
| L6 LOD 远景 | 让远处的地平线不再平坦 | DynDOLOD + xLODGen | [DynDOLOD](../07-mesh-tools/dyndolod.md) |
| L5 后处理 | 全局光照/景深/辉光/视差开关 | ENBSeries 预设、Community Shaders | [ENB 预设与 CS 衔接](../08-practices/enb-presets-and-cs-bridge.md) |
| L4 天气与光照 | 决定情绪与色彩的总开关 | Obsidian / Cathedral / NAT + ELFX / Lux | [天气 mod 生态](../06-weather-lighting/weather-mods-overview.md) |
| L3 世界内容 | 地形/山脉/树/草/水 | MM / HLT / RW2 等 | 03~05 分类 |
| L2 材质替换 | 贴图与静态网格 | SMIM / Skyland / 202X 等 | 02 分类 |
| L1 网格底座 | 修接缝、加切线、补面 | SMIM | [SMIM](../02-textures/smim.md) |

**选型逻辑**：L1/L2 决定"材质统一感"，L3 决定"世界形状"，L4 决定"氛围"，
L5 决定"镜头感"，L6 决定"远景可信度"。**预算有限时优先 L4**——
天气光照是单位成本视觉收益最大的一层（社区共识，多个指南均如此建议）。

## 三大选型轴线

1. **一体化 vs 混搭**：一体化包（Skyland AIO、Noble、Vivid Landscapes AIO）
   胜在风格统一；混搭（SMIM + 202X + 单独山脉/树/草）胜在单点质量上限。
   混搭的前提是理解[覆盖规则](../08-practices/install-order-and-conflicts.md)。
2. **分辨率分层**：同一包常提供 4K/2K/1K 甚至 512（Verdant）。
   原则是"**2K 全覆盖胜过 4K 爆显存**"——见[性能预算](../08-practices/performance-budget.md)。
3. **视差依赖**：视差（parallax）地形/网格**必须**有 ENB 或 Community Shaders
   才能显示（一手源：Skyrim 202X 发布页"To see the parallax effect, download the
   latest ENB version for Skyrim SE Or Community Shaders"）。无 ENB/CS 时，
   视差包的白配置不如普通 2K 包。原理见[视差与 Complex Material](../01-principles/parallax-and-complex-material.md)。

## 本工作区其它库的分工

- **渲染框架本身**（Community Shaders 功能/安装/版本）→ `community-shaders-kb`，本库不重复。
- **角色捏脸/身形/骨骼** → `character-appearance-kb`。
- **MO2 覆盖规则/USVFS 机制** → `mo2-usvfs-kb`，本库只在实战条目里引用结论。
- **工具链版本**（SKSE/Address Library/引擎修复）→ `skyrim-tools-kb`。

## 版本敏感性

本库条目记录的事实均绑定 2026-10 前后的上游版本。游戏已进入 1.7.x 分支
（见 `character-appearance-kb/00-overview/game-version-1-7-x.md` 与
`skyrim-tools-kb`），部分环境 mod 是否适配 1.7.x 需在条目内单独确认——
目前确认适配的有 No Grass In Objects 1.6.11+（一手源：Nexus 更新日志）。

## 证据等级约定

- **一手源**：Nexus 发布页描述/文件页/更新日志、官方仓库 README、官方站点。
- **社区经验**：STEP 指南、Nolvus 等整合指南、论坛高赞回帖。
- **未核实**：单一二手转述且无出处的说法，本库明确标注，不当作事实传播。
