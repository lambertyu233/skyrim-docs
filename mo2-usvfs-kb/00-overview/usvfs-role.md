---
id: usvfs-role
title: USVFS 在 MO2 中的角色
category: 00-overview
version: 1.0.0
updated: 2026-09-20
tags: [概览, USVFS, VFS, 架构]
source: https://github.com/ModOrganizer2/usvfs
summary: USVFS（用户态虚拟文件系统）是 MO2 的核心组件，用 API hooking 把"别处"的文件呈现给指定进程。
kind: concept
---

# USVFS 在 MO2 中的角色

**USVFS（User Space Virtual File System，用户态虚拟文件系统）** 是 MO2 的心脏。官方定义：

> USVFS 让 Windows 程序创建**只对一组选定进程可见**的文件/目录链接；它靠 **API hooking** 骗过文件访问函数，使它们"发现/打开"其实位于别处的文件。

## 它在 MO2 里做什么

1. **不改动游戏目录**：mod 实际在 `mods\` 各自的文件夹里，USVFS 在游戏/工具进程启动的那一刻，把合并后的视图"塞"进该进程的眼中。
2. **进程级可见**：链接只对 MO2 启动的游戏/工具进程可见；其它程序（包括资源管理器）看到的仍是真实目录。
3. **优先级叠加**：多个 mod 文件夹 + Overwrite + 游戏原文件，按优先级叠加成一份统一的虚拟 Data 目录。
4. **会话级生命周期**：MO2 关闭或进程结束，虚拟链接随之消失，不留下任何残留。

## 与 MO2 其它子系统的关系

- **DirectoryRefresher**：在 mod 变动时后台多线程重建虚拟目录树（见 [DirectoryRefresher](03-architecture/directory-refresher.md)）。
- **UsvfsConnector**：启动游戏时把"虚拟路径 → 真实路径"的映射表交给 usvfs（见 [UsvfsConnector](03-architecture/usvfs-connector.md)）。
- **VFS 节点类**：DirectoryEntry / FileEntry / FilesOrigin 等描述虚拟目录树（见 [VFS 节点类](03-architecture/vfs-node-classes.md)）。

> USVFS 自身仍是"进行中（alpha）"状态，但作为 MO2 核心组件接受了大量真实世界测试。当前许可为 GPLv3。
