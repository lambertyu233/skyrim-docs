---
id: what-is-cs
title: 什么是 Community Shaders
category: 00-overview
version: 1.1.0
updated: 2026-09-21
tags: [概览, 入门, 框架, ENB]
aliases: [CS 是什么, Community Shaders 是什么, community shaders, 画质模组]
source: https://modding.wiki/en/skyrim/developers/community-shaders
summary: Community Shaders 是开源、模块化的 Skyrim 图形增强框架，提供先进光照、材质与视觉特效。
---

# 什么是 Community Shaders

**Community Shaders（CS）** 是一个开源、综合性的 Skyrim 图形增强框架，提供先进的光照、材质与视觉特效。其设计是**模块化**的——你可以只启用想要的功能，同时保持良好性能。

官方对自身定位的一句话是：**它不是「游戏之上的一层后处理」，而是直接在引擎层修好并扩建 Skyrim 自己的着色器**。Nexus 发布页的表述是「不像 ENB 那样替换整条后处理管线，而是用 bug 修复、现代渲染技法和可选插件增强 Skyrim 现有的着色器」。

## 核心定位

- **开源**：代码完全开放，遵循 GPL-3.0 许可（官方明确承诺「永不闭源」）。
- **模块化**：核心功能随基础安装附带，附加功能可单独下载启用。
- **用户驱动**：由社区维护文档、测试与开发（GitHub + Discord）。
- **兼容性取向**：设计上替代 ENBSeries 的大部分功能，避免与之同时运行。
- **体量**：Nexus 上标注「Mods using this mod」的 MOD 有 **564** 个，是当前 Skyrim 画质生态的实际基座。

## 快速上手

- 游戏内按 **END** 打开 Community Shaders 菜单。
- 新手从 [安装指南](../01-installation/installation-guide.md) 开始（从没 mod 过的话，官方推荐先读 *A Dragonborn's Fate*）。
- 想提升画质看 [Vanilla 设置指南](../01-installation/vanilla-setup.md)。
- 从 ENB 迁移看 [ENB 迁移指南](../01-installation/enb-migration.md)。
- 看**哪个功能 CS 有、ENB 有没有**：见 [官方功能对照矩阵](feature-matrix.md)。
- 看**版本现状与支持边界**：见 [版本与支持策略](version-and-support.md)。

## 与其他方案的对比（要点）

| 维度 | Community Shaders | ENBSeries |
|------|-------------------|-----------|
| 授权 | 开源 (GPL-3.0) | 闭源 |
| 架构 | 模块化插件，**集成于引擎**（SKSE + CommonLibSSE-NG） | 注入式后处理包装层 |
| 菜单 | 游戏内 ImGui 菜单（END），可**逐天气**调参 | `enbseries.ini` 配置 |
| 兼容 | 与 ENB **互斥**（检测即自行禁用） | — |
| 性能 | 常被称为「可能比原版还快」；统一着色器缓存 + 多线程编译，**只需编译一次** | 视预设而定，差异极大 |
| 预设 | [Effects 11](https://mod.pub/skyrim-se/415-effects-11) 支持**未加密** ENB 预设；后续由 Post Processing 接棒（TBA） | 原生 |
| VR | **主版本已停止支持**（转 [Open Shaders](https://www.nexusmods.com/skyrimspecialedition/mods/180419)） | 有 VR 版本 |
| 强项领域 | 引擎级修复、PBR、地形/草/水、阴影体系、性能 | 后处理（DoF、Bloom、色彩分级）、镜头特效 |

> 两边真正的能力差异，一张表看完：[官方功能对照矩阵](feature-matrix.md)。

## 维护提示

本资料库以分层结构组织（概览 / 安装 / 功能 / 参考 / 开发 / 工具 / 社区），每个条目独立成文件并带 `frontmatter` 元数据，便于增删改查与版本化协作。新增内容后运行 `scripts/build_index.py` 刷新索引。
