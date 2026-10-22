---
id: vram-exhaustion-symptoms
title: VRAM 耗尽症状与处置
category: 09-troubleshooting
version: 1.0.0
updated: 2026-10-22
tags: [VRAM, 爆显存, stutter, CTD, 排错]
kind: tutorial
source: https://www.nexusmods.com/skyrimspecialedition/mods/2347
summary: Skyrim 爆显存不弹窗：先 stutter 后 CTD；按"降贴图分辨率→查 ENB 分配→降 LOD 档→减 mod"处置。
aliases: [卡顿, 显存不足, 爆显存处置, out of vram, 降分辨率]
---

# VRAM 耗尽症状与处置

## 症状链（一手源：202X 页 + 社区经验）

**走路 stutter（新物体/新 cell 加载时）→ 频繁 stutter → CTD**。
Skyrim **不会**提示"显存不足"——这是它最危险的地方。

## 排查顺序

1. **确认是显存问题**：刚装完大贴图包/视差包/水 mod 后出现，高度可疑。
2. **降贴图分辨率**：同包 4K→2K（202X 有 Downscale Mod；Skyland 有 1K）。
   **全 2K 胜过半 4K**。
3. **查 ENB 分配**：`VideoMemorySizeMb` 是否≈显卡实际显存（过高会
   "过度占用易 CTD"，一手源：LoversLab 引 STEP）；`ReservedMemorySizeMb`
   走路卡顿时从 64 → 128/512。
4. **关驱动级 AF**，改用 ENB AF（视差也会因驱动 AF 出怪）。
5. **降 LOD 档位**（DynDOLOD High→Medium）。
6. **减视差/水/草**（带宽三巨头）。
7. 仍不行才减 mod 数量。

## 各 mod 的显存刻度（一手源）

- 202X 全 4K：**8GB+ 显存**（二手源：mythiq；作者提供 2K 降级版）。
- Cathedral Weathers：**~16MB VRAM**（自称）。
- Water for ENB：提供 2K 选项。
- Embers XD：lite 2K/1K "for systems short on video memory"。

## 与系统内存的区别（社区经验）

- SE 是 64 位，**ENBoost 冗余**（STEP 结论，见
  [VRAM 与 ENBoost](../01-principles/vram-and-enboost.md)）——
  别在 SE 上折腾 ENBoost 的内存补丁。
- ILS/CTD 若无贴图包也出现 → 查插件/脚本问题，转
  `skyrim-tools-kb/09-diagnostics`。

## 相关

- [VRAM 与 ENBoost](../01-principles/vram-and-enboost.md)
- [性能预算](../08-practices/performance-budget.md)
