---
id: ini-files
title: INI 文件体系
category: 01-installation
version: 1.0.0
updated: 2026-09-20
tags: [ini, config, skyrimeditor, settings]
aliases: [INI 文件, Skyrim.ini, SkyrimPrefs.ini, ini 配置在哪]
source: https://ck.uesp.net/wiki/INI_files
summary: Skyrim 与 Creation Kit 的配置分层为自动生成、用户自定义与 MOD 定义三类 INI，后者可覆盖前者。
status: stable
kind: reference
---

# INI 文件体系

INI 文件控制《天际》与 Creation Kit 的大量运行参数。理解其**层级覆盖关系**是排错与优化的基础。

## 自动生成的 INI（被 Steam 校验覆盖）

- 游戏：`Skyrim.ini`、`SkyrimPrefs.ini`
- 编辑器：`SkyrimEditor.ini`、`SkyrimEditorPrefs.ini`
- 预设模板：`low.ini`、`medium.ini`、`high.ini`、`VeryHigh.ini`、`Skyrim_default.ini`
- 注意：校验本地游戏缓存（Validate Local Game Files）时，Steam 会**还原**这些文件中的改动。

## 用户自定义的 INI（优先于自动生成）

- `SkyrimCustom.ini` → 覆盖 `Skyrim.ini`
- `SkyrimEditorCustom.ini` → 覆盖 `SkyrimEditor.ini`

将个人修改放在 `*Custom.ini` 中，可避免被 Steam 还原。

## MOD 定义的 INI

- 命名与插件同名（如 `screenshots.esp` 对应 `screenshots.ini`）。
- 仅当该插件被游戏加载时才生效，用于覆盖 `Skyrim.ini` 中的设置。
- MOD 定义的 INI 会随插件**自动上传到 Steam 创意工坊**。

### 示例

```ini
; 文件: Skyrim\Data\screenshots.ini  （配合 screenshots.esp）
[Display]
bAllowScreenshot=1
```

## Papyrus 相关设置

脚本层面的 INI 设置在 [INI Settings (Papyrus)](https://ck.uesp.net/wiki/INI_Settings_(Papyrus))；运行时也可通过
`Utility.SetINIBool / SetINIFloat / SetINIInt / SetINIString` 读写。

## 相关条目

- [获取与启动](install-and-launch.md)
- [Data 目录与插件格式](data-files.md)

> 来源：[UESP INI files](https://ck.uesp.net/wiki/INI_files)
