---
id: esl-flagging
title: ESL 化（突破 255 插件上限）
category: 04-loadorder
kind: tutorial
version: 1.0.0
updated: 2026-09-22
tags: [插件上限, ESL, 轻量主文件, FormID, 优化]
aliases: [ESLify, esl 标记, 255, light master, espfe, 压缩 FormID]
source: https://loot.github.io/docs/help/Introduction-To-Load-Orders
summary: 把普通插件标记为轻量主文件（.esl / ESPFE），保留独立更新能力而不再占 255 名额——现代做法优于合并。
---

# ESL 化

## 为什么可行（官方规则）

LOOT 官方文档明确：Skyrim SE / Skyrim VR / Fallout 4 中，
**常规 `.esm` + `.esp` 上限 255 个**，而 **`.esl` 可再额外加载 4096 个**。

关键约束：**ESL 的 FormID 空间被压缩到 `0x000`–`0xFFF`**（4096 个新记录）。
这就是"能不能 ESL 化"的判据——插件新增的记录数必须放得下，
且**压缩 FormID 不能破坏依赖它的补丁**。

## 判断与操作

1. **看是否可压缩**：在 xEdit 里检查插件新增记录数量；
   超过 4096 个新记录就**不能**直接 ESL 化。
2. **压缩 FormID**（xEdit 的 "Compact FormID"）——这一步会**改写 FormID**，
   所以任何**依赖该插件 FormID 的补丁都要同步更新**。
3. **加 ESL 标记**（"Add ESL flag"）；扩展名仍可保持 `.esp`，
   这类文件社区称为 **ESPFE**（.esp 带 esl flag）。
4. 相关工具：社区有 ESLify 类批量工具，会缓存已压缩的 mod 数据并同步改写依赖它的插件与数据文件。

## 铁律与陷阱

- **不要"先压缩再合并"**：如果某插件要参与合并，请用**原始未压缩**的版本；
  把已压缩的插件拿去合并会让 FormLink 映射错乱（来源：ESLify Everything 官方 wiki）。
- **压缩 FormID 会打穿依赖**：别对"被大量补丁引用"的插件随手压缩，
  除非你确认能同步更新那些补丁。
- **不要中途改**：FormID 变了，**同一存档读到一半时不要做 ESL 化**。
- 顺序上建议：**先 ESL 化，再考虑合并**（见 [zEdit / zMerge（插件合并，已停滞）](../04-loadorder/zedit-zmerge.md)）。

## 与"合并"的对照

| | ESL 化 | 合并 |
|---|---|---|
| 插件数量 | 不变（但不再占 255 名额） | 变少 |
| 可单独更新 | ✅ | ❌（合并后要整体重建） |
| FormID | 压缩（可能破坏依赖） | 重映射（更容易破坏脚本/MCM/facegen） |
| 推荐度 | **首选** | 仅在简单小插件上使用 |

## 相关

- [xEdit / SSEEdit（记录编辑器与冲突检测）](../04-loadorder/xedit.md)（执行压缩与加标记）
- [zEdit / zMerge（插件合并，已停滞）](../04-loadorder/zedit-zmerge.md)（合并的风险）
- [LOOT（插件排序）](../04-loadorder/loot.md)（上限与位次的官方依据）
- [术语表（工具语境）](../00-overview/glossary.md)（ESL / FormID）
