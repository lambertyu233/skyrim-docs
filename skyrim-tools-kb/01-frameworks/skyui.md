---
id: skyui
title: SkyUI（含 MCM 框架）
category: 01-frameworks
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [前置, UI, 界面, MCM, 依赖库]
aliases: [SkyUI SE, skyui 5.2, 12604, 界面前置, Error Code 1]
source: https://www.nexusmods.com/skyrimspecialedition/mods/12604
summary: 现代 UI 与 MCM（Mod Configuration Menu）的承载者——几乎所有带设置菜单的 mod 都靠它，因此它是事实上的必装前置。
---

# SkyUI

## 两层价值

1. **UI 重做**：把原版为手柄设计、键鼠难用的物品/魔法/交易界面换成列表式 PC 友好界面。
2. **MCM 框架**：提供"模组配置菜单"基础设施。**任何在游戏内出现设置菜单的 mod，都要靠它。**
   这也是为什么它出现在大量 mod 的 Requirements 里——不是因为外观，而是因为 MCM。

## 硬依赖：SKSE64

SkyUI 是 SKSE 插件。**用普通启动器进游戏 → SkyUI 报 Error Code 1**，
这是新手最经典的报错，根因几乎都是启动方式不对（见 [SKSE64（Skyrim Script Extender）](../01-frameworks/skse64.md)）。

另一个经典坑：**打开游戏内置的模组菜单会关闭 SkyUI**。
Nexus 官方安装指南明确建议：**停止使用游戏内置 mod 菜单**，改用 MO2 / Vortex。

## 历史上关于"5.2 SE Plugin"的说明

Nexus 的 SKSE64 安装指南提到过一个补丁文件
`SkyUI 5.2 SE Plugin with Master Added`，用途是应对"内置 mod 菜单被打开后 SkyUI 失效"。
现代工作流下（从不打开内置菜单）通常用不到它。

## MCM 的两个延伸

| 组件 | 作用 |
|---|---|
| **MCM Helper** | 让 mod 作者用 JSON 定义 MCM，而不是写一堆 Papyrus——现代 mod 的主流做法，见 [MCM Helper](../01-frameworks/mcm-helper.md) |
| **UIExtensions** | 给 MCM 补控件（滑块、文本输入等） |

## 相关

- [MCM Helper](../01-frameworks/mcm-helper.md)
- [SKSE64（Skyrim Script Extender）](../01-frameworks/skse64.md)
- [Mod Organizer 2（工具视角）](../03-managers/mo2-tool.md)（在管理器内启动 SKSE 才能让 SkyUI 正常工作）
