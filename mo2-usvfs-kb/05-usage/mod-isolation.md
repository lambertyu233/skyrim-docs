---
id: mod-isolation
title: mod 隔离与游戏目录干净
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 隔离, 游戏目录]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 每个 mod 独立存放，游戏目录保持原样；启用/禁用不会互相破坏。
kind: concept
---

# mod 隔离与游戏目录干净

MO2 的官方特性之一就是 **mod isolation（游戏目录保持干净）**。

## 它为什成立

- 每个 mod 是 `mods\` 下的独立文件夹，互不叠加在磁盘上。
- 真正的"合并视图"只存在于被 usvfs 注入的进程的**内存**里（见 [进程级可见的虚拟链接](01-mechanism/process-local-links.md)）。
- 因此没有哪个 mod 会"踩"到另一个 mod 的文件，游戏原文件也不会被覆盖。

## 带来的能力

- 随便启用/禁用/重排序 mod，磁盘零改动。
- 出错时只需调整 MO2 里的勾选与顺序，不必去游戏目录里翻找、删除残留。
- 与 Steam/平台"验证游戏文件完整性"完全兼容（游戏目录没被动过）。

> 工具（如 BodySlide、xEdit）写出的新文件不会进游戏目录，而是进 [Overwrite 目录](overwrite-dir.md)。
