---
id: papyrus-tweaks-ng
title: Papyrus Tweaks NG
category: 09-diagnostics
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [性能, 脚本引擎, Papyrus, INI, 调优]
aliases: [Papyrus Tweaks NG, PapyrusTweaks.ini, 脚本性能, 脚本延迟, iMaxOpsPerFrame, 77779, Nightfallstorm]
source: https://www.nexusmods.com/skyrimspecialedition/mods/77779
summary: 脚本引擎的修复/调整/性能增强集合（Nightfallstorm），100% 可配置、可随时装卸；改 ini 里的几个开关就能显著缩短脚本密集场景的执行时间。
---

# Papyrus Tweaks NG

Nexus：`skyrimspecialedition/mods/77779`，作者 **Nightfallstorm**，源码 GPL-3。
官方描述：*"Collection of fixes, tweaks and performance improvements for Skyrim's script engine.
100% configurable. Install/Uninstall anytime."*

## 它解决什么

Papyrus 的原始设计没考虑"几百个 mod 同时跑脚本"。表现为：
进城、开战、读档时**脚本延迟尖峰**、NPC 反应迟钝、任务推进卡顿。
这个 mod 调整脚本引擎的调度方式与限额。

**注意体感描述（社区口径）**：它不"让脚本变快"，而是**让脚本更聪明地分配时间**。

## 配置

配置文件：`SKSE/Plugins/PapyrusTweaks.ini`
（Nexus Files 里会提供一份**参考副本**，STEP 的推荐做法是"安装主文件并合并这份参考 ini"）。

v4.0 起设置被拆成两类：

| 分组 | 面向 |
|---|---|
| **VMTweaks** | 所有人：按喜好调脚本引擎 |
| **Logger Tweaks** | mod 作者 / 高级用户：改进 Papyrus 日志 |

## 有实测数据的几个开关（社区实测，可复现）

一份性能讨论帖给出的三处改动：

```
iMaxOpsPerFrame = 2000
bSpeedUpNativeCalls = true
bIgnoreMemoryLimit = true
```

在脚本极重的测试场景里，同一套回归脚本的执行时间**从约 140 秒降到约 14 秒**
（约 90% 降幅）。**但这是特定 modlist 的实测**，不代表普遍比例；
且 `bSpeedUpNativeCalls` 涉及事件执行顺序，属于需要留意的调整项。

（来源：性能讨论帖，**属社区经验**；具体键名与默认值请以你机器上的 ini 与发布页为准）

## 需要注意的坑

1. **历史上踩过事件顺序 bug**：`SpeedUpNativeCalls` 曾改变事件执行顺序，
   少数对顺序敏感的脚本（社区举出过具体任务例子）会出错，后续版本修复。
   所以**改这几个开关后要观察一段时间**。
2. **运行时兼容性会滞后**：发布页讨论区可见用户反馈
   `failed to open address library file` 一类的报错，根因是该版本尚未支持最新的游戏运行时；
   作者已表态会更新。**遇到这类报错先确认是不是版本滞后，而不是去重装 Address Library。**
3. v4.1.0 起把 **Quest** 加进了脚本类排除列表（会重置该 INI 设置）——
   升级大版本后**建议核对 ini 是否被迁移**。

## 与 po3 Tweaks 的关系

两者都可能出现在同一个 modlist 里。作者本人致谢里明确提到
**INI 设置的设计受了 powerofthree's Tweaks 的启发**——名字相似是历史原因，
**功能不重叠**（一个管 Papyrus 调度，一个管引擎修复）。

## 相关

- [powerofthree's Tweaks（引擎修复与调整）](../09-diagnostics/po3-tweaks.md)
- [Papyrus 日志与脚本排错](../09-diagnostics/papyrus-logging.md)（日志侧的调优）
- [Papyrus 编译器与反编译](../08-creation/papyrus-compiler-decompiler.md)
- [排错索引：从症状找答案](../../01-navigation/troubleshooting-index.md)（"进城卡顿"一类症状）
