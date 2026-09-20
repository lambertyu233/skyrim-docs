---
id: vfs-node-classes
title: VFS 节点类：DirectoryEntry / FileEntry / FilesOrigin
category: 03-architecture
version: 1.0.0
updated: 2026-09-20
tags: [架构, 类, DirectoryEntry, FileEntry, FilesOrigin]
source: https://deepwiki.com/ModOrganizer2/modorganizer
summary: 虚拟目录树由 DirectoryEntry（目录）、FileEntry（文件，可多来源）、FilesOrigin（来源追踪）等类构成。
kind: reference
---

# VFS 节点类：DirectoryEntry / FileEntry / FilesOrigin

MO2 在内存里用一棵树表示虚拟文件系统的"合并视图"。DeepWiki 给出的核心类：

| 类 | 职责 | 源码路径 |
|----|------|----------|
| `DirectoryEntry` | 表示一个虚拟目录，内含文件与子目录 | `src/shared/directoryentry.h` |
| `FileEntry` | 表示单个文件，**可能同时存在于多个 mod 中** | `src/shared/fileentry.h` |
| `FilesOrigin` | 追踪某个文件究竟由哪些 mod 提供 | `src/shared/filesorigin.h` |
| `FileRegister` | 集中登记 VFS 中所有文件的注册表 | `src/shared/fileregister.h` |
| `VirtualFileTree` | 游戏 Data 目录的合并虚拟表示 | `src/core/virtualfiletree.h` |

## 这些类如何协作

1. 每个 mod 是一个"来源（origin）"，由 `FilesOrigin` 记录它贡献了哪些文件。
2. `FileEntry` 聚合同名文件的所有来源；最终"哪个来源胜出"由优先级决定（见 [FileEntry 优先级冲突](fileentry-priority.md)）。
3. `DirectoryEntry` 把文件和子目录组织成树，`VirtualFileTree` 是整棵树的入口。
4. `FileRegister` 让 MO2 能快速按名查找任意文件、列出冲突。

> 这棵树由 [DirectoryRefresher](directory-refresher.md) 在 mod 变动时重建，再由 [UsvfsConnector](usvfs-connector.md) 在启动游戏时翻译成 usvfs 能用的映射。
