---
id: wabbajack
title: Wabbajack（整合包一键安装）
category: 03-managers
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [管理器, 整合包, 自动化, 安装, modlist]
aliases: [整合包安装器, 一键装整合, 整合, 集合]
source: https://wiki.wabbajack.org/
summary: 自动重建整套 modlist 的安装器：不打包任何 mod 文件，只分发"从原始站点重新下载并还原"的指令，社区整合包的标准分发方式。
---

# Wabbajack

> 官方定位：**"automated Modlist Installer that can reproduce an entire modding setup on another machine
> without bundling any assets or re-distributing any mods."**

## 工作方式（为什么它合法且可靠）

Wabbajack 编译出的 `.wabbajack` 文件里**只有指令**：

- "从 Nexus 用官方 API 下载 mod X 的版本 Y"；
- "解包到 mod 目录"；
- "对某文件应用 BSDiff 二进制补丁"（用于被清理过的 esp、被优化过的资产）；
- "改这个 ini"。

因此它**不重新分发任何受版权保护的文件**。下载走 **Nexus 官方 API**，
与你在网站上手动下载等价——同样会为 mod 作者计入下载量与捐赠点。

## 安装流程（官方 wiki）

1. 从 GitHub Releases 取 Wabbajack（免费开源，GPL3）。
2. 打开 → Gallery → 选 list → 下载 `.wabbajack` 文件。
3. **先读该 list 自带的 README**，按需下载第三方/站外文件。
4. 选两个路径：
   - **Installation Location**（安装位置）：不能等于 Wabbajack 自身位置、不能等于游戏位置、
     不能与另一个 list 相同（list **不可合并**）、不能放在 Windows 受管目录里。
   - **Download Location**（下载位置）：可与其他 list 共用（省重复下载），但同样不能是游戏位置或受管目录。
5. 等待完成（几分钟到几小时，取决于体积、网速、硬件），再按 README 做收尾步骤。

**Windows 受管目录（官方明确列出，必须避开）**：
`C:\Windows`、`C:\Users\<用户名>\Documents`、`Images`、`Videos`、`OneDrive`、
`C:\Program Files`、`C:\Program Files (x86)`。

## License 与生态规则（值得知道）

- **Modlist 必须免费**。任何形式的付费墙、付费抢先体验、
  "付费给当前版本、旧版免费"都被禁止。
- **接受捐赠可以**，前提是捐赠**不换取**对 list 的访问权。
- 作者可以选择不让自己的 mod 进入 list 吗？官方答复是**不能**——
  因为 Wabbajack 用的是公共 Nexus API，与任何用户手动下载等价。

## 常见误解

| 误解 | 实际 |
|---|---|
| 装完可以随便往上加 mod | 技术上可以，但**不在支持范围**：补丁与排序是针对固定集合做的 |
| list 可以两个叠起来用 | 官方明确 "lists can't be merged" |
| 下载位置和安装位置可以随便放 | 都不能在受管目录；安装位置还不能与另一个 list 相同 |

## 相关

- [Vortex（Nexus 官方管理器）](../03-managers/vortex.md)（Nexus Collections，另一条整合分发路线）
- [Mod Organizer 2（工具视角）](../03-managers/mo2-tool.md)（Wabbajack 的 list **基于 MO2**）
- [Crash Log Analyzer（崩溃日志解读）](../09-diagnostics/crash-log-analyzer.md)（对整合包用户有专门的排错提示）
