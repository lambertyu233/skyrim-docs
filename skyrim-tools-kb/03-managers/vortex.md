---
id: vortex
title: Vortex（Nexus 官方管理器）
category: 03-managers
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [管理器, Vortex, Nexus, 部署, 集合]
aliases: [Nexus Mod Manager, NMM, deploy mods, purge mods, cyclic rules]
source: https://wiki.nexusmods.com/index.php?title=Frequently_Asked_Questions
summary: Nexus 官方管理器：把「安装」与「部署」拆成两阶段，用链接把 mod 铺进游戏目录；支持 Nexus Collections 一键装整合。
---

# Vortex

## 核心模型：安装 ≠ 部署（官方 FAQ）

Vortex 明确把装 mod 分两阶段：

1. **安装阶段**：解包 mod 归档、走 FOMOD 安装器，文件落到独立的 **mod 目录**——此时对游戏**毫无影响**。
2. **部署（Deploy）阶段**：把文件**链接**进游戏目录，这一刻才开始生效。
   禁用 mod 后再部署，链接会被移除——所以"部署 = 把你的 mod 选择提交给游戏"。

**Purge Mods** 是部署的反操作：移除全部链接但**不删 mod**，
用来把游戏目录恢复成原版状态（做备份前、或排错时用）。**Purge 不是破坏性操作**，
点一下 Deploy 就恢复。

> 因为部署可能要几秒到几十秒，官方建议在 Settings → Interface 关掉
> **"Deploy Mods when Enabled"**，改成手动部署，避免每改一个 mod 就卡一次。

## 常见困惑与官方解释

- **"我装了 mod，但 Plugins 里看不到 esp。"**
  Plugins 页只显示**已部署**的文件。若关了自动部署又没手动部署，插件不会出现，mod 也不会生效。
- **"Plugins not sorted because of cyclic rules。"**
  你自己的规则形成了环（A 要在 B 后、B 要在 A 后）。Vortex 内置的 LOOT 排序**本身无环**，
  所以这个错误只会由**自建规则/分组规则**引起。点 "More" 看受影响插件。
- **Profiles**：默认隐藏，需在 Settings → Advanced 打开 **Enable Profile management**。
- **Staging folder**：mod 目录与游戏需在**同一卷**上（否则无法建立硬链接）。

## Nexus Collections

Vortex 是 Nexus Collections（官方整合）的客户端。
与 Wabbajack 的差别在于**分发机制**：Collections 走 Nexus 平台自身的清单，
Wabbajack 走 `.wabbajack` 文件与作者自建下载源。

## 什么时候选它、不选它

- **选**：你主要从 Nexus 下载、想要一键整合、不想理解虚拟文件系统的概念。
- **不选**：你要做深度冲突排查（MO2 的左侧顺序 + 冲突面板更直观），
  或者你的工作流重度依赖从管理器启动 xEdit/Synthesis 等工具。

## 相关

- [Mod Organizer 2（工具视角）](../03-managers/mo2-tool.md)（对照）
- [Wabbajack（整合包一键安装）](../03-managers/wabbajack.md)（另一种整合分发）
- [LOOT（插件排序）](../04-loadorder/loot.md)（Vortex 内置的排序引擎就是 LOOT）
