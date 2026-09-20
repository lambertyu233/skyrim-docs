---
id: directory-refresher
title: DirectoryRefresher：多线程重建虚拟目录树
category: 03-architecture
version: 1.0.0
updated: 2026-09-20
tags: [架构, DirectoryRefresher, 多线程, 重建]
source: https://deepwiki.com/ModOrganizer2/modorganizer
summary: DirectoryRefresher 是后台服务，mod 变动时在独立线程上重建虚拟文件树，保持 UI 响应。
kind: reference
---

# DirectoryRefresher：多线程重建虚拟目录树

`DirectoryRefresher` 是 MO2 的一个**后台服务**，负责在 mod 增删改时**重建虚拟文件树**。

## 为什么需要它

- mod 数量可能成百上千，逐个扫描目录、计算优先级、构建树是磁盘密集型操作。
- 放在 UI 线程会卡死界面，所以放到**独立的工作线程**上执行（MO2 整体是多线程架构，UI 与磁盘操作分离）。

## 它做什么

1. 扫描各 mod 文件夹与游戏 Data 目录。
2. 调用 VFS 节点类（`DirectoryEntry` / `FileEntry` / `FilesOrigin`）重建 `VirtualFileTree`。
3. 计算好每个文件的来源与优先级，供冲突检测与启动游戏时使用。
4. 完成后通知 UI 刷新（如左侧 mod 列表的冲突标记）。

> 这也是为什么改动 mod 后，MO2 有时会短暂"刷新中"——它在后台重建树。相关类见 [VFS 节点类](vfs-node-classes.md)。
