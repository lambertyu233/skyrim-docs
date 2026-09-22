---
id: choose-a-tool
title: 按任务选工具
category: 00-overview
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [总览, 选型, 决策, 索引]
aliases: [用哪个工具, 工具选择, 选哪个, which tool, 该装什么, 工具推荐]
source: https://wiki.wabbajack.org/
summary: 「我要做 X」→ 该用哪个工具的对照表，按用户意图而非工具名组织，并标出该项最常被误用的替代品。
---

# 按任务选工具

表里给的是**正解**，冒号后是**最常被误用的替代品**——那些替代品不是不能用，而是在这个场景下有已知的坑。

## 装与管理

| 我要… | 正解 | 常见误用 |
|---|---|---|
| 装 mod 并保持游戏目录干净 | MO2（USVFS）或 Vortex（部署链接） | 直接往 `Data\` 里拖 |
| 一键获得成型的整合包 | Wabbajack | 手动照整合包列表一个个装 |
| 让脚本类 mod 生效 | SKSE64（版本精确匹配）+ Address Library | 用游戏本体启动器启动 |
| 卸载 mod 后清掉残留脚本 | FallrimTools / ReSaver | 以为"禁用 mod"就干净了 |
| 备份/切换不同角色的 modlist | MO2 Profile / Vortex Profile | 手工改 `plugins.txt` |

## 排序与冲突

| 我要… | 正解 | 常见误用 |
|---|---|---|
| 自动排序插件 | LOOT + masterlist | 手工排 300+ 插件 |
| 消解两个 mod 改同一记录的冲突 | xEdit 手工做补丁，或 Synthesis 自动生成 | 靠调加载顺序"谁赢" |
| 清掉脏编辑（ITM / 删除引用） | xEdit 的 **Quick Auto Clean** | 手动 Apply Filter for Cleaning（已废弃） |
| 突破 255 插件上限 | 优先 **ESL 化**（xEdit 压缩 FormID + ESL 标记） | 无脑合并（zMerge 已停止更新） |
| 生成个性化补丁 | Synthesis（C# / Mutagen） | xEdit Pascal 脚本（语言老、文档少） |
| 合并一批小插件 | zMerge（仅在确认无脚本/无 MCM/无导航网格时） | 合并任务 mod、MCM mod、频繁更新的 mod |

## 资产与生成

| 我要… | 正解 | 常见误用 |
|---|---|---|
| 打开/改 `.nif` 模型 | NifSkope（活跃分支是 fo76utils 的 dev11） | 用 2018 年的官方 dev7 处理 SE 资产 |
| 把 LE 的 mod 移植到 SE | Cathedral Assets Optimizer | 只改文件名 |
| 生成远景 LOD | xLODGen（地形）→ TexGen → DynDOLOD（物体/树木） | 只跑 DynDOLOD 不跑 xLODGen |
| 解包 `.bsa` / `.ba2` | BSA Browser / Bethesda Archive Extractor | 用 CK 的 Archive.exe 反解 |
| 做 3D 模型 | Blender + PyNifly（或 Blender NIF Plugin） | 直接用 NifSkope 建模 |
| 生成/转换贴图 | Cathedral Assets Optimizer（批量）、Texconv（DDS 编码） | 用普通图片软件存 DDS（丢 mipmap/格式） |

## 创作、本地化、音频

| 我要… | 正解 | 常见误用 |
|---|---|---|
| 新建任务/NPC/世界 | Creation Kit | 用 xEdit 从零建内容 |
| 反编译 `.pex` 看脚本 | Champollion | 直接读二进制 |
| 翻译 mod | xTranslator 或 ESP-ESM Translator | 手工改 strings 文本 |
| 生成新配音 | xVASynth（+ xVATrainer 训练自有音色） | 拼接头文件式拼接 |
| 生成口型 `.lip` | FaceFXWrapper（需 `FonixData.cdf`） | 手写 lip |
| 打包成 `.fuz` | Yakitori Audio Converter | 只放 `.wav`（游戏不读） |

## 排错

| 我要… | 正解 | 常见误用 |
|---|---|---|
| 拿到可读的崩溃日志 | Crash Logger SSE（与 Trainwreck **二选一**） | 同时装两个 |
| 读懂崩溃日志 | Phostwood's Crash Log Analyzer（在线） | 肉眼读地址行 |
| 修引擎级崩溃/卡顿 | SSE Engine Fixes + Scrambled Bugs + Bug Fixes SSE | 只装其中一个就以为齐了 |
| 看 NPC 身上物品来自哪个 mod | More Informative Console | 翻 xEdit 反查 FormID |
| 降低脚本延迟尖峰 | Papyrus Tweaks NG | 关掉所有脚本 mod |

> 相关：[工具链全景：从装 mod 到造 mod](../00-overview/tools-ecosystem-map.md)（阶段全景）、[排错索引：从症状找答案](../../01-navigation/troubleshooting-index.md)（症状 → 条目）。
