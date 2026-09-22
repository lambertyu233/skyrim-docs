---
id: xedit
title: xEdit / SSEEdit（记录编辑器与冲突检测）
category: 04-loadorder
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [冲突, 记录编辑, 补丁, 清理, 官方文档]
aliases: [SSEEdit, TES5Edit, 冲突检测, 打补丁, 快速自动清理, quickautoclean, 164]
source: https://tes5edit.github.io/
summary: 模改的核心工作台：把插件里的每条记录展开对比、检测冲突、手写补丁、清理脏编辑——LOOT 排顺序，xEdit 管内容。
---

# xEdit / SSEEdit

同一套程序，按游戏改名为 `SSEEdit.exe`（Skyrim SE）/ `TES5Edit.exe`（LE）/ `FO4Edit.exe`。
分发在 **Nexus（Skyrim SE mods/164）**与 **GitHub（TES5Edit）**。

## 两种启动方式（用 exe 名或命令行参数）

| 模式 | 参数 | 重命名 |
|---|---|---|
| 正常编辑 | `-sse` | `SSEEdit.exe` |
| 快速自动清理 | `-quickautoclean` / `-qac` | `SSEEditQuickAutoClean.exe` |
| 快速清理（单次） | `-quickclean` | `SSEEditQC.exe` |
| 显示冲突 | `-quickshowconflicts` | `SSEEditQuickShowConflicts.exe` |
| 极速显示冲突（跳过模块选择） | `-veryquickshowconflicts` | `SSEEditVQSC.exe` |

其他常用参数：`-IKnowWhatImDoing`（解锁高级功能）、`-D:`（Data 路径）、
`-o:`（输出路径）、`-B:`（备份路径）、`-autoload`（跳过选择窗口，按 `plugins.txt` 全载）、
`-moprofile:`（载入指定 MO2 profile 的加载顺序）、`-autoexit`。
（来源：xEdit `whatsnew.md` 与官方文档）

> **必须从 mod 管理器启动**：直接双击 exe 时 xEdit 看不到 MO2 的虚拟文件系统，
> 等于打开一个空的 Data。见 [Mod Organizer 2（工具视角）](../03-managers/mo2-tool.md)。

## 四大用途

1. **冲突检测**：左侧树按记录类型分组，**红色 = 冲突**。能看到每个插件对同一条记录写了什么值。
2. **手写补丁**：把想要的字段值复制进一个新插件（"copy as override into"），
   生成只含必要覆盖的小 esp——这才是"消解冲突"的正解。
3. **清理脏编辑**：走 **Quick Auto Clean**（见 [脏编辑与清理（ITM / UDR）](../04-loadorder/dirty-edits-cleaning.md)）。
4. **查明真相**：某个物件/数值到底来自哪个插件？打开看记录即可。
   配 More Informative Console 能在游戏内直接反查（[More Informative Console](../09-diagnostics/more-informative-console.md)）。

## 清理机制的重要变更（官方 whatsnew）

- **4.0.2 起，三个手动清理函数被废弃**：
  "Apply Filter for Cleaning"、"Undelete and Disable References"、
  "Remove Identical to Master records" 现在**只弹一条说明**，不再执行。
  官方口径是统一用 Quick Auto Clean。
- `-quickautoclean` 会**重复 3 轮** "Filter → UDR → Remove ITM"，
  每轮自动保存，最后跑一次 **BOSS/LOOT Cleaning Report**。
- Quick Clean 会**自动关掉 "Simple Records"**（以识别最多 ITM）并开启
  "I Know What I'm Doing"（以绕过编辑警告）。
- 一个老 bug 的修复：早年清理 `Dawnguard.esm` 会导致灵魂石冢部分 worldspace 不加载；
  现在 Quick Clean 保存前会把 group 与主记录标脏，强制逐元素写出而非直接拷贝字节——
  **所以 Quick Clean 产出的 CRC 与旧手动流程不同**，这是正常现象。
- 导航网格（navmesh）比较维度改进：三角形顶点按**坐标**而非顶点编号比较，
  能识别多得多的 `NAVM` ITM（需关闭 "Simple Records"）。

## 边界

- **不查正文链接、不做批量资产转换**——它不是 CAO，也不是 NifSkope。
- 手工建新内容（任务、NPC、世界）**用 Creation Kit 更合适**；
  xEdit 擅长改已有记录与做补丁。

## 相关

- [脏编辑与清理（ITM / UDR）](../04-loadorder/dirty-edits-cleaning.md)
- [Synthesis（自动化补丁管线）](../04-loadorder/synthesis.md)（自动化替代品）
- [ESL 化（突破 255 插件上限）](../04-loadorder/esl-flagging.md)（用 xEdit 压缩 FormID 并加 ESL 标记）
- [TES5Edit / xEdit 清理](../../creation-kit-kb/05-tools/tes5edit.md)（CK 库的视角）
