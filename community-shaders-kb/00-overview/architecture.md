---
id: architecture
title: 架构与缓存系统
category: 00-overview
version: 1.0.0
updated: 2026-09-20
tags: [架构, 缓存, 性能, 引擎]
aliases: [CS 架构, 着色器缓存, shader cache, CS 怎么工作, 缓存系统]
source: https://modding.wiki/en/skyrim/developers/community-shaders#cache-system
summary: CS 通过运行时着色器缓存与磁盘缓存替换原版着色器；理解其机制有助于排错与开发。
---

# 架构与缓存系统

Community Shaders 在运行时替换 Skyrim 的原版着色器管线，并以**缓存系统**管理编译产物。理解这套机制对排错（尤其是“编译着色器”卡住、黑屏、特效异常）至关重要。

## 整体架构（要点）

- **基础安装（Core）** 携带一组核心特性（见 [功能总览](../02-features/core)）。
- **附加特性（Addons）** 单独下载，按需启用。
- **渲染替换**：CS 接管材质/光照/后处理相关着色器，支持 PBR、屏幕空间特效、体积光等。
- **游戏内菜单**：按 END 打开，可实时调整设置、场景管理、性能浮层、RenderDoc 捕获等。

## Shader Cache（着色器缓存）

**Shader Cache** 是已编译着色器的运行时集合，用于替换 Skyrim 的原版着色器。

- 清空调色器缓存会强制下次游戏遇到对应着色器时重新编译。
- 主要用于**着色器开发**与热加载，**正常游戏无需清理**。

## Disk Cache（磁盘缓存）

**Disk Cache** 将已编译着色器存储到磁盘，由 Shader Cache 自动填充。

- 若磁盘缓存缺失、过期或无效，屏幕左上角会出现 **“Compiling Shaders”（正在编译着色器）**。
- 此时游戏**不会冻结**，但在编译完成前交互被禁用。
- 完成后，后续启动应当即时，无额外延迟。

**位置**：`Data/ShaderCache`

**清理方式**：
- 删除该文件夹；或
- 在 UI 右上角点击 “Clear Shaders” 按钮。

> ⚠️ 只删除 `ShaderCache` 文件夹，**不要**删除 `Shaders` 文件夹。另建议同时删除 `UnifiedWaterCache` 文件夹。

## 排错关联

- 更新 CS 后若没出现“编译着色器”弹窗 → 手动删除 Disk Cache（MO2: `Overwrite/ShaderCache`；Vortex: `<游戏>/Data/ShaderCache`）。详见 [FAQ](../03-reference/faq.md) 与 [安装-更新](../01-installation/installation-guide.md)。
- “Shaders failed to compile” 红错 → 多为 CS 与附加特性版本混用，或缓存未重生。
