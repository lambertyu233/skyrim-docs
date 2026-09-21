---
id: light-limit-fix
title: Light Limit Fix 光源上限修复
category: 02-features
kind: core
status: released
version: 1.1.0
updated: 2026-09-21
tags: [光照, 性能, 引擎修复, 粒子光, 调试]
aliases: [光源上限, light limit fix, 光太多闪烁, 4 光源限制]
source: https://modding.wiki/en/skyrim/developers/community-shaders/Features-Home/light-limit-fix
summary: 用聚簇着色（clustered shading，Starfield 同款）真正解除动态光源数量限制，并让 ENB 粒子光以真实光源形式接入；附带 LLFDEBUG 可视化。
---

# Light Limit Fix 光源上限修复

> 分类：核心特性（1.4+ 并入） · 状态：已发布

解除光源数量限制，并加入粒子光等功能。

> ⚠️ **阴影数量上限尚未解除。** 被解除的是**光源**数量。

## 特性

- 自研的 **clustered shading（聚簇着色）**，高性能、可扩展——**Starfield 也用的是这套**。
- **无限光源**：火把、魔法光等不再受限。
- 对「ENB light」粒子光提供**受限支持**。
- 为**草地**提供高性能光照。

### Clustered Shading 聚簇着色

这是让整个项目成立的魔法：无 bug、可扩展的灯光，从而实现**真正的光源上限修复**与**优化的粒子光**。官方配了一张用 ELFX Shadows 演示的可视化图——红方块标出原版「灯限已达」的位置，而这些灯现在**完全不再参与灯限计算**。

实现参考：`pezcode/Cluster`、`mateeeeeee/Adria-DX11` 工程，以及 *Practical Clustered Shading* 演示。

### Unlimited Dynamic Lights 无限动态光源

火把、投射物、法术危险区、室外灯光**全部无限制**。室内仍有大量灯未被修好，但它们**不再与动态放置的灯冲突**。

### Unlimited Magic Lights 无限魔法光

**魔法光上限从 4 提升到 2,147,483,647**。现在每个角色都能无限制地施放光。

### Particle Lights 粒子光（重要）

> ⚠️ **CS 1.4 到 1.7 之间不支持 ENB 粒子光；1.8 起为受限支持。**
>
> ⚠️ **粒子光只是为了向后兼容才保留的。官方推荐改用替代方案，例如 [Light Placer](https://www.nexusmods.com/skyrimspecialedition/mods/127557)。**

粒子光的做法是：利用逆向出的渲染器信息在 CPU 上重建光的颜色，从而生成**真实的、可被聚簇着色系统使用、也能被 NPC 感知**的光源。因此**大多数提供「ENB light」的 MOD 是兼容的**（如 ENB Light、ENB Lights For Effect Shaders、Rudy102 的 ENB Light 系列）。

相比 ENB 的粒子光，它的优点：

- 走聚簇着色而非延迟着色，**可扩展性好得多**；
- 有**真正的镜面光照**，金属与头发能被正确照亮；
- 支持**视差阴影**；
- **透明物体**（玻璃、Blended Roads）也能被粒子光照亮；
- **第一人称网格**可以发光；
- **不渲染粒子光网格**，彻底消除 overdraw，性能大幅提升；
- 没有 FOV 问题与畸变；
- 没有假阳性光源（例如白色闪烁的火把）；
- 半径无限制，光可以任意大。

### Light Limit Visualization（LLFDEBUG）

在 **Advanced → Shader Defines** 里加入 `LLFDEBUG` 后可开启三种可视化：

- 可视化灯限：达到**严格灯限**（portal-strict）时显示**红色**；
- 可视化严格灯数；
- 可视化聚簇灯数。

> 官方注明这是**开发者调试功能，不面向正常游戏**。

## 安装相关的常见事故

- **装了 Lux：重装时取消勾选 `optimized` / `split` 网格。** LLF 已取代这些网格（它们原本就是为了绕开引擎灯限），留着只会掉性能。
- **别勾选任何「支持粒子光照」的选项**——那些选项与 CS 不兼容。
- 装了 **ENB Light 类 MOD 不会发光**，改用 CS Light / Light Placer 的补丁。

## 相关条目

- [Light Placer](../../05-tools/light-placer.md) · [测试与调试手法](../../04-development/testing-and-debugging.md)
- [实战常见坑](../../06-community/common-pitfalls.md)

## 贡献者

doodlum（VR 之外全部功能的原始实现）、alandtse（VR 支持与重构）、Nukem（渲染器文档）、jonahex（光照与草着色器原始逆向）、powerofthree（粒子逆向与 CommonLibSSE）、rudy102 / fadingsignal / mindflux（粒子光资料）、mwilsnd、ProfJack、sicsix（ISL 支持）。

---
*本条目依据官方功能页精修整理；如与官方页面不一致，以官方为准。*
