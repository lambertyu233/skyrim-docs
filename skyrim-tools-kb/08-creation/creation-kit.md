---
id: creation-kit
title: Creation Kit（官方创作工具）
category: 08-creation
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [创作, 官方工具, 编辑器, 索引]
aliases: [Creation Kit, CK, creation kit 下载, 官方编辑器, 做 mod]
source: https://ck.uesp.net/wiki/Main_Page
summary: Bethesda 官方编辑器：新建任务、NPC、世界、对话与导航网格的正路；改已有记录或做补丁则应该用 xEdit。深度操作见 creation-kit-kb。
---

# Creation Kit

> 本条目只讲"它在工具链里的定位与边界"。**编辑器的逐项操作、Papyrus 语言、
> 快捷键、教程都在 `creation-kit-kb`（29 条）**，本文不重复。

## 定位：什么时候用它，什么时候不用

| 任务 | 用 CK | 用 xEdit |
|---|---|---|
| 新建任务 / NPC / 世界 / 对话 | ✅ | ✗（能做但 UI 不是为此设计） |
| 改已有记录的字段值 | 慢 | ✅ |
| 做兼容补丁 | ✗ | ✅ |
| 清理脏编辑 | ✗ | ✅（Quick Auto Clean） |
| 生成 facegen / 校验脸 | ✅ | ✗ |
| 批量改上百条记录 | ✗ | ✅（脚本）或 Synthesis |

**一句话**：CK 造新东西，xEdit 改旧东西。社区经验是"90% 的时间在 xEdit，需要造新内容才开 CK"。

## 在完整流程中的位置

1. CK 里建内容（记录 + 脚本 + 资源引用）；
2. 资源（网格/贴图/音频）由 `05-assets` 的工具链产出；
3. 脚本由 Papyrus 编译器编译（[Papyrus 编译器与反编译](../08-creation/papyrus-compiler-decompiler.md)）；
4. 打包用 Archive.exe（[Archive.exe（BSA 打包）](../../creation-kit-kb/02-features/archive-exe.md)）；
5. 出来之后交给 xEdit / LOOT 纳入加载顺序。

## 使用前必做的两件事

1. **让 CK 认得多重 master**：BethINI 可以自动为 Skyrim 配置"支持多重 master 与已装 DLC"
   （官方发布页功能列表明确提到）→ [BethINI（INI 配置优化）](../11-config/bethini.md)。
2. **别在 `Program Files` 下安装游戏/CK**——UAC 会打断保存与日志写入。

## 已知的坑（来自 CK 库与本库的交集）

- CK 会**打乱导航网格 edge link 表的顺序**（即使没实质改动），
  导致 xEdit 里出现大量 `NAVM` 假 ITM——新版 xEdit 改成按坐标比较才能识别。
  → [脏编辑与清理（ITM / UDR）](../04-loadorder/dirty-edits-cleaning.md)
- CK 生成静态物体 LOD 时**只能用一张 texture atlas**，限制画质与工作量 →
  这是 **xLODGen** 存在的理由（[xLODGen（地形 LOD 生成）](../06-lod/xlodgen.md)）。
- 生成的 facegen 与 `.lip` 口型文件是**独立产物**，需要一起分发；
  口型也有 CK 之外的生成路径（[FaceFXWrapper（生成口型 .lip）](../10-audio/facefxwrapper.md)）。

## 相关

- `creation-kit-kb/`（全库 29 条：安装、界面、游戏系统、Papyrus、教程）
- [Papyrus 编译器与反编译](../08-creation/papyrus-compiler-decompiler.md)
- [xEdit / SSEEdit（记录编辑器与冲突检测）](../04-loadorder/xedit.md)
- [BethINI（INI 配置优化）](../11-config/bethini.md)
