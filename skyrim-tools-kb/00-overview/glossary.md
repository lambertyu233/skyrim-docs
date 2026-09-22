---
id: glossary
title: 术语表（工具语境）
category: 00-overview
kind: concept
version: 1.0.0
updated: 2026-09-22
tags: [总览, 术语, 缩写, 速查]
aliases: [名词解释, esp esm esl, plugins.txt, dirty edit, ITM, UDR, LOD, VFS, 黑话]
source: http://wrye-bash.github.io/docs/Wrye%20Bash%20General%20Readme.html
summary: 工具语境下的高频缩写与概念：插件类型、冲突与脏编辑、LOD、虚拟文件系统、Papyrus，逐个给出「是什么 + 谁在管」。
---

# 术语表

## 插件与文件

- **Plugin**：任何 `.esp` / `.esm` / `.esl` 文件。存放记录（record）。
- **ESM（Elder Scrolls Master）**：主文件。是"主"由**文件内部的一个 flag** 决定，不由扩展名决定。
  但 Skyrim SE/VR 与 Fallout 4 里，`.esm` / `.esl` **扩展名本身就一律视为主文件**。
- **ESL / light master**：轻量主文件。在 Skyrim SE / VR / FO4 / Starfield 里最多可加载 **4096 个**，
  且**不占** 255 常规上限。代价是 FormID 空间被压缩到 `0x000`–`0xFFF`，压缩 FormID 可能破坏依赖它的补丁
  （来源：LOOT Introduction To Load Orders）。
- **FormID**：记录的唯一 ID，前两位是加载次序（00–FE），所以位次一变，引用就可能错位。
- **master**：某插件所依赖的插件。"缺 master"= 前置没装。
- **FOMOD**：安装时出选项的向导格式（MO2/Vortex 都能渲染）。
- **BSA / BA2**：Bethesda 归档格式，装贴图与网格。BA2 是 Fallout 4 以后的格式。

## 加载与覆盖

- **Load order（插件顺序）**：`.esp/.esm/.esl` 的加载次序，决定记录级"谁覆盖谁"。
  存于 `%LOCALAPPDATA%\Skyrim Special Edition\plugins.txt`（全部插件则在 `loadorder.txt`）。
- **Install order（安装顺序 / 左侧顺序）**：mod **文件**的覆盖次序，决定贴图/网格哪个版本生效。
  与插件顺序是**两码事**——这是新手最大的认知断层。
- **Rule of one（唯一规则）**：同一条记录只能存在一个最终版本，最后加载的插件胜出。
- **Conflict（冲突）**：分**资源冲突**（同一路径的两个文件）与**数据冲突**（两个插件改同一记录）。
  冲突本身不是错，是有意的覆盖；只有当"覆盖掉的值你其实想要"时才是问题。
- **VFS / USVFS**：虚拟文件系统。MO2 借它让游戏"以为"文件都在 `Data\`，实际散落在各 mod 目录。
- **Overwrite（覆盖目录）**：MO2 里没有归属的文件落点，长期不清会掩盖问题。

## 脏编辑与清理

- **ITM（Identical To Master）**：与 master 完全相同的记录——通常是误改。会遮蔽别人对该记录的修改。
- **UDR（Undeleted and Disabled Reference）**：被"删除"的引用。**必须**改成"未删除 + disabled"，
  否则可能崩游戏。注意缩写惯例是反的：`Scan For UDRs` 扫的是"被删除的引用"。
- **Dirty edit（脏编辑）**：插件里不该有的改动，ITM/UDR 都是。官方 master 必须清；第三方 mod 慎清。
- **Cleaning（清理）**：xEdit 里现在统一走 **Quick Auto Clean**，旧的"Apply Filter for Cleaning"
  三个手动函数**已废弃**，点了只会弹说明。

## 视觉与生成

- **LOD（Level Of Detail）**：远处低精度模型。分**地形 LOD（terrain）**、**物体 LOD（object）**、
  **树木 LOD（tree）**三类，分别由 xLODGen、DynDOLOD、TexGen 负责。
- **Billboard**：树 LOD 用的面片贴图。
- **Texture atlas（图集）**：把多张贴图拼成大图以减少 draw call；LOD 生成的关键产物。
- **Occlusion（遮挡）**：预先算出"从 A 点看不到 B 区域"，用于剔除；缺了会看到远景破洞。
- **hdpt / HDPT**：头部部件记录（发型、眉毛）。属于捏脸领域，见 `character-appearance-kb`。

## 脚本与引擎

- **Papyrus**：游戏脚本语言，编译产物是 `.pex`，源码是 `.psc`。
- **SKSE plugin**：以 DLL 形式注入进程的扩展，**版本必须匹配游戏运行时**，靠 Address Library 抗更新。
- **cosave（`.skse`）**：与 `.ess` 配对，存 SKSE 插件的序列化数据（如 RaceMenu 的滑块值）。
- **CTD**：Crash To Desktop。
- **Papyrus log**：脚本调试日志，需在 INI 里显式打开；性能剖析见 [Papyrus 日志与脚本排错](../09-diagnostics/papyrus-logging.md)。

## 容易混淆的三组

| A | B | 差别 |
|---|---|---|
| LOOT | xEdit | 前者排**插件顺序**，后者处理**记录内容** |
| 插件顺序 | 安装顺序 | 前者管记录（右侧），后者管文件（左侧） |
| ESL 化 | 合并（merge） | 前者保留独立插件、压缩 FormID；后者把多个插件压成一个 |

> 更多跨库术语（身形、骨骼、shader 名词）见各库自身的 `glossary` 条目。
