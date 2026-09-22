---
id: oar-dar
title: OAR / DAR 是什么，与动作引擎的关系
category: 05-ecosystem
kind: concept
version: 1.0.0
updated: 2026-09-21
tags: [OAR, DAR, 替换器, 条件动画, 生态]
aliases: [OAR 和动作引擎关系, DAR 是什么, OAR DAR 区别, 替换型动画, 需要刷补丁吗]
source: https://forums.nexusmods.com/topic/13497416-open-animation-replacer-a-pose/
summary: Open/Dynamic Animation Replacer 是"按条件替换已有动画"的 SKSE 插件，与补丁器互补而非替代；Pandora 官方点名 OAR 接替了 PCEA/Sexy Move。
---

# OAR / DAR 是什么，与动作引擎的关系

## 定义

- **DAR**（Dynamic Animation Replacer）与 **OAR**（Open Animation Replacer）：都是 SKSE 插件，做同一件事——**在"已有动画命令"被触发时，按条件改播另一个 hkx 文件**。
- 二者的哲学差异（中文社区总结）：DAR 在周年纪念版时代更新滞后、兼容出问题；**OAR 正是在此背景下诞生**，目标是取代 DAR，兼容 DAR 的动画，扩展性更强且**开源**，更可能被社区持续维护。

## 与补丁器的分工（务必分清）

| | FNIS / Nemesis / Pandora | DAR / OAR |
| --- | --- | --- |
| 类型 | 补丁器（Patcher） | 替换器（Replacer） |
| 工作 | **新增**动画命令 / 更新动画数据库 | 对**已有**命令按条件改播别的文件 |
| 是否需要对方 | 不需要 | 需要命令已存在（原版或补丁器新增） |
| 运行时机 | 每次改动动画 mod 后刷一次 | 装好即生效，运行时判断 |

一句话：**OAR 不是"另一个动作引擎"，它不替代 FNIS/Nemesis/Pandora。** 详见 [Patcher 与 Replacer 的区别](../01-principles/patcher-vs-replacer.md)。

## Pandora 官方对 OAR 的定位

Pandora 官方对比表有一句关键脚注：

> Pandora does not support FNIS/Nemesis features for which a modern alternative exists, e.g **Sexy Move, PCEA replaced by OAR** and baked motion data obsolete by AMR.
> （Pandora 不支持那些已有现代替代方案的 FNIS/Nemesis 特性，例如 Sexy Move、PCEA——已被 **OAR** 取代；baked motion data——已被 **AMR** 取代。）

含义：像 **PCEA**（PC Exclusive Animation Path，按角色分配动画）这类老功能，Pandora **有意不做**，因为 **OAR 的条件系统是更好的现代替代**。

> 来源：Pandora 官方 Wiki https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/wiki

## 一个常见误判

有玩家把"装了 OAR 动画包却不加载"归咎于换了 Pandora。实际排查下来，问题多在 OAR 侧：动画包条件写错、文件冲突，或 OAR 未能读到动画包（需打相关修复补丁）。**OAR 的问题优先查 OAR 日志**（`Documents\My Games\Skyrim Special Edition\SKSE\OpenAnimationReplacer.log` 一类）。

> 社区案例：Nexus 论坛 https://forums.nexusmods.com/topic/13497416-open-animation-replacer-a-pose/

## 与本工作区其他资料的关系

本工作区有 OAR 的独立资料库 `oar-kb/`，讲解**条件写法、目录结构、替换心智模型**。若你要写 OAR 条件或按阶段拆分动画，请转去 [实战](../../oar-kb/08-practices/)；本文只负责"OAR 在生态中的位置"。

## 相关

- [Patcher 与 Replacer 的区别](../01-principles/patcher-vs-replacer.md)
- [AMR 动画运动革命](amr.md)
- [相关工具链](related-tools.md)
