---
id: install-workflow
title: 装完动作包的刷新流程（最常见翻车点）
category: 08-compatibility
kind: tutorial
version: 1.0.0
updated: 2026-09-30
tags: [安装, 流程, Pandora, 刷新, 排错]
aliases: [攻击失效, 装完没反应, T-Pose, 重跑 pandora, 动作包安装顺序]
source: https://www.nexusmods.com/skyrimspecialedition/mods/117052
summary: 新增/改动动作包后的固定流程：FOMOD 选对框架 → 启用插件 → 重跑 Pandora 勾补丁 → 排序 → 进游戏自检。
---

# 装完动作包的刷新流程（最常见翻车点）

## 为什么必须刷新

改动 `1hm_behavior.hkx` 等行为文件的 mod（框架、闪避、格挡类）需要把补丁合进动画数据库；**不重跑引擎 = 新命令不存在 = 攻击失效/大字 T-Pose**。机制见 [behaviour-engine-kb/01-principles/behaviour-patcher.md](../../behaviour-engine-kb/01-principles/behaviour-patcher.md)。BFCO 作者置顶帖明确提示过 tkDodge 兼容问题要靠重跑 Nemesis & Pandora 解决【一手源】。

## 固定流程

1. **FOMOD 安装时选对框架选项**（MCO / BFCO / Pandora / Nemesis / OAR 各分支选错是第一翻车点）。
2. **启用所有附带的 .esp/.dll**，确认 [version-pitfalls](./version-pitfalls.md) 里的 SE/AE 文件选对。
3. **重跑行为引擎**：Pandora 界面里勾选新增 mod 的补丁项 → Launch；**Pandora 与 Nemesis/FNIS 不要同时跑**。
4. **LOOT 排序**（只管插件顺序不管资源覆盖——资源覆盖规则见 [mo2-usvfs-kb/05-usage/](../../mo2-usvfs-kb/05-usage/)）。
5. 进游戏自检：轻击/重击/蓄力/方向重击各来一下；位移类招式检查 [AMR/AMF](../02-foundations/amr-amf.md) 是否在位。

## 常见症状 → 分叉点

| 症状 | 最易误判的点 |
|---|---|
| 攻击完全无效（大字/无动作） | 不是 mod 冲突，是**没重跑 Pandora** 或 FOMOD 框架选项选错 |
| 只有重击失效 | 没装/装了冲突的**重击热键 mod**（MCO 要四选一、BFCO 要一个都不装） |
| 位移招式原地漂移/被吸回 | [AMR/AMF](../02-foundations/amr-amf.md) 缺位或 ini 磁吸开关 |
| 进图动画加载慢、偶发 T-Pose | 没装 [Animation Queue Fix](../02-foundations/animation-queue-fix.md)（OAR 官方要求） |
| 踉跄完全不触发 | [MaxsuPoise](../04-poise/maxsu-poise.md) 的硬前置（BDI/DMenu/MSLF）没装齐 |

## 更多排错

症状索引见 [01-navigation/troubleshooting-index.md](../../01-navigation/troubleshooting-index.md)；Pandora 自身故障见 [behaviour-engine-kb/04-pandora/pandora-troubleshooting.md](../../behaviour-engine-kb/04-pandora/pandora-troubleshooting.md)。
