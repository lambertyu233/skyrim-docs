---
id: lip-fuz-workflow
title: 配音制作完整链路（wav → lip → fuz）
category: 10-audio
kind: tutorial
version: 1.0.0
updated: 2026-09-22
tags: [配音, 口型, fuz, 工作流, 教程]
aliases: [配音流程, 加配音, 做配音, 语音文件放哪, Sound Voice 路径, fuz 是什么, 对话没声音]
source: https://github.com/Nukem9/FaceFXWrapper
summary: 从「生成音频」到「游戏里听到并看到嘴动」的五步链路，含文件放置路径与三个最常卡住的环节。
---

# 配音制作完整链路

## 五步链路

```
① 生成/录制音频（wav）
   └─ xVASynth / xVATrainer / 自己录
② 生成口型（.lip）
   └─ FaceFXWrapper（脱离 CK）或 CK 内 "Generate Lip File"
③ 打包成游戏格式（.fuz）
   └─ Yakitori Audio Converter（wav + lip → fuz）
④ 放到正确路径
   └─ Data\Sound\Voice\<你的插件名>\
⑤ 在对话记录里接上
   └─ Creation Kit（VOICE TYPE / 音频框 / from wav）
```

## 三个最容易卡住的环节

### 1. 放了 wav 却没声音 → 游戏读的是 `.fuz`

游戏不直接读裸 `.wav`。**必须打包成 `.fuz`**（内部是 xwm 音频 + lip）。
这是"我明明放了音频文件"最常见的原因。

### 2. 有声音但嘴不动 → 缺 `.lip`

`.lip` 是独立文件，需要单独生成。两条路：

- **FaceFXWrapper**：命令行、可批量、不依赖 CK，但需要 `FonixData.cdf`
  且输入必须是 **16 kHz 单声道**（见 [FaceFXWrapper（生成口型 .lip）](../10-audio/facefxwrapper.md)）；
- **CK 内生成**：在对话编辑窗里点音频框 → "from wav" → "Generate Lip File"。
  前提是 **CK 能找到你的 wav**——文件必须在正确路径、命名正确，
  否则 CK 的文件列表里**只会显示原版音频**（这是社区里反复出现的困惑）。

### 3. 嘴动了但**对不上** → 结构性限制

口型是**文本驱动**（文本 → 音素 → 口型映射），不是从波形反推。
所以一段情绪起伏大的真实演绎配上平铺文本，必然不同步。
社区实测结论：想要好效果，要么把音频节奏做得规整，
要么**逐句反复调整**（详见 [FaceFXWrapper（生成口型 .lip）](../10-audio/facefxwrapper.md) 与
Nexus 论坛的 lip/fuz 讨论串）。

## 路径与命名

- 路径：`Data\Sound\Voice\<插件名>\<VoiceType>\<文件名>.fuz`
  （具体子目录结构由你的对话记录里的 Voice Type 决定）
- 命名：CK 里音频框选中的文件名就是它要找的文件名，**命名不一致 = 找不到**。

## 反向：提取游戏自带语音

用 **Yakitori** 打开 `.fuz` → 选 **Ignore lip** → 得到 `.xwm` → 再转成
ogg/wav（需要 ffmpeg 或在线转换）。用于做参考、做字幕或做数据集。
（社区教程常见做法）

## 检查清单（做完一项勾一项）

- [ ] wav 单声道、采样率满足要求（FaceFXWrapper 要 16 kHz；CK 路径另有要求）
- [ ] `.lip` 已生成且与音频同名
- [ ] 已打包为 `.fuz`，且**不是**直接放 wav
- [ ] 路径与文件名和 CK 对话记录里的完全一致
- [ ] 关掉 Papyrus 之外的调试日志，进游戏实测

## 相关

- [xVASynth（AI 语音合成）](../10-audio/xvasynth.md)、[xVATrainer（训练自有音色）](../10-audio/xvatrainer.md)
- [FaceFXWrapper（生成口型 .lip）](../10-audio/facefxwrapper.md)、[Yakitori Audio Converter（fuz/wav/xwm 互转）](../10-audio/yakitori-audio-converter.md)
- [Creation Kit（官方创作工具）](../08-creation/creation-kit.md)
- [对话系统（Dialogue）](../../creation-kit-kb/03-game-systems/dialogue.md)
- [常见错误认知](../12-sources/common-misconceptions.md) 第 17、18 条
