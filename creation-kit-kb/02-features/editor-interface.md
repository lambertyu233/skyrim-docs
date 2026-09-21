---
id: editor-interface
title: 编辑器界面
category: 02-features
version: 1.0.0
updated: 2026-09-20
tags: [interface, render-window, cell-view, object-window, editor]
source: https://ck.uesp.net/wiki/Bethesda_Tutorial_Creation_Kit_Interface
summary: Creation Kit 由菜单栏、对象窗口、单元格视图、渲染窗口、预览窗口等面板组成，是 MOD 编辑的主工作区。
status: stable
kind: reference
---

# 编辑器界面

Creation Kit 采用多窗口（dockable panel）布局。熟悉各面板职责，是高效编辑的前提。

## 核心窗口

| 窗口 | 作用 |
| --- | --- |
| **Menu Bar / Toolbar**（菜单栏 / 工具栏） | 文件、编辑、视图、各编辑器入口与常用操作。 |
| **Object Window**（对象窗口） | 按类型浏览所有可放置的 Form（Actor、Weapon、Spell、Static 等），是「素材库」。 |
| **Cell View**（单元格视图） | 列出世界中的 Cell 与世界空间，用于进入/编辑具体区域。 |
| **Render Window**（渲染窗口） | 3D 视口，放置、移动、旋转、缩放物体，进行地形与 Navmesh 编辑。 |
| **Preview Window**（预览窗口） | 选中物体的快速预览。 |
| **Reference Window / Properties** | 查看与编辑当前选中引用的属性。 |
| **Landscape Editor**（地形编辑器） | 抬升/下压地形、绘制纹理（快捷键 `H` 进入）。 |
| **Navmesh**（导航网格） | 编辑 AI 可行走路径（快捷键 `CTRL+E` 切换）。 |
| **Plugin Window / Messages** | 管理已加载插件与编译/校验消息。 |

## 工作流提示

1. 在 **Object Window** 找到物体 → 拖入 **Render Window**。
2. 用 **Render Window** 的位移/旋转/缩放 Gizmo 摆放（详见[快捷键映射](keyboard-mapping.md)）。
3. 在 **Cell View** 切换要编辑的 Cell / Worldspace。
4. 用 **Landscape / Navmesh** 编辑器完善地形与寻路。
5. 保存为 `.esp`，用 [Archive.exe](archive-exe.md) 打包资源。

## 相关条目

- [快捷键映射](keyboard-mapping.md)
- [术语表](glossary.md)
- [Creation Kit 界面教程](../06-tutorials/ck-interface-tutorial.md)

> 来源：[UESP Bethesda Tutorial Creation Kit Interface](https://ck.uesp.net/wiki/Bethesda_Tutorial_Creation_Kit_Interface)
