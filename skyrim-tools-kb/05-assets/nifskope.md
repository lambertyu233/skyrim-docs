---
id: nifskope
title: NifSkope（NIF 模型编辑器）
category: 05-assets
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [模型, nif, 编辑器, 资产, 树状视图]
aliases: [nif 编辑, 改模型, 模型编辑器, dev7, dev11]
source: https://github.com/niftools/nifskope
summary: 直接读写 Bethesda 的 .nif 网格：查材质路径、改节点、调 flags、烘焙贴图——不开 3D 软件就能完成的模型级手术。
---

# NifSkope

## 是什么

NifTools 项目下用于读写 **NIF（NetImmerse File Format）** 的工具。
官方仓库 README 列的适用游戏包括 Morrowind、Oblivion、Skyrim、Fallout 3 / NV、Civilization IV 等。

它以**树状结构**展示 nif 文件（`NiNode` → `BSTriShape` → `BSShaderTextureSet` → 贴图路径…），
可以改节点名、变换、flags、材质路径、贴图槽位，并在右侧预览渲染结果。

## 哪个版本（重要）

这是最容易踩的坑——**官方 `niftools/nifskope` 分支停在 2018 年的 dev7**，
处理现代 SE 资产时功能不足。社区实际在用的活跃分支：

| 分支 | 状态 | 说明 |
|---|---|---|
| **fo76utils/nifskope（dev11）** | 活跃 | 支持到 Starfield，Windows/Linux/macOS |
| hexabits/nifskope（dev9） | 最后更新约 2023 | 开发分支 |
| SpectralPlatypus/nifskope | 约 2023 | 基于 dev7 加功能（如凸分解生成） |
| niftools/nifskope（dev7） | 2018 停更 | 名义"官方" |
（来源：Beyond Skyrim 的 Arcane University wiki 的 NifSkope 页 —— **属社区整理，但版本时间线可核对各仓库**）

> 结论：**跟活跃分支走**，并注意不同分支的 UI 有差异。

## 典型用途

- 查/改一件装备用的**贴图路径**（排查"紫色/丢失贴图"）。
- 改 `NiAlphaProperty` 修透明、改 `NiStringExtraData` 挂行为（如 `PRN` 与 attach 点）。
- 组合/拆分部件、调整骨骼节点（配 XPMSE 之类的骨架）。
- 导出为 OBJ 供 3D 软件参考，或从 3D 软件导入后再在 NifSkope 里收尾。

## 边界

- **不擅长建模**。真正的建模在 Blender（见 [Blender + PyNifly（3D 建模工作流）](../05-assets/blender-pynifly.md)）。
- **不做批量处理**。要批量改几百个 nif，用 CAO（[Cathedral Assets Optimizer（CAO）](../05-assets/cathedral-assets-optimizer.md)）。
- LE 与 SE 的 nif 二进制头不同——**给 SE 用 LE 的 nif 需要转换**，别只改扩展名。

## 相关

- [Blender + PyNifly（3D 建模工作流）](../05-assets/blender-pynifly.md)、[Cathedral Assets Optimizer（CAO）](../05-assets/cathedral-assets-optimizer.md)
- [BSA / BA2 归档工具](../05-assets/archive-tools.md)（先从 bsa 里取出 nif）
- [身形（体模）](../../character-appearance-kb/03-body/)（身形与网格的关系）
