---
id: smim
title: SMIM 静态网格改进模组
category: 02-textures
version: 1.0.0
updated: 2026-10-22
tags: [SMIM, 静态网格, 网格, 底座, Brumbek]
kind: reference
source: https://www.nexusmods.com/skyrimspecialedition/mods/659
summary: Brumbek 的静态 3D 模型改进项目：900+ 网格、30000+ 放置点，环境美化的公认底座，但其自带纹理会覆盖其它贴图替换器。
aliases: [静态网格改进, Static Mesh Improvement, mesh fix, 网格修补]
---

# SMIM 静态网格改进模组

- **作者**：Brumbek（一手源：Nexus 659）
- **Nexus**：skyrimspecialedition/mods/659；2016-10-29 上传，当前 2.08
  （2018-07-03），文件页 2025-02-17 仍有更新
- **规模**：900+ 个网格改进，30000+ 处世界放置（一手源：发布页）
- **体积**：约 1008MB

## 它是什么

把 Skyrim 里"被忽视的"低模静态物（建筑构件、杂物、家具、景观物）重做：
修接缝、补细节，并修正部分原版贴图错误。作者自 2012-02 启动，目标 500 个
"最严重 offender"，实际远超。

## 三个必须知道的行为（一手源：发布页）

1. **`textures-smim/` 里的 SMIM 专属纹理会覆盖任何贴图替换器**——
   SMIM 网格用的是 SMIM 纹理，不是你的 Skyland/202X 的同名纹理。
   作者建议**先装 SMIM，再装贴图替换器**（后装的赢）。
2. SMIM 还修改了若干**原版贴图的错误**（如木桩），这些会与替换器冲突，
   装哪个取决于你的load order——"None of this hurts your game"。
3. **强烈建议配 USSEP**；USSEP 是 BSA 包，SMIM 松散文件永远优先，顺序无关。

## 兼容性

- 202X 页面："SMIM, is like an extension for this mod, just overwrite SMIM"
  （一手源：Nexus 2347）——202X 覆盖 SMIM。
- Majestic Mountains 用的网格比 SMIM 面数高，**建议让 MM 覆盖 SMIM 网格**
  （一手源：Nexus 11052 readme）。
- Blended Roads 与 SMIM 桥梁兼容（一手源：Blended Roads 页）。
- 大量 mod 提供 "SMIM patch"；STEP 指南中 ELFX/SMIM 组合是标准操作。

## 相关

- [Skyrim 202X](../02-textures/skyrim-202x.md)、[材质包选型](../02-textures/texture-pack-selection.md)
- 安装顺序总原则见[安装顺序与冲突](../08-practices/install-order-and-conflicts.md)
