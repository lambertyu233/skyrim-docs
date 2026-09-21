---
id: inverse-square-lighting
title: Inverse Square Lighting 平方反比光照
category: 02-features
kind: core
status: released
version: 1.1.0
updated: 2026-09-21
tags: [光照, 物理, xEdit, LightPlacer, 开发]
aliases: [平方反比, inverse square, 光照衰减, 光衰减]
source: https://modding.wiki/en/skyrim/developers/community-shaders/Features-Home/inverse-square-lighting
summary: 用「光源有尺寸」+「衰减截断值」把光照衰减换成平方反比，性能几乎无代价；附带实时灯光编辑器，并给出 xEdit 与 Light Placer 两种配置法。
---

# Inverse Square Lighting 平方反比光照

> 分类：核心特性（1.4.7+ 并入） · 状态：已发布

让光照衰减更接近真实世界。原版 Skyrim 只有一套**粗糙的衰减函数**，会让灯看起来像**聚光灯**——中心极亮、边缘生硬；换成平方反比后光会自然得多。

> ⚠️ **这项功能自己什么都不做**，它不修改任何现有光照。你必须额外安装**为平方反比光照设计**的照明 MOD，才能吃到效果。

## 特性

- 新的平方反比衰减函数，**每个光源**可单独设 intensity / size / cutoff。
- **自动计算光半径**：半径不是直接指定的，而是由「强度」与「截断值」实时算出来的；强度会**平滑衰减到截断值**。
- 与半径相同的普通衰减灯相比，**性能差异几乎为零**。
- 内置**游戏内灯光编辑器**，MOD 作者可实时预览改灯效果。

## 用法

### 玩家

装一个用到该特性的**受支持照明 MOD** 即可（特性本身已随核心安装）。

### 照明 MOD 作者

直接把衰减写成 `1/d²` 是不现实的——光源处会无限亮，而且照射距离无限远。本算法用两个手段解决：

- **给光源一个「尺寸」**：尺寸让距离为 0 处的亮度有限，且光源附近的亮度分布随尺寸变化；
- **用「截断值（cutoff）」**：设定一个光强阈值，低于它光就归零。**光的半径由强度（fade）与截断值实时算出**，不是直接设定。

参数默认值：cutoff 未指定或填 1.0 时，**普通灯默认 0.05、阴影灯默认 0.022**。

> ⚠️ cutoff 越低越真实，但**光半径会更大**，可能得反过来调小光的半径来**控制光溢出（light bleed）**。
>
> 官方给了一个 [Desmos 图表](https://www.desmos.com/calculator/qrol6ltk9g)帮助理解三者关系：红线是原版衰减（F 控制 fade、r 控制半径），绿线是平方反比（I 控制强度、s 控制尺寸、c 控制截断）。

有两种方式把灯设为平方反比：

1. **xEdit**：打开一个 `LIGH` 记录 → 双击 **Flags (sorted)** → 勾上 **Unknown: 14**。这个原本未使用的 flag 被**挪用**来表示「使用平方反比衰减」。
   - **Fade** 控制强度；
   - **FOV** 参数控制尺寸；
   - **Falloff Exponent** 参数控制截断值。
   - 注：较新版本的 xEdit 很快会直接显示为 *Inverse Square Falloff* 而不是 Unknown 14。
2. **Light Placer**（3.1.1 起完整支持）：在灯光的 `"flags"` 字段里加上 **`InverseSquare`** 即可。此时 **fade** 控强度、**size** 控尺寸、**cutoff** 控截断。

### Light Editor 灯光编辑器

打开 CS 菜单 → Inverse Square Lighting 设置即可进入。可以**实时预览**改灯效果，包括开关平方反比、调光色与强度等。

> ⚠️ 官方警告两条：编辑器**不面向游戏玩法**，使用期间**不建议存档**（可能引发问题）；改动**不能直接保存**，只能把数值抄进 xEdit 或 Light Placer 的配置文件。

## 兼容性

- **与所有照明 MOD 兼容**，但只有**为平方反比设计**的照明 MOD 才会真正使用新的衰减。
- 兼容 [Light Placer](https://www.nexusmods.com/skyrimspecialedition/mods/127557) 与 [Light Placer VR](https://www.nexusmods.com/skyrimspecialedition/mods/135822)（已加入直接支持，作者可把灯标记为 `InverseSquare`）。

## 相关条目

- [Light Placer](../../05-tools/light-placer.md)
- [测试与调试手法](../../04-development/testing-and-debugging.md)（Light Editor 与 A/B 测试）
- 官方推荐的照明 MOD 见 [Vanilla 设置指南](../../01-installation/vanilla-setup.md)

## 贡献者

sicsix、Bottle、SkrubbySkrubInAShrub。

---
*本条目依据官方功能页精修整理；如与官方页面不一致，以官方为准。*
