---
id: dynamic-cubemaps
title: Dynamic Cubemaps 动态立方体贴图
category: 02-features
kind: core
status: released
version: 1.1.0
updated: 2026-09-21
tags: [反射, 环境, 材质, 水体]
aliases: [动态立方体贴图, cubemap, 动态反射球, dynamic cubemaps]
source: https://modding.wiki/en/skyrim/developers/community-shaders/Features-Home/dynamic-cubemaps
summary: 用「屏幕空间反射捕获」让物体反射真实环境而非假场景，并完整支持 ENB 的 dynamic cubemaps 规范。
---

# Dynamic Cubemaps 动态立方体贴图

> 分类：核心特性（1.0+ 并入） · 状态：已发布

让物体**反射自己身处的真实环境**，而不是一张预先做好的假场景。

## 核心原理：Screen-Space Reflection Capture

把屏幕信息投影到一个球面当作立方体贴图使用。含义是：**只要某处被看见过一次，之后即使离开视野也能取用**——代价是精度。该方案受 Minecraft 的 *Nostalgia Shader* 启发，doodlum 在其上做了大量扩展。

在室外，这份数据会与反射立方体贴图混合，**带上随时间与天气变化的天空**。

### 三阶段流水线（每帧只跑一个，为性能）

1. **Capture 捕获**：把屏幕空间信息投影到原始立方体贴图，并更新用于淡入淡出的位置数据。
2. **Inference 推断**：补出因淡出或缺失而丢失的信息。
3. **Specular Irradiance 镜面辐照度**：生成用于反射的模糊纹理。

## 相比 ENB 规范多做了什么

**完整支持 ENBSeries 的 dynamic cubemaps 规范**（含 complex material 支持），并额外提供：

| 扩展 | 说明 |
|------|------|
| **有色反射** | 原版 cubemap 可用 **sRGB F0 反射率值**替代（可从 [physicallybased.info](https://physicallybased.info/) 这类 PBR 数值库取）。别把动态 cubemap 做成纯黑——**给它一个颜色**。黑色 cubemap 会被映射为 F0 = 1.0 |
| **模糊反射** | 标准反射做轻微模糊，观感更真实 |
| **Inference 推断** | 生成更准确的 cubemap |
| **淡入淡出** | 依位置淡入淡出数据；配合推断能**估计你身后/头顶/脚下的东西**，因此穿过一个 cell 时反射会变化 |
| **室外也加屏幕空间数据** | 因此夜间能捕获灯光与窗户，以及阴影、草等 |

此外它加入了 **fresnel** 形式的低成本**镜面 GI**（面向电介质表面），室内外都生效——所有表面现在都会在掠射角下轻微反射环境。

## 联动与调试

- **水反射可横跨整个屏幕**，并**完全取代室内 cubemap**。
- [Skylighting](../additional/skylighting.md) 会判定物体是否被天空遮挡，**阻止动态立方体贴图在不应出现天空反射的地方渲染天空反射**。
- 想检验某物体是否吃到动态 cubemap，用 [TESTCUBEMAP 测试模式](../../04-development/testing-and-debugging.md)。

## 贡献者

doodlum、jiaye。

---
*本条目依据官方功能页精修整理；如与官方页面不一致，以官方为准。*
