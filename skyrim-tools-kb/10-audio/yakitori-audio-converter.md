---
id: yakitori-audio-converter
title: Yakitori Audio Converter（fuz/wav/xwm 互转）
category: 10-audio
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [音频, fuz, xwm, 转换, 打包, 工具]
aliases: [Yakitori, Yakitori Audio Converter, fuz 打包, 音频转换, 解包 fuz, 73100]
source: https://www.nexusmods.com/fallout4/mods/9322
summary: 在 `.fuz` / `.wav` / `.xwm` 等格式之间批量互转的 GUI：既能「wav + lip → fuz」打包配音，也能反向从自带语音里提取音频。
---

# Yakitori Audio Converter

一个专做 **Bethesda 音频格式互转**的 GUI 工具（Fallout 4 侧 Nexus 页 `mods/9322`；
Skyrim 侧亦有分发）。支持 fuz / xwm / wav 等格式的组合转换。

## 两种常用模式

| 方向 | 用途 |
|---|---|
| **打包**：`wav + lip → fuz` | 做 mod 配音的最后一步（游戏读的是 fuz） |
| **解包**：`fuz → xwm (+ lip)` | 从游戏自带的语音包里提音频做参考 |

**关键选项：`Mode` / "Extract lip" 或 "Ignore lip"**——
想只要音频就选 **Ignore lip**，避免多出一个你不需要的 lip 文件。

## 操作流程（官方文档口径）

1. 通过 File 菜单或拖拽添加文件；
2. 选择输出格式；
3. 选择输出目录；
4. （可选）设编码器/解码器参数——**不确定就保持默认**；
5. 按 Convert；
6. 完成后文件列表**按转换结果分组**，失败的可在右键菜单里看每个文件的具体错误。

## 它依赖外部程序（这点很关键）

xwm 的编解码**调用外部工具**（Microsoft 的 `xWMAEncode.exe`；音频文件输入还需要 `ffmpeg.exe`）。
因此：

- 某些输入格式需要你**自己把 `ffmpeg.exe` 放进 Yakitori 目录**；
- 报错信息里会带上外部命令的输出——**照着看就能定位**。

官方列出的典型错误与对策：

| 错误现象 | 原因与对策 |
|---|---|
| `xWMAEncode.exe ... ExitCode: -2147221501`（编码 xwm） | **文件体积超过上限** → 降低采样率或比特率（如 22.05 kHz / 32 kbps），或先转成 aif 再转 |
| `Input file type is neither PCM nor xWMA`（解码 xwm） | 输入不是 PC 版 fuz(xwm) 格式 |
| `Requested audio format unsupported` | 同上，格式不兼容 |
| `E_NOTIMPL (Not implemented)` | 采样率与 xwm 比特率的组合**不受支持** |

## 官方自己写明的限制

> **"There may be a bug in this tool. Please be sure to MAKE A BACKUP of the original audio files."**

另外：日志窗口行数过多会影响性能，需定期清空；界面（.NET ListView 分组）较慢，
偶尔需要打开 About 对话框重置。

## 其它可替代/互补的做法

- **Creation Kit 内直接生成 lip**（"Generate Lip File"）——前提是 CK 能找到你的音频文件；
- 社区另有 **Unfuzer** 一类"只做打包/解包"的轻量工具
  （社区经验，见 LoversLab / Nexus 论坛的音频制作讨论串）。

## 相关

- [配音制作完整链路（wav → lip → fuz）](../10-audio/lip-fuz-workflow.md)（完整链路）
- [FaceFXWrapper（生成口型 .lip）](../10-audio/facefxwrapper.md)（生成 lip）
- [BSA / BA2 归档工具](../05-assets/archive-tools.md)（从 bsa 里取出 fuz）
- [Creation Kit（官方创作工具）](../08-creation/creation-kit.md)
