---
id: weather-mods-overview
title: 天气 mod 生态总览
category: 06-weather-lighting
version: 1.0.0
updated: 2026-10-22
tags: [天气, weather, 选型, 生态, NAT]
kind: concept
source: https://www.nexusmods.com/skyrimspecialedition/mods/12125
summary: 一次只装一个天气 mod；七大主流（Obsidian/Cathedral/NAT/CoT/Vivid WD/Dolomite/Aequinoctium）各有明确作者与风格，雷雨音效另算一层。
aliases: [天气 mod, 云, 雪, 雷雨, climates]
---

# 天气 mod 生态总览

## 铁律

**天气 mod 之间互斥**（Cathedral Weathers 原话："Not compatible with other
weather mods"，一手源：Nexus 24791）。雷电/降雨特效 mod（True Storms）
通常作为可叠加层，但同功能（都改雷声）依然冲突。

## 主流选手与作者（一手源：Nexus 各页 / Epicube 对比视频整理）

| mod | 作者 | Nexus | 备注 |
|---|---|---|---|
| **Obsidian Weathers and Seasons** | DrJacopo（Megaloblast）+ Arindel | 12125 | ~90 天气，~400kB 插件，随时可装卸 |
| **Cathedral Weathers and Seasons** | DrJacopo + Arindel（"The Community"） | 24791 | MOTM；围绕 Lightweight Grass 设计；~16MB VRAM |
| **NAT（Natural and Atmospheric Tamriel）** | **l00ping**（Nexus 名 L00） | SE 版 Nexus 搜 "NAT" | **必须放在 load order 最后**（发布页原话）；自带 FX/SSS/粒子 |
| **Climates of Tamriel SE** | JJC71 | — | 老牌经典 |
| **Vivid Weathers Definitive Edition** | Mangaclub - Doodlezoid | — | 老牌 VE 移植 |
| **Dolomite Weathers** | DrJacopo + Kojak747 | — | Natural Lighting 系 |
| **Aequinoctium** | Arindel | — | CWS 的前身之一 |
| **Rustic Weathers and Lighting** | Arindel | — | Rustic 系天气 |
| **True Storms SE** | **fadingsignal** | 2472 | 雷雨音效+贴图，无脚本可随时装卸 |
| **Mythical Ages** | Arindel | — | |
| **Azurite Weathers** | JonnyWang（Megaloblast） | — | |
| **RAID Weathers** | Olivier Doorenbos | — | |

## 与光照/ENB 的耦合（一手源）

- **Cathedral Weathers 的草-地过渡会被多数 ENB 破坏**；其"地平线接缝修复"
  （把远雾混入第 28 层云）也会被 ENB 破坏——选 ENB 预设要专门找
  "works with Cathedral Weathers without breaking the horizon" 的
  （STEP 给了名单：A Cathedralist's ENB、Blubbos ENB ReShade、
  CELESTIAL CATHEDRAL、iiENB、Ljoss、Lucid ENB、PRENB、
  Ragnar's Vivid ENB for Cathedral Weathers 2、Serio's ENB）。
- NAT 自带 tonemapping/粒子/伪云影，与重度 ENB 叠加易过艳——
  作者所有展示图均**未用 ENB/ReShade/SweetFX**（一手源：NAT 页）。

## 选型速查（社区经验）

- 要"自然奇幻 + 现代维护"：Cathedral Weathers。
- 要"阴郁压迫 + 远景清晰"：Obsidian。
- 要"All-in-one 视觉 overhaul + 愿意读长文"：NAT（且接受置底）。
- 只要更好的雷声雨声：True Storms 叠在任意天气 mod 上（同功能仍冲突）。

## 相关

- [Obsidian Weathers](../06-weather-lighting/obsidian-weathers.md)、
  [Cathedral Weathers](../06-weather-lighting/cathedral-weathers.md)
- [ELFX](../06-weather-lighting/elfx.md)、[室内光照 mods](../06-weather-lighting/interior-lighting-mods.md)
- [ENB 预设与 CS 衔接](../08-practices/enb-presets-and-cs-bridge.md)
