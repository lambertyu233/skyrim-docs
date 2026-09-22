---
id: wrye-bash
title: Wrye Bash（管理器 + Bash Patch）
category: 03-managers
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [管理器, Wrye Bash, Bash Patch, 冲突解决, 批量安装]
aliases: [Bash, bashed patch, 巴什补丁, WB, 瑞士军刀]
source: http://wrye-bash.github.io/docs/Wrye%20Bash%20General%20Readme.html
summary: 老牌"瑞士军刀"：既是 mod 安装/冲突管理器，也提供 Bash Patch 自动合并 leveled list 等记录级修补——后者至今不可替代。
---

# Wrye Bash

> 官方定位原文：**"a powerful mod management utility"**，功能包括
> mod 安装与冲突管理、插件加载顺序管理、提高兼容性、
> **通过自动合并兼容 mod 来突破 255 插件上限**、ini 与设置文件管理、截图管理等。

## 两个身份

1. **模组管理器**：BAIN 安装向导、安装顺序与资源冲突管理。
   与 MO2 并存时职责需分工——社区常见做法是 **MO2 管安装与启动、Wrye Bash 只用来做 Bash Patch**，
   从 MO2 内启动它。
2. **Bash Patch 生成器**：本项目最核心、**至今没有完整替代品**的能力，
   见 [Bash Patch（Wrye Bash 的记录合并）](../04-loadorder/bashed-patch.md)。

## 官方文档里的关键术语（值得记住）

- **Resource Conflict（资源冲突）**：两个 mod 放了同路径文件 → 用**安装顺序**解决。
- **Data Conflict（数据冲突）**：两个插件改同一记录 → 用**加载顺序或打补丁**解决。
- **ITM / UDR**：官方 Readme 的定义与社区惯例相反的地方在于——
  **UDR 这个缩写指的是"修好之后的"引用**（undeleted + disabled），
  而 "Scan For UDRs" 扫的其实是"被删除的引用"。这一点官方特意加注澄清。

> 冲突在官方口径里**不是贬义词**：*"they are not inherently bad, and most modding is the result of purposeful conflicts."*

## 版本与状态

- 支持 Oblivion / Nehrim / Fallout 3 / FNV / Skyrim（LE）/ Enderal / Fallout 4 / **Skyrim SE**。
- 有 **Python 版**与 **Standalone 版**：官方建议一般用户用 **Standalone**（依赖更少）。
- 开发活跃度：从官方仓库的 `dev` 主分支与 AFK Mods 论坛帖子可见仍在维护；
  **WIP 构建在官方 Discord 的 `#wip-builds` 频道**。

## 与其他管理器的关系

- 与 MO2 **可以共存**（官方文档与社区共识）；关键是不要让两者同时管同一批安装顺序。
- 与 LOOT 协同：LOOT 会给插件打 **Bash Tag 建议**，Bash Patch 据此决定合并哪些记录。

## 相关

- [Bash Patch（Wrye Bash 的记录合并）](../04-loadorder/bashed-patch.md)：Bash Patch 做什么、什么时候必须打。
- [LOOT（插件排序）](../04-loadorder/loot.md)、[脏编辑与清理（ITM / UDR）](../04-loadorder/dirty-edits-cleaning.md)
- [Mod Organizer 2（工具视角）](../03-managers/mo2-tool.md)
