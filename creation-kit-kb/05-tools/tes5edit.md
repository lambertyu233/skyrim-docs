---
id: tes5edit
title: TES5Edit / xEdit 清理
category: 05-tools
version: 1.0.0
updated: 2026-09-20
tags: [tes5edit, xedit, cleaning, itm, udr, mod-cleaning]
source: https://ck.uesp.net/wiki/TES5Edit_Mod_Cleaning_Tutorial
summary: TES5Edit（xEdit）用于清理插件——移除 ITM、撤销误删记录、清理导航等，提升兼容性与稳定性。
status: stable
kind: tutorial
---

# TES5Edit / xEdit 清理

**TES5Edit**（及其后续通用的 **xEdit**）是 MOD 社区最常用的插件检查与清理工具。发布 MOD 前清理插件，可显著减少冲突与崩溃。

## 为什么要清理

MOD 在 CK 中编辑时，常会无意引入「与官方主文件完全相同」或「误删又被引用」的记录。这些脏数据会在多 MOD 叠加时放大冲突。

## 三类常见问题

| 问题 | 含义 | 处理 |
| --- | --- | --- |
| **ITM**（Identical to Master） | 记录与主文件完全相同，毫无意义 | 移除 |
| **UDR**（Undeleted and Disabled Reference） | 本应删除却被「禁用占位」的引用 | 彻底删除 / 修复 |
| **Deleted Navmesh / 脏引用** | 误删导致其它 MOD 引用失效 | 清理或恢复 |

## 基本清理流程

1. 启动 xEdit，仅勾选要清理的插件（及其依赖的主文件）。
2. 右键插件 → **Apply Filter for Cleaning**，等待分析完成。
3. 按提示移除 ITM、处理 UDR（通常「Remove」即可）。
4. 退出 xEdit 并保存改动，得到更干净、向后兼容的 `.esp`。

> 注意：清理前务必**备份**原始 `.esp`；不确定时不要随意删除被其它 MOD 依赖的记录。

## 相关条目

- [Data 目录与插件格式](../01-installation/data-files.md)
- [上传 Steam 创意工坊](../06-tutorials/upload-steam-workshop.md)

> 来源：[UESP TES5Edit Mod Cleaning Tutorial](https://ck.uesp.net/wiki/TES5Edit_Mod_Cleaning_Tutorial)
