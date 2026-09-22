---
id: zedit-zmerge
title: zEdit / zMerge（插件合并，已停滞）
category: 04-loadorder
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [合并, 插件上限, zEdit, zMerge, 遗留工具]
aliases: [合并插件, merge plugins, 255 上限, 合并工具, mator]
source: https://github.com/z-edit/zedit
summary: 把多个插件合并成一个以突破插件上限的老方案；因为已多年停更、且 ESL 化更安全，现在只应在明确无脚本/无 MCM 的场景下使用。
---

# zEdit / zMerge

## 是什么

- **zEdit**：xEdit 的前端重写（同一套记录编辑内核），加上 **JavaScript** 脚本层与 patcher 框架。
- **zMerge**：zEdit 内置的**插件合并工具**——把若干 `.esp` 合成一个，
  是"碰到 255 上限"的传统答案。

## 现状：请谨慎对待

- zMerge **自 2021 年 8 月起未再更新**；zEdit 最后一个 release 是 **v0.6.7（2022-11-11）**
  （来源：官方 Releases 与社区记录）。
- 官方仓库的措辞是"development has been quiet for some time"，社区对它的共识也是**维护停滞**。

## 合并的真实风险（这是重点）

合并会**改写 FormID**，从而破坏：

- 依赖原插件 FormID 的**脚本**与 **DLL**；
- **MCM** 的注册；
- **facegen**（NPC 面容）与**导航网格**；
- **任务/别名**（quest alias）与对话；
- 依赖原插件的其它补丁（它们指向的插件消失了）。

社区的经验判据：**含脚本、含 MCM、含导航网格、含 facegen、频繁更新、
或者被很多人当前置的 mod，都不要合并。**

## 现代首选：先 ESL 化

在 Skyrim SE/VR 里，**ESL 化比合并安全得多**：保留独立插件、只是不再占常规 255 名额
（额外最多 4096 个）——且合并会把多个插件变成一个难以维护的巨物，
ESL 化则保持每个 mod 可单独更新。见 [ESL 化（突破 255 插件上限）](../04-loadorder/esl-flagging.md)。

> 顺序建议：**先 ESL 化 → 仍不够再考虑合并 → 合并只挑简单的小插件与补丁集合。**

## 如果确实要用

1. **先备份加载顺序**（zMerge 会改写并可能禁用被合并的插件）。
2. 通过 mod 管理器启动 zEdit（否则看不到虚拟文件系统）。
3. 合并产物存成一个**独立的输出 mod**（如 `Merge Output - Patches`），
   而不是写进游戏目录或原 mod 目录——这样随时可回退。
4. **不要在存档用到一半时合并或重建合并**——FormID 变化会打到存档里。
5. 合并后若有 ESLify/压缩 FormID 类工具参与，注意 zMerge 有时会丢 FormLink 映射，
   需要重建合并（社区经验）。

## 相关

- [ESL 化（突破 255 插件上限）](../04-loadorder/esl-flagging.md)（现代首选）
- [Synthesis（自动化补丁管线）](../04-loadorder/synthesis.md)（另一种自动化，但改的是内容不是插件数量）
- [xEdit / SSEEdit（记录编辑器与冲突检测）](../04-loadorder/xedit.md)（验证合并前后记录是否一致）
