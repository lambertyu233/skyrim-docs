---
id: community-sources
title: 社区来源清单
category: 09-sources
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 来源, 社区, 论坛, 教程]
aliases: [OAR 社区来源, 论坛在哪, community sources]
source: https://forums.nexusmods.com/topic/13487504-for-animations-what-is-the-difference-between-fnisnemesis-and-oar/
summary: 官方没写的部分散在 Nexus 论坛（scorrp10 的经典解释）、巴哈姆特两篇中文教程、LoversLab 的条件嵌套踩坑帖、整合文档里；本页按可信度分级列出。
---

# 社区来源清单

> **使用纪律**：本页内容一律属**社区口径**，与官方描述分开引用。社区帖的价值在于补官方没写的操作细节；其风险在于"某个整合/某个版本下的现象被当成通则"。引用时请写清上下文。

## A 级：可复现、与官方口径一致

### 1. Nexus 论坛 — scorrp10 的划时代解释

**为什么 A 级**：他把"补丁器 vs 替换器"讲得比官方描述还清楚，而且用具体例子（`ChairIdle` → `chair_idlebasevar1.hkx`、`"7GOM34"` → `GomaPeroPero1\7GOM34.hkx`）。本库 [Replacer 与 Patcher 的分工](../00-overview/replacer-vs-patcher.md) 直接引用。

- **帖 1**：<https://forums.nexusmods.com/topic/13487504-for-animations-what-is-the-difference-between-fnisnemesis-and-oar/>（2024-05）
- **帖 2**：<https://forums.nexusmods.com/topic/13497416-open-animation-replacer-a-pose/>（2024-08 起，2024-12-30 scorrp10 的长回复）

**他给出的核心区分**（原文要点）：

> FNIS/Nemesis 是**往游戏里添加全新动画事件**的工具——你的脚本里写了 `Debug.SendAnimationEvent(actor, "AnimationEventName")`，数据库里就必须存在这个字符串键。
> DAR/OAR 则是在条件满足时，把**已有**动画事件**重定向**到另一个 hkx 文件。

**同帖里可复用的两条排查指引**：

- 排查 OAR 问题时看 `Documents\My Games\Skyrim Special Edition\SKSE` 下的 OAR 日志；
- OAR 替换不工作，**大概率是某些 mod 的条件写坏了或存在冲突**，而不是补丁器的问题。

### 2. Nexus 论坛 — 预览按钮的前置条件（社区独有的发现）

同一个帖 1 里，一位玩家分享了他**在官方文档和教程里都找不到**的答案：

> 教程和帖子里都说可以预览动画，但我一直调不出预览按钮……昨天我才发现，**要让预览按钮出现，你必须先把自己选为目标（`prid 14`）**。

**为什么 A 级**：具体、可复现、官方描述**确实没写**，且与官方"选中求值目标后条件才显示图标与当前值"的机制一致。

### 3. Nexus 论坛 — 对话 idle 的完整实现链路

- **帖**：<https://forums.nexusmods.com/topic/13506665-need-answer-with-oar-how-it-actually-works/>（2025-01）

把"CK 里能选的 idle 名 → 行为文件里的动画事件 → 具体 hkx 路径"这条链路讲通了，并示范了走 OAR 与走补丁器两条路的区别。本库整理在 [替换的心智模型](../08-practices/animation-key-model.md#二怎么查游戏到底请求哪个文件名)。

### 4. 巴哈姆特 — 两篇中文实操教程（质量意外地高）

| 教程 | 链接 | 讲什么 |
| --- | --- | --- |
| 《OAR的簡單應用 - 以高跟鞋閒置動畫為例》 | <https://forum.gamer.com.tw/Co.php?bsn=2526&sn=154942> | **User 模式 + 条件分流 + Animation Log 调试**的完整流程，含"必须保存"等界面细节 |
| 《OAR的簡單應用 - 武器or動作關鍵字替換》 | <https://m.gamer.com.tw/forum/C.php?bsn=2526&snA=45432> | 给特定武器绑特定动作；**演示了"必须在原有 OR 内加条件"** |

**为什么 A 级**：

- 截图全、步骤细、有按键与菜单名的实测记录；
- 与官方口径**互相印证**（User 模式写 user.json、Legacy 归 DAR、Animation Log 是 overlay）；
- 补充了官方没写的 UI 约定（橙色 `*` 表示未保存、`(User)` 标记、`Not Found` / `?????` 的含义）。

本库整理在 [编辑器条件分流](../08-practices/editor-workflow-idle.md) 与 [给特定武器绑特定动作](../08-practices/editor-workflow-weapon.md)。

### 5. LoversLab — 条件嵌套的经典踩坑帖

- **帖**：<https://www.loverslab.com/topic/245858-how-to-have-both-follower-and-pc-play-idle-animations-with-oar-conditions>（2025-02）

**为什么 A 级**：它直接给出了"**父条件必须是 OR，所有选项都挂在 OR 下面**"这条规律，并附带一份**真实的 `config.json` 样本**（含 `priority`、`replaceOnLoop`、`negated`、`editorID` 等字段）。本库 [容器条件](../03-conditions/condition-containers.md) 与 [`config.json`](../02-structure/config-and-priority.md) 都引用了它。

**注意帖子的局限**：楼主最终**没能在 OAR 条件层面解决**，而是绕道把 idle 放进另一个 mod 的 `basicidle` 文件夹。所以**只采信它的"条件结构规律"，不要采信它的结论**（"OAR 做不到"）。

## B 级：有用但需注意上下文

### 6. LoversLab — "改个名就能当 idle 用"

- **帖**：<https://www.loverslab.com/topic/229457-making-an-idle-animation>（2024-04）

多人确认：如果动画已是 `.hkx`，**改名为 `mt_idle.hkx` 放到对应目录**即可。

**上下文警告**：这条**只在文件名本来就是游戏请求的那个时才成立**（且帖里也有人提醒"改完要跑 FNIS/Nemesis"——那是针对新增动画事件的说法，与 OAR 替换的场景不同）。不要读成"文件名随便起"。

### 7. Gate to Sovngarde 整合文档 — 动画排错章节

- **链接**：<https://gatetosovngarde.wiki.gg/wiki/Animations>

**为什么 B 级**：它是**某个整合**的排错文档，很多步骤是整合特有的（列了要删的具体目录，如 `…\OpenAnimationReplacer\Left hand equipment swap`）。但它有几条通用价值：

- **"开 Animation Log → 演动作 → 记下文件夹号 → 回编辑器筛选"** 这套流程；
- **"Major Issue Detected with OAR"** 的成因里包含 **Vortex 部署模式（需 Hardlink + NTFS）** 这一条——这是官方 FAQ 没提的部署侧因素；
- **T-Pose / 动画不播** 的分步处理清单。

**采信方式**：把它的"流程"当参考，把它的"具体文件路径与 mod 名"当整合专属信息。

## C 级：只作线索，需自行验证

| 来源 | 说明 |
| --- | --- |
| 3DM 论坛的 OAR 描述页翻译帖（`bbs.3dmgame.com/thread-6549290-1-1.html`） | 基本是**描述页的中文翻译**，含目录树图示。适合初读，但**版本可能滞后**，关键数值请回官方页核对 |
| Nexcrow / ndangira.net 等 mod 聚合站 | 只做元信息（下载量、版本、日期）。**不要采信它们的"描述"改写** |
| 各类整合的 Discord / 群聊结论 | 无法追溯来源，仅作排查线索 |

## 相关

- [官方来源清单](official-sources.md)
- [不可信来源警示](unreliable-sources.md)
