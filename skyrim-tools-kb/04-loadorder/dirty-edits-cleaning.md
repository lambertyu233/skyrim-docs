---
id: dirty-edits-cleaning
title: 脏编辑与清理（ITM / UDR）
category: 04-loadorder
kind: tutorial
version: 1.0.0
updated: 2026-09-22
tags: [清理, 脏编辑, ITM, UDR, 排错]
aliases: [清理脏编辑, cleaning, identical to master, 删除引用, quick clean, 脏数据]
source: https://tes5edit.github.io/docs/7-mod-cleaning-and-error-checking.html
summary: 什么是 ITM/UDR、为什么它们会坏事、以及「只清官方 master」这条铁律——含 xEdit 现行 Quick Auto Clean 的正确用法。
---

# 脏编辑与清理

## 定义（沿用 Wrye Bash 官方 Readme 的措辞）

- **ITM（Identical To Master）**：插件里某条记录的内容**与 master 完全相同**。
  通常是无意改动。危害在于：它会把"别人对该记录的修改"挡在外面——
  因为按唯一规则，**后加载的（你这个没实质改动的）副本胜出**，
  于是真正想改这条记录的 mod 失效了。
- **UDR（Undeleted and Disabled Reference）**：**被删除的引用**。
  直接删除记录引用是危险的，正确做法是先"取消删除"、再改为 disabled。
  > 官方特意提醒这个缩写常被用反：**UDR 指的是"修好之后"的状态**，
  > 而 "Scan For UDRs" 扫的其实是"被删除的引用"，LOOT 报告的 UDR 数量
  > 也是"可以被修的删除引用数"。

## 铁律：只清官方 master

**该清的**：`Update.esm`、`Dawnguard.esm`、`HearthFires.esm`、`Dragonborn.esm`
（LOOT 会明确列出它们有 ITM/UDR）。

**不该清的**：第三方 mod 的插件。原因：
它们在别人机器上出现的"ITM"往往是**相对你的 master 顺序**而言的，
清掉可能删掉作者的**有意覆盖**，造成缺件或任务卡死。

> 社区经验：大量"我清了 XX.esp 之后某任务坏了"的帖子，根因都是这一条。

## 现行做法：Quick Auto Clean

1. 把 xEdit 那个 exe **另存/重命名为** `SSEEditQuickAutoClean.exe`，
   或在 MO2 的参数里加 `-quickautoclean`。
2. 启动后**只勾一个**要清的插件（它会自动带上所需 master）。
3. 程序自动执行 **3 轮** `Filter → Undelete and Disable References → Remove ITM`，
   每轮保存，最后输出 **BOSS/LOOT Cleaning Report**。

**注意**：`-quickautoclean` 与 `-quickclean` 的区别是——
前者三轮全自动保存，后者只扫一次并**询问**你是否保存。

## 为什么手动流程被废弃

xEdit 4.0.2 起，"Apply Filter for Cleaning"、"Undelete and Disable References"、
"Remove Identical to Master records" 三个手动函数**点了只弹说明**。
官方立场：Quick Auto Clean 是唯一支持路径。此外还有两个技术原因：

- Quick Clean 现在会**把 group 与主记录标脏**再保存，逐元素写出，
  以避免早年"清 `Dawnguard.esm` 后灵魂石冢部分区域不加载"的老 bug。
- 因此 **Quick Clean 的产物 CRC 与旧手动流程不同**——这不是错误。

## 清理之外：还有一类"看起来像脏"的东西不是脏

- **有意的覆盖**：作者故意写一份与 master 相同的记录来"锁死"某个值，防止被别的 mod 改。
- **navmesh 的假 ITM**：CK 会打乱 edge link 表的索引顺序；
  新版 xEdit 改成按**三角形坐标**比较顶点，能识别出多得多的真 ITM——
  所以"清完之后 LOOT 报的 ITM 数反而变多"在新旧工具混用时是可能的。

## 相关

- [xEdit / SSEEdit（记录编辑器与冲突检测）](../04-loadorder/xedit.md)（工具本身与命令行）
- [LOOT（插件排序）](../04-loadorder/loot.md)（谁在报 ITM/UDR 数量）
- [Wrye Bash（管理器 + Bash Patch）](../03-managers/wrye-bash.md)（官方术语定义出处）
- [常见错误认知](../12-sources/common-misconceptions.md) 第 8 条
