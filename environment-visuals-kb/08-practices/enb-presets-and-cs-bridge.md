---
id: enb-presets-and-cs-bridge
title: ENB 预设选择与 Community Shaders 衔接
category: 08-practices
version: 1.0.0
updated: 2026-10-22
tags: [ENB, 预设, Community Shaders, CS, 迁移]
kind: tutorial
source: https://stepmodifications.org/wiki/SkyrimSE:2.0.0
summary: ENB 文件放游戏根目录而非 Data；预设要与天气 mod 配对（地平线修复易被破坏）；CS 是模块化替代路线，视差/复杂水两家互通。
aliases: [enb 预设, enbseries, enblocal, community shaders 迁移, PI-CHO, Rudy ENB]
---

# ENB 预设选择与 Community Shaders 衔接

## ENB 基础事实（一手源：enbdev.com + 社区经验）

- **ENBSeries 官方站 = enbdev.com**（Boris Vorontsov）；二进制
  （`d3d11.dll` + `enbhost.exe` + `enbseries/`）放**游戏根目录**
  （与 SkyrimSE.exe 同级），**不是 Data**。
- 预设 = `enbseries.ini` + `enblocal.ini`（+ 可能的 shaders/贴图）。
  预设里带 Data 的部分才走 mod 管理器。
- 改性能先动 `enbseries.ini` 的 `EnableBloom` / `EnableDepthOfField` /
  `EnableAmbientOcclusion`——但与预设设计冲突时会"变丑"，谨慎。

## 预设配对（一手源：STEP wiki）

STEP 不为指南指定预设，但给了一份**为 Cathedral Weathers 做、不破坏地平线**
的名单：A Cathedralist's ENB、Blubbos ENB ReShade、CELESTIAL CATHEDRAL ENB、
iiENB、Ljoss、Lucid ENB、PRENB、Ragnar's Vivid ENB for Cathedral Weathers 2、
Serio's ENB。

原因（一手源：CWS 页）：**多数 ENB 会破坏** CWS 的草-地过渡与
"远雾混入第 28 层云"的地平线修复。选预设先看它声明支持哪个天气 mod。

## 性能（一手源：STEP ENBSeries INI Reference）

- `EnableSunRays`（godrays）：约 2-5% FPS。
- `EnableSkyLighting`：最高约 15% FPS；`EnableDirectionalSkyLighting` 在其之上再吃性能。
- `EnableCloudShadows`：默认开且**游戏内不可改**，由预设作者决定。

## Community Shaders 路线（详见 community-shaders-kb）

- **视差**：202X 页明说视差可用 "ENB **or** Community Shaders"；
  Water for ENB 同样双支持（"Shades of Skyrim"）。
- **Complex Material**：CS 的 Extended Materials 实现了 CRPM 视差
  （约 0.22ms）+ Complex Material 规格（一手源：modding.wiki）。
- 迁移注意：ENB 与 CS 的某些功能**互斥或行为不同**（如 Complex Grass 的
  normal map 要求见[草类生态](../04-flora/grass-mods-overview.md)）。

## 驱动级 AF 必须关（一手源：Skyrim Stability Guide）

用 ENB 的 `ForceAnisotropicFiltering=true` + `MaxAnisotropy=16`；
**显卡控制面板的 AF 关掉**——驱动强制 AF 破坏视差。

## 相关

- [视差与 Complex Material](../01-principles/parallax-and-complex-material.md)
- [VRAM 与 ENBoost](../01-principles/vram-and-enboost.md)
- [Cathedral Weathers](../06-weather-lighting/cathedral-weathers.md)
