---
id: choosing-engine
title: 如何选择引擎：决策指南
category: 06-practices
kind: guide
version: 1.0.0
updated: 2026-09-21
tags: [选型, 决策, FNIS, Nemesis, Pandora, 建议]
source: https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/wiki
summary: 按游戏版本、动画类型、modlist 规模与生物需求给出选型建议，并说明迁移要点。
---

# 如何选择引擎：决策指南

## 一句话建议

- **SE/AE 新 modlist → 选 Pandora**（活跃、快、全生物支持、有官方文档）。
- **已有稳定 Nemesis、规模不大且无生物需求 → 可继续 Nemesis**（迁移有成本）。
- **LE（传奇版）→ 只能 FNIS 或旧 Nemesis**。
- **使用 Wabbajack 整合包 → 跟随整合包自带的选择**，不要自行替换。

## 决策表

| 你的情况 | 推荐 | 理由 |
| --- | --- | --- |
| SE/AE、想要完整生物动画 | **Pandora** | 官方"full creature support"；Nemesis 仅"部分生物" |
| SE/AE、动画数量巨大（数万） | **Pandora** | 社区实测 4.4 万+ 动画一轮约 25 秒；Nemesis 大列表易崩 |
| SE/AE、想少折腾、要文档 | **Pandora** | 有官方 GitHub Wiki；Nemesis 中级以上无公开文档 |
| 已有 Nemesis 且稳定、无生物需求 | 维持 **Nemesis** | 迁移需重装动画 mod，收益有限 |
| LE 玩家 | **FNIS** / 旧 Nemesis | 官方对比表：只有 FNIS 支持 LE |
| 只用 OAR 替换动画、不新增 | **不需要引擎** | 替换器不依赖补丁器 |
| 完全无动画/战斗/行为 mod | **不需要引擎** | 装了是额外开销 |

## 为什么新装更推荐 Pandora

1. **性能**：增量(反)序列化 + 预加载 + 克制并行（见 [Pandora 架构](../04-pandora/pandora-architecture.md)）。
2. **容错**：非法编辑被隔离回退，不会整轮失败。
3. **兼容**：同时吃 FNIS 与 Nemesis 补丁格式。
4. **文档**：官方 Wiki 成体系（本库主要来源）。
5. **活跃**：Nexus 持续更新（v4.4.0-beta，2026-08）。

## 需要注意的坑

- **FNIS 与 Nemesis/Pandora 不能同时生效**。
- 从 FNIS/Nemesis 迁到 Pandora 前，**建议重装动画 mod**——旧引擎会直接改写各 mod 目录的 `.hkx`，污染新引擎的输入。
- Pandora 是"work in progress"：仍有零星小 bug，少数 niche 动画 mod 可能不工作；遇问题先看 `Engine.log`。
- 若只有"替换动画"需求（站姿、武器风格），那属于 **OAR/DAR** 的范畴，与引擎选择无关。

## 相关

- [官方三引擎对比表](../00-overview/engine-comparison.md)
- [标准刷补丁流程](install-workflow.md)
- [常见报错](troubleshooting-common.md)
