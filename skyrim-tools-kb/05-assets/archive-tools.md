---
id: archive-tools
title: BSA / BA2 归档工具
category: 05-assets
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [归档, bsa, ba2, 解包, 打包, 资产]
aliases: [bsa 解包, 归档工具, BSA Browser, Bethesda Archive Extractor, BAE, BSArch, archive.exe, 提取文件]
source: https://ck.uesp.net/wiki/Archive.exe
summary: 把 `.bsa` / `.ba2` 里的网格、贴图、声音取出来，或把 loose files 打回归档的一组工具；选错工具是「改完不生效」的常见原因。
---

# BSA / BA2 归档工具

## 先分清两件事

- **BSA**：Skyrim LE / SE 的归档格式（`.bsa`）。
- **BA2**：Fallout 4 之后的格式（`.ba2`），Skyrim SE 不使用。

归档里放网格、贴图、声音等资源。游戏读资源的优先级通常是
**loose files（散落文件）优先于 bsa**——所以"改了贴图但没效果"，
很多时候是**新文件没放对路径**，或反过来**被 bsa 里的版本盖住**。
（MO2 侧的优先级规则见 [BSA 归档的优先级解析](../../mo2-usvfs-kb/03-architecture/bsa-priority-resolution.md)）

## 工具一览

| 工具 | 类型 | 用途 |
|---|---|---|
| **Archive.exe** | 官方（随 Creation Kit） | 官方打包工具；能打包但**反解体验差** |
| **BSArch / BSArchPro** | 命令行 / GUI | xEdit 生态里的归档打包/解包工具；`BSArch` 是 `BSArchPro` 的命令行版 |
| **BSA Browser** | GUI | 浏览与**批量**提取 bsa |
| **Bethesda Archive Extractor（BAE）** | GUI | 浏览/提取，支持多种 Bethesda 归档格式 |
| **CAO** | GUI（批量） | 除转换资产外，也**能创建 Bethesda 归档**（见 [Cathedral Assets Optimizer（CAO）](../05-assets/cathedral-assets-optimizer.md)） |

> 各工具的**维护者与最新版本请以 Nexus 发布页为准**——本条目刻意不写版本号与作者名，
> 因为它们是长期由社区接力维护的小工具，署名与版本变动频繁，转述容易出错。
> 官方口径的 Archive.exe 说明见 UESP 的 Creation Kit wiki。

## 典型用途

### 1. 取参考资源

想研究某件官方装备的网格/贴图 → 用 BSA Browser 从
`Skyrim - Meshes.bsa` / `Skyrim - Textures*.bsa` 中提取 →
在 NifSkope 里看结构（[NifSkope（NIF 模型编辑器）](../05-assets/nifskope.md)）。

### 2. 检查 mod 到底改了什么

同一个资源在 bsa 与 loose files 里各有一份时，**只改一处会让人误判**。
排查顺序：先确认 mod 安装后文件落在哪里（MO2 的文件树），再看 bsa 里是否有旧版本。

### 3. 打包发布

loose files 便于用户覆盖，bsa 便于分发与减少文件数。
官方 Archive.exe 的坑（社区经验）：**打包时要注意列表文件与目录结构**，
打错会造成"装上去什么都没变"。

## 常见症状

| 症状 | 原因 |
|---|---|
| 改了 bsa 里某个文件，进游戏没变 | 有 loose file 盖住，或路径/大小写不符 |
| 装了带 bsa 的 mod 但资产缺失 | 归档未正确注册（部分 mod 需要配合插件的 bsa 标志） |
| 提取出来的 nif 打不开 | 用了不支持 SE 格式的旧版查看器 → 换成活跃分支 |

## 相关

- [NifSkope（NIF 模型编辑器）](../05-assets/nifskope.md)、[DDS 与贴图工具链](../05-assets/texture-tools.md)、[Cathedral Assets Optimizer（CAO）](../05-assets/cathedral-assets-optimizer.md)
- [BSA 归档的优先级解析](../../mo2-usvfs-kb/03-architecture/bsa-priority-resolution.md)（bsa 与 loose file 的优先级）
- [Archive.exe（BSA 打包）](../../creation-kit-kb/02-features/archive-exe.md)（官方打包工具）
