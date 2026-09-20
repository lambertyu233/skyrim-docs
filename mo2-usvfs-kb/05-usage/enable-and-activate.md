---
id: enable-and-activate
title: 启用 mod 与激活插件
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 启用, 插件, 加载顺序, 备份]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 左窗格勾选启用 mod（仅对当前 profile 生效）；右窗格 Plugins 勾选激活 ESP/ESM，插件必须在 mod 根目录才会被识别。
kind: tutorial
---

# 启用 mod 与激活插件

要真正在游戏里生效，分两步：**先启用 mod，再激活其插件**。

## 启用 mod

- 在左窗格**勾选复选框**。**只对当前 profile 生效**。
- 若 `Flags` 列出现闪电图标，说明它有些文件与其它已启用 mod 冲突——见 [冲突解决与优先级](conflict-resolution.md)。
- **批量操作**：Shift 连选一段、或 Ctrl 逐个多选，然后按**空格键**切换这批 mod 的启用状态。

## 激活插件（Plugins 标签页）

- 已启用 mod 中，**位于 mod 根目录**的 ESM/ESP 会出现在右窗格 Plugins 标签页；**放在子文件夹里的插件不会被使用**。
- 勾选复选框即激活。
- 插件名前有警告图标 = **缺少某个 master**，悬停可看到是哪个。
- 悬停任意 ESM/ESP 会显示：来源、作者、描述、Enabled Masters，以及有关联 ini 文件时的**回形针**提示。

### 加载顺序

- **拖放**即可调整顺序（详见 [冲突解决与优先级](conflict-resolution.md) 中的加载顺序部分）。
- 右键标签页内有三个选项：
  - `Enable all`：激活全部 ESM/ESP。
  - `Disable all`：取消激活全部，**但保留 Skyrim.esm 与 Update.esm**（游戏运行必需）。
  - `Lock load order`：把选中的插件**锁定**在该顺序（仅对已激活插件可用）。之后其它插件可以插进它们**之间**，但它们彼此的相对顺序固定。

### 备份与恢复插件列表

- **备份**：点 Plugins 标签页右上的 `Create Backup` 按钮。
- **恢复**：点其左侧的 `Restore Backup…` 按钮。
- 恢复后的效果：备份时未激活的插件会被取消勾选；备份之后的所有优先级/加载顺序改动被回退；备份之后新增的插件会被取消勾选、按字母顺序置于列表底部。
- **注意：备份插件列表不含 INI 文件、BSA 顺序与 mod 列表**（mod 列表另有备份入口，见 [备份与恢复](backup-and-restore.md)）。

### Sort 按钮

- Plugins 标签页左上角的 `Sort` 按钮使用 LOOT 自动排序插件。
- 你在**外部 LOOT 应用**里写过的规则会被沿用，但**不装独立 LOOT 程序就无法写规则**。
- 注意：内置 `Sort` 就是 LOOT，但**缺少报告窗口与元数据编辑功能**——需要这些就用外部 LOOT（见 [常用工具配置配方](tool-recipes.md)）。

> 相关：[界面总览](ui-layout.md)（右窗格标签页）、[BSA 管理与解包](bsa-management-usage.md)（插件与 BSA 的顺序关系）。
