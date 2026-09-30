---
id: key-utils-and-dmk
title: 按键输入底层：dTry's Key Utils 与 DMK
category: 02-foundations
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [Key Utils, DMK, 按键, 输入检测, 方向重击]
aliases: [dTry Key Utilities, Directional Movement Keys, 按键检测插件, 方向键注入]
source: https://www.nexusmods.com/skyrimspecialedition/mods/174499
summary: 两个"把按键输入喂给行为图"的底层插件：dTry's Key Utils（一代，魔法效果检测）与 DMK（二代，图变量检测）。
---

# 按键输入底层：dTry's Key Utils 与 DMK

## 一句话

动作 mod 要知道"玩家正按着哪个方向/哪个键"，靠的就是这两个底层插件。**DMK 是 dTry's Key Utils 的继任者**，两者都是被动底座、装上即可，几乎无冲突面。

## dTry's Key Utils（一代）

- Nexus [mods/69944](https://www.nexusmods.com/skyrimspecialedition/mods/69944)，GitHub [D7ry/DtryKeyUtil](https://github.com/D7ry/DtryKeyUtil)【一手源】。
- 官方描述原文："A simple SKSE key utility plugin. Currently supports movement input trace & button ID input trace & user input event trace through spells/magic effects. Script: none."——把输入转成魔法效果，供 OAR/DAR 的 `HasMagicEffect` 条件或其它 mod 读取。
- 依赖 Address Library；dTry 停更后由 doodlum 的 **dTry Plugin Updates**（Nexus 85740）提供 1.6.640/NG 的 FOMOD 移植【一手源】。
- 使用场景：BFCO 的伪方向重击（官方 FAQ 原文提到需要它）、TK Dodge RE 的第一人称八向可选文件等【一手源】。

## DMK = Directional Movement Keys（二代）

- Nexus [mods/174499](https://www.nexusmods.com/skyrimspecialedition/mods/174499)，作者 Viny（上传名 xYZeroYx，也是 BFCO 官方 Credits 里 "Help update BFCO.dll" 的人），2026-03-11 首发【一手源】。
- 作者原话："basically its Dtry Keys without the use of magic effects and stuck problems"——改用**行为图变量**（`DirecionalCycleMoveset` 0-8 八向、`CameraMovementCMF` 等）注入方向，无魔法效果、无卡顿问题；支持任意键盘布局与手柄，可随时装卸【一手源】。
- **与 BFCO 的关系**：BFCO Requirements 页面把 DMK 列为方向重击前置；用 CFM（Combat Movement Framework，内置同类功能）者无需 DMK【一手源】。注意：BFCO 的"真方向重击"是行为层原生实现，DMK 主要服务于伪方向重击/热键派生类玩法与按 DMK 制作的动作包（如 For Honor 社区转换包）【一手源+推断】。
- 2026-07 曾短暂出现新 runtime 适配空窗，后更新【社区经验】。
