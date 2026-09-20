---
id: saves-management
title: 存档查看与 Fix Mods
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 存档, Saves, Fix Mods]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: Saves 标签页显示存档及其缺失插件；右键 Fix Mods… 可把该存档所需的 mod 一键恢复回原配置。
kind: tutorial
---

# 存档查看与 Fix Mods

## Saves 标签页

- 位置：右窗格 **Saves** 标签页，显示你的存档。
- **悬停**某个存档会弹出信息，其中包括**该存档用到、但当前 profile 缺失的 ESP**。
  - 提示：界面里 `Missing ESPs` 这一行**只是表头**，并不是在断言该存档有问题。
- **右键**存档 → `Fix Mods…`：列出缺失的 ESP，以及**可能包含这些插件**的 mod（如果有的话）。
  - 这是把某个存档对应的整套 mod **恢复回原始配置**的快捷途径——想接着老存档继续玩时非常有用。

## 与 profile 的关系

- 存档是跟 profile 走的（若你在创建 profile 时选择了保存游戏）。因此，切换/备份 profile 也就意味着切换/备份了对应的存档集合。
- 重装或迁移整个 MO 安装前，别忘了 `profiles` 目录（见[备份与恢复](backup-and-restore.md)）。

> 相关：[Profile 切换](profile-switching.md)、[启用 mod 与激活插件](enable-and-activate.md)（缺失插件也常表现为"插件带警告图标 = 缺 master"）。
