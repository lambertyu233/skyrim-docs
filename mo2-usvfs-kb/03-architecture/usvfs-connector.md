---
id: usvfs-connector
title: UsvfsConnector：启动游戏时交付映射表
category: 03-architecture
version: 1.0.0
updated: 2026-09-20
tags: [架构, UsvfsConnector, 映射, 启动]
source: https://deepwiki.com/ModOrganizer2/modorganizer
summary: 游戏启动时，UsvfsConnector 把"虚拟路径→真实路径"的映射表交给 usvfs 完成注入。
kind: reference
---

# UsvfsConnector：启动游戏时交付映射表

当你通过 MO2 点击"运行"时，**`UsvfsConnector`** 负责把 MO2 算好的虚拟视图"交给" usvfs。

## 它做什么

- 把构建好的虚拟目录树翻译成一份 **映射表**：每条记录是一个"进程会请求的路径"→"真实磁盘上该文件的位置"。
- 例如：`Data\Textures\rock.dds` → `C:\MO2\mods\ModA\Textures\rock.dds`。
- 在启动游戏进程的同时，把这份映射交给 usvfs，usvfs 据此注入进程并开始重定向。

## 为什么这一步关键

- 此前所有工作（[DirectoryRefresher 建树](directory-refresher.md)、[FileEntry 定优先级](fileentry-priority.md)、[BSA 拉入](bsa-priority-resolution.md)）都是为了产出这份映射。
- 映射一旦交付，进程对自己打开的是"别处"的文件**毫无察觉**。

> 注入与重定向的实际行为，可用 [调试 usvfs](04-debugging/debugging-usvfs.md) 的日志亲眼看到。
