---
id: iframe-generator
title: IFrame Generator RE——动画无敌帧框架
category: 03-dodge
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [IFrame, 无敌帧, dodge, Maxsu, doodlum]
aliases: [无敌帧生成, 闪避无敌帧, MaxsuIFrame]
source: https://www.nexusmods.com/skyrimspecialedition/mods/74401
summary: Maxsu 的无敌帧框架：在动画注释里声明无敌帧，免脚本不改行为图；DMCO 硬前置、TK Dodge RE 可选。
---

# IFrame Generator RE——动画无敌帧框架

## 一句话

官方描述原文："A framework that allow modders to generates invincibility frames for their animations in a script-free way"——作者在动画文件里用注释声明无敌帧，**不改行为图、免脚本**。

## 基本事实

- **作者是 Maxsu（maxsu2017），不是 Sokkvabekk**【一手源】。
- 原版 [mods/74401](https://www.nexusmods.com/skyrimspecialedition/mods/74401) v1.03（2022-09，停更）；**AE 版 [mods/82737](https://www.nexusmods.com/skyrimspecialedition/mods/82737) 由 doodlum 维护**（源码 doodlum/MaxsuIFrame-ng，v1.03.1，明确 "Only compatible with AE"，2026-08-25 页面更新）【一手源】。
- 独立框架，**不依赖 TK Dodge**；反向关系是 TK Dodge RE 把它列为可选前置（要闪避无敌帧时装）、DMCO 新版把它列为必需。

## 给玩家的定位（官方原话）

> "The only thing you need to know about is that you had install some animations mods that require this mod… So all you need to do is download and install this mod."

即：某 mod 的 Requirements 写了它，装；没写，不用管。要求 SKSE + Address Library。
