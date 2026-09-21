---
id: terrain-shadows
title: Terrain Shadows 地形阴影
category: 02-features
kind: core
status: released
version: 1.1.0
updated: 2026-09-21
tags: [地形, 阴影, 高度图, xLODGen, 世界地图]
aliases: [地形阴影, terrain shadows, 山体阴影]
source: https://modding.wiki/en/skyrim/developers/community-shaders/Features-Home/terrain-shadows
summary: 无限距离的粗糙地形阴影，游戏内与世界地图都生效；依赖高度图，原版三大世界空间自带，其它需自行生成或用 xLODGen 输出。
---

# Terrain Shadows 地形阴影

> 分类：核心特性（1.4.7+ 并入） · 状态：已发布

为地形提供**无限距离的粗糙阴影**，在游戏内与世界地图上都生效。

## Height Maps 高度图（关键前提）

> ⚠️ **这项功能只有在找到了该世界空间对应的高度图时才会生效。**

- **原版高度图已随 CS 提供**，覆盖 **Skyrim 本体、Solstheim、Forgotten Vale**。
- 其它世界空间需**自己生成**高度图，放到：

```none
(Game Folder)/data/textures/HeightMaps/
```

- 命名规则：

```none
[worldspace editorID].HeightMap.[West cell].[South cell].[East cell].[North cell].[z black].[z white].[z min].[z max].dds
```

- 更详细的说明写在 CS 安装目录内：`(Game Folder)/Data/textures/HeightMaps/readme.txt`。
- **可以直接用 xLODGen 的输出**：Terrain Shadows 会自动使用在 xLODGen 产物里找到的任何高度图，**无需额外操作**。但 `Data/textures/HeightMaps/` 里的高度图**会覆盖** xLODGen 的。
- 💡 **不需要每次更新 LOD 都重新生成高度图**。高度数据通常不变（除世界空间 MOD 外），所以：① 原版文件可用于大多数负载；② 需要生成时，**生成一次基本可以永久使用**。

## 常见问题（官方 FAQ）

**怎么知道当前世界空间有没有找到高度图？**
→ 看 CS 配置界面里 Terrain Shadows 下的**调试菜单**。

**在哪里能看到效果？**
→ **黎明/黄昏的高山、世界地图上、以及远处**。（相机周围的阴影被原版阴影贴图覆盖了。）
→ 注意**原版太阳角度即使在破晓也相当高**。可以搭配 EVLaS 或 **NAT3** 这类会大幅压低日出日落太阳角的天气 MOD——但注意：**同时用 Sky Sync 时不要再装 EVLaS**（两者互斥）。

**兼容世界地图 MOD 吗？**
→ 兼容。

**还需要地形底面网格吗？**
→ **对本 MOD 不是必需的**；但推荐为 [Sky Sync](sky-sync.md) 生成。

**为什么允许 `HeightMaps` 目录覆盖 xLODGen 输出？**
→ 官方解释：高度图应当**独立于 xLODGen**。两者目的不同：有人可能想要比 xLODGen 更高精度的图，或为了性能用裁剪过的版本。

## 相关条目

- [Sky Sync](sky-sync.md)（推荐配地形底面网格）
- [True PBR 美术师指南](../../04-development/pbr-for-artists.md)（地形 PBR）

## 贡献者

ProfJack（编码）、doodlum（CS 框架与重构）、alandtse / FlayaN（框架与重构）、sheson（xLODGen）。

---
*本条目依据官方功能页精修整理；如与官方页面不一致，以官方为准。*
