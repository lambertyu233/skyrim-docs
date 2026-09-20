---
id: what-is-cs
title: 什么是 Community Shaders
category: 00-overview
version: 1.0.0
updated: 2026-09-20
tags: [概览, 入门, 框架]
source: https://modding.wiki/en/skyrim/developers/community-shaders
summary: Community Shaders 是开源、模块化的 Skyrim 图形增强框架，提供先进光照、材质与视觉特效。
---

# 什么是 Community Shaders

**Community Shaders（CS）** 是一个开源、综合性的 Skyrim 图形增强框架，提供先进的光照、材质与视觉特效。其设计是**模块化**的——你可以只启用想要的功能，同时保持良好性能。

## 核心定位

- **开源**：代码完全开放，遵循 GPL-3.0 许可。
- **模块化**：核心功能随基础安装附带，附加功能可单独下载启用。
- **用户驱动**：由社区维护文档、测试与开发（GitHub + Discord）。
- **兼容性取向**：设计上替代 ENBSeries 的大部分功能，避免与之同时运行。

## 快速上手

- 游戏内按 **END** 打开 Community Shaders 菜单。
- 新手从 [安装指南](01-installation/installation-guide.md) 开始。
- 想提升画质看 [Vanilla 设置指南](01-installation/vanilla-setup.md)。
- 从 ENB 迁移看 [ENB 迁移指南](01-installation/enb-migration.md)。

## 与其他方案的对比（要点）

| 维度 | Community Shaders | ENBSeries |
|------|-------------------|-----------|
| 授权 | 开源 (GPL-3.0) | 闭源 |
| 架构 | 模块化插件，集成于引擎 | 注入式后处理 |
| 菜单 | 游戏内 END 菜单 | enbseries.ini 配置 |
| 兼容 | 与 ENB 互斥（检测即禁用） | — |
| 预设 | Effects 11 / 后续 Post Processing 支持未加密 ENB 预设 | 原生 |

## 维护提示

本资料库以分层结构组织（概览 / 安装 / 功能 / 参考 / 开发 / 工具），每个条目独立成文件并带 `frontmatter` 元数据，便于增删改查与版本化协作。新增内容后运行 `scripts/build_index.py` 刷新索引。
