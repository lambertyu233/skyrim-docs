---
id: behavior-data-injector
title: Behavior Data Injector（BDI）——免补丁注入动画变量
category: 02-foundations
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [BDI, Behavior Data Injector, 注入, json, Maxsu]
aliases: [动画变量注入, 免补丁注入, bdi 前置, Dropkicker]
source: https://github.com/max-su-2019/BehaviorDataInjector
summary: Maxsu 与 Dropkicker 的 SKSE 插件：用 json 配置注入新动画变量与事件，免写行为补丁；MaxsuPoise 与 DMCO 的硬前置。
---

# Behavior Data Injector（BDI）——免补丁注入动画变量

## 一句话

官方描述原文："SKSE plugin that allow you to add new animation variables & events via json config files **without behavior patch**."——动画作者不用写 Nemesis/FNIS/Pandora 补丁就能引入自定义 graph 变量与事件，降低补丁冲突面。

## 基本事实

- **作者不是 Dtry**：Nexus 页 "Created by **Maxsu and Dropkicker**"（maxsu2017 上传）【一手源】。
- GitHub：[max-su-2019/BehaviorDataInjector](https://github.com/max-su-2019/BehaviorDataInjector)；doodlum 有 AE 适配 fork【一手源】。
- **版本分游戏版本**：v0.13（2022-11）文件说明原文 "Supports only v1.5.97"；1.6+ 用 [mods/78159](https://www.nexusmods.com/skyrimspecialedition/mods/78159)【一手源】。主仓库提交停在 2022-2023，对 1.6.1170+ 的持续维护状态**未核实**。
- 附带 **"Payload Interpreter - Nemesis Less Patch"** 配置：可让 [Payload Interpreter](./payload-interpreter.md) 免装 Nemesis 补丁【一手源，文件页说明】。

## 谁需要它

- **MaxsuPoise**（硬性要求：BDI / BDI Universal Support / DMenu / Modern Stagger Lock Framework）
- **DMCO 新版**（Requirements 列 BDI + BDI Universal Support）
- 普通玩家不用理解它：某 mod 的 Requirements 里写了，装就是了。

## 相关条目

[MaxsuPoise](../04-poise/maxsu-poise.md) · [DMCO](../03-dodge/dmco.md)
