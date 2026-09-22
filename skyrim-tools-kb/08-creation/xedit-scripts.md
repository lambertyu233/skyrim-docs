---
id: xedit-scripts
title: xEdit 脚本与批量改记录
category: 08-creation
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [脚本, xEdit, 批处理, 自动化, Pascal]
aliases: [xEdit 脚本, Pascal 脚本, 批量改记录, xedit script, 自动化改记录]
source: https://tes5edit.github.io/
summary: 用 xEdit 内建的 Pascal 脚本做批量记录操作——一次性个案的快车道；但反复重建的场景应改用 Synthesis/Mutagen。
---

# xEdit 脚本

## 为什么要有它

手工在 xEdit 里改 5 条记录没问题，改 500 条就会出错。
xEdit 内建脚本语言（Pascal 风格）可以遍历插件、按规则批量改记录——
例如"把某类护甲全部改成某身形""把所有某关键词的装备加个 flag"。

## 适用与不适用

| 场景 | 用 xEdit 脚本 | 用 Synthesis |
|---|---|---|
| 一次性任务 | ✅ 快 | 过重 |
| 每次改 modlist 都要重做 | ✗ | ✅ 可重跑 |
| 逻辑复杂（多记录关联） | ✗ 难写难调 | ✅ C# 有类型与调试器 |
| 只需要改几条 | ✅ | ✗ |

**社区共识**（来自多次讨论的总结）：xEdit 的脚本语言**老旧、文档稀少、
调试体验差**——所以"要不要学它"的答案取决于你是不是只做一次性的事。

## 两个实务要点

1. **脚本是"改"不是"理解"**：先用 xEdit 的冲突视图看清要改什么，
   再写脚本；否则脚本跑完你不知道自己改了什么。
2. **产物用独立插件承载**：让脚本把结果写进一个新 esp，
   而不是就地改原 mod——这样随时可回退，也符合"不改别人 mod"的惯例。

## 与其它自动化手段的分工

```
一次性 + 少量        → 手工 xEdit
一次性 + 大量        → xEdit 脚本
可重跑 + 规则简单    → Bash Patch（leveled list 类）
可重跑 + 规则复杂    → Synthesis（C# / Mutagen）
```

## 相关

- [xEdit / SSEEdit（记录编辑器与冲突检测）](../04-loadorder/xedit.md)（工具本体与命令行）
- [Synthesis（自动化补丁管线）](../04-loadorder/synthesis.md)（现代替代/补充）
- [Bash Patch（Wrye Bash 的记录合并）](../04-loadorder/bashed-patch.md)
- [Papyrus 编译器与反编译](../08-creation/papyrus-compiler-decompiler.md)（注意别把 Pascal 脚本与 Papyrus 混为一谈）
