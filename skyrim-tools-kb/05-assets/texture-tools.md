---
id: texture-tools
title: DDS 与贴图工具链
category: 05-assets
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [贴图, DDS, 压缩, mipmap, 优化]
aliases: [贴图压缩, texconv, BC7, 贴图格式, 紫色贴图, 贴图模糊]
source: https://github.com/Guekka/Cathedral-Assets-Optimizer
summary: Skyrim 贴图是 DDS 容器 + 压缩格式 + mipmap 链的三件套；画图软件能出图，但格式与 mipmap 得靠专用工具，出错就表现为糊、闪、紫。
---

# DDS 与贴图工具链

## 概念拆解（出错时按这个顺序排查）

一张 Skyrim 贴图 = **DDS 容器** × **压缩格式** × **mipmap 链**：

| 维度 | 说明 | 出错表现 |
|---|---|---|
| 压缩格式 | 漫反射常用 BC1/BC3，法线常用 BC5/BC7；**格式与用途不匹配会颜色错乱** | 法线图发紫/发花 |
| sRGB / 线性 | 颜色图与法线/数据图的空间不同 | 整体偏亮/偏暗 |
| mipmap | 远距离用的逐级缩小副本 | **缺 mipmap → 远处闪烁（shimmering）** |
| 分辨率 | 实际显存占用的大头 | 4K 贴图堆太多 → 爆显存、掉帧 |
| 命名/路径 | 模型里写死的路径 | 贴图整块缺失（紫/黑） |

## 工具分层

| 场景 | 工具 |
|---|---|
| **批量**重压/降采样/修 mipmap | **Cathedral Assets Optimizer**（[Cathedral Assets Optimizer（CAO）](../05-assets/cathedral-assets-optimizer.md)） |
| DDS 编解码（命令行） | **Texconv**（DynDOLOD 生态里也随附；官方要求 VC++ 运行库） |
| 单张精修 | Photoshop / GIMP / Paint.NET + DDS 插件（导出时必须手动选对格式与 mipmap 选项） |
| 从归档里取贴图 | BSA/BA2 工具（[BSA / BA2 归档工具](../05-assets/archive-tools.md)） |
| 生成 LOD 用的图集 | **TexGen**（[TexGen（LOD 贴图生成）](../06-lod/texgen.md)） |

> 通用图片软件的问题是**默认不生成完整 mipmap 链、压缩格式选项藏在导出对话框里**——
> 单张改图没问题，成规模就必须用 CAO 一类工具。

## 判断"是不是贴图问题"

1. **紫色**：通常不是贴图本身，而是**路径写错或文件缺失**（模型找不到贴图）。
2. **远处闪烁/摩尔纹**：mipmap 缺失或生成错误。
3. **近看发花/发灰**：法线图压缩格式不对，或当成 sRGB 处理了。
4. **整块糊**：被更低优先级的 mod 覆盖（安装顺序问题 → [Mod Organizer 2（工具视角）](../03-managers/mo2-tool.md)）。

## 相关

- [Cathedral Assets Optimizer（CAO）](../05-assets/cathedral-assets-optimizer.md)
- [BSA / BA2 归档工具](../05-assets/archive-tools.md)
- [TexGen（LOD 贴图生成）](../06-lod/texgen.md)
- `community-shaders-kb/`（着色器侧的贴图与材质话题）
