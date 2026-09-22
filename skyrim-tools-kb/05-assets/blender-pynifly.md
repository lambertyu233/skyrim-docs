---
id: blender-pynifly
title: Blender + PyNifly（3D 建模工作流）
category: 05-assets
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [模型, Blender, 插件, 建模, 导出]
aliases: [PyNifly, blender 插件, 导出 nif, 3D 模型]
source: https://github.com/BadDogSkyrim/PyNifly
summary: 在 Blender 里直接导入/导出带骨骼与蒙皮的 SE 网格，是"真正做模型"的路径；NifSkope 负责收尾，CAO 负责批量。
---

# Blender + PyNifly

## 分工

| 工具 | 职责 |
|---|---|
| **Blender** | 建模、拓扑、UV、权重、形态键（morph）、动画 |
| **PyNifly（Blender 插件）** | 在 Blender 内直接**导入/导出 `.nif`**，保留骨骼、蒙皮、材质、形态键 |
| **NifSkope** | 导出后精修：flags、贴图槽、附加数据（见 [NifSkope（NIF 模型编辑器）](../05-assets/nifskope.md)） |
| **CAO** | 批量格式转换与优化（见 [Cathedral Assets Optimizer（CAO）](../05-assets/cathedral-assets-optimizer.md)） |

## 为什么需要专门的 nif 插件

`.nif` 不是通用 3D 格式，它承载 Bethesda 特有的节点类型、shader 属性、
骨骼与形态键约定。用通用导出格式（fbx/obj）往返会丢信息。
PyNifly 这个方向的工具存在的意义就是**端到端保住这些约定**。

> 历史上还有 **Niftools 的 Blender NIF Plugin**（老分支）与
> **Blender Skyrim Art Tools** 一类整合工具。它们在旧版 Blender 上是主流；
> 迁移到新版 Blender 时要注意插件的 Blender 版本要求。
> [Blender 天际美术工具](../../creation-kit-kb/05-tools/blender-skyrim-art-tools.md) 里记录了这条线。

## 典型流程（做一件装备）

1. 用 BSA 工具从 `Skyrim - Meshes.bsa` 取出参考模型（或从 mod 里取）。
2. Blender 导入参考 → 建模/改造 → 赋材质与 UV。
3. 绑定骨骼（沿用游戏骨架的骨骼名）与权重，需要变形就加 morph。
4. 导出 nif → NifSkope 校 flags、贴图槽、附加数据。
5. 需要打包就 CAO / BSArch 做 bsa；不需要就作为 loose files 分发。
6. 进游戏实测，用 xEdit 建记录把它接进去（ARMO / STAT 等）。

## 常见坑

- **坐标系与缩放**：导出后模型大小/朝向不对，多半是单位或轴向设置。
- **骨骼名不匹配**：换骨架（如 XPMSE）后，骨骼名必须与游戏一致，否则权重失效。
- **morph 丢失**：身形滑块不起作用时，先确认 morph 有没有真的烘焙进 nif
  （原理见 [运行时 morph 与离线烘焙——为什么拖滑块衣服跟着变，换预设就穿模](../../character-appearance-kb/03-body/morph-runtime-vs-bake.md)）。
- **LE/SE 二进制差异**：导出的 nif 要按目标版本设置，或事后用 CAO 转。

## 相关

- [NifSkope（NIF 模型编辑器）](../05-assets/nifskope.md)、[Cathedral Assets Optimizer（CAO）](../05-assets/cathedral-assets-optimizer.md)、[BSA / BA2 归档工具](../05-assets/archive-tools.md)
- [Blender 天际美术工具](../../creation-kit-kb/05-tools/blender-skyrim-art-tools.md)
- [运行时 morph 与离线烘焙——为什么拖滑块衣服跟着变，换预设就穿模](../../character-appearance-kb/03-body/morph-runtime-vs-bake.md)
