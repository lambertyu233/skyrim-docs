---
id: more-informative-console
title: More Informative Console
category: 09-diagnostics
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [诊断, 控制台, 反查, 排错, 工具]
aliases: [More Informative Console, MIC, 控制台增强, 反查来源, 看物品来自哪个mod, 19250]
source: https://www.nexusmods.com/skyrimspecialedition/mods/19250
summary: 点开控制台就告诉你「这个对象/物品来自哪个 mod、被谁最后修改过」——把 xEdit 里的反查搬进游戏内，排查「这个东西哪来的」的最快路径。
---

# More Informative Console

Nexus：`skyrimspecialedition/mods/19250`。

## 它解决的问题

原版控制台点一个对象只给 BaseID / RefID 之类的裸信息。
要搞清楚"这件装备是哪来的""这个 NPC 是谁最后改的"，
传统做法是拿 FormID 回 xEdit 里去翻。

More Informative Console 把这段搬进游戏内：**点一下就能看到
对象所属的插件、以及最后修改它的插件**。

## 典型用法

| 场景 | 怎么用 |
|---|---|
| 某物品/装备看起来不对 | 点开它，看生效的插件是不是你预期的那个 → 不是就是覆盖顺序问题（[Mod Organizer 2（工具视角）](../03-managers/mo2-tool.md)） |
| 某个 NPC 外貌/数值异常 | 看最后修改者是谁，再回 xEdit 查记录 |
| 排查"某 mod 到底有没有生效" | 点一个它本该改动的东西，看插件归属 |
| 配合 SPID 排错 | 确认分发是否真的应用到了目标 NPC（[Spell Perk Item Distributor (SPID)](../02-distribution/spid.md)） |

## 为什么它在诊断链里很好用

崩溃日志回答"**崩在哪**"，这个工具回答"**眼前这个东西是谁做的**"。
两者结合，能把"行为诡异但不崩溃"这类最难查的问题压缩到几分钟。

## 注意

- 它是 SKSE 插件，需要 SKSE 系前置；版本要匹配运行时。
- 与其它控制台类插件（如 `ConsoleUtilSSE`，[ConsoleUtilSSE](../01-frameworks/consoleutil.md)）**用途不同**：
  后者是给**脚本**用控制台的能力，前者是给**人**看的界面增强。

## 相关

- [xEdit / SSEEdit（记录编辑器与冲突检测）](../04-loadorder/xedit.md)（更深入的反查）
- [Crash Log Analyzer（崩溃日志解读）](../09-diagnostics/crash-log-analyzer.md)
- [Mod Organizer 2（工具视角）](../03-managers/mo2-tool.md)（覆盖与优先级）
- [排错索引：从症状找答案](../../01-navigation/troubleshooting-index.md)
