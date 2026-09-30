---
id: version-pitfalls
title: 版本地雷——1.5.97（SE）与 1.6.x（AE）的分界
category: 08-compatibility
kind: reference
version: 1.0.0
updated: 2026-09-30
tags: [版本, 1.5.97, AE, SE, 地雷]
aliases: [1.5.97 还是 1.6, ae se 区别, 版本装错, runtime 版本]
source: https://www.nexusmods.com/skyrimspecialedition/mods/145100
summary: 动作系统各插件对 1.5.97/1.6.x 的支持分界表——前置装错版本会直接炸 MCM 或攻击失效。
---

# 版本地雷——1.5.97（SE）与 1.6.x（AE）的分界

先确定自己游戏版本：1.5.97（SE 最终版）还是 1.6.x（AE）。SKSE64 与本体的精确版本对应关系见 [skyrim-tools-kb/01-frameworks/](../../skyrim-tools-kb/01-frameworks/)（SKSE64 条目）。下表只列**官方页面明说的**分界【一手源，除注明外】：

## 明确分版本下载的

| 插件 | 1.5.97 | 1.6.x（AE） | 出处 |
|---|---|---|---|
| **Behavior Data Injector** | mods/78146（v0.13 官方原文 "Supports only v1.5.97"） | mods/78159 | 【一手源】 |
| **IFrame Generator RE** | mods/74401（v1.03 停更） | mods/82737（doodlum AE 版，"Only compatible with AE"） | 【一手源】 |
| **SCAR 本体** | v1.06+ 官方移除 1.6 支持 | 用 doodlum 的 SCAR AE Support（mods/77285） | 【一手源】 |
| **dTry's Key Utils** | SE 版 DLL | AE 版 DLL（或 doodlum 的 dTry Plugin Updates FOMOD） | 【一手源】 |

## 明确双版本支持的

- **AMF**：v1.2.0 官方原文 "supports 1.5.97, 1.6.640, 1.6.1170, 1.6.1179, 1.7.104, VR"。
- **Animation Queue Fix**：作者原话 "compatible with any non-ancient Skyrim version, including 1.5.97, 1.6+ and VR"。
- **Payload Interpreter** v1.0.1：clib-ng 通吃全部版本。
- **Dual Wield Parrying SKSE**：README "Tested with 1.5.97… Compatible with 1.6.353 and above"。

## 明确卡死的

- **SmoothCam**：官方仅支持 1.5.97 与 1.6.x（README 原文）。
- **Valhalla Combat / Elden Parry**：2022 年停更，最新 AE 需社区补丁（见各自条目）。
- **POISE NG**：已隐藏停更。

## 症状对照

前置版本装错的典型表现：**MCM 菜单消失/炸开**、**攻击直接失效**、**CTD on launch**。排错时第一步永远是核对 SKSE 版本与每个 SKSE 插件的 AE/SE 文件选择。工具层面的版本矩阵见 [skyrim-tools-kb/12-sources/common-misconceptions.md](../../skyrim-tools-kb/12-sources/common-misconceptions.md)。
