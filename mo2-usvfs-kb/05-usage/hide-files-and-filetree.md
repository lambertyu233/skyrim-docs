---
id: hide-files-and-filetree
title: 文件树、隐藏文件与冲突面板
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 文件树, Filetree, .mohidden, 冲突]
aliases: [隐藏文件, 冲突面板, 遮蔽单个文件]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: Conflicts 页显示谁覆盖谁并可 Hide 文件（加 .mohidden 后缀）；Filetree 页可新建/改名/删除/隐藏/拖动文件。
kind: tutorial
---

# 文件树、隐藏文件与冲突面板

## 打开 Mod Information

**双击**左窗格里的某个 mod，或右键 → `Information`。各标签页如下。

| 标签页 | 作用 |
| --- | --- |
| **Textfiles** | 显示 mod 内所有文本文件（含 readme）。左侧列表点文件名即可查看，可编辑并用底部 `Save` 保存。**只显示 ASCII 格式的 `*.txt`**。 |
| **INI-Files** | 显示并编辑 mod 内的 ini 文件；也可在左下框右键 → `Create Tweak` 新建 ini tweak（见 [游戏 INI 与 ini tweaks](ini-and-tweaks.md)）。 |
| **Images** | 查看 mod 内的图片。 |
| **Optional ESPs** | 把本 mod 的插件移到**非激活的可选位置**——文件还在手边，但不会误启用。注意：放在这里的插件**不会**触发 MO 平时"该 mod 含多个 ESP"的提示。 |
| **Conflicts** | 所有冲突文件总览（见下）。 |
| **Categories** | 修改该 mod 的分类。 |
| **Nexus Info** | 显示 Mod ID 对应 Nexus 页面的文本。Mod ID 不对要改，否则版本信息也跟着错；`Version` 也可在此修正；点蓝色 `Visit on Nexus` 打开网页。 |
| **Notes** | 为 mod 写备注；悬停左窗格的便签图标即可看到。 |
| **Filetree** | 显示 mod 内全部文件（含 MO 生成的 `meta.ini`——**别动它**），见下。 |

## Conflicts 面板

右侧三个数字，从上到下依次是：

1. **处于冲突中、且正在覆盖其它 mod** 的文件数；
2. **处于冲突中、正被其它 mod 覆盖** 的文件数；
3. **不与任何已启用 mod 冲突** 的文件数。

- **上框**：本 mod **覆盖低优先级 mod** 的文件。左侧是文件路径，右侧按**优先级从低到高**列出冲突文件的来源。
  - 想让**别的 mod**来提供该文件？把本 mod 的优先级调到那个 mod 之前。
  - 或者右键某个冲突文件 → `Hide`，等效于把该文件从本 mod 移除。
- **下框**：本 mod **被高优先级 mod 覆盖**的文件。左侧是路径，右侧是提供该文件的 mod 名（只有一个）。**此框中无法 Hide 任何文件。**

## Hide 的实质：`.mohidden`

- `Hide` 实际是给文件**追加 `.mohidden` 扩展名**，让它不生效。
- 恢复：进入 `Filetree` 标签页，右键该文件 → `Unhide`。
- 这也是高级用法：两个 mod 互相覆盖**不同**文件、而你更想要两者各一部分时，可以用 Hide 精确取舍（详见[冲突解决与优先级](conflict-resolution.md)）。

## Filetree 面板

- 显示 mod 内**全部文件**，包含 MO 生成的 `meta.ini`（**勿动**，MO 把 mod 信息存在里面）。
- 右键菜单可：**新建文件夹**（`New Folder`，在所在层级下创建）、**打开文件**（`Open`）、**重命名**（`Rename`，也可双击文件改名）、**删除**（`Delete`）、**隐藏**（`Hide`）。
- 支持**拖放**在 mod 内移动文件/文件夹。
- 最适合用来核对"东西到底装对目录没有"，尤其是 **FOMOD 装歪**的情况。

> 相关：[冲突解决与优先级](conflict-resolution.md)、[虚拟删除](../01-mechanism/virtual-delete.md)、[Overwrite 目录与维护](overwrite-dir.md)。
