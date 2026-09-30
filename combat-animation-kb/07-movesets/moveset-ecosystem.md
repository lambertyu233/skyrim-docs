---
id: moveset-ecosystem
title: 动作包（moveset）生态格局
category: 07-movesets
kind: concept
version: 1.0.0
updated: 2026-09-30
tags: [moveset, 动作包, 生态, 招式库, MCO, BFCO]
aliases: [动作包推荐, moveset 怎么装, 哪些动作包]
source: https://www.nexusmods.com/skyrimspecialedition/mods/117052
summary: 动作包是"内容"不是框架：MCO 系作者多为西系、BFCO 双支持多为中文作者系；文件名里的 MCO/BFCO/SCAR 字样决定依赖。
---

# 动作包（moveset）生态格局

## 一句话

动作包（moveset）是给 [攻击框架](../00-overview/framework-choice.md) 供"招式库"的**内容**，不是框架本身——换框架要么找对应版本，要么用 [MCO to BFCO Converter](../01-frameworks/mco-to-bfco-converter.md) 转。

## 格局（按官方页核实）【一手源】

| 阵营 | 作者 | 特点 |
|---|---|---|
| MCO 单支持 | Smooth（For Honor）、Edg3lord（Edgemaster）、Verolevi（Vanargand 系） | 西方作者主要绑定 MCO |
| MCO+BFCO 双支持 | Black/black364（ER Katana/Rapier、WoLong）、Achang 团队（Elden Rim） | 中文作者系多双支持或 BFCO 原生 |
| BFCO 原生 | BF001 官方动画、社区 BFCO 转换整合 | BFCO 官方提供 Converter 作为过渡 |

## 文件名怎么读

Nexus 页面标题常写成 `ADXP I MCO I BFCO xxx (SCAR)`——逐段解读：

- **MCO / BFCO**：适配哪个攻击框架（hkx 文件名与注释遵循谁的规范）。
- **SCAR**：附带 [SCAR](../06-ai-camera/scar.md) patch——NPC 才能用这些招式；没打 SCAR patch 的包只对玩家生效。
- **OAR / DAR**：条件替换层（OAR 向后兼容 DAR 包）。

## 装包的通用检查单

1. 确认包的框架与你装的框架一致（不一致先想 Converter）。
2. FOMOD 里按框架选对选项（MCO/BFCO/Pandora）。
3. 装完**重跑 Pandora** 并勾选新增补丁项。
4. 位移类招式确认 [AMR/AMF](../02-foundations/amr-amf.md) 在位。
5. 技能/连招不触发时先查：[Payload Interpreter](../02-foundations/payload-interpreter.md) 与重击键四选一是否就位。
