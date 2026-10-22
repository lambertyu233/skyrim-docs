---
id: cathedral-landscapes
title: Cathedral Landscapes
category: 03-landscape
version: 1.1.0
updated: 2026-10-22
tags: [Cathedral Landscapes, 草地, 地形, DrJacopo, 社区]
kind: reference
source: https://www.nexusmods.com/skyrimspecialedition/mods/21954
summary: Cathedral 系列的风景/草地组件：致密草（3 倍于原版的可生长表面）+ 配套地表与地形 LOD；v3.0.3 起提供 ESPFE 选项但切勿在旧存档上用。
aliases: [cathedral 草地, cathedral concept, 致密草地, lightweight grass]
---

# Cathedral Landscapes

- **作者栏**："The Community"，上传者 **DrJacopo**（一手源：Nexus 21954）
- **Nexus**：skyrimspecialedition/mods/**21954**；当前 **v3.0.3**，
  25,306 endorsements；依赖 **Cathedral Weathers and Seasons**
- **体积**：约 941MB

## 定位（一手源：发布页）

"A dense grass mod that **outperforms vanilla Skyrim** with complementary
landscape and terrain LOD to eliminate grass pop-in."

**Lightweight Grass & Landscape Overhaul** 血统：草比原版更轻，
可生长表面达原版 **3 倍**，陡坡也长草（Reach 全覆盖）。
是"Cathedral 哲学"（公开共享、社区共建）在风景层的落地。

## 版本要点（均一手源：Nexus 21954 changelog）

- **v3.0.3 新增 ESPFE（light plugin）选项——⚠️ 旧存档切勿选**：
  作者原话 "DO NOT try to use the optional ESPFE plugin with an existing
  savegame"；以旧版 CL 为 master 的 mod/补丁会因此 CTD/ILS。稳妥选传统 fat ESP。
- v3.0.2：给所有草加 object bounds，**LOD 草多样性 +约 40%**——
  需重跑 DynDOLOD 才能生效。
- v3.0：草基于**实拍草叶**；短草进入 Reach；雪基于 Cathedral Snow 4.3。
- v1.2：地形 LOD 打进 BSA（改善与 A Quality World Map 等地图 mod 兼容）。
- 默认 `iMinGrassSize=60`；捆绑 Blended Roads / "Really Blended Roads" 选项。

## 与 Cathedral Weathers 的关系

CWS 围绕 Lightweight Grass Overhaul 设计草-地过渡，很多 ENB 会破坏这些过渡
（一手源：Nexus 24791）。CL 的 Nexus 依赖项直接列了 CWS。

## Credits（一手源）

G'k、J'Tharpla、Deorder（Cathedral Concept 完成的关键角色）；
JonnyWang 的资产可自由使用（条件：你的 mod 也开放权限）；
Mindflux 的高模蕨类（ENB Particle Patch）。

## 相关

- [Cathedral Weathers](../06-weather-lighting/cathedral-weathers.md)
- [LOD 生成完整流程](../08-practices/lod-generation-workflow.md)
- [DrJacopo 3D 素材库](../04-flora/grass-mods-overview.md)（80687，modder 资源）
