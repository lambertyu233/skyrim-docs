---
id: vram-and-enboost
title: VRAM 预算与 ENBoost 内存管理
category: 01-principles
version: 1.0.0
updated: 2026-10-22
tags: [VRAM, 显存, ENBoost, ENB, 内存, 性能]
kind: concept
source: https://stepmodifications.org/wiki/SkyrimSE:2.0.0
summary: Skyrim SE 是 64 位但仍受 VRAM/系统内存行为影响；ENBoost 在 SE 上已被 STEP 判定为冗余，真正的显存管理靠分辨率分层与 ENB 参数。
aliases: [enbboost, videoMemorySizeMb, 爆显存, 显存不足]
---

# VRAM 预算与 ENBoost 内存管理

## 先破一个讹传：SE 上还要不要 ENBoost？

**STEP 官方立场（一手源）**："ENBoost is entirely redundant in Skyrim SE on a
64-bit system with > 4 GB RAM…… The ENBoost option exists solely so that the
Skyrim LE engine can behave more like a 64-bit game engine…… Use it only for
Skyrim LE."

即：**SE/AE 64 位 + >4GB 内存 → ENBoost 不必要**。中文教程里"装 ENB 必配
ENBoost 防爆显存"是 LE 时代遗留。仅当 SE 跑在 ≤4GB 内存的 64 位系统上才考虑。

## 如果确实用 ENB，关键参数（社区经验，STEP/Skyrim Stability Guide）

`enblocal.ini`：

- `VideoMemorySizeMb`：ENB 可支配的总显存。STEP 公式：
  ≥8GB 系统内存 → "Total Available Graphics Memory - 170(Win7)/350(Win8/10)"；
  <8GB 系统内存 → "(VRAM + System RAM) - 2048"。
- `ReservedMemorySizeMb`：默认 64；**走路时物体加载卡顿**先试着加到 128/512。
- `AutodetectVideoMemorySize`：不确定就留 true。
- `ForceAnisotropicFiltering=true` + `MaxAnisotropy=16`，**并关掉显卡控制面板的
  AF**——驱动级强制 AF 会破坏视差效果（一手源：Skyrim Stability Guide）。
- `EnableCompression=true` 与卡顿的取舍（关掉解卡顿但更接近无 ENBoost 的内存风险）。

## Skyrim 自己的内存块（LE 遗物，SE 已不需要）

Skyrim Memory Patch（SKSE.ini 512MB 首块）针对 LE 的 256MB 块爆满 CTD，
SE 不适用——见 `skyrim-tools-kb`。

## SE/AE 上的现实规则（社区经验）

1. **爆显存的症状不是弹窗，是 stutter → CTD**。Skyrim 202X 页面原话：
   "Crashes, lags, low fps? Check your enb settings, vram and allocation"。
2. 202X 全 4K 需要 **8GB+ 显存**（二手源：mythiq 对该页的转述，建议以 Nexus
   文件页的分辨率选项为准——作者提供 2K/1K 降级版）。
3. Cathedral Weathers 自称仅占 **~16MB VRAM**（一手源：Nexus 24791）。
4. Water for ENB 提供 **2K 版**供低显存（一手源：Nexus 37061）。
5. 降级顺序：先降同一贴图包的分辨率（4K→2K），再砍 LOD 质量档位，
   最后才减 mod 数量——见[性能预算](../08-practices/performance-budget.md)。

## 相关

- [视差与 Complex Material](../01-principles/parallax-and-complex-material.md)（视差是带宽敏感大户）
- [ENB 预设与 CS 衔接](../08-practices/enb-presets-and-cs-bridge.md)
