---
id: texture-formats-and-compression
title: DDS 压缩格式与贴图实务
category: 01-principles
version: 1.0.0
updated: 2026-10-22
tags: [压缩, BC1, BC5, BC7, DDS, 法线, mipmap, 原理]
kind: concept
source: https://www.nexusmods.com/skyrimspecialedition/mods/18247
summary: 漫反射用 BC1/BC3、法线用 BC5、alpha/视差通道有专门讲究；压缩格式选错是"贴图发灰/伪影"的常见根因。
aliases: [BC3, 法线压缩, DXT1, DXT5]
---

# DDS 压缩格式与贴图实务

## 各通道常用格式（一手源 + 社区经验）

| 贴图类型 | 常用格式 | 说明 |
|---|---|---|
| 无 alpha 漫反射 | BC1（DXT1） | Skyrim 3D Landscapes 明确"DXT1 for non-alpha diffuse"（一手源） |
| 带 alpha 漫反射 | BC3（DXT5） | 同上"DXT5 for alpha diffuse and normal maps"（一手源） |
| 法线 | BC5（3Dc/ATI2） | 双通道法线的行业标准做法 |
| 视差/高度图 | BC4 | Community Shaders 官方建议"recompress parallax textures to BC4"以省带宽（一手源：modding.wiki） |
| 高保真 PBR 组 | BC7 | 无损块压缩，显存换质量；老游戏引擎支持有限，多用于 CS/ENB 工作流 |

## 容易踩的坑

- **法线图不要用 BC1**：R/G 通道被压烂会出现 shading 错误（阶梯状高光）。
- **视差通道的压缩精度**：Complex Material 的 G 通道 ≤4/255 会被判黑并**禁用整个
  complex material**（一手源：modding.wiki）——写通道图必须注意 grayscale 2.2。
- **mipmap 与 alpha 缩放**：Folkvangr 明确其贴图"mipmap alpha scaling"处理
  以在远处保留细节（一手源：Nexus 44899 changelog）；Terrain LOD Redone
  则相反——大面积 LOD 贴图**删掉了 mipmap**（"they are wasting only space"，
  一手源：Nexus 9135）。同一手段在不同场景结论相反，别一概而论。
- **切线（tangents）**：视差/法线需要正确切线空间；SSE NIF Optimizer 会给
  需要的网格补切线（一手源：Nexus 4089）。HLT 曾因"Reach/Aspen 树切线空间
  问题"出过可见 bug（一手源：Nexus 50961 changelog）。

## 分辨率与显存的换算直觉（社区经验）

- 一张 4K BC1 ≈ 22MB 显存；2K ≈ 5.5MB；1K ≈ 1.4MB（含 mipmap 约 +33%）。
- 材质包从 4K 降 2K，显存约降到 1/4，视觉损失远小于预期——这是
  [性能预算](../08-practices/performance-budget.md) 的核心手段。

## 工具

- NVIDIA Texture Tools / DirectXTex（命令行批处理）、Photoshop + 插件（作者工作流）。
- 检查/扫描贴图兼容性可顺手用 [SSE NIF Optimizer](../07-mesh-tools/sse-nif-optimizer.md)
  的 "scan textures" 功能（一手源：Nexus 4089）。
