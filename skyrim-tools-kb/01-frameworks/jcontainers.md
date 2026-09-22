---
id: jcontainers
title: JContainers SE
category: 01-frameworks
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [前置, 脚本, JSON, 数据存储, 依赖库]
aliases: [JContainers SE, JC, 16495, JSON 容器]
source: https://www.nexusmods.com/skyrimspecialedition/mods/16495
summary: 让 Papyrus 能操作 JSON 结构的容器库（数组/字典嵌套），比 PapyrusUtil 更重但表达力更强，两者常同时被不同 mod 依赖。
---

# JContainers SE

## 提供什么

把 **JSON 语义**引入 Papyrus：嵌套数组、字典、按路径取值、序列化到磁盘。
典型用途：

- 复杂配置（多层菜单设置）的持久化；
- mod 之间通过文件交换结构化数据；
- 需要"嵌套字典"而 `StorageUtil` 的平铺键值表达不了时。

## 与 PapyrusUtil 的关系（最常被问）

| | PapyrusUtil | JContainers |
|---|---|---|
| 数据模型 | 平铺键值 + 一维列表 | 任意嵌套（JSON） |
| 存储位置 | form 挂载 / 外部 `.json` | 外部文件 |
| 依赖它的 mod | 极多 | 较多 |

两者**不冲突、可共存**，而且经常同时出现——因为不同 mod 选了不同方案。
"我装了 PapyrusUtil 还要不要 JContainers"的答案是：
**看你装的 mod 的 Requirements 怎么写**，不是二选一。

## 安装要点

- SKSE 插件形式安装（`Data/SKSE/Plugins/JContainers.dll` + `.pex`）。
- **发布页若落后于上游**，可去 GitHub releases 取更新版（社区常用做法，属社区经验）。
- AE 需要 AE 版文件。

## 需要注意

- 它写的 JSON 文件**不在存档里**。卸载 mod 时这些文件不会自动清，
  也不会被 FallrimTools 处理（ReSaver 主要面向 `.ess` 的 Papyrus 堆）。
- 依赖它的 mod 若报"容器不存在"，先检查是不是被**后装的版本覆盖**了 dll。

## 相关

- [PapyrusUtil SE](../01-frameworks/papyrusutil.md)
- [FallrimTools / ReSaver（存档清理）](../09-diagnostics/fallrimtools-resaver.md)（存档清理的边界）
