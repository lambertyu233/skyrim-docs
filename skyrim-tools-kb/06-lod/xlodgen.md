---
id: xlodgen
title: xLODGen（地形 LOD 生成）
category: 06-lod
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [LOD, 远景, 地形, 生成器, 官方文档]
aliases: [地形 LOD, terrain lod, LOD 生成, lodgen, 远景生成]
source: https://dyndolod.info/DynDOLOD-Reference
summary: 形如 xEdit 的 LOD 生成器（本质就是改名后的 xEdit），负责地形 LOD 与最终的遮挡数据；是 DynDOLOD 流程的第一与最后一步。
---

# xLODGen

## 官方定位（dyndolod.info 的 Reference）

> **"xLODGen is a renamed xEdit."**
> **"xLODGen is a Creation Kit replacement LOD generator, meant for mod authors
> to generate vanilla style LOD for their mods and new worldspaces."**

Skyrim 有**三类 LOD**：**object（物体）/ tree（树木）/ terrain（地形）**。
xLODGen 主要负责**地形 LOD**（以及后文提到的遮挡数据），
物体与树木 LOD 由 DynDOLOD 接手。

**它相对 Creation Kit 的优势**（官方原文意思）：CK 的静态物体 LOD 只能用一张
texture atlas（HD LOD 贴图除外），既限制画质又要为生成 LOD 模型做大量额外工作；
**xLODGen 允许像普通模型那样自由使用贴图**。

## 在标准流程里的位置

STEP 官方的 SkyrimSE 指南给出的顺序是：

```
xLODGen（地形）→ TexGen → DynDOLOD → xLODGen（Occlusion 遮挡）
```

**必须最先跑 xLODGen**：它把地形 LOD 的贴图与网格先更新到位，
DynDOLOD 才有正确的地基可依赖。

## 操作要点（STEP 指南口径）

1. 从 mod 管理器启动 xLODGen。
2. 勾选**所有 worldspace**。
3. 右侧**只勾 Terrain LOD**（这一趟只做地形）。
4. 按推荐分辨率设置生成（指南特别强调：**超过推荐分辨率纯属浪费性能，没有任何好处**；
   只有 ≥4K 显示分辨率时才值得把 LOD4/8/16 从 256 提到 512）。
5. 生成完成后，把输出**剪贴/移动到一个独立的输出 mod**（如 `xLODGen Output`）并启用。
6. 若用了临时的"资源用"插件，**生成完要禁用**（只在地形生成时需要）。

**注意**：Mod Organizer 2 的 Overwrite 目录里不要长期堆产物——
把输出放进独立 mod 才能在重跑与回退时保持可控。

## 遮挡（Occlusion）

流程的最后一步也用 xLODGen：**更新遮挡数据**，修掉远处地形上的"破洞"——
官方指南点名的重灾区是**水面之上的远景**。

## 什么时候必须重跑

> **任何影响外景物体的 mod 被增删或位置变动，都要重新生成 LOD。**

## 相关

- [TexGen（LOD 贴图生成）](../06-lod/texgen.md)、[DynDOLOD（物体与树木远景）](../06-lod/dyndolod.md)、[遮挡数据生成（Occlusion）](../06-lod/occlusion.md)
- [Mod Organizer 2（工具视角）](../03-managers/mo2-tool.md)（从管理器启动、Overwrite 归位）
- [配置第三方程序与快捷方式](../../mo2-usvfs-kb/05-usage/third-party-executables.md)（工具在 MO2 里的挂载方式）
