---
id: overlay-links
title: 多目录叠加（Overlay）
category: 01-mechanism
version: 1.0.0
updated: 2026-09-20
tags: [机制, overlay, 叠加, 优先级]
source: https://github.com/ModOrganizer2/usvfs
summary: USVFS 可把多个目录叠加到同一个目标上，按优先级决定哪个"赢"，这正是 mod 合并的原理。
kind: concept
---

# 多目录叠加（Overlay）

USVFS 能把**多个目录叠加（overlay）到同一个目标目录上**——这正是 MO2"把几十个 mod 合并成一份 Data"的实现基础。

## 叠加如何工作

- 游戏真实 `Data\`、各个 mod 的 `mods\ModA\...`、`mods\ModB\...`、以及 `overwrite\`，都被"铺"在同一棵虚拟目录树上。
- 当进程请求 `Data\Textures\rock.dds` 时，usvfs 在所有叠加层中查找该文件，按**优先级**返回最上面那一份。
- 排在最前（优先级最高）的来源即为"赢家"，被进程读取；其它来源对该路径"隐藏"。

## 这与冲突解决是同一件事

叠加 + 优先级 = MO2 的**冲突解决**规则。优先级由 mod 列表顺序、profile、BSA 等因素决定（见 [冲突解决与优先级](../05-usage/conflict-resolution.md) 与 [FileEntry 优先级冲突](../03-architecture/fileentry-priority.md)）。

> 启动游戏时，这份"虚拟路径→真实来源"的映射由 [UsvfsConnector](../03-architecture/usvfs-connector.md) 交给 usvfs。
