---
id: install-and-config
title: 安装与 ini 配置
category: 01-installation
kind: guide
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 安装, ini, MO2, overwrite]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: 用惯用的 mod 管理器正常安装即可，随时装卸；插件生成的 ini 默认落在 MO2 的 overwrite 里，千万别删，否则设置重置。
---

# 安装与 ini 配置

## 安装

- 用你惯用的 mod 管理器（**MO2 / Vortex**）**正常安装**即可。
- 官方描述：「Use your mod manager of choice.」
- 也可以手动把文件丢进 `Data` 文件夹。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## 装卸安全性

**可以中途安装/卸载。** 官方 FAQ 原文大意：

> 可以。这个插件对你的游戏没有持久影响，随时都能安装/卸载。

原因是它**完全通过 SKSE 实现**，不写存档数据、不改 esp。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（FAQ）

## 插件生成的 ini 在哪里（重要）

- 文件位于 **`Data\SKSE\Plugins\`**，主文件名形如 **`OpenAnimationReplacer.ini`**。
- **如果你用 MO2**：这些文件默认会落到 **overwrite** 目录里（因为它是游戏首次启动、插件已装的情况下生成的）。

⚠️ **不要删除插件生成的 `.ini` 文件**，否则设置会重置回默认。这是官方 FAQ 里单列的一条。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（FAQ：「The settings reset!」）

## 已知的 ini 键

| 键 | 位置 | 作用 |
| --- | --- | --- |
| `bLoadDefaultBehaviorsInMainMenu` | `Data\SKSE\Plugins\OpenAnimationReplacer.ini` | **主菜单崩溃**时官方建议把它设为 `false`。这是"在主菜单预加载动画"的开关。 |

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（FAQ：crash in main menu）

> 注意：这个键**同时影响**动画预加载行为，而 0.6.1 开发日志提到 `DefaultFemale` 之所以总是"后加载的那个"正是因为启用了它。关掉它能规避主菜单崩溃，但会失去主菜单预加载的收益。取舍自己判断。

## 首次启动的心理预期

- 主菜单会**开始预加载动画**，界面上有一条小小的进度条。这是正常行为，不是卡死。
- 装了大量动画包时，预加载需要一点时间。**开局那几秒的 T-Pose 通常是预加载还没完**，不是故障。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（Features：Animations can start preloading while in the main menu / a small progress bar）

## 可选的"清理"动作

OAR 会在插件旁缓存一份**动画哈希**文件（用于重复动画过滤），文件名以 `.bin` 结尾。这个文件**可以安全删除**——手动删，或在设置菜单里点按钮删。

> 来源：<https://bakemono.app/p/patreon/25643772/81916525>（0.8.0 开发日志：The hashes are cached in a .bin file stored next to the plugin … The file can be safely deleted）

## 相关

- [前置需求与支持的版本](requirements.md)
- [兼容性 FAQ](compatibility-faq.md)
- [游戏内编辑器](../05-editor/in-game-editor.md)
