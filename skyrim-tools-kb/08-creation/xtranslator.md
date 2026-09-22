---
id: xtranslator
title: xTranslator（翻译工具）
category: 08-creation
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [翻译, 本地化, 编辑器, 字符串]
aliases: [翻译工具, 汉化, esp 翻译, 翻译 esp, 134, fuz 播放, EspCompare]
source: https://www.nexusmods.com/skyrimspecialedition/mods/134
summary: 功能最全的 Bethesda 文本编辑与翻译工具：编辑 esp/esm/pex 文本、字符串文件、MCM 菜单，带 EspCompare 与词典、批量替换、内建 fuz 播放。
---

# xTranslator

## 官方定位

> **"a comprehensive text editor and translation tool designed for Skyrim, Fallout 4, and Starfield.
> It allows users to edit esp/esm/papyrusPex files with advanced functionalities and data analysis."**

同一套工具按游戏改名（如 `falloutNVTranslator`），且**可以在运行中切换游戏工作区**，
不必去每个游戏的页面各下一份。

## 五种工作模式（发布页原文）

| 模式 | 用途 |
|---|---|
| **Esp mode** | 直接加载 esp/esm 并就地翻译 |
| **Strings mode** | 翻译本地化 esp 附带的 `STRINGS / DLSTRINGS / ILSTRINGS` 文件（**不改 esp**）；官方标注此模式**已废弃**，建议用 Hybrid |
| **Hybrid mode** | 把本地化 esp 当"记录骨架"来编辑 strings 文件（**推荐**） |
| **MCM/Translate** | 翻译 MCM 与 UI 字符串（SkyUI 及原版 UI） |
| **PapyrusPex** | 内建 pex 反编译器，可翻译脚本里的字符串（内部变量会被锁为不可编辑） |

## 值得知道的实用功能

- **EspCompare**：在两个不同语言的 esp 之间直接生成字符串对照，**这是把旧版翻译迁移到新版 mod 的正解**。
- **词典**：可从现有 `.strings` 批量构建对照表，复用旧翻译。
- **fuz 映射与播放**：能听音频对应对白——翻译对白时的效率利器。
- **在线翻译接口**、正则批量替换、差异视图、别名完整性检查（Alias Tool Check）、
  简繁转换、XML 导入导出、从 BSA/BA2 提取文件。

## 一条重要边界（发布页明确）

> **"This translator is *not* a tool for to localize/delocalize \*.esp/\*.esm file.
> Use xEdit to perform this kind of task."**

即：**把 esp 在"本地化 / 非本地化"之间转换**要用 xEdit 做，
xTranslator 负责的是**文本内容**，不是文件结构。

## 兼容性与来源

- 官方强调 **"The home for this tool is the Nexus"**，请不要从别处下载。
- 有个经典故障：**Avast 杀毒版本过旧会导致它启动不了**（发布页专门说明）。
- 版本演进里新增了 **Ollama 本地模型**支持（可用本地 LLM 做翻译端点）。

## 相关

- [ESP-ESM Translator](../08-creation/esp-esm-translator.md)（另一套工具）
- [Papyrus 编译器与反编译](../08-creation/papyrus-compiler-decompiler.md)（pex 反编译的另一条路）
- [配音制作完整链路（wav → lip → fuz）](../10-audio/lip-fuz-workflow.md)（fuz 结构）
