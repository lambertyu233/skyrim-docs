---
id: esp-esm-translator
title: ESP-ESM Translator
category: 08-creation
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [翻译, 本地化, 编辑器, 字符串]
aliases: [ESP-ESM Translator, esm 翻译, 翻译工具, 汉化工具, 921, EET]
source: https://www.nexusmods.com/skyrimspecialedition/mods/921
summary: 与 xTranslator 并列的另一套 Bethesda 翻译工具，长于多游戏/多格式与"直接以原始格式编辑"，社区里两套都有人用。
---

# ESP-ESM Translator

## 定位

法国作者 Epervier 666 开发的 Bethesda 文本翻译工具，
支持多款 Bethesda 游戏（Oblivion / Skyrim / Fallout 3 / NV / 4 等），
在**Skyrim SE 的 Nexus 上以 mod 921 分发**。

它与 **xTranslator** 是社区里并存的两套方案。选择依据通常是：

| 需求 | 倾向 |
|---|---|
| 词典复用、EspCompare 做版本迁移、fuz 播放、pex 翻译 | **xTranslator**（本库 [xTranslator（翻译工具）](../08-creation/xtranslator.md)） |
| 强调"以游戏原始格式直接打开编辑"、多游戏统一处理 | **ESP-ESM Translator** |
| 团队协作 / 术语统一 | 两者都提供词典机制，取团队习惯的那套 |

> 社区论坛里向新手推荐翻译工具时，这两者与老的 `tesvTranslator` 常被一起列出；
> **`tesvTranslator` 是更早的一代**，见于 LE 时代的老帖。

## 使用前的通识（两套工具都适用）

1. **先备份**：翻译会写回 esp/esm，改坏了很难回退。
2. **分清两条路线**：
   - 直接改 esp 里的文本 → 产出仍是同一个插件，**兼容性最好但体积不省**；
   - 做成 strings 本地化文件 → 需要配合 esp 的本地化标志，分发时要一起给。
   （结构层面的"本地化/非本地化"转换在 xEdit 做，不在翻译工具里。）
3. **编码**：中文翻译要确认工具输出的编码与游戏读取一致，
   否则表现为乱码或方框。文档目录（`08-creation/` 内其它条目）与本库
   [配置文件体系（哪个 ini 在哪、归谁管）](../11-config/settings-files.md) 都强调过编码问题。
4. **术语表**：先定术语再翻译，后期统一成本极高。

## 相关

- [xTranslator（翻译工具）](../08-creation/xtranslator.md)
- [Papyrus 编译器与反编译](../08-creation/papyrus-compiler-decompiler.md)（脚本内字符串）
- [配置文件体系（哪个 ini 在哪、归谁管）](../11-config/settings-files.md)（编码与文件落点）
