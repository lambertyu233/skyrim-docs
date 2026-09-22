---
id: editor-plugins
title: 编辑器插件（写脚本/配置的外围工具）
category: 08-creation
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [编辑器, 插件, 语法高亮, 生产力]
aliases: [Notepad++, VSCode, papyrus 插件, 写脚本工具, sublime]
source: https://ck.uesp.net/wiki/Compiling_Scripts
summary: 给 Papyrus / JSON / INI 配一套称手编辑器的做法：语法高亮、跳转、编译快捷键、日志过滤——纯效率工具，不装也能做 mod。
---

# 编辑器插件

CK 自带的脚本编辑窗口功能有限。真正写脚本的人基本都在外部编辑器里写，
再回到 CK 或命令行编译。下面是**按用途**的清单，不绑定具体插件名——
这类项目更迭快，请以各自发布页为准。

## 1. 写 Papyrus（`.psc`）

| 需要 | 怎么满足 |
|---|---|
| 语法高亮 | 装 Papyrus 语法定义（Notepad++ / Sublime / VS Code 都有社区维护的版本） |
| 函数跳转 / 补全 | 部分编辑器插件支持解析 `Data\Scripts\Source` 提供补全 |
| 一键编译 | 配一个"外部工具/任务"调用 `PapyrusCompiler.exe`，参数 `-import` 指向 Source 目录 |
| 批量编译整个 mod | 写个脚本遍历 `.psc` 逐个编译，比在 CK 里点快得多 |

**要点**：编译必须带 `-import "<game>\Data\Scripts\Source"`，
否则报"找不到父类/类型未知"。→ [Papyrus 编译器与反编译](../08-creation/papyrus-compiler-decompiler.md)

## 2. 写配置（`.json` / `.ini` / `.yaml`）

MCM Helper、SPID/KID、OAR `config.json`、Synthesis 设置等都是结构化文本。
通用建议：

- 用**带 JSON 校验**的编辑器（VS Code / Notepad++ 的 JSON viewer），
  一眼看出多余逗号、注释位置错误；
- `.ini` 注意**编码**：多数工具要 UTF-8，带 BOM 与否视工具而定（见 [配置文件体系（哪个 ini 在哪、归谁管）](../11-config/settings-files.md)）；
- 大文件用**折叠 + 搜索**而不是肉眼找（SPID 的 `_DISTR.ini` 常常上千行）。

## 3. 看日志

- **Papyrus log** 用支持"按关键词高亮/过滤"的编辑器打开，比全文搜索快。
- **Crash log** 建议直接用在线分析器（[Crash Log Analyzer（崩溃日志解读）](../09-diagnostics/crash-log-analyzer.md)），
  而不是人工读地址行。

## 4. 浏览 mod 目录

- **MO2 的文件树与冲突面板**本身就承担了一部分"编辑器"职责
  （看某个文件最终来自哪个 mod）→ [文件树、隐藏文件与冲突面板](../../mo2-usvfs-kb/05-usage/hide-files-and-filetree.md)
- **NifSkope / xEdit** 是资产与记录的专用"浏览器"。

## 相关

- [Papyrus 编译器与反编译](../08-creation/papyrus-compiler-decompiler.md)
- [Crash Log Analyzer（崩溃日志解读）](../09-diagnostics/crash-log-analyzer.md)
- [配置文件体系（哪个 ini 在哪、归谁管）](../11-config/settings-files.md)
- [Mod Organizer 2（工具视角）](../03-managers/mo2-tool.md)
