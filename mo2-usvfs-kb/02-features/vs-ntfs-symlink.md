---
id: vs-ntfs-symlink
title: USVFS vs NTFS 符号链接
category: 02-features
version: 1.0.0
updated: 2026-09-20
tags: [特性, 对比, NTFS, 符号链接]
aliases: [NTFS symlink, USVFS 和软链接, symlink 区别]
source: https://github.com/ModOrganizer2/usvfs
summary: 逐项对比 USVFS 与 NTFS 符号链接在可见性、权限、生命周期、文件系统、overlay、虚拟删除上的差异。
kind: reference
---

# USVFS vs NTFS 符号链接

下面基于 USVFS 的"最终目标"整理（来自官方 README 的 Comparison to symbolic links）。与 NTFS 符号链接相比：

| 特性 | USVFS | NTFS 符号链接 / 连接点 |
|------|-------|------------------------|
| 可见范围 | 只对调用者选定的进程可见 | 对所有应用程序可见 |
| 生命周期 | 会话结束时消失 | 持久存在于文件系统 |
| 目标写权限 | 不需要 | 需要 |
| 管理员权限 | 安装与使用都不需要 | 创建某些链接需要 |
| 文件系统依赖 | 跨文件系统（FAT32/只读/网络盘均可） | 限 NTFS |
| 多目录叠加 | 支持（overlay 到同一目标） | 不支持 |
| 虚拟删除/替换 | 支持（让文件不可见或被替换） | 不支持 |

## 一句话总结

NTFS 符号链接是**文件系统级的、全局的、持久的、需要权限的**；USVFS 是**进程级的、会话级的、免权限的、与文件系统无关的、可叠加可隐藏的**。

> USVFS 不是要"取代"符号链接，而是用一套更适合 mod 管理的范式，规避了符号链接在权限、可见性、清理上的麻烦。其代价见 [USVFS 的代价与风险](usvfs-drawbacks.md)。
