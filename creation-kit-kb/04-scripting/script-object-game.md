---
id: script-object-game
title: Game 脚本对象
category: 04-scripting
version: 1.0.0
updated: 2026-09-20
tags: [papyrus, script-object, game, global, native]
aliases: [Game 脚本, Game 对象, 取玩家, GetPlayer]
source: https://ck.uesp.net/wiki/Game_Script
summary: 全局静态（Global）脚本对象，提供存档、时间、天数、玩家控制、工具函数等游戏级 API。
status: stable
kind: reference
---

# Game 脚本对象

全局静态（Global）脚本对象，提供存档、时间、天数、玩家控制、工具函数等游戏级 API。

> 来源：https://ck.uesp.net/wiki/Game_Script

## 概述

本条目汇总该 Papyrus 脚本对象最常用的原生（native）函数。所有函数均来自游戏引擎暴露，无法在脚本中重写其实现。完整列表与参数请以官方页面为准。

## 常用函数

| 函数 | 说明 |
| --- | --- |
| `GetPlayer - Game` | 返回玩家 Actor 引用。 |
| `GetForm - Game` | 按 Form ID 从当前加载的插件中取回 Form。 |
| `GetFormFromFile - Game` | 按 Form ID 与插件名取回 Form。 |
| `GetCurrentWeather - Game` | 返回当前天气对象。 |
| `SetGameSettingFloat - Game` | 修改 GMST 浮点游戏设置。 |
| `GetHourOfDay - Game` | 返回当前一天中的小时（0-24）。 |
| `Wait - Game` | 游戏等待指定游戏小时数。 |
| `EnablePlayerControls - Game` | 恢复对玩家的控制。 |
| `DisablePlayerControls - Game` | 禁用对玩家的控制。 |
| `GetPerkPoints - Game` | 返回玩家可用 perk 点数。 |
| `AdvanceSkill - Game` | 提升指定技能经验。 |
| `ShowTitle - Game` | 在屏幕上显示标题文字。 |

## 使用提示

- 脚本对象即「类」，运行于具体实例（如某个 Actor 或某个箱子）。
- `Self` 指向调用函数的当前实例；全局对象（Game / Debug）无 Self。
- 编译与连接请参见同板块的「编译脚本」条目。

