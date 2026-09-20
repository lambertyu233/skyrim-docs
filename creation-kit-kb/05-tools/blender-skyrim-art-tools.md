---
id: blender-skyrim-art-tools
title: Blender 天际美术工具
category: 05-tools
version: 1.0.0
updated: 2026-09-20
tags: [blender, nif, art, mesh, export, modeling]
source: https://ck.uesp.net/wiki/Blender_Skyrim_Art_Tools
summary: Blender 天际美术工具是一套 Blender 插件，用于建模并导出 Skyrim 可用的 NIF 网格与碰撞。
status: stable
kind: tool
---

# Blender 天际美术工具

**Blender Skyrim Art Tools** 是一套面向《天际》的 **Blender 插件**，让美术人员能在 Blender 中建模并导出游戏可用的 **NIF** 网格（含碰撞、骨架、材质等）。

## 它能做什么

- 在 Blender 中创建/编辑静态与可装备网格。
- 配置碰撞（Collision）、骨骼（Skeleton）与顶点权重。
- 导出为 Skyrim 兼容的 `.nif` 格式，供 CK 的 Object Window 引用。
- 配合 [Archive.exe](02-features/archive-exe.md) 将模型与贴图打包为 `.bsa`。

## 与 CK 的衔接

1. 在 Blender 中完成模型与材质。
2. 用 Art Tools 导出 `.nif` 与贴图（`.dds`）。
3. 将文件放入 Data 目录对应路径（Meshes/、Textures/）。
4. 在 CK 的 Object Window 新建对应 Form（如 Static / Armor）并指向该 NIF。

## 提示

- NIF 是 Skyrim 专有模型格式，导出设置（骨骼名、碰撞类型）需与游戏约定一致。
- 复杂角色/动画建议参考官方与社区范例工程，避免骨骼不匹配。

## 相关条目

- [Archive.exe 打包](02-features/archive-exe.md)
- [术语表（NIF / DDS）](02-features/glossary.md)

> 来源：[UESP Blender Skyrim Art Tools](https://ck.uesp.net/wiki/Blender_Skyrim_Art_Tools)
