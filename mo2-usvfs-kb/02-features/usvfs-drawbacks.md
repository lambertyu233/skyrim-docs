---
id: usvfs-drawbacks
title: USVFS 的代价与风险
category: 02-features
version: 1.0.0
updated: 2026-09-20
tags: [特性, 风险, 性能, 杀软, 调试]
source: https://github.com/ModOrganizer2/usvfs
summary: USVFS 带来内存/CPU 开销、初始化时机限制、新 bug 源，以及易触发杀软误报。
kind: reference
---

# USVFS 的代价与风险

USVFS 强大，但也有明确代价（来自官方 README）：

- **性能开销**：每个被 hook 的文件调用都会经过 usvfs，必然带来一定的内存与 CPU 开销（理想情况下很小，但并非零）。
- **初始化时机**：usvfs 仅在**每个进程初始化阶段**才激活。若某依赖 DLL 在 usvfs 就位前就被加载，它可能错过重定向。
- **新的 bug 源**：注入式 hook 会引入一类"难以诊断"的问题，可能让受影响进程出现诡异故障。
- **杀软误报**：所用技术与部分恶意软件相似，**容易被杀软/反恶意软件拦截或干扰**（且常常毫无提示）。需要把整个 MO2 安装目录加入排除项，必要时甚至要卸载某些顽固杀软。

> 实际排错与缓解见 [VFS/USVFS 常见排错](../06-reference/troubleshooting-vfs.md)，以及杀软清单与 HVCI 章节。
