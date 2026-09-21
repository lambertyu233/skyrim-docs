---
id: extended-translucency
title: Extended Translucency 扩展半透明
category: 02-features
kind: core
status: released
version: 1.1.0
updated: 2026-09-21
tags: [半透明, 材质, 织物, 玻璃]
aliases: [扩展半透明, translucency, 透光, 皮肤透光]
source: https://modding.wiki/en/skyrim/developers/community-shaders/Features-Home/extended-translucency
summary: 让薄织物与脏玻璃呈现近乎照片级的半透明观感；侧看更不透明并产生「边缘轮廓」，支持按 nif 网格覆盖材质模型。
---

# Extended Translucency 扩展半透明

> 分类：核心特性（1.4.7+ 并入） · 状态：已发布

为**薄织物**与**有杂质的玻璃**提供接近照片级的渲染。效果是：**从侧面看时材质更不透明，并产生「边缘轮廓（rim edge）」**。例如蕾丝袖口的褶皱会更有结构，玻璃瓶会更「古董」。

## 游戏内设置（END → Extended Translucency）

### Material Models 材质模型

控制材质不透明度**如何随视角变化**：

| 值 | 名称 | 说明 |
|:--:|------|------|
| 0 | Disabled | 不做各向异性半透明 |
| 1 | Rim Light | 朴素的边缘光效果，**不是**基于物理模型 |
| 2 | Isotropic Fabric | *假想*织物：单向排布的线。**尊重法线贴图** |
| 3 | **Anisotropic Fabric（推荐）** | 常见织物：切线与副法线双向编织。**但吃不到法线贴图**（Skyrim 的切/副法/法线数据不受法线贴图影响） |

> 这是**全局默认值**；每个 nif 网格可以设自己的值来覆盖它（见下）。
> 官方补充：这些模型**虽非专为此设计，但对「低透明度的脏玻璃」效果很好**。

### Transparency Increase 透明度提升

半透明材质**平均而言会变得更不透明**，这可能偏离原作者意图。调这个滑块来补偿，并**扩大输出的动态范围**。

> 给 MOD 作者：该效果会**从纹理原始 alpha 反推线材的粗细与密度**。例如 alpha 0.5 → 各向同性模型下 *线粗:线距 = 1:1*（沿表面法线看时通光面积为 0.5）。因此 alpha 与织物密度参数基本线性相关。

### Skinned Mesh Only（仅蒙皮网格）

阻止该效果作用于**静态网格**，可用于修复奇怪的透明渲染瑕疵。

> ⚠️ **此选项目前默认开启**。所以你会**看不到**炼金瓶、蒸馏器、展示柜等静态网格上的效果。如果没看出任何令人不适的问题，把它关掉并 **SAVE** 设置。

## 给 MOD 作者 / 进阶用户：按网格覆盖

需要 [Outfit Studio](https://www.nexusmods.com/skyrimspecialedition/mods/201) 或 [Nifskope](https://github.com/niftools/nifskope/releases) 给网格加一个 `NiIntegerExtraData`：

- 节点名设为 **`AnisotropicAlphaMaterial`**；
- 值填 0–3（对应上表），**填 0 可在该网格上强制关闭此效果**。

> 带显式 `AnisotropicAlphaMaterial` 设置的网格**不受**「Transparency Increase」等滑块影响，以尊重作者意图。请把透明度提升**预乘进网格纹理的 alpha 通道**。

## 兼容性与性能

- 与任何 CS 效果一样，**与 ENB 不兼容**。
- 默认套用到某些网格上可能产生非预期渲染，此时给该网格加 `AnisotropicAlphaMaterial=0` 关掉。
- **性能开销可忽略**——本质上只是着色器里几行向量数学：

```glsl
alpha = alpha / min(1.0, (abs(dot(view, normal)) + 0.001));
```

## 许可

GPL-3.0。若想在别的游戏里用这段着色器代码或数学，**至少**需注明出处。

## 贡献者

doodlum（发起与打磨）、alandtse（合并协助与图形管线调试）、davo0411（MOD 页）等。

---
*本条目依据官方功能页精修整理；如与官方页面不一致，以官方为准。*
