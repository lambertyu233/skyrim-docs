---
id: tools-ecosystem-map
title: 工具链全景：从装 mod 到造 mod
category: 00-overview
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [总览, 工具链, 生态地图, 工作流]
aliases: [工具大全, 需要哪些工具, 模改工具链, modding toolchain, essential tools, 必装工具, 工具清单]
source: https://tes5edit.github.io/
summary: 按"安装 → 排序 → 修补 → 生成 → 排错"五个阶段把 Skyrim SE/AE 的工具串成一条链路，并指出每个阶段最容易被忽略的环节。
---

# 工具链全景

Skyrim 模改不是"装一个 mod"，而是一条**流水线**：模组管理器把文件摆好 → 排序工具决定谁覆盖谁 →
补丁工具消解冲突 → 生成工具烘焙派生数据 → 诊断工具兜住崩溃。工具选错或顺序颠倒，
症状往往不是"报错"，而是**游戏能进但行为诡异**——这是本资料库要解决的核心问题。

## 一、五个阶段

| 阶段 | 做什么 | 主力工具 | 产物 |
|---|---|---|---|
| ① 前置 | 让脚本类 mod 能跑起来 | SKSE64、Address Library、SkyUI、MCM Helper、PapyrusUtil | `Data/SKSE/Plugins/*.dll` |
| ② 安装 | 把 mod 文件放进虚拟文件系统 | MO2 / Vortex / Wrye Bash / Wabbajack | 虚拟覆盖层（不改游戏目录） |
| ③ 排序与清理 | 决定插件加载次序、清掉脏编辑 | LOOT、xEdit（SSEEdit） | `plugins.txt`、清理后的插件 |
| ④ 修补与生成 | 消解记录级冲突、烘焙 LOD/远景 | Synthesis、zMerge、xLODGen、DynDOLOD、TexGen | 补丁 esp、LOD 网格与贴图 |
| ⑤ 诊断 | 崩溃与脚本问题归因 | Crash Logger SSE、Crash Log Analyzer、FallrimTools | crash log、清理后的存档 |

## 二、每一阶段最容易踩的坑

1. **前置阶段**：SKSE64 必须与 `SkyrimSE.exe` 的**精确版本**匹配（1.5.97 / 1.6.640 / 1.6.1170 各一份），
   装错表现为"游戏根本起不来"或"插件静默不加载"。Address Library 同理，SE 与 AE 两份文件不能混装。
2. **安装阶段**：MO2 与 Vortex 都**不写入游戏目录**——但实现方式不同（MO2 用 USVFS 钩子、Vortex 用硬链接部署）。
   "装完了没效果"九成是**没部署 / 没启用 / 左侧顺序被后面的 mod 覆盖**。
3. **排序阶段**：LOOT 解决的是**插件级**顺序，解决不了**记录级**冲突。别把 LOOT 当万能药。
   脏编辑（ITM / 删除引用）必须用 xEdit 清，且**只清官方 master**（`Update.esm` 等），清第三方 mod 常常是错的。
4. **修补阶段**：Synthesis / zMerge 都是**生成器**——改了 modlist 就要重跑；产物必须排在 LOOT 排序之后。
5. **诊断阶段**：`Crash Logger SSE` 与 `Trainwreck` **只能装一个**，同时装会互相干扰。

## 三、按角色分岔

- **只想玩整合包**：① Wabbajack（或 Nexus Collections）→ ④ 由整合包作者预先做好 → ⑤ 出问题才用 Crash Logger。
  基本不需要 ③ 的手工部分。
- **自己攒 modlist**：① → ② MO2 → ③ LOOT + xEdit → ④ 按需 → ⑤ 常备 Crash Logger。
- **改别人的 mod**：上面全要，再加 ⑤ 资产工具（NifSkope / CAO）与 `08-creation` 的创作工具。
- **做动画**：还要 `behaviour-engine-kb`（FNIS/Nemesis/Pandora）与 `oar-kb`（OAR）——见 [动画与行为工具链总览](../07-behaviour/animation-toolchain-overview.md)。

## 四、与其他资料库的边界

本库只覆盖"**工具**"这一层。以下深水区在各自独立的库里，本库只做索引：

| 主题 | 去哪个库 |
|---|---|
| OAR 条件语法、submod、`config.json` | `oar-kb` |
| FNIS / Nemesis / Pandora 原理与排错 | `behaviour-engine-kb` |
| Community Shaders 各功能 | `community-shaders-kb` |
| Creation Kit 编辑器操作与 Papyrus 语言 | `creation-kit-kb` |
| MO2 / USVFS 机制与设置细节 | `mo2-usvfs-kb` |
| 捏脸 / 身形 / 骨骼物理 | `character-appearance-kb` |

## 延伸

- 手上有"症状"而不是"主题"时，先读 [排错索引：从症状找答案](../../01-navigation/troubleshooting-index.md)。
- 不确定该用哪个工具 → [按任务选工具](../00-overview/choose-a-tool.md)。
- 看到不认识的缩写 → [术语表（工具语境）](../00-overview/glossary.md)。
