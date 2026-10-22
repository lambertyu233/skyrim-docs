---
id: kb-scope-and-boundaries
title: 本库收录范围与边界
category: 00-overview
version: 1.0.0
updated: 2026-10-22
tags: [总览, 范围, 边界, 分工]
kind: concept
source: https://www.nexusmods.com/skyrimspecialedition/
summary: 明确本库收录什么、不收录什么，以及与工作区其它资料库的边界，避免重复建设。
aliases: [收录范围, scope, 不收录, 本库管什么, 内容边界]
---

# 本库收录范围与边界

## 收录

- **静态环境视觉**：建筑/景观/杂物的材质与网格替换（textures & static meshes）。
- **地形、山脉、道路**：含其 LOD 配套资源。
- **植被**：树木 overhaul、草类插件、草地 INI、去草丛工具。
- **水体**：水面材质、流动、波浪、瀑布、水缝修补。
- **天气与光照**：weather mod、interior/exterior 灯光 overhaul、火焰/粒子视觉。
- **视差与 Complex Material**：作为材质管线的一部分收录原理与工具。
- **LOD 生成工具**：xLODGen / DynDOLOD / TexGen / SSE Terrain Tamriel。
- **网格工具**：SSE NIF Optimizer / Cathedral Assets Optimizer / NifSkope（指针）。
- **性能与 VRAM 管理**：ENBoost、分辨率分层、显存预算。

## 不收录（去别的库）

| 内容 | 归属 |
|---|---|
| Community Shaders 的功能/安装/版本矩阵/Subsurface Scattering 等 | `community-shaders-kb` |
| 角色外观：捏脸、身形、骨骼、NPC 分配 | `character-appearance-kb` |
| MO2/Vortex 安装器机制、USVFS、覆盖冲突的底层原理 | `mo2-usvfs-kb` |
| SKSE/Address Library/Engine Fixes 版本对应 | `skyrim-tools-kb` |
| 动作/战斗动画、行为引擎（FNIS/Nemesis/Pandora） | `behaviour-engine-kb`、`combat-animation-kb` |
| 城市/村庄 overhaul（JK's、ETaC 等 gameplay+visual 混合体） | 仅在与环境层冲突处引用，不展开 |
| 具体 ENB 预设的调参教程 | 只收录选型原则，预设本身随用随查 Nexus |

## 写作纪律（沿袭工作区 AGENTS.md）

1. 引用落到条目路径，用 markdown 相对链接（同库上一层目录、跨库上两层，
   链接文字写条目标题）。
2. 关键数值（版本号、Nexus ID、文件大小、VRAM 占用）**照抄一手源**，不凭记忆改写。
3. 区分一手源 / 社区经验 / 未核实；版本绑定上游，过期明说。
4. 不用 CSDN、toolify 等内容农场与 AI 聚合站作为来源——已集中记录于
   [不可信来源](../10-sources/unreliable-sources-and-fabrications.md)。
