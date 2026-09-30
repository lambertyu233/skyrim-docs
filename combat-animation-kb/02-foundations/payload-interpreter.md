---
id: payload-interpreter
title: Payload Interpreter——动画注释解释器
category: 02-foundations
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [Payload Interpreter, 注释, annotation, dTry, PIE]
aliases: [payload, 注释解释器, PIE 事件, 动画指令, D7ry]
source: https://github.com/D7ry/PayloadInterpreter
summary: dTry 的 SKSE 插件：把动画 payload 注释在触发瞬间翻译成指令（施法/粒子/存变量等），现代动作包的地基之一。
---

# Payload Interpreter——动画注释解释器

## 一句话

把动画标注（annotation）里"无意义"的 payload 字符串翻译成指令并在该标注触发瞬间执行——作者原话 "it works just like python, but for Skyrim animations"。

## 基本事实【一手源】

- GitHub：[D7ry/PayloadInterpreter](https://github.com/D7ry/PayloadInterpreter)（Nexus 署名 dTry），Nexus 页 [mods/65089](https://www.nexusmods.com/skyrimspecialedition/mods/65089)。
- 最新 **v1.0.1（2023-06-02）**：借助 clib-ng 支持所有天际版本（含 VR），明确支持 1.6.640。
- v1.0.1 changelog：自带一个 Nemesis 补丁，注入无害的虚拟事件 **PIE** 作为宿主——"from now on, the only animation event whose payload will get interpreted will be 'PIE'"。
- 指令示例：`weaponSwing.@CAST|0x12FD0|Skyrim.esm|...`（挥剑瞬间施法）、`@SETGHOST`、`@PLAYPARTICLE`、`@SGVB/F/I` 等；支持 ini 自定义指令（`$` 开头）。

## 依赖与现状

- Nexus Requirements：Address Library、**Project New Reign - Nemesis（需运行其行为补丁）**、VC++ 2022【一手源】。
- **dTry 本人不更新了**：doodlum 的 dTry Plugin Updates 页原话 "dTry is too busy at the moment to update his plugins"【一手源】。
- 与 Pandora 的搭配：社区构建（Schaken Mods / Nexus 190740 等）让 DLL 适配 1.6.1170+ 并兼容 Pandora 环境【社区经验】；或用 BDI 附带的 "Payload Interpreter - Nemesis Less Patch" 配置免装 Nemesis 补丁【一手源，BDI 文件页说明】。

## 谁在用它

MCO 把它列为硬性前置；BFCO 3.100 系动作包注释也大量走 PIE 宿主（`BFCO_NextIsAttack1` 等派生注释）；Elden Counter 依赖它。相关：[Key Utils 与 DMK](./key-utils-and-dmk.md)。
