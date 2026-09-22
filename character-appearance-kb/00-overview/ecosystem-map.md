---
id: ecosystem-map
title: 捏脸与身形生态地图
category: 00-overview
kind: concept
version: 1.0.0
updated: 2026-09-22
tags: [总览, 生态, 路线图, 选型]
aliases: [ecosystem, 该装什么, body mod 有哪些, 捏脸需要什么]
source: https://www.nexusmods.com/skyrimspecialedition/mods/19080
summary: 把"人物外貌"拆成五层（前置框架 / 脸 / 身形 / 骨骼物理 / 分配），说明每层谁负责、谁依赖谁、装错会怎样。
---

# 捏脸与身形生态地图

Skyrim 的"人物外貌"不是一个 mod，而是**五层叠起来的一条链**。每一层只解决自己的问题，
层与层之间靠"文件覆盖"和"运行时 API"连接。理解这条链，比记住任何一个 mod 名字都重要。

## 五层结构

| 层 | 解决的问题 | 代表 mod | 装错的典型症状 |
|---|---|---|---|
| **L0 前置框架** | 让 DLL 插件能跑 | SKSE64、Address Library、SkyUI、草稿级的 PapyrusUtil / JContainers / MCM Helper | 菜单打不开、滑块全空 |
| **L1 脸** | 脸部几何与纹理、表情、捏脸界面 | RaceMenu、High Poly Head、EFM / EFA、脸纹理 | 黑脸、没滑块、预设不生效 |
| **L2 身形** | 身体网格与滑块 | CBBE / UNP / BHUNP / CBBE 3BA + BodySlide | 穿模、裸体不生效、滑块缺失 |
| **L3 骨骼与物理** | 挂点、物理抖动与碰撞 | XPMSE、HDT-SMP / Faster HDT-SMP、CBPC | 不抖、头发穿透、CTD |
| **L4 分配** | 把身形/外观发给 NPC | RaceMenu BodyGen、OBody NG、AutoBody | NPC 全是同一个身材 |

## 依赖方向（关键）

```
L0 前置  →  L1 / L2 / L3 / L4 全部依赖它
L2 身形  →  依赖 L3 的骨骼节点（没有 XPMSE 就没有物理骨骼可挂）
L3 物理  →  依赖 L2 的网格带物理变体（身形要选 physics 版本）
L1 脸    →  与 L2 皮肤 UV 必须同族（CBBE 皮肤 ↔ CBBE 系身形）
L4 分配  →  依赖 L1 的 RaceMenu 的 morph API + L2 的 .tri morph 文件
```

**几条反复踩的坑**：

- **L1 与 L2 的皮肤 UV 必须同族。** CBBE 有自己的 UV 映射，UNP 系有另一套；
  给 CBBE 做的皮肤贴图不能直接用在 UNP 系，反之亦然 —— 错配会在手、颈、脚出现接缝。
- **L3 不给 L2 兜底。** 只装 CBPC / HDT-SMP 不会自动让身形好看；
  身形要在 BodySlide 里构建，且必须勾 `Build Morphs` 才会有 `.tri` 文件供 RaceMenu 调。
- **L4 不是必需层。** 不装分配工具，玩家角色照样能捏；它只决定 NPC 是否"身材统一"。

## 两条互斥红线

1. **同一时刻只能启用一个女性身形 + 一个男性身形**。CBBE 与 UNP / BHUNP 不能共存。
2. **CBPC 与 HDT-SMP 争同一个 body 插槽**。要"身体用 CBPC、头发衣服用 SMP"必须做额外处理
   （把 `cbp.dll` 改名 `zcbp.dll` 或编辑 `defaultBBPs.xml`），详见
   [`04-physics/physics-overview.md`](../04-physics/physics-overview.md)。

## 该往哪读

- 我不确定从哪开始 → [`learning-path.md`](learning-path.md)
- 名词看不懂 → [`glossary.md`](glossary.md)
- 版本对不上 → [`version-matrix.md`](version-matrix.md)
- 已经出故障了 → [`06-troubleshooting/`](../06-troubleshooting/dark-face.md)

## 来源

Nexus 各 mod 发布页描述（RaceMenu、CBBE、3BA、BHUNP）、
GitHub 官方仓库 README（BodySlide、FSMP、OBody NG）、UESP 与 Creation Kit wiki。
层与层之间的依赖关系为**跨多个官方页交叉比对**得出，非单一来源陈述。
