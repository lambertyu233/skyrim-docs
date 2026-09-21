---
id: animation-log-and-debugging
title: 动画日志、事件日志与 trace
category: 05-editor
kind: guide
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 日志, 调试, trace, 排错]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: 动画日志是屏幕右上角的 overlay，实时显示最近激活/被打断的动画剪辑与来源；关掉 UI 后仍留在屏幕上；3.0.0 起还有 show trace，能列出最终选中动画前的条件求值顺序。
---

# 动画日志、事件日志与 trace

## 动画日志（Animation Log）

官方原文：

> 有没有想过**刚才播的是哪个动画**？有没有想过**它是从哪来的**？我加动画日志就是为了这个目的。
> 点主 UI 里的按钮即可开启。你可以**关掉 UI，而动画日志会继续留在屏幕上**，陪你游玩。
> 可以在设置菜单里**自定义要记录哪些动画**。有些事件（比如缓慢转鼠标产生的动画回声）会非常刷屏。
> 也可以在设置里**启用写入 SKSE 日志文件**，方便事后分析。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

**它是 overlay，不是窗口**：显示在屏幕**右上角**，列出最近激活/被打断的动画剪辑。0.8.0 开发日志对它的描述是"**一个显示在屏幕右上角的调试 overlay**"。

> 来源：<https://bakemono.app/p/patreon/25643772/81916525>

### 使用前提

**必须先选中求值目标**（控制台点角色，或在 OAR UI 里输 FormID），否则日志区块不会指向任何对象。社区教程原话：

> 只要你控制台有正确选取人物，log 区块应该会像我这样**即时告诉你现在角色用的是哪些动作**（超级方便）。

> 来源：<https://forum.gamer.com.tw/Co.php?bsn=2526&sn=154942>

### 它能回答什么

| 想看什么 | 怎么看 |
| --- | --- |
| 现在播的是哪个动画、来自哪个 mod / 哪个 `.hkx` | 直接读日志（含动作目录、模组名、文件名） |
| 某个状态的动画到底走哪条路径 | 在游戏里"演"一遍那个状态，看日志刷出什么 |
| 我认定的那个 submod 有没有被扫描到 | 看日志里有没有出现它对应的原始动画路径 |

**实战用法**（社区工作流的共同套路）：**开日志 → 做动作 → 记下刷出来的文件夹名/编号 → 回编辑器按名字筛选**。

> 来源（巴哈姆特）：<https://forum.gamer.com.tw/Co.php?bsn=2526&sn=154942>
> 来源（Gate to Sovngarde 整合文档的同款流程）：<https://gatetosovngarde.wiki.gg/wiki/Animations>

## 动画事件日志（Animation Event Log，自 2.1.0）

> 自 **2.1.0** 起还有一个**动画事件日志**。它**主要对行为（behavior）modder 有用**，会列出被跟踪引用上发生的**所有动画事件**。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

用途：配合 [函数系统](../04-functions/functions-and-events.md)——你想确认动画里的 `OAR.xxx` 注释事件**到底有没有发出来**，这里能直接看到。

## show trace（自 3.0.0）

> 给动画日志加了一个 **"show trace"** 按钮，会显示**所有按求值顺序检查过的条件**，直到最终动画被选中。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（3.0.0 变更条目）

**这是排查"为什么选中了别人而不是我"的终极工具**——它把 OAR 的决策链摊开给你看。

## SKSE 日志文件位置

```
C:\Users\<用户名>\Documents\My Games\Skyrim Special Edition\SKSE\OpenAnimationReplacer.log
```

同目录下还会有：

- `OpenAnimationReplacer-DetectionPlugin.log`（Detection Plugin 的日志）
- `PairedAnnotationFix.log`（配对动画注释修复插件的日志，作者说"相当啰嗦"）
- （如有异常）崩溃日志由 .NET Script Framework / Crash Logger 提供

> 来源：本工作区实测记录；路径与社区一致（见 <https://forums.nexusmods.com/topic/13497416-open-animation-replacer-a-pose/> 里 scorrp10 的指引）

## 日志能回答的问题（速查）

| 想看什么 | 怎么找 |
| --- | --- |
| 我的 submod 有没有被扫描到 | 搜**被替换的原动画路径**是否出现在日志里 |
| 有没有动画加载失败 | 搜 `fail` / `invalid` / `could not` |
| DAR 旧 mod 被转成了什么 | 搜 `Legacy` |
| 有哪些动画会被动态替换 | 搜 `interruptible`——日志会列出"原始动画 → 会替换" |
| 是不是路径过长导致读不到 | 搜不到任何痕迹时，先按 260 字符上限自查 |

> 来源：本工作区实测记录 `OAR/OAR-补充文档.md`。

## 一条经验

> **建议**：改完一次就**跑一次游戏再看日志**，比反复猜快得多。日志是唯一能区分「配置没加载」和「配置加载了但条件没命中」的手段。

> 来源：本工作区实测记录 `OAR/OAR-补充文档.md`。

## 相关

- [游戏内编辑器](in-game-editor.md)
- [排错对照表](troubleshooting.md)
- [替换的心智模型](../08-practices/animation-key-model.md)
