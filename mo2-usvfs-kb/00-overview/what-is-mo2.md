---
id: what-is-mo2
title: 什么是 Mod Organizer 2
category: 00-overview
version: 1.0.0
updated: 2026-09-20
tags: [概览, 入门, MO2, 虚拟文件系统]
aliases: [MO2 是什么, Mod Organizer 2, 模组管理器]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: MO2 是开源 mod 管理工具，靠虚拟文件系统（VFS）在运行时合并 mod，保持游戏真实目录干净。
kind: concept
---

# 什么是 Mod Organizer 2

**Mod Organizer 2（MO2）** 是一个开源的 PC 游戏 mod 管理工具，目标是让 mod 的安装与管理对初学者与老手都一样简单、干净。它最关键的革命性设计是：**mod 不写入游戏目录，而是在运行时通过一个"虚拟文件系统（VFS）"合并呈现给游戏进程**。

## 关键定位

- **开源**：代码开放，社区持续维护（Tannin 开创，后由社区接手为 MO2）。
- **虚拟部署**：mod 各自独立存放，运行时统一"叠加"成游戏看到的 Data 目录；关闭 MO2 后游戏目录原样如初。
- **mod 隔离**：游戏目录始终保持干净，启用/禁用 mod 不会互相破坏。
- **Profile（档案）**：可为同一游戏保存多套不同的 mod 组合与加载顺序，无缝切换。
- **冲突解决**：多个 mod 提供同名文件时，按优先级决定"谁胜出"。
- 另外还提供 **BSA 解包（Bethesda 游戏）、Nexus 集成、BAIN/FOMOD 安装器、存档查看器、归档失效（archive invalidation）、可定制分类** 等。

## 为什么需要 VFS

传统方案（如直接覆盖游戏文件，或是 NTFS 符号链接/连接点）要么污染游戏目录、要么需要管理员权限、要么全局可见。MO2 的 VFS（由 **USVFS** 实现）解决了这些痛点——它才是 MO2 的"心脏"。

> 想理解 VFS 本身的工作原理，见 [USVFS 在 MO2 中的角色](usvfs-role.md) 与 [核心机制：API Hooking](../01-mechanism/api-hooking.md)。
