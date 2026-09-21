---
id: pandora-troubleshooting
title: Pandora 排错：Engine.log 与常见故障
category: 04-pandora
kind: tutorial
version: 1.0.0
updated: 2026-09-21
tags: [Pandora, 排错, Engine.log, 实例恢复, 中文教程]
aliases: [Pandora 报错, pandora 失败, Pandora 排错, pandora crash]
source: https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/blob/main/README.md
summary: Pandora 官方 Troubleshooting 全文要点 + 中文社区经验，覆盖崩溃、无位移、0 动画、FNIS mod 读不到等故障。
---

# Pandora 排错：Engine.log 与常见故障

## 官方 Troubleshooting（README 全文要点）

**① 用了 Pandora 输出就崩溃 / 出 bug？**

> `Engine.log` **会标出那些编辑失败的补丁**，便于排错。你可以试着**禁用日志里失败最频繁的 mod** 再跑一次。
> 如果确定是某个 mod 的问题，建议把日志同时发给**该 mod 作者**和**引擎开发者**。

**② 动画没有位移（no movement）？**

> 那是**某个 mod 缺 motion data**。**这不是 Pandora 的问题，是 mod 的问题。**

**③ 提示 "0 animations added" 或无法输出文件？**

> **以管理员身份运行引擎**，或把引擎安装位置**移出受保护目录**（如 `C:\Program Files`）。

**④ `Engine.log` 里有一大堆 warning？**

> warning 不是大问题，除非它们明显影响游戏内行为。**不要把来自其他 mod 的 warning 当 bug 上报。**

**⑤ Pandora 读不到 FNIS mod？**

> 若你的**游戏路径与注册表路径不同**，或你有**多个安装**，用 `--tesv` 参数；否则确保注册表路径正确。

> 来源：Pandora 仓库 README https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/blob/main/README.md

## 中文社区补充经验

来源：烽火 MOD 使用指南（适用于神话整合 9.0+ / 烽火技能树 10.6+）。

**移动施法等动作丢失：**

- **方法 1（推荐）**：使用 **Pandora 4.1.2** 版本，无需额外前置；
- **方法 2**：用 Pandora 最新版 + 安装 **Auto Skeleton Patch** 作为前置（**不一定有效**）。

**配套 mod 报 Pandora 相关错误（如 SCAR Magic Patch 的通用做法）：**

> 删除现有的 Pandora Output → 重装该 mod → 在 Pandora 里重新生成输出。

**从 FNIS 迁到 Pandora 的坑（社区反复提及）：**

- 曾有一个"首次运行不生成 FNIS data file"的问题。**变通做法：保留 FNIS，先跑一次 FNIS 让它生成数据文件，再由 Pandora 接管**（Pandora 只需该文件，首次运行会把它变成自己的）。
- 有用户报告：若 Pandora 生成结果**只有 txt**，检查是否装了 **.NET 7 Desktop Runtime**，并看 `Engine.log`。

**社区实测参考（Nexus 论坛）：**

- 44,190 个动画（无生物）、63 个 Pandora/Nemesis mod + 61 个 FNIS mod，**一轮约 25.28 秒**（首轮约 1.5 分钟）。
- 有用户报告动画数接近 5 万时会明显变慢（可能 5 分钟左右）。

## 排查顺序建议

1. **看 `Engine.log`** —— 找出失败的补丁与 mod；
2. 禁用失败最频繁的 mod 重跑；
3. 检查输出路径是否正确、输出 mod 是否启用、是否与别的 mod 有文件冲突；
4. 检查注册表/游戏路径（多安装用 `--tesv`）；
5. 以管理员身份运行 / 移出受保护目录；
6. 若从 FNIS/Nemesis 迁来，考虑**重装动画 mod**（旧引擎改过的 hkx 会污染输入）。

## 相关

- [常见报错（跨引擎）](../06-practices/troubleshooting-common.md)
- [标准刷补丁流程](../06-practices/install-workflow.md)
- [Pandora 安装指南](pandora-install.md)
