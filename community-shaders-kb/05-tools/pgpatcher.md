---
id: pgpatcher
title: PGPatcher（Parallax / PBR 修补器）
category: 05-tools
version: 1.0.0
updated: 2026-09-20
tags: [工具, PBR, 视差, 网格修补, 纹理]
aliases: [Parallax 修补, PBR 修补, PGPatcher 怎么用, 视差贴图修补, pgpatcher 报错]
source: https://modding.wiki/en/skyrim/developers/community-shaders/pgpatcher-home
summary: 独立工具，修补纹理 MOD 的加载顺序（视差 / 复杂材质 / PBR），是 True PBR 工作流核心。
---

# PGPatcher（Parallax / PBR 修补器）

**PGPatcher** 是一个独立工具，用于修补纹理 MOD 的加载顺序，覆盖 **视差（parallax）/ 复杂材质（CM）/ PBR** 三类需求。它是 True PBR 工作流的核心组件。

## 在 True PBR 中的角色

True PBR 依赖被标记 PBR 的网格。PGPatcher 让 MOD 作者不必随包发布“已标记网格”，而是发布 **JSON**，在用户侧告诉工具：
- 替换哪些纹理路径；
- 对网格应用哪些 PBR 值。

这对重纹理原版模型或盔甲尤其推荐——可让用户把你的 PBR 纹理套用到其 bodyslide 输出。

## 关键组成

- **PGtools**：PGPatcher 的 MOD 作者工具，便于测试时快速批量改动（详见 PGPatcher GitHub wiki）。
- 运行 PGPatcher 需要配置 `Instance Location`（MO2 实例路径）与 `Output` 路径——各环境不同（MO2 实例路径可在 MO2 文件夹图标→“Open Instance folder” 找到）。

## 相关

- 美术师完整流程见 [True PBR 美术师指南](../04-development/pbr-for-artists.md)。
- Auto Parallax 与 True PBR（experimental）不兼容，应改用 PGPatcher（见 [不兼容 MOD](../03-reference/incompatible-mods.md)）。

> 具体下载、JSON 字段与运行步骤请以官方 PGPatcher 页面与 GitHub wiki 为准。
