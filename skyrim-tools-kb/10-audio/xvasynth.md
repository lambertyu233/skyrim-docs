---
id: xvasynth
title: xVASynth（AI 语音合成）
category: 10-audio
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [语音, AI, 配音, TTS, 工具]
aliases: [AI 配音, 生成配音, 语音合成, 44184, Dan Ruta]
source: https://github.com/DanRuta/xVA-Synth
summary: 用游戏角色音色做神经语音合成的桌面应用：逐字母控制音高与时长、支持音色转换与批量合成，是给 mod 做大段新对白的现行主力工具。
---

# xVASynth

作者 **Dan Ruta**，仓库 `DanRuta/xVA-Synth`（GPL-3.0）。
除 Nexus 分发外也在 Steam 上架（xVASynth v2）。

## 技术构成（官方 README）

> **"This is an Electron UI wrapped around inference of FastPitch models trained on voice data from video games."**

- **前端**：Electron（JS）；
- **后端**：Python（FastPitch 模型推理），通过 **localhost:8008** 的 HTTP 服务与前端通信；
- **模型**：**应用本身不含任何音色**——**必须另外安装 voice sets**。
  带 asset 文件的模型按游戏/类别归类，其余进 "Other"。

## 下载与安装

- 官方建议：**尽量从 Nexus 下载应用**（那里的编译版最新）。
- 应用本体可放任意位置；**建议放 SSD**（减少音色加载时间）。
- 音色包放进：`xVASynth/resources/app/models/<游戏>/`
- 首次运行 Windows 可能询问是否允许运行 python 服务脚本——**要点允许**。

## 核心能力

| 能力 | 说明 |
|---|---|
| **逐字母控制** | 每个字母的 **pitch / duration / energy** 都能单独拖，用于控制情绪与重音 |
| **音色转换（v3+）** | 不是 TTS，而是"把一段参考音频重新生成为某个音色"——可录音或拖入音频文件 |
| **ARPAbet 发音** | 用 `{ }` 包裹 ARPAbet 标注精确指定发音；可自建词典；内置 CMUdict（约 13.5 万词，美音） |
| **批量合成** | 用 `.txt` 或 `.csv` 一次生成成百上千行，支持并行（**强烈建议用 GPU**） |
| **3D 音色可视化** | 把音色嵌入投影到 3D 空间方便探索/找音色，可按游戏、性别着色 |
| **插件体系** | 支持前后端（JS / Python）插件 |
| **Nexus API 集成** | 在应用内看音色更新/下载（Premium 可应用内直下） |

## 实务建议（作者在 README 里给的）

- 单段**至少 2 秒、尽量不超过 5 秒**；长文本**拆成小句再在 Audacity 里拼接**。
- 通过改**标点与拼写**来获得不同的输出效果。
- **缩写要按读音拼出来**（如 `xVA` → `Ex vee ay`）。
- 数字会自动转文本，但**年份要手动拆**（`1990` → 写 `19 90` 才读成 nineteen ninety）。
- 音质最好的路径是**逐句精修 pitch/duration**，全自动出的结果会偏"合成味"。

## 与口型的关系（重要）

xVASynth 生成的音频**不会自动带来口型**。`.lip` 需要用 **FaceFXWrapper**
从文本生成，再与音频一起打包成 `.fuz`——完整链路见
[配音制作完整链路（wav → lip → fuz）](../10-audio/lip-fuz-workflow.md)。

> 社区实测的坑：**纯文本生成的 lip 与"精修过节奏的音频"容易不同步**——
> 因为 lip 是基于文本+节奏算的，不是从波形反推的。
> 详见 [FaceFXWrapper（生成口型 .lip）](../10-audio/facefxwrapper.md)。

## 相关

- [xVATrainer（训练自有音色）](../10-audio/xvatrainer.md)（训练自己的音色）
- [FaceFXWrapper（生成口型 .lip）](../10-audio/facefxwrapper.md)、[Yakitori Audio Converter（fuz/wav/xwm 互转）](../10-audio/yakitori-audio-converter.md)、[配音制作完整链路（wav → lip → fuz）](../10-audio/lip-fuz-workflow.md)
- [Creation Kit（官方创作工具）](../08-creation/creation-kit.md)（把音频接进对话记录）
