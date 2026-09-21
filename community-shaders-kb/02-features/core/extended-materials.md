---
id: extended-materials
title: Extended Materials 扩展材质
category: 02-features
kind: core
status: released
version: 1.1.0
updated: 2026-09-21
tags: [材质, 视差, 复杂材质, 地形]
source: https://modding.wiki/en/skyrim/developers/community-shaders/Features-Home/extended-materials
summary: 用 Contact Refinement Parallax Mapping 提供高性价比视差与视差阴影，并支持 Complex Material 规范（环境遮罩、真实金属与镜面反射）。
---

# Extended Materials 扩展材质

> 分类：核心特性 · 状态：已发布

CS 的**材质地基**：更省性能的视差、视差阴影，以及 Complex Material 规范支持。

## Parallax 视差

- 原版 Skyrim **支持视差，但着色器是坏的**；[SSE Parallax Shader Fix](https://www.nexusmods.com/skyrimspecialedition/mods/31963) 能修，但物体看上去**依然明显扁平**。
- CS 用的是高度优化的 **Contact Refinement Parallax Mapping**，相比传统 POM / steep parallax，**性能与画质都显著更好**。
- 官方旧基准（用**明显更早的** CS 版本测得）：约 **0.22 ms** 开销、该场景 **6%** 帧率损失。

> ⚠️ **地形视差要求「所有」地形纹理都支持视差。** 部分替换会出问题——[Vanilla Complex Parallax - Landscapes](https://www.nexusmods.com/skyrimspecialedition/mods/88295) 是官方推荐的完整方案。
>
> 💡 CS 自带**大量地形渲染性能优化**，用来抵消视差开销。
>
> 💡 视差是**带宽瓶颈型**效果。想提速可以把视差纹理**重压成 BC4**。

## Parallax Shadows 视差阴影

所有视差材质都带**近似软阴影**支持。这是一项**极其廉价**的效果，对**所有平行光与点光源**生效。

## Complex Material 复杂材质

支持 **Complex Material 规范**（使用环境遮罩 environment mask），包含**视差**、更真实的**金属**与**镜面反射**。官方注明它是**基于 Nexus 上那份 CM 指南**实现的，**可能与其它着色器 MOD 的实现不完全一致**。

已知支持：Majestic Landscapes、Majestic Mountains Complex Material、Parallax Spell Impacts。

已知注意事项：

- 对**环境遮罩 alpha 通道非法**的改装内容可能出现纹理扭曲（官方举例：*Immersive Creatures* 里的 Durzog）。
- **不支持皮肤着色器**（官方说明：没有 MOD 用到这个特性）。
- CS 为此特性附带了一个 bug fix。

## 需求

- [Community Shaders](https://www.nexusmods.com/skyrimspecialedition/mods/86492)
- 用 **[PGPatcher](https://www.nexusmods.com/skyrimspecialedition/mods/120946) 修补过**的材质

## 相关条目

- [PGPatcher](../../05-tools/pgpatcher.md) · [True PBR 美术师指南](../../04-development/pbr-for-artists.md)
- 地形视差排查见 [实战常见坑](../../06-community/common-pitfalls.md)

## 贡献者

aers（原版视差修复与 SSE Engine Fixes）、shadowking97（原始着色器）、jeromeJrm（Complex Material 指南）、Ent、Pfuscher、MJP、thyrn、VishVadeva（基准测试）、hakasapl（Terrain Helper 支持）等。

---
*本条目依据官方功能页精修整理；如与官方页面不一致，以官方为准。*
