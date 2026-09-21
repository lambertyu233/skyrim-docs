---
id: incompatible-mods
title: 不兼容 MOD 清单
category: 03-reference
version: 1.1.0
updated: 2026-09-21
tags: [兼容, ENB, 排错, 警告, 照明, 天气]
source: https://modding.wiki/en/skyrim/developers/community-shaders/faq#what-mods-are-not-compatible-with-cs
summary: 与 CS 冲突或需调整的 MOD 汇总，分为完全不兼容与需微调两类。
---

# 不兼容 MOD 清单

> ⚠️ **切勿绕过 CS 的兼容保护**——否则失去官方支持且极易 CTD。

## 完全不兼容（会导致无法初始化或崩溃）

- **ENBSeries**：经 [Effects 11](https://mod.pub/skyrim-se/415-effects-11) 支持未加密预设；详见 [ENB 迁移指南](../01-installation/enb-migration.md)。
- **Particle lights / ENB lights**：1.4–1.7 不支持，1.8 有限支持；建议改用 [Light Placer](https://www.nexusmods.com/skyrimspecialedition/mods/127557)。
- **Skyrim Upscaler**（DLSS / FSR2 / XeSS）：与 [Upscaling - CS](https://www.nexusmods.com/skyrimspecialedition/mods/156952) 冲突。注意 CS 的 Upscaling **本身不支持 XeSS**（详见 [Upscaling 条目](../02-features/additional/upscaling.md)）。
- **EVLaS / AELaS**：与 [Sky Sync - CS](../02-features/core/sky-sync.md) 冲突。Sky Sync **检测到它们会自动禁用自己**；官方 Vanilla 设置指南明确要求「不要装 EVLaS」。
- **ReShade Helper**
- **NVIDIA Reflex Support**
- **TAA Sharpen**
- **SSE Parallax Shader Fix**：CS 已取代；删除 `d3dcompiler_47.dll`（Linux 除外）。
- **Native Mesh Light Flicker Fix**
- **Dynamic Wetness**：与 PBR 冲突导致发白。

## 需调整 / 轻微不兼容

- **Lux**：重装时**不勾选** “optimized/particle” 网格；可选 [Lux CS patch](https://www.nexusmods.com/skyrimspecialedition/mods/153919)。
- **Skyrim Souls**：菜单透明，禁用帧生成。
- **Skyrim Together Reborn**：与 Upscaling 同用易崩，玩 STR 时移除此功能。
- **Alternative Conversation Camera**：黑边不兼容，禁用此功能。
- **Display Tweaks**：Borderless upscale 不兼容，用 CS Upscaling；需无边框窗口。
- **Improved Camera**：月球变暗，测试版已修复。
- **ReShade**：深度缓冲特效与帧生成不兼容；1.4 起不支持 UI 屏蔽 ReShade。
- **Auto Parallax**：与 True PBR（experimental）不兼容，用 PGPatcher。
- **PrivateProfileRedirector**：使用 ≥0.6.x。
- **Simplicity of Snow / Ash**：PBR 下多 pass 错误，改用单 pass（如 BDS3）。
- **Skyrim Platform**：多问题。
- **MARA**：致崩且误指 CS。

## 不再需要（不致崩，功能已集成）

- **Capture Warmer**、**Sky Reflection Fix**：已集成入 CS。
- **Rim Lighting Removed**：CS 自有调整。
- **Splashes of Storms**：CS 湿润特效覆盖（主观可选；Splashes of Skyrim 不同）。

## 版本演进：被并入核心的特性

CS 升级后，以下特性被并入核心或他处，**达到对应版本须移除**：

| 特性 | 并入核心版本 |
|------|------------|
| Dynamic Cubemaps | 1.0+ |
| Complex Parallax Materials | 1.0+ |
| Water Parallax | 1.0+ |
| Tree LOD Lighting | 1.0+ |
| Light Limit Fix | 1.4+ |
| Frame Generation | 1.4+ |
| Extended Translucency | 1.4.7+ |
| Inverse Square Lighting | 1.4.7+ |
| Terrain Shadows | 1.4.7+ |
| Water Effects | 1.4.7+ |
| Grass Collision | 1.5+ |
| Grass Lighting | 1.5+ |
| Screen-Space Shadows | 1.5+ |
| Subsurface Scattering | 1.5+ |
| Sky Sync | 1.7+ |
| Cloud Shadows | 1.8+ |

低于指定版本则仍兼容。

> 各功能的准确纳入版本另见 [版本与支持策略](../00-overview/version-and-support.md)。

## 照明 MOD 之间的互斥规则

CS 本身与几乎所有照明 MOD 兼容，但**照明 MOD 彼此之间**有一套硬规则（出自官方 Vanilla 设置指南）：

- ⚠️ **同一时间只用一款室内 + 一款室外照明 MOD。**
- ⚠️ **同一时间只用一款天气 MOD**（天气 MOD 会改写室外光照）。
- ⚠️ **不要用 EVLaS** —— Sky Sync 已完全取代它。
- ⚠️ **Modern Lighting Overhaul 2 高于 1.3.6 的版本与 CS 不兼容。**
- ⚠️ **Window Shadows Ultimate** 与以下互斥：Window Shadows RT、**Lux**、ELFX Shadows、Enhanced Lights and FX、Relighting Skyrim (Interiors)、Skyrim is Luminous。
- ⚠️ **Lux CS** 与 **Ambient Templates for Lighting Mods**、**Windows Shadows Ultimate** 互斥。
- ⚠️ 任何使用 **ENB Light / ENB Particle Lights** 的 MOD 与 CS 不兼容——用了也不会发光，改用 **CS Light / Light Placer** 补丁。

> 官方推荐的照明与天气 MOD 清单见 [Vanilla 设置指南](../01-installation/vanilla-setup.md)。
