---
id: dyndolod
title: DynDOLOD（物体与树木远景）
category: 06-lod
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [LOD, 远景, 物体, 树木, 生成器, 官方文档]
aliases: [远景生成, 动态 LOD, 树木 LOD, object lod, 远景 mod]
source: https://dyndolod.info/DynDOLOD-Reference
summary: 基于 xLODGen 扩展的远景生成套件：自动为整条加载顺序生成物体/树木 LOD 与动态远景，自带数千个新 LOD 模型；代价是流程长、重跑频繁。
---

# DynDOLOD

> 官方定位（dyndolod.info）：**"DynDOLOD is a modified xLODGen"**——
> 它在 xLODGen 的物体/树木 LOD 生成之上，把"为 mod 与整条加载顺序配置 LOD"
> 的大量流程自动化，并**附带数千个新的 LOD 模型与贴图**，外加新的 LOD 类型与特性。
>
> ⚠️ 官方同时明确：**它不是给普通玩家的一键工具**，目标用户是"熟悉 xEdit 这类工具的
> enthusiast modder"——要会读手册与 FAQ。手册在压缩包内的
> `docs\DynDOLOD_Manual_SSE.html`。

## 三个主要步骤（官方 Reference）

1. **扫描 `*_lod*.nif`**：扫描顺序由 `DynDOLOD_[游戏模式].ini` 里的
   `Folder1=`、`Folder2=`… 决定，**后扫描到的同名模型胜出**——
   于是"用文件夹结构覆盖 LOD 模型"成为一种可控手段。
   扫描范围是**整个 `data/meshes`（先 bsa 后 loose files）**，
   所以 mod 只要自带 LOD 模型就会被自动发现。
2. **应用补丁**：用 `..\DynDOLOD\Edit Scripts\DynDOLOD\Rules\*.patch`
   与 `..\data\DynDOLOD\*.patch` 增改记录。
3. **扫描 base record**：收集 `ACTI / CONT / DOOR / FURN / MSTT / STAT / TREE / GRAS` 中适合做 LOD 的条目。
   默认**忽略** STAT 记录上的原版远景设置（除非勾了 "Prefer base record LOD assignments over rules"）——
   这就是 DynDOLOD 能为原本没有 LOD 的东西（雕像、石门、道路）补上远景的原因。

## 依赖（官方 Requirements）

- **SKSE** 与 **PapyrusUtil 2.8+**
- **DynDOLOD Resources**：版本**只能与 standalone 相同或更高，绝不能低于**。
- Vanilla LOD Billboards（TES5LODGen 的）或 Indistinguishable / Seamless Billboards，
  再按 mod 覆盖可选 billboard。
- **Microsoft Visual C++ Redistributable（2015/2017/2019）**——
  `LODGen.exe` / `Texconv.exe` 需要；缺了会报 `C0000135` 或 DLL 缺失。

## 标准流程中的位置

`xLODGen（地形）` → **`TexGen`** → **`DynDOLOD`** → `xLODGen（Occlusion）`。
三个输出各建独立 mod，**依次排在前一个输出之后**（STEP 指南口径）。

## 性能与取舍

- **草地 LOD（grass billboard）**：DynDOLOD v3+ 支持，
  但官方/STEP 的说法是**代价显著（可达 10 FPS 量级）而收益细微**，
  **只在确认有性能余量时才生成**。
- LOD 质量档位（Low/Medium/High）直接对应显存与帧率，
  官方口径是"视觉与性能完全交给你"，所以没有"正确答案"。

## 必知的两条纪律

1. **改了影响外景的 mod 就必须重跑**（增删或移动）。
2. **产物要放进独立输出 mod**，不要留在游戏目录或 Overwrite 里。

## 相关

- [xLODGen（地形 LOD 生成）](../06-lod/xlodgen.md)、[TexGen（LOD 贴图生成）](../06-lod/texgen.md)、[遮挡数据生成（Occlusion）](../06-lod/occlusion.md)
- [PapyrusUtil SE](../01-frameworks/papyrusutil.md)（硬依赖）
- [常见错误认知](../12-sources/common-misconceptions.md) 第 15、16 条
