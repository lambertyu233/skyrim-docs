---
id: backup-and-restore
title: 备份与恢复
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 备份, 恢复, modlist, 插件列表]
aliases: [备份 MO2, 恢复存档, backup, 防丢档]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 左窗格可备份/恢复 mod 列表，Plugins 页可备份/恢复插件加载顺序；重装前要备份 downloads/mods/profiles 等目录。
kind: tutorial
---

# 备份与恢复

## 备份 mod 列表（左窗格）

- **备份**：点 profile 下拉框右侧的 `Create Backup`（保存磁盘图标）按钮。
- **恢复**：点它左侧的 `Restore Backup…` 按钮。
- 恢复后的效果：
  - 备份时**未启用**的 mod 会被取消勾选；
  - 备份之后的**所有优先级改动被回退**；
  - 备份之后**新增**的 mod 会被取消勾选，并按字母顺序**置于 mod 列表底部**。

## 备份插件列表（右窗格 Plugins 页）

- **备份**：Plugins 标签页右上的 `Create Backup`。
- **恢复**：其左侧的 `Restore Backup…`。
- 详见[启用 mod 与激活插件](enable-and-activate.md)。

## 三者互不包含

| 备份对象 | 入口 | 不包含 |
| --- | --- | --- |
| mod 列表 | 左窗格 `Create Backup` | INI 文件、BSA 顺序、插件（加载顺序）列表 |
| 插件列表 | Plugins 页 `Create Backup` | INI 文件、BSA 顺序、mod 列表 |

> 所以完整保底要**两边都备份**。

## 备份整个 MO 安装（重装/迁移前）

升级或重装前，应备份以下内容：

- **`downloads`**：所有来自 Nexus 的归档。
- **`mods`**：左窗格里"已安装"的 mod 实体。
- **`profiles`**：你定义的全部 **profile**，包括其中的存档（如果你选了保存游戏到 profile）。
- 若改过分类，还有 **`categories.dat`**（见[自定义 mod 分类](mod-categories.md)）。

> 若是 instanced 安装，设置本身存放在 `%LocalAppData%/ModOrganizer`，与 MO 程序目录分开，所以删掉程序目录内容不会丢设置（见[便携安装 vs 实例安装](portable-vs-instance.md)）。

> 相关：[更新、合并与卸载](update-and-uninstall.md)、[存档查看与 Fix Mods](saves-management.md)。
