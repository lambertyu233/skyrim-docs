---
id: facefxwrapper
title: FaceFXWrapper（生成口型 .lip）
category: 10-audio
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [口型, lip, 音频, 命令行, 工具]
aliases: [lip 生成, 口型文件, lip file, 生成 lip, FaceFX, 不同步]
source: https://github.com/Nukem9/FaceFXWrapper
summary: 不开 Creation Kit 就能从 wav + 文本生成游戏原生 .lip 的命令行工具；需要从 CK/GECK 里取 FonixData.cdf，且输入必须是 16kHz 单声道。
---

# FaceFXWrapper

作者 **Nukem9**。README 一句话定位：
**"A utility to generate native LIP files for TES/Fallout games without using or installing the Creation Kit."**

支持 Skyrim、Skyrim SE、Fallout 3 / NV / 4。

## 命令行（README 原文格式）

```
FaceFXWrapper [Type] [Lang] [FonixDataPath] [WavPath] [ResampledWavPath] [LipPath] [Text]
```

参数含义：

| 参数 | 取值 / 说明 |
|---|---|
| `Type` | `Skyrim` 或 `Fallout4` |
| `Lang` | `USEnglish` |
| `FonixDataPath` | `FonixData.cdf` 的路径（**见下方"它不提供这个文件"**） |
| `WavPath` | 源音频 |
| `ResampledWavPath` | 重采样后的 wav **输出**路径 |
| `LipPath` | 生成的 `.lip` **输出**路径 |
| `Text` | 对白文本（用引号包起来） |

官方示例：

```
FaceFXWrapper Skyrim USEnglish FonixData.cdf c00jorrvaskrfight__000bd639_1.wav resampled.wav output_1.lip "My special sentence"
```

**跳过重采样阶段**的用法（你自己已备好重采样 wav）：

```
FaceFXWrapper Fallout4 USEnglish FonixData.cdf my_precreated_resampled.wav output_2.lip "My special sentence"
```

## 两个硬约束

1. **输入音频必须是 16 kHz、16 bit、单声道。**
   不满足就让工具去重采样（第一种用法），或自己先转好（第二种用法）。
2. **`FonixData.cdf` 不随工具提供**，必须从 **G.E.C.K. 或 Creation Kit** 里取
   —— 通常在编辑器文件的 `\Data\Sound\Voice\Processing\` 下。

## 为什么口型会不同步（关键认知）

它算口型的输入是**文本 + 音频**，靠 **Fonix 数据**做音素→口型的映射。
所以：

- 若你的音频是"有情绪、有停顿、有语气变化"的真实演绎，
  而文本只是平铺的句子，**口型节奏就会明显对不上**。
- 社区实测的结论是：**纯文本生成的 lip，只有在音频节奏也"规整"时才准**；
  想要好效果要么精修音频节奏、要么反复试。

> 另一条社区观察：**"从波形反推口型"的鲁棒方案并不存在**，
> 这类工具本质是**文本驱动**的。所以对白合成里的"口型难以同步"是结构性问题，
> 不是工具没调好。

## 授权注意

README 明确：它**使用了 Creation Kit 的代码**，受 **Bethesda 的许可协议**约束；
压缩资源文件归 Bethesda Softworks LLC。

## 相关

- [配音制作完整链路（wav → lip → fuz）](../10-audio/lip-fuz-workflow.md)（完整链路）
- [Yakitori Audio Converter（fuz/wav/xwm 互转）](../10-audio/yakitori-audio-converter.md)（把 lip + wav 打包成 fuz）
- [xVASynth（AI 语音合成）](../10-audio/xvasynth.md)（音频来源）
- [Creation Kit（官方创作工具）](../08-creation/creation-kit.md)（CK 内也能生成 lip）
