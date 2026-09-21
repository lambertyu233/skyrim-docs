---
id: conflict-resolution
title: 冲突解决与优先级
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 冲突, 优先级, 赢家]
aliases: [冲突解决, mod 冲突, 谁覆盖谁, conflict resolution, 冲突怎么排]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 同名文件冲突时，mod 列表中靠下者（优先级高）覆盖靠上者；BSA 亦参与排序。
kind: tutorial
---

# 冲突解决与优先级

当多个启用 mod（或 mod 与游戏原文件）提供**同一相对路径**的文件，就产生冲突。MO2 用"优先级"裁决谁被读取。

## 核心规则

- 在左侧 mod 列表中，**越靠下优先级越高**，会覆盖（盖住）上面的 mod。
- 对该路径，优先级最高的来源即"赢家"，被进程读取；其余来源被隐藏（但 MO2 会在 UI 标红提示冲突）。
- 这与底层 [FileEntry 多来源优先级冲突](../03-architecture/fileentry-priority.md) 是同一套规则——叠加 + 排序。

## BSA 与 loose file

- BSA 内容也被拉进虚拟目录（见 [BSA 的优先级解析](../03-architecture/bsa-priority-resolution.md)），参与同一套排序。
- 想用 loose file 盖过某个 BSA 内的资源：让该 loose file 所在 mod 优先级高于 BSA 所属 mod 即可。
- 反之高优先级 mod 的 BSA 会压过低优先级 mod 的 loose file——注意"存档失效（archive invalidation）"与 BSA 加载顺序的影响。

## 操作步骤

1. 在 mod 列表里上下拖动调整顺序（或右键设置优先级）。
2. 用 MO2 的冲突筛选/高亮确认谁覆盖谁。
3. 必要时把想"永久胜出"的文件放进高优先级 mod，或利用 [Overwrite 目录](overwrite-dir.md)。

> 想看 usvfs 实际把请求重定向到了哪个文件？开 [调试 usvfs](../04-debugging/debugging-usvfs.md) 日志。
