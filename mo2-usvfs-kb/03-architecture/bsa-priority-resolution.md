---
id: bsa-priority-resolution
title: BSA 归档的优先级解析
category: 03-architecture
version: 1.0.0
updated: 2026-09-20
tags: [架构, BSA, 优先级, 归档]
aliases: [BSA 优先级, bsa 加载顺序, bsa priority, 归档优先级]
source: https://deepwiki.com/ModOrganizer2/modorganizer
summary: BSA 归档内容会被拉进虚拟目录，与 loose file 一起参与优先级判定，决定冲突谁胜。
kind: reference
---

# BSA 归档的优先级解析

BSA（Bethesda Archive）是 Bethesda 游戏把资源打包成的归档文件。USVFS 不会忽略它们——**BSA 的内容也会被拉进虚拟目录，参与优先级判定**。

## 机制要点

- MO2 解析每个启用 mod 的 BSA，把其中的文件路径"展开"进虚拟目录树，作为该 mod 的贡献来源。
- 这样，BSA 里的 `Textures\rock.dds` 和某个 loose file 的 `Textures\rock.dds` 就是**同一路径的两个来源**，照常按优先级排序。
- BSA 本身也有优先级顺序（通常与其所属 mod 的优先级一致，并受"存档失效/archive invalidation"与 BSA 加载顺序影响）。

## 实际影响

- 想用 loose file 覆盖某 BSA 内的资源？只要让该 loose file 所在 mod 优先级更高即可。
- 反之，高优先级 mod 的 BSA 会盖过低优先级 mod 的 loose file——这正是 STEP 指南里"BSA Priorities"要讲清楚的坑。

> 使用层面的冲突处理见 [冲突解决与优先级](../05-usage/conflict-resolution.md)；mod 隔离与游戏目录干净见 [mod 隔离](../05-usage/mod-isolation.md)。
