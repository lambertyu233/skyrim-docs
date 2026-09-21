---
id: data-files
title: Data 目录与插件格式
category: 01-installation
version: 1.0.0
updated: 2026-09-20
tags: [data, esm, esp, bsa, load-order, plugin]
source: https://ck.uesp.net/wiki/Data_file
summary: 游戏资源集中在 Data 目录；.esm 为主文件、.esp 为插件、.bsa 为资源归档，加载顺序决定覆盖优先级。
status: stable
kind: reference
---

# Data 目录与插件格式

《天际》的所有内容（网格、贴图、脚本、声音、关卡数据）都组织在游戏的 **Data** 目录下。MOD 开发的核心，就是向 Data 目录新增并管理各类文件。

## 主要文件类型

| 扩展名 | 含义 | 说明 |
| --- | --- | --- |
| `.esm` | Master（主文件） | 被其他插件依赖的基础数据，如 `Skyrim.esm`。主文件须先于依赖它的 `.esp` 加载。 |
| `.esp` | Plugin（插件） | MOD 最常见的产出，承载新增/修改的记录。 |
| `.bsa` | Bethesda Archive | 资源归档（网格、贴图、声音等），减少 loose files。 |
| `.esl` | Light Plugin | 轻量插件，占用独立 FE 加载槽，缓解 255 个插件上限。 |

## 加载顺序（Load Order）

- 插件按列表顺序加载，**后加载者覆盖先加载者**的同名记录（Form ID）。
- 主文件（.esm）始终排在普通插件之前；官方主文件通常最前。
- 工具（如 LOOT）可自动排序以降低冲突。

## 最佳实践

- 资源尽量打包为 `.bsa` 而非零散 loose files：更易安装/卸载、便于排查问题。
- 修改前先做 **可写副本**，并用版本控制（Git）跟踪 `.esp` 的变更。
- 清理插件（移除 ITM、撤销误删记录）参见工具链的 [TES5Edit 清理](../05-tools/tes5edit.md)。

## 相关条目

- [INI 文件体系](ini-files.md)
- [Archive.exe 打包](../02-features/archive-exe.md)

> 来源：[UESP Data file](https://ck.uesp.net/wiki/Data_file)
