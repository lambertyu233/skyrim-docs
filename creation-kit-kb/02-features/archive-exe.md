---
id: archive-exe
title: Archive.exe（BSA 打包）
category: 02-features
version: 1.0.0
updated: 2026-09-20
tags: [archive, bsa, packaging, tool]
source: https://ck.uesp.net/wiki/Archive.exe
summary: Archive.exe 是 CK 自动归档之外的 BSA 打包替代工具，位于游戏安装目录，建议以 .bsa 替代松散文件。
status: stable
kind: tool
---

# Archive.exe（BSA 打包）

`Archive.exe` 是《天际》自带的资源打包工具，用于将 MOD 的资源（网格、贴图、声音等）打包为 **`.bsa`** 归档。它是 CK 内置「自动归档」功能的可靠替代。

## 为什么用 Archive.exe

- CK 的自动归档面向 Steam 创意工坊上传，存在局限：不会自动收集全部依赖文件，界面难用，且在部分机器上会无故失败。
- Archive.exe 即使 CK 报错也能工作，可打包任意复杂度的 MOD。

## 安装位置

```
<安装目录>\Steam\steamapps\common\skyrim\Archive.exe
```

图标为「积木块」样式。

## 为何优先用 .bsa 而非松散文件（Loose Files）

- **易安装/卸载**：玩家不易装错；临时移除某个 MOD 只需移走其 `.bsa`。
- **便于排错**：Skyrim 使用外部脚本，松散脚本多了会难以分辨问题来源；`.bsa` 移走即彻底失效，无需翻找脚本列表。
- **切换角色配置**：带 `.bsa` 的 MOD 可临时移除/恢复，方便不同流派（如潜行）的切换。

> 打包 `.esp` 依赖的网格/贴图替换 MOD 为 `.bsa`，也能在画面出错时大幅减少麻烦。

## 相关条目

- [Data 目录与插件格式](../01-installation/data-files.md) — .bsa 的定位
- [编辑器界面](editor-interface.md)

> 来源：[UESP Archive.exe](https://ck.uesp.net/wiki/Archive.exe)
