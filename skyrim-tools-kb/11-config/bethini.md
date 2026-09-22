---
id: bethini
title: BethINI（INI 配置优化）
category: 11-config
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [配置, INI, 性能, 画质, 预设]
aliases: [ini 优化, 游戏设置, 4875, 帧数优化, INI 编辑器]
source: https://www.nexusmods.com/skyrimspecialedition/mods/4875
summary: 把 Bethesda 那堆混乱的 INI 整理、纠错并按预设优化的工具——顺带把 Creation Kit 配好多重 master，是「装完 mod 先跑一次」的那类步骤。
---

# BethINI

作者 **DoubleYou**。Skyrim SE 版走 Nexus `skyrimspecialedition/mods/4875`；
LE / Fallout 3 / NV / FO4 各有对应页面。**当前版本 3.6.1（最后更新 2022-05-01）**
——引用版本号时请注意这条数据可能已过期。

> 新一代（面向 Starfield / SE / FO4）叫 **BethINI Pie**，官方描述里点名了它。

## 官方给的七条理由（发布页原文要点的转述）

1. 自动把 INI **重新排序**成合理顺序，便于手工继续调；
2. 自动修掉常见错误，**包括一些会导致 CTD 的**；
3. **自动检测你装的 mod，并按作者建议调整**；
4. 预设的画质/性能比启动器生成的预设**在 95% 情况下更好**；
5. 能改的设置**比游戏内更多**，且每项都有解释；
6. 自动**备份**你的 INI；
7. 对 Skyrim，还会**自动把 Creation Kit 配置成支持多重 master 与已装 DLC**。

## 两种版本

| 版本 | 说明 |
|---|---|
| **Standalone** | 便携、解压即用。⚠️**官方明确：不要通过 Mod Organizer 运行**。可能被杀毒误报 |
| **AHK Script 版** | 需要 AutoHotkey v1.1.x；被杀毒误报时改用这个 |

## 推荐使用流程（发布页原文顺序）

1. **不要先删 INI 文件**；
2. 运行 BethINI；
3. **MO2 用户**：在 Setup 页通过 **INI Path** 选择你的 profile（会自动检测），
   并**强烈建议先关掉 MO2**；
4. Basic 页 → Presets 区点 **Default** 把 INI 重置为默认状态；
5. 只使用 ENBoost 之外还用 ENB 的 LE 用户需勾 **ENB Mode**（会被自动检测，不确定就别动）；
6. 选目标预设；
7. 勾上 **Recommended Tweaks**（对所有用户都推荐的那批）；
8. 按需微调；
9. **Save and Exit**。

## 为什么它属于"装 mod 之后"的步骤

发布的更新记录里能看出它的维护方式是"跟着社区实践走"：
Recommended Tweaks 会**增删条目**（例如加入与音效缓存、对话转向角、
物品名长度相关的项；也**移除过**会导致阴影闪烁的调整项）。

含义：**别把某篇文章里的"推荐值"当成永久有效**——
以你所用版本的 Recommended Tweaks 与 Custom 页为准。

## 与其它配置类工具的关系

| 工具 | 管什么 |
|---|---|
| **BethINI** | `Skyrim.ini` / `SkyrimPrefs.ini` 的整理与预设 |
| **SSE Display Tweaks** | 帧率/同步/刷新率（[SSE Display Tweaks](../09-diagnostics/sse-display-tweaks.md)） |
| **PrivateProfileRedirector** | INI 读取的性能（[PrivateProfileRedirector SE（INI 读取加速）](../11-config/privateprofile-redirector.md)） |
| **各 mod 自己的 ini** | `po3_Tweaks.ini`、`PapyrusTweaks.ini` 等 → [配置文件体系（哪个 ini 在哪、归谁管）](../11-config/settings-files.md) |

## 风险提示

它**会改你的 INI 并写回**——虽然会自动备份，仍建议**自己也留一份副本**
（[配置文件体系（哪个 ini 在哪、归谁管）](../11-config/settings-files.md) 给了各文件的位置）。

## 相关

- [配置文件体系（哪个 ini 在哪、归谁管）](../11-config/settings-files.md)、[PrivateProfileRedirector SE（INI 读取加速）](../11-config/privateprofile-redirector.md)
- [Creation Kit（官方创作工具）](../08-creation/creation-kit.md)（多重 master 的配置）
- [SSE Display Tweaks](../09-diagnostics/sse-display-tweaks.md)
