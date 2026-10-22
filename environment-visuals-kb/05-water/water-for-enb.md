---
id: water-for-enb
title: Water for ENB（mindflux）
category: 05-water
version: 1.0.0
updated: 2026-10-22
tags: [Water for ENB, 水体, mindflux, ENB, CS, 位移]
kind: reference
source: https://www.nexusmods.com/skyrimspecialedition/mods/37061
summary: 为 ENB/CS 位移水体设计的水 mod：多水样式、消水缝、粒子瀑布、大量内置补丁；v2.21（2026-08）仍高频更新，与其它水 mod 互斥。
aliases: [WFE, 位移水, displacement, particle waterfalls]
---

# Water for ENB（mindflux）

- **作者**：**mindflux**（一手源：Nexus 37061 文件信息）
- **Nexus**：skyrimspecialedition/mods/**37061**；当前 **v2.21**
  （主文件 2026-08-01），42,495 endorsements
- **同作者**：Embers XD、Particle Patch（见[Embers XD](../06-weather-lighting/interior-lighting-mods.md)）

## 功能（一手源：发布页）

- **位移（displacement）支持**：ENB/CS 下的真实水面起伏；
- 多种水样式可选；大量自定义项；
- **消除绝大多数水缝**；更透明的静水；
- 大水体去流向、河流保留原版流向；
- 幽灵海/湖/河各自波形；黑暗环境无发光瀑布；
- 4K 主贴图 + **2K 性能版**；
- **粒子瀑布**附加组件（需 `iMaxDesired≥10000`，一手源：files 页）；
- **支持 Community Shaders**（"Shades of Skyrim"系列）。

## 依赖与互斥（一手源：发布页）

- **必须**有 ENBSeries 或 Community Shaders 才有高级水效。
- **与任何其它水 mod 互斥**（RW2/Pure Waters 等二选一）。
- 与 Depths of Skyrim 配合良好；兼容 iNeed/RND2.0/Keep it Clean/
  Wade In Water（选 Legacy iNeed Support）。
- 卸载警告：**Shades of Skyrim for ENB 版不建议中途卸载**（不开新局别卸）；
  CS 版可随时安全卸载。

## 补丁生态（一手源：发布页）

安装器内置大量补丁：Atlas Map Markers、Beyond Skyrim: Bruma、
ELFX Shadows、ETaC、Falskaar、Folkvangr、JK 系列、MEZF、
Flat World Map Framework 等；官方推荐用 **Synthesis patcher**
（有 panthuncia 为 Shades of Skyrim ENB/CS 做的专用 patcher）。

## Load order（一手源：发布页）

`Water for ENB.esm` → 各处 patches（ Landscape Fixes 在前）→
主插件 → 其它补丁 → FWMF 补丁最后。

## 相关

- [Realistic Water Two](../05-water/realistic-water-two.md)
- [ENB 预设与 CS 衔接](../08-practices/enb-presets-and-cs-bridge.md)
