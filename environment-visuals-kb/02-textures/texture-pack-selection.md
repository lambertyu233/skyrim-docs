---
id: texture-pack-selection
title: 材质包选型与混搭原则
category: 02-textures
version: 1.0.0
updated: 2026-10-22
tags: [选型, 混搭, 覆盖, 分辨率, 材质]
kind: concept
source: https://www.nexusmods.com/skyrimspecialedition/mods/659
summary: 一体化 vs 混搭怎么选；覆盖规则三定律；分辨率分层策略；SMIM 纹理覆盖陷阱。
aliases: [材质选型, 覆盖规则, 降级, 2k, 4k, base]
---

# 材质包选型与混搭原则

## 两种路线

| 路线 | 代表 | 优点 | 代价 |
|---|---|---|---|
| 一体化 | Skyland AIO、Noble、Vivid Landscapes AIO、202X 全量 | 风格统一、省心 | 单点未必最强、体积/显存大 |
| 混搭 | SMIM + 202X + MM + HLT + 单城市包 | 单点质量上限 | 要懂覆盖规则、接缝风险 |

**混搭第一定律**：建筑/风景/杂物分别选"主包"，其余全部让位。
典型组合：底座 SMIM → 主包 202X 或 Skyland AIO → 单点覆盖
（MM 山脉、HLT 树、CleverCharff 城市、RUSTIC 单件）。

## 覆盖规则三定律（机制详见 mo2-usvfs-kb）

1. **后装赢**（同文件路径，load order 后者胜；松散文件永远赢 BSA）。
2. **先底座后覆盖**：SMIM 先装，贴图包后装（SMIM 官方建议）。
3. **让该赢的赢**：MM 覆盖 SMIM 网格（面数更高）；202X 覆盖 SMIM；
   ELFX 被 202X 覆盖——这些结论全部来自各自发布页，见对应条目。

## 分辨率分层策略

- 同一包先看有没有 2K/1K 选项：202X（有 Downscale Mod）、Skyland（1K/2K）、
  Water for ENB（2K）、Embers XD（lite 2K/1K）、Verdant（1K/512）。
- **全 2K 优于半 4K**：显存溢出时表现是 stutter→CTD，不是画质下降。
- 大地图（山脉、风景）优先保分辨率；小杂物（ingot、杯子）放心 1K。

## 风格一致性检查（社区经验）

混搭前问三个问题：
1. 明暗基调一致吗？（Noble 偏暗手绘，Skyland 偏亮扫描）
2. 雪/岩石的处理一致吗？（MM 的雪与 Fluffy Snow/Simplicity of Snow 的配合）
3. 视差依赖一致吗？（一半视差一半没有 = 接缝与观感撕裂）

## 相关

- [SMIM](../02-textures/smim.md)、[Skyland AIO](../02-textures/skyland-aio.md)、
  [Skyrim 202X](../02-textures/skyrim-202x.md)、[Noble Skyrim](../02-textures/noble-skyrim.md)
- [安装顺序与冲突](../08-practices/install-order-and-conflicts.md)
- [性能预算](../08-practices/performance-budget.md)
