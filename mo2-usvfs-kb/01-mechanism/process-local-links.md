---
id: process-local-links
title: 进程级可见的虚拟链接
category: 01-mechanism
version: 1.0.0
updated: 2026-09-20
tags: [机制, 进程可见, 隔离]
source: https://github.com/ModOrganizer2/usvfs
summary: USVFS 创建的链接只对调用者选定的进程可见，其它程序（含资源管理器）看到的是真实目录。
kind: concept
---

# 进程级可见的虚拟链接

与 NTFS 符号链接"对全系统所有程序可见"不同，USVFS 的链接**只对一组被选中的进程可见**。

## 这意味着什么

- 只有**通过 MO2 启动**的游戏/Tool（如 xEdit、LOOT、BodySlide）才会"看到"虚拟合并后的 Data 目录。
- 直接双击游戏 exe、或用资源管理器打开游戏目录，看到的仍是**未经修改的真实目录**——mod 文件物理上并不在那里。
- 因此多个程序可以各自拥有不同的"视图"，互不干扰。

## 对比 NTFS 符号链接

| 维度 | USVFS | NTFS 符号链接/连接点 |
|------|-------|----------------------|
| 可见范围 | 仅选定进程 | 所有进程（全局） |
| 是否改动真实目录 | 否 | 是（创建了真实链接对象） |

> 这是 mod 隔离与"游戏目录保持干净"能够成立的基础，详见 [mod 隔离](../05-usage/mod-isolation.md)。
