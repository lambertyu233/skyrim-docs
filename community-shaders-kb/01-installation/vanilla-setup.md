---
id: vanilla-setup
title: Vanilla 设置指南
category: 01-installation
version: 2.0.0
updated: 2026-09-21
tags: [画质, 设置, 照明, 天气, 推荐, PBR, MOD清单]
aliases: [原版设置, vanilla 配置, 游戏设置怎么调, CS 前置设置]
source: https://modding.wiki/en/skyrim/developers/community-shaders/vanilla-setup-guide
summary: 在已稳定安装 CS 的基础上，按官方推荐搭配照明、天气、窗口阴影、粒子补丁与 PBR 纹理，把画面推到最佳。
---

# Vanilla 设置指南

本页面向**已稳定安装完整 CS 套件**的玩家，讲如何充分发挥画质潜力。

> 还没装好 CS 的话，请先走 [安装指南](installation-guide.md)。从没 mod 过 Skyrim 的，官方推荐先读 **A Dragonborn's Fate**（moddinglinked.com）或 **STEP Modifications Guide**，再回来。
>
> 提供的 FOMOD 选项仅为**推荐**设置。**请务必读你要下载的 MOD 的说明**——官方原话是这能替作者和支持省下大量时间。

## 照明（Lighting）

照明 MOD 是让你把 CS 用到位的关键一环。官方点名**当前最流行的两款室内方案是 True Light 与 Lux CS**，两者观感都很好，纯按审美选。

> ✅ **装任何照明 MOD 之前，先装 Light Placer 与 CS Light。**

规则（官方明确）：

- 照明 MOD 会**手动放置光源**（室内或室外），因此作者常把编辑**拆成两个插件**（一个室外、一个室内），方便你跨 MOD 混搭。
- ⚠️ **同一时间只用一款室内 + 一款室外照明 MOD。**
- ⚠️ **你的室外光照同时受天气 MOD 影响。**
- ⚠️ **任何用到 ENB Light / ENB Particle Lights 的 MOD 都与 CS 不兼容。** 用了的话，**那些物体不会发出任何光**。请改找基于 **CS Light 或 Light Placer** 的补丁。

### True Light

> 一套覆盖面广的现代照明 MOD，使用 po3 的 Light Placer 与 CS 的 Inverse Square Lighting 特性。

FOMOD 选项（官方记录的推荐流程）：`Next` → `Yes` → `Yes（推荐）` → `Yes（推荐）` → `Regular` → **`True Light Exteriors`（想混搭室内外的话不要选它）** → `Dwemer Swap BOS` → `FX Glow Remover BOS` → `Install`。

### Lux CS

> 针对 Lux 与 Community Shaders 的色调映射与 Image Space 编辑，带 Light Placer 支持。

- Lux CS 的说明页里有 **Lux 本体的 FOMOD 选项指引**。
- 想要**室外光照编辑**，用 **Lux Via** 与 **Lux Orbis**。
- ⚠️ **Lux CS 与「Ambient Templates for Lighting Mods」「Windows Shadows Ultimate」不兼容。**

FOMOD 选项：`LightPlacer addon` → `Bright` → `Install`。

### 其它常见照明 MOD

以下是**通用型**照明 MOD：能与 CS 一起工作，但**不使用 CS 的色调映射器或 Light Placer**。

> ⚠️ **不要用 EVLaS**——Sky Sync 已完全取代它。
>
> ⚠️ **Modern Lighting Overhaul 2 高于 1.3.6 的任何版本都与 CS 不兼容。**

- **Lux Via / Lux Orbis**（仅室外）
- **ELFX**（含室内、室外独立插件）
- **Luminosity Lighting Overhaul**（仅室内）
- **Relighting Skyrim**（含室内、室外独立插件）
- **Skyrim is Luminous**（光源编辑，去说明页确认兼容性）
- **Lightened Skyrim**（含室内、室外独立插件）

## 天气（Weathers）

天气 MOD 改写室外光照与天气数据，让 CS 套件充分发挥。**务必读它们的说明页**——里面常链接到其它视觉 MOD。**先确认你喜欢的天气 MOD 有没有 CS 移植版。**

> 官方鼓励你都试一遍，它们各有审美取向。
>
> ⚠️ **同一时间只用一款天气 MOD。**

官方给出的（非穷尽）清单：

- **NAT.CS III**（dBottle）
- **Obsidian CS**（dBottle）
- **Astralite Weathers**（Laminin）
- **Azurite III CS**（Dlizzio）
- **Vanilla CS**（dBottle）
- **Real Weathers Remastered**（PixelsSquared）
- **Nirn Whispers**（CarbonDice）

## 其它视觉增强

### 窗口阴影（室内）

**Window Shadows Ultimate（WSU）**是**高度推荐**的室内照明 MOD，能产生真实的窗户阴影。别忘了同时看它的 **Patch Hub**。

> ⚠️ **WSU 与以下互斥**：Window Shadows RT、**Lux**、ELFX Shadows、Enhanced Lights and FX、Relighting Skyrim (Interiors)、Skyrim is Luminous。

FOMOD 选项：先按你的负载装所需补丁 → `Brightest` → `Normal` → `Enable` → `Install`。

### CS Particle Patch

**修复了大量原版网格的光照，强烈推荐。**

- 与 **ENB Particle Patch 兼容**，但**必须让 CS Particle Patch 覆盖它**。
- 安装时**务必检查它的需求**——不是所有需求都是硬性的。

### DIAL（Dynamic Interior Ambient Lighting）

按**一天中的时间**调整室内亮度。**高度推荐。**

### 亮度调节

- **室内**：看 `Ambient Templates for Lighting Mods` 的 FOMOD 亮度选项（**百分比越高越亮**）。
- **室外**：由你的天气 MOD 插件决定。可以先用 **KreatE** 调亮度值，再把改好的值**复制进 xEdit 里的插件**。

### 去除假辉光（Remove Fake FX）

要去掉原版光源周围那圈 **2D 假辉光**，**True Light 的 FOMOD 提供了 Base Object Swapper 配置**。

### 立方体贴图（Cubemaps）

**Seamless Dynamic Cubemaps** 提供动态立方体贴图纹理，并修复多种改装与原版 cubemap。**与 PBR 纹理搭配良好。**

## PBR 纹理

CS 通过 **True PBR** 支持 PBR 纹理；用上进阶渲染技法后，PBR 纹理能接近真实生活的观感。

**入门推荐**（官方清单）：

- **Faultier's PBR Skyrim** — 对原版纹理做了全面重制，适合起步；
- **Skyland PBR**
- **Cathedral Landscapes PBR**
- **Vanaheimer Landscapes**（主文件里选 PBR 那项）

也要**为你已有的纹理 MOD 找 PBR 补丁**——建议从 **PBR Hub** 开始找。想自己创作 PBR 纹理，看 [True PBR 美术家指南](../04-development/pbr-for-artists.md)。

> ⚠️ **加了 PBR 纹理就必须用 [PGPatcher](../05-tools/pgpatcher.md) 修补网格**，否则不会正确生效。
>
> 好习惯：**为 PGPatcher 的输出单独建一个 output mod**，并严格按 PGPatcher 说明里的冲突管理来做。
>
> ✅ 用 **Asset Doctor** 确认没有缺失纹理。
>
> ✅ **PBR 纹理受益于「没坏掉的网格」**——可以从 **Mesh Improvement Compilation** 这类网格修复包起步（网格修复 MOD 的海洋是无尽的）。

## 性能

铁律：**你加的 MOD 越多，性能越差。** 除非机器很强，加上这些 MOD 与纹理会带来帧率下降。

## 预设（Presets）

目前设置预设**仅适用于 CS 的实验构建**，在该项目的 **Discord** 获取。

## 相关条目

- [安装指南](installation-guide.md) · [ENB 迁移指南](enb-migration.md) · [系统与环境需求](requirements.md)
- [Light Placer](../05-tools/light-placer.md) · [PGPatcher](../05-tools/pgpatcher.md)
- [实战常见坑](../06-community/common-pitfalls.md)（照明/天气冲突的排错）
