---
id: nemesis-overview
title: Nemesis 概览：第二代动作引擎（模板化 + 开源）
category: 03-nemesis
kind: tool
version: 1.0.0
updated: 2026-09-21
tags: [Nemesis, 复仇女神, Shikyo Kira, 概览, 开源]
aliases: [Nemesis 是什么, 第二代动作引擎, nemesis unlimited behavior engine, Nemesis 怎么装, Nemesis 是干嘛的]
source: https://www.nexusmods.com/skyrimspecialedition/mods/60033
summary: Nemesis（Project New Reign，作者 Shikyo Kira，2019）开源、向后兼容 FNIS，用模板机制让社区自定义动画类型，但更新不活跃、文档缺失。
---

# Nemesis 概览：第二代动作引擎（模板化 + 开源）

## 基本信息

| 项 | 值 |
| --- | --- |
| 全称 | Project New Reign - Nemesis Unlimited Behavior Engine |
| 作者 | **Shikyo Kira**（Nexus 用户名 shikyokira） |
| Nexus | https://www.nexusmods.com/skyrimspecialedition/mods/60033 |
| 源码 | https://github.com/ShikyoKira/Project-New-Reign---Nemesis-Main |
| 出现 | 2019 |
| 支持 | Skyrim SE / AE（无 LE 官方支持，无 MacOS） |
| 开源 | **Open Source (GPLv3)** |
| 打补丁方式 | **Imperative（命令式）** |
| 状态 | 仍可用，但**更新不活跃**、**文档缺失** |

## 官方自我定位

> Your all in 1 skyrim behavior framework. Automated behavior modification extraction, behavior patching and more. Currently still in beta stage.
> （你的一站式天际行为框架。自动化行为修改提取、行为补丁修复等。目前仍处于 beta 阶段。）

**它能做什么（官方列表）：**

- 自动化行为修改提取
- 自动化行为补丁修复（利用上述提取功能）
- 根据行为模板生成新的自定义行为
- 支持自定义行为 / 自定义动画类型
- 支持 Python 脚本
- 从基础到高级的行为冲突解决
- 清晰的错误调试系统，若出错会提供相应解决方法

**不兼容（官方明列）：**

- FNIS
- FNIS PCEA

> 来源：Nemesis Nexus 描述页 https://www.nexusmods.com/skyrimspecialedition/mods/60033

## 基础用法（官方步骤）

1. 像装 mod 一样下载安装该工具。
2. 进入 `data/nemesis_engine`，运行 `Nemesis Unlimited Behavior Engine.exe`。
3. 勾选你要打补丁的 mod。
4. 如有必要，**拖动调整优先级**。
5. 选择 **Launch Nemesis Behavior Engine**。
   - 若提示更新引擎，选 **Update Engine**；没提示就不用更新。
   - 勾选/取消勾选 mod **不影响引擎版本**。
6. 完成后关闭 Nemesis。
7. 启动天际。

## 关键设计：模板机制（相比 FNIS 的最大进步）

Nemesis 允许任何人制作并上传**行为模板 / 动画模板**，由社区自行扩展新动画类型——不再需要等作者更新工具。作者本人 2019 年说明（社区转录）：

> Nemesis 自带所有既有动画类型（b、s、so、km…），并可接受自定义行为模板——mod 作者能创建的动画类型**不受限制**，与 FNIS 的硬编码不同。每个用户的 Nemesis 有**自己的引擎版本**；装了带 Nemesis 提取文件的 mod 后会提示"更新引擎"（< 1 分钟），无需等作者发布新工具。

> 转引自社区转录 https://ik63.ru/nemesis-unlimited-behavior-engine-ne-rabotaet

## 迁移与共存

- Nemesis **向后兼容绝大多数 FNIS mod**（官方对比表：Almost all FNIS Mods）。
- 但**不能与 FNIS 同时生效**；从 FNIS 迁移需干净卸载，并注意 FNIS 改写过的 hkx。
- 想用 Pandora 时，Nemesis 的补丁格式 Pandora 全兼容，迁移成本低。

## 相关

- [Nemesis 复杂度分级](nemesis-complexity-tiers.md)
- [Nemesis 的局限](nemesis-limitations.md)
- [官方三引擎对比表](../00-overview/engine-comparison.md)
