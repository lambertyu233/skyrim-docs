---
id: animation-toolchain-overview
title: 动画与行为工具链总览
category: 07-behaviour
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [动画, 行为, 索引, 总览, 工具链]
aliases: [动画工具, 动作工具, 行为引擎工具, animation tools, 做动画要什么工具, 动画链]
source: https://github.com/ersh1/OpenAnimationReplacer
summary: 动画相关工具的「两族四层」心智模型，并给出本工作区三个相关库的读法——本条目只做索引，不重复正文。
---

# 动画与行为工具链总览

动画改造是 Skyrim 里工具链最绕的一块。**本条目只给地图**——
真正的机制与排错在 `behaviour-engine-kb` 与 `oar-kb` 里。

## 两族：Patcher vs Replacer

这是理解全套工具的第一刀：

| | **Patcher（补丁器）** | **Replacer（替换器）** |
|---|---|---|
| 做什么 | 向行为引擎**新增**动画（往动画数据库里加事件） | **替换**已有动画（同一个事件名换一个文件） |
| 代表 | FNIS、Nemesis、Pandora | OAR、DAR |
| 产物 | 重写后的 `behaviors\*.hkx` | 你自己的 mod 目录 + 条件配置 |
| 谁在用 | 动画包作者（大量新动作必需） | 玩家与轻量改造者 |

> 关键结论：**两者不是二选一，而是分工**。想让游戏"多出"一个动作，
> 必须有 Patcher；只想换掉"原有"动作，Replacer 就够。

## 四层

1. **行为引擎层**：FNIS / Nemesis / Pandora——重写行为文件，注册新动画事件。
   → `behaviour-engine-kb`（28 条）
2. **替换层**：OAR（现行）/ DAR（旧）。
   → `oar-kb`（33 条，含 125 个条件名、`config.json` 字段、编辑器调试）
3. **文件层**：`.hkx` 动画与行为文件本身——改名、挪位置、转换 LE/SE。
   → 本库 [hkx 文件工具（动画与行为文件）](../07-behaviour/hkx-tools.md)
4. **补充插件层**：修动画相关的引擎行为（队列、配对动画等）。
   散见本库 `09-diagnostics/`，以及各动画 mod 自己的说明。

## 最容易搞错的四件事

1. **文件名 = 目标状态下游戏请求的原始文件名**。换了没效果，**先查文件名，再查条件**。
2. **`.hkx` 内容不用改**，改名 + 挪位置就能生效（替换类）。
3. **旧的 DAR 目录必须移出 `meshes\`**，否则与 OAR 双份生效。
4. **判"弓已拉开"必须用 `AttackState`，不能用 `IsAttacking`**——
   整段弓攻击里 `IsAttacking` 都为真。

## 相关库

| 主题 | 库 |
|---|---|
| FNIS / Nemesis / Pandora 原理、安装、排错 | `behaviour-engine-kb` |
| OAR 条件全清单、submod、优先级、游戏内编辑器 | `oar-kb` |
| 改造别人动画包的六步方法论 | [实战](../../oar-kb/08-practices/) |
| 动画文件的改名/转换工具 | 本库 [hkx 文件工具（动画与行为文件）](../07-behaviour/hkx-tools.md) |
