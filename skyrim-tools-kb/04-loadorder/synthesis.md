---
id: synthesis
title: Synthesis（自动化补丁管线）
category: 04-loadorder
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [冲突解决, 自动化, 补丁, C#, Mutagen, 生成器]
aliases: [patcher, 自动补丁, 代码补丁, zEdit 替代, 33996]
source: https://github.com/Mutagen-Modding/Synthesis
summary: 用 C# 补丁程序（patcher）代替手工改记录：读你的完整 modlist，输出一个针对你这套配置生成的补丁插件——改一次 modlist 就重跑一次。
---

# Synthesis

## 定位

一个**补丁管线 + GUI**（官方描述：*"Framework and GUI to empower people to create mods via code
instead of by hand"*）。你挑选若干 **patcher**（每个都是一个小 C# 程序 + 自己的设置），
Synthesis 把它们跑在你的完整加载顺序上，输出**合并后的一个补丁插件**。

它建立在 **Mutagen** 之上——读写成千上万条 Bethesda 记录类型的 .NET 库，
也是"写自己的 patcher 很现实"的原因。

## 为什么值得用它（而不是手工 xEdit）

关键差别是**产物可重建**：

- 手工补丁记录的是**别人当时的 modlist**；
- Synthesis 的输出记录的是**你当前的 modlist**，加了一个 mod 之后**重跑一分钟**就行，
  不必去找"有没有人发布这个组合的补丁"。

典型 patcher 能干的事：把物品铺进所有相关 leveled list、
给一批 NPC 统一改名/加 perks、把装备批量换身形、
生成 NPC 面容补丁、按标签给 NPC 分配服装、按规则整体调整敌人数值……

## 对比表（社区与官方材料口径）

| 对手 | 差别 |
|---|---|
| xEdit 的 Pascal 脚本 | 语言老旧、文档稀少；Synthesis 用 C#，有类型检查、自动补全与整个 .NET 生态 |
| zEdit 的 JS autopatcher | 两套生态各有独占补丁；zEdit 开发已停滞（见 [zEdit / zMerge（插件合并，已停滞）](../04-loadorder/zedit-zmerge.md)） |
| 手工 xEdit 补丁 | 一次性任务更快；**反复重建**的任务 Synthesis 胜出 |

## 使用流程（社区整理 + 官方 wiki）

1. 解压到游戏目录**之外**的独立文件夹（放 `Program Files` 会出权限问题）。
2. 把 `Synthesis.exe` 加进 mod 管理器的可执行列表，**从管理器启动**——
   否则它读不到你实际的 modlist。
3. 在 Repository Browser 里挑 patcher、设参数（首次运行会编译，**很慢**；之后复用构建）。
4. 按 Run，输出落到 `Output/`。
5. 把输出**作为一个 mod** 启用，并**排在加载顺序最后**（在 LOOT 排完其它插件之后）。
6. **任何影响相关记录的改动之后，都要重跑。**

## 已知限制（诚实列出）

- 需要 .NET 运行时；首次编译可能十几分钟。
- GUI 朴素，复杂配置有时要手工编辑 JSON。
- 第三方 patcher 质量与维护状况参差。
- 输出可能与你手工做过的补丁或整合包自带的补丁**重叠**——要理解整条链路。

## 两个 MO2 相关的坑

- **必须在 MO2 里跑**，并且为了兼容 MO2 的 VFS，官方在实现里做了线程限制
  （release note 里提到 "Pin cores at 2 for Mo2, as threading causes issues inside its VFS"）。
- 输出 mod 建议**每次重建前清空**，避免旧文件残留造成"改了没效果"。

## 相关

- [Bash Patch（Wrye Bash 的记录合并）](../04-loadorder/bashed-patch.md)、[xEdit / SSEEdit（记录编辑器与冲突检测）](../04-loadorder/xedit.md)
- [zEdit / zMerge（插件合并，已停滞）](../04-loadorder/zedit-zmerge.md)（已停滞的同类生态）
- [Mod Organizer 2（工具视角）](../03-managers/mo2-tool.md)（从管理器启动）
