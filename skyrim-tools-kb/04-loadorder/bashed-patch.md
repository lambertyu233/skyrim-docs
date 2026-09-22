---
id: bashed-patch
title: Bash Patch（Wrye Bash 的记录合并）
category: 04-loadorder
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [冲突解决, Wrye Bash, leveled list, 自动补丁]
aliases: [Bash Patch, bashed patch, 巴什补丁, leveled list 合并, 战利品列表合并, bash tag]
source: http://wrye-bash.github.io/docs/Wrye%20Bash%20General%20Readme.html
summary: Wrye Bash 的自动化记录合并：把多个插件对 leveled list、NPC 面容等「可合并记录」的改动汇总进一个补丁，避免后加载者全胜。
---

# Bash Patch

## 它解决的具体问题

有些记录冲突是**可以机械合并**的。最典型的是 **Leveled List（分级列表）**——
决定"这个宝箱里可能开出什么""这个怪会穿什么"。

两个 mod 都给强盗加战利品，按唯一规则只有后加载者的版本生效，
**先加载那个 mod 的物品就消失了**。Bash Patch 会把两边的条目**并起来**。

它是 MOD 生态里少数"自动解决记录级冲突"的工具——比手工在 xEdit 里逐条复制快得多。

## Bash Tag：它怎么知道该合并什么

LOOT 会给每个插件输出 **Bash Tag 建议**（如 `Relev`、`Delev`、`Stats`、`Names` 等），
Wrye Bash 读取这些标记，决定对哪些记录执行哪种合并操作。
这一层是"为什么 LOOT 与 Wrye Bash 要一起用"的原因。

## 与其他冲突工具的定位

| 工具 | 处理方式 | 适用 |
|---|---|---|
| **手工 xEdit 补丁** | 人决定每条记录的最终值 | 精准、个案、可控 |
| **Bash Patch** | 机械合并"可合并记录"（leveled list 等） | 大批量、规则明确 |
| **Synthesis** | 代码化补丁，覆盖更广（NPC、法术、perk…） | 自动化、可重跑 |

三者**可以共存**，社区常见工作流是 Bash Patch 打底、Synthesis 处理更复杂的逻辑、
个别疑难手工在 xEdit 里做。

## 操作要点

1. **必须从 mod 管理器启动 Wrye Bash**（MO2 下否则看不到虚拟文件系统）。
2. 打之前**先跑 LOOT**——Bash Tag 是它的输出。
3. Bash Patch **是产物**：改动 modlist 后要**重建**，不要当成一次性设置。
4. Bash Patch 插件应排在**加载顺序较后**的位置（让它的覆盖生效），
   具体位置与其它补丁工具的先后关系需按你的 modlist 顺序安排。

## 相关

- [Wrye Bash（管理器 + Bash Patch）](../03-managers/wrye-bash.md)（Wrye Bash 本体）
- [LOOT（插件排序）](../04-loadorder/loot.md)（Bash Tag 的来源）
- [Synthesis（自动化补丁管线）](../04-loadorder/synthesis.md)（覆盖范围更广的自动化替代/补充）
- [xEdit / SSEEdit（记录编辑器与冲突检测）](../04-loadorder/xedit.md)（手工个案）
