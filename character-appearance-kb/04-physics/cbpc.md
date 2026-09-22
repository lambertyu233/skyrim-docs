---
id: cbpc
title: CBPC（碰撞物理）
category: 04-physics
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [物理, CBPC, 碰撞, 胶囊体, Shizof]
aliases: [cbp, 碰撞物理, 胶囊体物理, 身体物理]
source: https://www.nexusmods.com/skyrimspecialedition/mods/21224
summary: CBPC 的作者、基于球体/胶囊近似的原理、它与 SMP 的分工、依赖与配置方式，以及共存时的 dll 加载顺序技巧。
---

# CBPC（CBP Physics with Collisions）

- 作者 **Shizof**
- Nexus：`https://www.nexusmods.com/skyrimspecialedition/mods/21224`
- 全称：**CBPC - CBP Physics with Collisions for SSE and VR**
- 基于 **polygonhell 的 CBP Physics（MIT）**

## 原理

用**球体 / 胶囊体近似**代替真实的网格顶点，做逐帧动态物理模拟。

所以它是**真实的物理模拟**，不是"预设动画"或"假物理"。
碰撞球可以适配身形（官方提供 PDF 配置指南）。

## 与 SMP 的分工

| | CBPC | HDT-SMP / FSMP |
|---|---|---|
| 模拟对象 | 球 / 胶囊 | 网格顶点 |
| 精度 | 中 | 高 |
| 性能 | **对 CPU 友好** | 重 |
| 适用 | **身体部位**（胸/臀/腹/大腿） | **头发、衣服、斗篷** |
| 能否管头发/衣服 | **不能** | 能 |

社区经验总结成一句话：**"身体用 CBPC，衣服头发用 SMP"**。

## 依赖

```
SKSE64（或 SKSEVR）
XP32 Maximum Skeleton Special Extended
FNIS
```

**不支持**：Player Size Adjuster and First Person Camera Height Fix SSE。

## 版本

社区经验里提及约 **1.6.x**（如 1.6.4）；
**确切最新版本未确认** —— 请以 Nexus Files 页为准。

## 配置

- 主体是 `cbp.dll`；
- 可选/常见预设配置：Sinful CBP、Immersive CBP Config、CBP Physics Config 等。

## 与 SMP 共存（必做步骤）

两者默认争同一批骨骼。共存前提：

1. 编辑 **`defaultBBPs.xml`**，让 SMP **忽略身体**、只管头发/衣服；
2. **把 `cbp.dll` 重命名为 `zcbp.dll`**（利用 dll 加载顺序让 SMP 先加载），
   或用 Engine Fixes 的 preload 机制。

> 这是**社区经验**，但多个 LoversLab 帖给出同一解法，值得采信。

## 调参不生效时的检查项（社区经验）

- 角色体重是否为 **0 或 100**；
- 是否被 SMP 覆盖（MCM 里的物理开关切错引擎）；
- 覆盖式文本配置（如 P2P 配置）在 MO2 左栏里是否位于 **CBPC / 身形之下**。

## 来源

- 作者、基于 polygonhell 的 CBP、球体近似、依赖：CBPC Nexus 页描述（经转述）—— **一手（经转述）**
- "SMP better for outfits, CBPC better for body"、"CBPC 不能管头发或衣服"：
  **社区经验（LoversLab 多帖一致）**
- `cbp.dll → zcbp.dll` 与 `defaultBBPs.xml`：**社区经验（多帖一致）**
- 不兼容 Player Size Adjuster…：Nexus 页 —— **一手（经转述）**
- CBPC 确切最新版本：**未确认**
