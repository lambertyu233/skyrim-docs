---
id: performance-budget
title: 性能预算与分辨率分层策略
category: 08-practices
version: 1.0.0
updated: 2026-10-22
tags: [性能, 帧数, 显存, 分辨率, 预算]
kind: concept
source: https://www.nexusmods.com/skyrimspecialedition/mods/44899
summary: 掉帧时按"草→视差→LOD 档→贴图分辨率→mod 数量"顺序降级；全 2K 胜过半 4K；每层都有作者给的低配选项。
aliases: [fps, 降级, 2k, 1k, lite, 低配]
---

# 性能预算与分辨率分层策略

## 降级顺序（社区经验，掉帧时从前往后试）

1. **草**：`iMinGrassSize` 调大（Verdant：60→100）；或换 GoS 路线草包。
   密草是帧数第一杀手（一手源：Folkvangr 页"Expect a similar impact to
   other heavy grass mods"）。
2. **视差**：视差是带宽敏感大户（一手源：modding.wiki：
   "Parallax mapping is bandwidth-bound"；CS 建议视差贴图重压缩 BC4）。
3. **LOD 档位**：DynDOLOD High→Medium→Low。
4. **贴图分辨率**：同包 4K→2K→1K。**全 2K 胜过半 4K**——
   显存溢出的表现是 stutter→CTD，不是画质降级。
5. **ENB 重效果**：SSR/DetailedShadow/SkyLighting 逐个关。
6. **减 mod 数量**：最后手段。

## 各包的低配选项（一手源汇总）

| mod | 低配选项 |
|---|---|
| Skyrim 202X | 2K 降级版 / Downscale Mod |
| Skyland | 1K 包（作者拒做 4K） |
| Noble Skyrim | performance FullPack（室外多 1K） |
| Water for ENB | 2K 贴图选项 |
| Embers XD | lite 2K / 1K |
| Verdant | 1K / 512 草贴图 |
| Cathedral Weathers | 自称 zero FPS loss、~16MB VRAM |
| Cathedral - 3D Pine Grass / Ultralite Tundra GoS | "XL models ala Grass on Steroids" 极省版（80687 files 页） |

## 作者的性能自述（一手源，可作为预期管理）

- HLT：GTX 970 约 **-5 FPS**。
- SFO：作者 **-1 ~ -10 FPS**（980ti），" struggling with FPS already 就别装"。
- NOTWL：3.00 起 atlas + 减面 + navcut，观感与性能兼顾（作者目标）。
- Cathedral Weathers：**zero FPS loss**（自称）。

## 测量纪律（社区经验）

- 一次只改一层，同一路线测两遍（取稳态，跳过加载）。
- 关注的不只是平均帧：**切区卡顿**指向内存/缓存（NGIO 1.6.3 优化过草生成），
  **持续低帧**指向 GPU 带宽（视差/水/草）。

## 相关

- [VRAM 与 ENBoost](../01-principles/vram-and-enboost.md)
- [草地 INI 设置](../04-flora/grass-ini-settings.md)
- [材质包选型](../02-textures/texture-pack-selection.md)
