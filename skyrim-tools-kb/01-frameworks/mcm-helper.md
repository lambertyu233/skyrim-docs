---
id: mcm-helper
title: MCM Helper
category: 01-frameworks
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [前置, UI, MCM, 配置, 依赖库]
aliases: [MCM Helper, 53000, MCM 助手, 配置菜单 json]
source: https://www.nexusmods.com/skyrimspecialedition/mods/53000
summary: 用 JSON 定义 MCM 菜单的框架，把"写 Papyrus 菜单脚本"变成"写一个配置文件"——现代 mod 的设置菜单基本都走它。
---

# MCM Helper

## 解决什么问题

传统 MCM 需要作者写大量 Papyrus：注册菜单、逐项建控件、手工读写设置。
MCM Helper 把这套流程改成：

- 一个 `config.json` 描述菜单结构（页、分组、控件、默认值）；
- 一个 `settings.ini` 存实际取值（可手工编辑、可预置推荐值）。

**副作用（对本工作区很重要）**：因为设置落在 `settings.ini` 里，
排查"某个选项是不是被改了"时，**直接看 ini 比进游戏看菜单快**。
整合包与指南也常用预置 ini 的方式发布推荐设置。

## 版本敏感（务必注意）

MCM Helper 是 SKSE 插件，**必须与游戏运行时版本匹配**。
Nexus Mods Wiki 的 SKSE64 指南专门点它的名：装错版本的典型表现是
**"SkyUI 里出现奇怪行为"**，而不是干脆崩溃——很难归因。

## 相关

- [SkyUI（含 MCM 框架）](../01-frameworks/skyui.md)：MCM 框架的承载者。
- [SKSE64（Skyrim Script Extender）](../01-frameworks/skse64.md)：版本匹配总原则。
- [powerofthree's Tweaks（引擎修复与调整）](../09-diagnostics/po3-tweaks.md)：同样是"ini 在 `Data/SKSE/Plugins/` 下"的配置范式。
- [配置文件体系（哪个 ini 在哪、归谁管）](../11-config/settings-files.md)：各类配置文件的落点与归属。
