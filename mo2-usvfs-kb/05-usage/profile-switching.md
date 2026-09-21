---
id: profile-switching
title: Profile（档案）切换
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, profile, 档案, 切换]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 每个 profile 保存独立的 mod 勾选与加载顺序，可在多套配置间无缝切换。
kind: tutorial
---

# Profile（档案）切换

MO2 的 profile（档案）系统让你为同一游戏保存**多套不同的 mod 组合与加载顺序**，互不干扰。

## profile 包含什么

- 哪些 mod 被**启用/禁用**。
- mod 的**顺序（优先级）**。
- 插件（ESP/ESM/ESL）的**加载顺序**。
- 各自的 INI/存档关联等。

## 切换时发生了什么

- 切换 profile 只是改变 MO2 接下来要喂给 usvfs 的"视图定义"。
- 下一次启动游戏/工具时，[UsvfsConnector](../03-architecture/usvfs-connector.md) 按新 profile 重建映射——磁盘上的 mod 文件一个都没动。

## 实用提示

- 新建空白 profile 时可选 `DefaultGameSettings`，用于排查"是不是 mod 导致的故障"。
- 排错时：先在空 profile 跑通，再逐步加 mod，能快速定位是哪个 mod 惹的祸。

> 切换 profile 偶尔会让 MO2 崩溃？先排查安全软件与 [VFS 排错](../06-reference/troubleshooting-vfs.md) 中的"Windows Event Log 服务"。
