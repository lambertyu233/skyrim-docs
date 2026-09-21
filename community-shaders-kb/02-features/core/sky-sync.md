---
id: sky-sync
title: Sky Sync 天空同步
category: 02-features
kind: core
status: released
version: 1.1.0
updated: 2026-09-21
tags: [天空, 天体, 太阳, 月亮, DynDOLOD]
source: https://modding.wiki/en/skyrim/developers/community-shaders/Features-Home/sky-sync
summary: 把光照、阴影与体积光同步到太阳与月亮的真实位置，并提供更真实的南天弧线日照路径；需生成地形底面网格。
---

# Sky Sync 天空同步

> 分类：核心特性（1.7.0+ 并入） · 状态：已发布

## 它修的是什么

原版 Skyrim 的天空有几处根本性错位：

- **太阳已经越过地平线很久，才慢慢淡入视野**；
- 来自太阳的**光照、阴影、体积光并不发自太阳的真实位置**，导致画面不匹配；
- **月光的行为最糟**：它根本不是从月亮发出的，而是来自天上一颗**隐形物体**，且该物体在夜间**朝太阳的反方向**移动。

Sky Sync 通过把太阳与月亮的光照和体积光**同步到它们在天空中的真实位置**来解决这些。

## 特性

- **光照、阴影、体积光与日月同步**。
- **可选的更真实日照路径**：太阳沿**南天弧线**横穿，室内外光照都更戏剧化，同时**保持原版的白昼长度**——「Skyrim 不再位于赤道上」。
- **太阳在穿越地平线时可见**，且位置会**依玩家海拔修正**，确保无论玩家在哪，日出日落时间一致。
- 白天太阳是主光源；**夜间可单独指定哪个月亮作为光源**，也可设为在 **Masser 与 Secunda** 之间**依亮度平滑切换**。
- 依「是否在地平线之上」与**月相**自动调整光照与体积光强度。
- **室内天空会自动旋转以对齐正北方**，为后续的 *Interior Sun Shadows* 铺路——室内日月位置现在能与室外正确对应。
- 与 CS 的体积光改进和优化搭配良好。
- **内建对 [Moon and Stars](https://www.nexusmods.com/skyrimspecialedition/mods/73336) 的支持**（可选）。

## 用法：必须生成地形底面（Terrain Underside）

> ⚠️ **Sky Sync 需要你的负载顺序里已生成并启用「地形底面网格（Terrain Underside Mesh）」**，否则日出日落前后光与体积光会**从地形下方漏出来**。

- 用 **DynDOLOD** 生成 LOD 时**勾选 `Terrain underside`** 即可。只为了生成底面网格而单跑一次 DynDOLOD 也是可以的。
- 参见 [DynDOLOD Terrain Underside 说明](https://dyndolod.info/Help/Terrain-Underside)。

默认使用**新的日照路径**；想用原版路径，去 Sky Sync 设置菜单里取消勾选。同一个菜单里也能设月光源的行为。

## 兼容性

- **与实现同类效果的其他 MOD 不兼容，例如 EVLaS。** Sky Sync 检测到它们会**自动禁用自己**以防出问题。
  - 因此官方 Vanilla 设置指南直接写明：**不要用 EVLaS，Sky Sync 已完全取代它。**
- 与**所有光照与天气 MOD 兼容**。
- 与 [Moon and Stars](https://www.nexusmods.com/skyrimspecialedition/mods/73336) 兼容（可选）。

## 相关条目

- [地形阴影](terrain-shadows.md)（同样受益于地形底面网格）
- [不兼容 MOD 清单](../../03-reference/incompatible-mods.md)（EVLaS / AELaS）
- [官方功能对照矩阵](../../00-overview/feature-matrix.md)

## 贡献者

sicsix、doodlum、SkrubbySkrubInAShrub。

---
*本条目依据官方功能页精修整理；如与官方页面不一致，以官方为准。*
