---
id: api-hooking
title: 核心机制：API Hooking
category: 01-mechanism
version: 1.0.0
updated: 2026-09-20
tags: [机制, hooking, 重定向, Win32]
aliases: [API Hook, hook 机制, api hooking, HOOK 原理]
source: https://github.com/ModOrganizer2/usvfs
summary: USVFS 通过 hook 文件访问类 Win32 API，拦截进程发起的路径请求并重写为真实路径。
kind: concept
---

# 核心机制：API Hooking

USVFS 的本质是 **API hooking（应用程序接口挂钩）**：在目标进程里"替换/拦截"它用来访问文件系统的 Win32 函数，从而把一次"打开 A"的请求，悄悄改到"打开 B"。

## 它是怎么骗过文件访问函数的

1. 当 MO2 启动游戏（或工具）时，usvfs 被注入该进程。
2. 进程调用 `CreateFileW`、`GetFileAttributesW`、`FindFirstFileW` 等文件 API 时，会先经过 usvfs 的 **hook**（所有 hook 函数统一命名为 `hook_<原函数名>`，见 [调试 usvfs](../04-debugging/debugging-usvfs.md)）。
3. hook 检查请求的路径是否落在被管理的虚拟目录里：
   - 命中 → 把路径**重定向**到该文件真实所在的 mod 文件夹，再调用底层原生函数。
   - 未命中 → 原样放行。
4. 进程完全不知道自己打开的是 `mods\ModA\...` 而不是 `Data\...`，对它而言一切正常。

## 为什么叫"用户态"

重定向发生在**进程自己的地址空间内**，不依赖任何文件系统/内核特性。这正是它能做到"只对指定进程可见""跨文件系统""无需管理员"的根本原因。

> 直观感受：打开 usvfs 调试日志，你会看到每一行都打印进程请求的**原始路径**和被 usvfs **重定向后的真实路径**——这是理解"重定向"最直观的材料。
