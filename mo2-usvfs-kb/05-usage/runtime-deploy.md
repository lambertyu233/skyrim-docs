---
id: runtime-deploy
title: 运行时部署 mod（不写入游戏目录）
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 部署, 运行时, VFS]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: MO2 在游戏进程启动的瞬间用 VFS 合并 mod，磁盘上的游戏目录始终未被修改。
kind: tutorial
---

# 运行时部署 mod（不写入游戏目录）

MO2 的核心体验是：**mod 从不写进游戏目录**。所有合并都发生在"运行时"。

## 流程

1. 你把 mod 装进 MO2 的 `mods\` 目录（各自独立文件夹）。
2. 你勾选要启用的 mod，调整顺序决定优先级。
3. 点"运行游戏"——此时 [UsvfsConnector](03-architecture/usvfs-connector.md) 把合并视图交给 usvfs，注入游戏进程。
4. 游戏进程"看到"的 `Data\` 是几十个 mod 叠加后的结果；**磁盘上的真实游戏目录一字未改**。
5. 关闭 MO2 / 退出游戏，虚拟链接消失，游戏目录恢复如初。

## 好处

- 游戏目录始终干净、可验证（Verify integrity 不会报"被改过"）。
- 启用/禁用 mod 只是改视图，不碰文件，不会破坏其它 mod 或游戏本身。
- 同一游戏可同时拥有多套互不相干的配置（profile）。

> 这与 [mod 隔离](mod-isolation.md) 是一体两面；冲突如何裁决见 [冲突解决与优先级](conflict-resolution.md)。
