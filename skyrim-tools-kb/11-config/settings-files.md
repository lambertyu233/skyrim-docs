---
id: settings-files
title: 配置文件体系（哪个 ini 在哪、归谁管）
category: 11-config
kind: concept
version: 1.0.0
updated: 2026-09-22
tags: [配置, INI, json, 路径, MO2, 排错]
aliases: [配置文件, ini 在哪, po3_Tweaks.ini, PapyrusTweaks.ini, ScrambledBugs.json, overwrite, 配置丢失, ini 位置]
source: https://www.nexusmods.com/skyrimspecialedition/mods/51073
summary: 四类配置文件（游戏 INI、mod 自带 ini/json、MCM 落盘设置、工具产物）的落点与归属规则——「改了没生效」有相当比例是改错了位置。
---

# 配置文件体系

Skyrim 的配置**分散在四个地方**，且**改错文件不报错、只是不生效**。
这是"我按教程改了但没反应"的高发原因。

## 一、游戏本体 INI（BethINI 管）

| 文件 | 位置 |
|---|---|
| `Skyrim.ini` | `文档\My Games\Skyrim Special Edition\` |
| `SkyrimPrefs.ini` | 同上 |
| `plugins.txt` / `loadorder.txt` | 同上（**加载顺序**，见 [LOOT（插件排序）](../04-loadorder/loot.md)） |

> `SkyrimCustom.ini` 亦存在，用于覆盖；具体支持度随版本变化，**不要凭空假设**。
> 用 BethINI 整理与预设 → [BethINI（INI 配置优化）](../11-config/bethini.md)

## 二、mod 自带的 INI / JSON（**装完首次进游戏才生成**）

这类**不在安装包里**，是**运行时生成**的：

| 文件 | 路径 | 备注 |
|---|---|---|
| `po3_Tweaks.ini` | `Data/SKSE/Plugins/` | **必须先进一次游戏**才会出现 → [powerofthree's Tweaks（引擎修复与调整）](../09-diagnostics/po3-tweaks.md) |
| `PapyrusTweaks.ini` | `SKSE/Plugins/` | 发布页会附一份**参考副本**，可合并 → [Papyrus Tweaks NG](../09-diagnostics/papyrus-tweaks-ng.md) |
| `ScrambledBugs.json` + `ScrambledBugs.log` | `Data/SKSE/Plugins/` | 逐项开关 + 报告启用了哪些 → [Scrambled Bugs](../09-diagnostics/scrambled-bugs.md) |
| OAR 的 `config.json` | 各 submod 目录内 | → `oar-kb` |
| SPID/KID 的 `*_DISTR.ini` / KID 配置 | `Data/` 下 | → `02-distribution/` |

### MO2 用户必读：它们会先落到 Overwrite

因为运行时生成，MO2 下这些文件**第一次会出现在 Overwrite 目录**里。
**正确做法**：跑一次游戏 → 把 Overwrite 里生成的文件**移回对应 mod 的目录**
（或建一个专门的"配置"mod），此后就在那个位置改。

> 这个坑在中文社区被反复记录：**即使你手动把 ini 放进
> `Data/SKSE/Plugins/`，Overwrite 里仍可能再生成一份**——
> 结果是你改了 A，游戏读的是 B。

## 三、MCM 落盘的设置

装了 **MCM Helper** 的 mod，菜单里的设置会写进 `settings.ini`
（→ [MCM Helper](../01-frameworks/mcm-helper.md)）。

**实用推论**：想看"某个选项现在到底是什么值"，**直接读 ini 比进游戏快**；
整合包也常以预置 ini 的方式发布推荐配置。

## 四、工具自己的产物

xEdit / DynDOLOD / TexGen / Synthesis / Wrye Bash 等都会写输出。
原则：**输出进独立的输出 mod，不要留在游戏目录或 Overwrite**
（→ [xLODGen（地形 LOD 生成）](../06-lod/xlodgen.md)、[Wrye Bash（管理器 + Bash Patch）](../03-managers/wrye-bash.md)）。

## 编码清单（踩过就长记性）

| 类型 | 编码 |
|---|---|
| 游戏 INI | 一般 ASCII/ANSI 兼容；**别塞非 ASCII 字符** |
| mod 的 ini/json | 多数要求 **UTF-8**；带不带 BOM 视工具而定 |
| 翻译/字符串 | 需与游戏读取的编码一致，否则乱码（→ [xTranslator（翻译工具）](../08-creation/xtranslator.md)） |
| 本资料库 | 一律 **LF + UTF-8** |

## 排错三步

1. **确认文件真的存在**（不是"我以为装了就有"）；
2. **确认游戏读的是哪一份**（Overwrite 遮蔽是最常见原因）；
3. **确认改的键名与当前版本一致**（这些键名会随版本增删）。

## 相关

- [BethINI（INI 配置优化）](../11-config/bethini.md)、[PrivateProfileRedirector SE（INI 读取加速）](../11-config/privateprofile-redirector.md)
- [Mod Organizer 2（工具视角）](../03-managers/mo2-tool.md)、[Overwrite 目录与维护](../../mo2-usvfs-kb/05-usage/overwrite-dir.md)
- [MCM Helper](../01-frameworks/mcm-helper.md)
