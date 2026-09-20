---
id: fileentry-priority
title: FileEntry 多来源优先级冲突
category: 03-architecture
version: 1.0.0
updated: 2026-09-20
tags: [架构, FileEntry, 优先级, 冲突]
source: https://deepwiki.com/ModOrganizer2/modorganizer
summary: 同名文件可来自多个 mod；FileEntry 按优先级排序，排在最前的"赢家"被进程读取。
kind: reference
---

# FileEntry 多来源优先级冲突

当**同一个相对路径**（例如 `Textures\rock.dds`）同时存在于多个来源时，就发生了冲突。`FileEntry` 的处理方式：

## 规则：按优先级排序，第一名获胜

- `FileEntry` 持有该文件的**所有来源**（来自不同 mod、Overwrite、游戏原文件），每个来源带一个优先级。
- 这些来源按优先级排序，**排在第一位的即为"赢家"**，被进程实际读取。
- 其它来源对该路径"隐藏"，但 MO2 仍会在 UI 中标出它们（冲突提示）。

## 优先级由什么决定

- **mod 在列表中的顺序**（越靠下优先级越高，覆盖上面的）。
- **profile** 的启用状态与顺序。
- **BSA 归档**也有自己的优先级，且可与 loose file 混合参与排序（见 [BSA 的优先级解析](bsa-priority-resolution.md)）。
- **Overwrite** 目录通常优先级最高，直接"盖"住一切。

> 这套规则在实际使用层面就是 [冲突解决与优先级](05-usage/conflict-resolution.md)。正是叠加 + 优先级（[多目录叠加](01-mechanism/overlay-links.md)）让 MO2 既能合并又能解决冲突。
