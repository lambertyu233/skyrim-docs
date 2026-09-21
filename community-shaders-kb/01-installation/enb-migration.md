---
id: enb-migration
title: ENB 迁移指南
category: 01-installation
version: 1.0.0
updated: 2026-09-20
tags: [ENB, 迁移, Effects11, 兼容]
aliases: [ENB 换 CS, 从 ENB 迁移, ENB 卸载, enb migration, 转投 CS]
source: https://modding.wiki/en/skyrim/developers/community-shaders/ENB-Migration-Guide
summary: 从 ENB 模组列表迁移到以 CS 为核心的配置：移除 ENB 二进制、替换特性、重装相关 MOD。
---

# ENB 迁移指南

将基于 ENB 的 MOD 列表转换为以 Community Shaders 为核心的配置。

## 基础转换

### 步骤 1：移除 ENB 二进制

CS 与 ENB 的 DLL **同时安装会导致游戏崩溃**。ENB 二进制位于游戏根目录（或 Rootbuilder 的 `Root` 文件夹），删除： `d3d11.dll` 与 `d3dcompiler_46e.dll`。

> **无需**删除 `enbseries` 文件夹与 ENB ini——加载 ENB 预设（经 Effects 11）时还要用到它们。

### 步骤 2：移除 ENB 专属 / 不兼容 MOD

CS 会在检测到某些不兼容 MOD 时**自我禁用**。先查 [FAQ](../03-reference/faq.md) 最新清单。常见需移除：

- EVLaS/AELaS（被 CS Sky Sync 替代）
- KiLoader、ENB Worldspace Weatherlists、ENB Input Disabler、ENB Helper Plus、ENB AO Toggler、ENB Custom UI Color
- ENB Anti-Aliasing（被 CS Upscaling 替代）、ENB Frame Generation（被 CS Upscaling 替代）
- Skyrim Upscaler（付费/免费均不支持）
- ENB Light 及其衍生（有限支持，建议换 Light Placer）
- ENB Light Inventory Fix (ELIF)、ENB Terrain Blending Fix（CS 已含）、NVIDIA Reflex（与 CS 同用会卡顿）、Native Mesh Light Flicker Fix（被 CS LLF 替代）、Native Water Light Stabilizer（被 CS LLF 替代）

> 列表非穷举。可在 MOD 列表中搜索含 “ENB” 的项先禁用。**Particle Patch 受 CS 支持，无需移除**（放加载顺序靠前让其被覆盖即可）；Water for ENB 完全兼容 CS 且有 CS 专用 FOMOD。
> 本清单最后更新：2026/06/15。

### 步骤 3：安装 CS 前置

先读 [安装指南](installation-guide.md)。必须装：Address Library、SSE Engine Fixes、Crash Logger（可选但推荐）。Engine Fixes 的 SKSE64 Preloader 需放入你之前放 ENB 二进制的根目录。

### 步骤 4：安装 CS + Effects 11

核心 MOD 必装且先加载，随后加载各附加特性。推荐与 Effects 11 搭配：
- **SSGI**：通过光遮挡与反弹带来更真实光照，质量远高于 ENB SSAO/IL（很重）。
- **Skylighting**：为屋檐、树荫、建筑内等遮蔽区增加着色，质量高于 ENB 版。

### 步骤 5：Effects 11 后处理

支持大多数 ENB 预设（有兼容限制），于 [mod.pub](https://mod.pub/skyrim-se/415-effects-11) 下载。预设安装方式与 ENBSeries 相同：`enbseries` 文件夹与 `enbseries.ini` 放入根目录（也可放 Data，但不推荐）。

**兼容注意**：
- **不支持**：Depth of Field、Sky Scattering、Prepass Shaders。
- **加密 ENB 预设无法加载**（需先解密），例如 Cabbage、Kauz、Dawnfire、Silent Horizons 2、Picta。
- CS 已替代：SSAO/IL→SSGI、Skylighting→Skylighting、抗锯齿→Upscaling、反射/水/水下→Water Effects、SSS→SSS、阴影→Screen Space Shadows。

### 步骤 6：重装部分 MOD

- **Lux**：重装并取消所有 particle 与 optimized 网格。
- **Embers XD**：重装并选 CS 选项。
- **Water for ENB**：重装并选 CS 选项（仅当你使用的风格需要）。

### 步骤 7：收尾

预设在 CS 菜单 `Effects 11` 标签页微调。仍有问题去 Discord。

## 完整转换

在基础转换之上进一步将整个列表转向 CS：

1. 完成基础转换（游戏已无图形问题）。
2. 移除更多 ENB 专属 MOD（不再需要但无害的，如 Sky Reflection Fix for ENB、Capture Warmer for ENB、Bright Waterfall Fix for ENB、Footprints - ENB patch、ENB Light Detection Fix、Word Wall Transparency Fix for ENB）。清单最后更新 2026/01/31。
3. **天气 MOD**：不用 Effects 11 时强烈依赖天气 MOD 决定室外观感。CS 补丁示例：NAT.CS（配 NAT.ENB III）、Obsidian CS（配 Obsidian，移除 Rudy ENB Obsidian 补丁）、Azurite III HDR/CS/Enhanced。
4. **用 Light Placer 替换 ENB Light**：搜索列表中的 “ENB Light” 并禁用（注意 MLO2 等未明示的依赖）。社区替代是 **Light Placer + CS Light**。
5. （WIP）未来可用 CS **Post Processing** 替代 Effects 11，充分利用 Linear Lighting 与 HDR Display，并支持 DoF 等 Effects 11 不支持的特性。
