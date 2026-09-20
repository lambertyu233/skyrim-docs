---
id: vanilla-setup
title: Vanilla 设置指南
category: 01-installation
version: 1.0.0
updated: 2026-09-20
tags: [画质, 设置, 照明, 推荐]
source: https://modding.wiki/en/skyrim/developers/community-shaders/vanilla-setup-guide
summary: 在已稳定安装 CS 的基础上，如何搭配照明、粒子补丁与 PBR 纹理让画面最佳。
---

# Vanilla 设置指南

本页面向**已稳定安装完整 CS 套件**的玩家，讲解如何充分发挥 CS 的画质潜力。

> 提供的 FOMOD 选项仅为**推荐**设置。请务必阅读所下载 MOD 的说明。

## 照明（Lighting）

照明 MOD 能让你充分利用 CS。当前最流行的两款室内方案是 **True Light** 与 **Lux CS**，外观都很好，按审美选择即可。

> 安装任何照明前，**先装 Light Placer 与 CS Light**。

- 照明 MOD 通常在室内/室外分别放置光源，作者常拆分为两个插件（ exterior / interior），便于混搭。
- **同一时间只使用一款室内 + 一款室外照明 MOD。**
- 任何使用 **ENB Light / ENB Particle Lights** 的 MOD 与 CS 不兼容——用了也不会发光，请改用 **CS Light** 或 **Light Placer** 的补丁。

## 其它视觉

- **CS Particle Patch**：修复大量原版网格光照，**强烈推荐**。与 ENB Particle Patch 兼容，但须让 CS 版覆盖后者。安装时注意其要求（并非全为硬需求）。
- **DIAL（Dynamic Interior Ambient Lighting）**：按昼夜调整室内亮度，强烈推荐。
- **Remove Fake FX**：去除原版光源周围的 2D 假辉光（True Light 的 FOMOD 提供 Base Object Swapper 配置）。

## PBR 纹理

- 推荐 **PGPatcher** 设置（注意 `Instance Location` 与 `Output` 路径因环境而异；MO2 实例路径可在 MO2 文件夹图标→“Open Instance folder”找到）。

## 预设（Presets）

目前设置预设仅适用于 CS 的**实验构建**，可在 Discord 获取。

> 更进阶的整体转换流程见 [ENB 迁移指南](enb-migration.md) 的“完整转换”部分。
