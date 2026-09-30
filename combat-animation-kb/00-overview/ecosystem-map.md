---
id: ecosystem-map
title: 动作系统五层生态地图
category: 00-overview
kind: concept
version: 1.0.0
updated: 2026-09-30
tags: [生态, 总览, 分层, 动作系统, 战斗]
aliases: [combat ecosystem, 动作系统全景, 战斗系统有哪些部分, 动作mod怎么分层, 该装哪些动作mod]
source: https://www.nexusmods.com/skyrimspecialedition/mods/117052
summary: 老滚5 动作系统从下到上分五层——行为引擎、运行时插件、攻击框架、配套子系统、动作包——各层分工与代表 mod。
---

# 动作系统五层生态地图

## 一句话

原版天际的战斗是"引擎层就写死的"，所有动作 mod 都是往这五层里各自插一层东西。**搞不清自己装的东西在哪一层，是兼容性事故的第一大来源。**

## 五层结构

| 层 | 干什么 | 代表 mod | 详见 |
|---|---|---|---|
| ① 行为引擎（补丁器） | 往动画数据库里新增动画命令/事件，生成 behavior 补丁 | **Pandora**（现役）、Nemesis（停更）、FNIS（淘汰） | [behaviour-engine-kb/00-overview/engine-comparison.md](../../behaviour-engine-kb/00-overview/engine-comparison.md) |
| ② 运行时插件（SKSE 框架） | 替换/解释/注入动画数据 | **OAR**（替换）、Payload Interpreter（读注释）、BDI（注入变量）、AMR/AMF（位移修正） | 本库 `02-foundations` |
| ③ 攻击动作框架 | 重写攻击行为逻辑（连招、蓄力、位移攻击） | **BFCO**（现役）、MCO（终版 1.6.0.6）、SkySA/ABR（淘汰） | 本库 `01-frameworks` |
| ④ 配套子系统 | 闪避、韧性/硬直、格挡/弹反、AI、碰撞、视角 | DMCO、MaxsuPoise、Elden Parry、SCAR、Precision、TDM | 本库 `03`–`06` |
| ⑤ 动作包（moveset） | 给框架喂"招式库"内容 | Elden Rim、For Honor in Skyrim、ER Katana 等 | 本库 `07-movesets` |

## 依赖方向

- **④③ 依赖 ①②**：攻击框架和大部分子系统要求先跑 Pandora/Nemesis 打补丁，再由 SKSE 插件在运行时接管。
- **⑤ 依赖 ③**：动作包的 hkx 文件名和注释（annotation）必须匹配框架的命名规范——MCO 动作包认 `mco_*`，BFCO 认 `BFCO_*`，所以有 [MCO to BFCO Converter](../01-frameworks/mco-to-bfco-converter.md)。
- **③ 互斥**：SkySA/ABR、MCO、BFCO 互相**不兼容**，三选一（见 [攻击框架选型](./framework-choice.md)）。

## 新手最常见的翻车点

装完动作包**必须重跑一次 Pandora**（在 Pandora 界面勾选对应 mod 的补丁项后 Launch），否则新增的动画命令不存在，表现为攻击无效、大字 T-Pose。机制解释见 [behaviour-engine-kb/01-principles/behaviour-patcher.md](../../behaviour-engine-kb/01-principles/behaviour-patcher.md)；OAR/DAR 与补丁器是互补而非竞争关系，见 [behaviour-engine-kb/01-principles/patcher-vs-replacer.md](../../behaviour-engine-kb/01-principles/patcher-vs-replacer.md)。

## 出处

- 分层与依赖关系：综合各框架官方 Nexus description 的 Requirements 区块（BFCO、MCO、DMCO、TK Dodge Redux 等）【一手源】。
