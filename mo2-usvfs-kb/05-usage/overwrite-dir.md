---
id: overwrite-dir
title: Overwrite 目录与维护
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, Overwrite, 维护, 工具产出]
aliases: [Overwrite 目录, 覆盖目录, overwrite 是什么, overwrite 要不要清]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 工具写出的新文件落入 Overwrite；应定期把其中内容归档进正式 mod，保持 Overwrite 干净。
kind: tutorial
---

# Overwrite 目录与维护

`Overwrite` 是 MO2 里一个特殊的高优先级文件夹：**工具（而非游戏）通过 VFS 写出的新文件，会落到这里**。

## 文件怎么进 Overwrite 的

- BodySlide 生成的 `_cbbe.dds`、xEdit 清洗出的 `.esp`、LOOT 排序结果、FNIS 输出等，经 usvfs 写出时，默认写入 `overwrite\`。
- 因为 Overwrite 优先级最高，它"盖"住一切同名文件——这正是你期望的行为（工具产物立即生效）。

## 为什么要维护一个干净的 Overwrite

- 若不清理，Overwrite 会越积越乱，文件名冲突、难以追溯"这文件是哪来的"。
- 它应是一个**中转站**，而不是长期仓库。

## 维护流程

1. 定期打开 `Overwrite`，查看里面的文件。
2. 把属于某个具体 mod 的产出，**移动/归类**到对应的正式 mod 文件夹里（必要时新建一个"工具输出"mod）。
3. 只保留真正需要"临时覆盖一切"的文件在 Overwrite 中。
4. 删除已归档的重复项，避免 Overwrite 与正式 mod 互相打架。

> Overwrite 与 [虚拟删除](../01-mechanism/virtual-delete.md) 方向相反：一个是"暴露工具写出的新文件"，一个是"隐藏某文件"。
