---
id: xvatrainer
title: xVATrainer（训练自有音色）
category: 10-audio
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [语音, AI, 训练, 配音, 工具]
aliases: [训练音色, 自训练语音模型, 做音色包, 克隆声音]
source: https://github.com/DanRuta/xva-trainer
summary: xVASynth 作者配套的训练工具：用你自己的音频数据训练一个可被 xVASynth 加载的音色模型——自建配音或非官方音色的正路。
---

# xVATrainer

`xVASynth` 官方 README 里以 **"New: xVATrainer, for training your own custom voices"** 的形式
指向同作者的独立仓库 `DanRuta/xva-trainer`。

## 它解决什么

xVASynth 只是**推理框架**，音色包要另外装。
当你要的音色**没有现成包**时（自创角色、非官方语种、某个特定声线），
就需要自己训练一个。

## 什么时候用它 / 不用它

| 场景 | 选择 |
|---|---|
| 有现成音色包 | 直接用 xVASynth，不碰这个 |
| 需要"某个角色但社区没有包" | 训练（注意版权与授权，见下） |
| 需要完整的新语言支持 | 训练 + 自建 ARPAbet 词典（xVASynth 侧） |
| 只是想把一段音频换成已有音色 | **用 xVASynth 的音色转换（v3+）**，不必训练 |

## 训练前的现实预期

- 训练属于**机器学习工程活**：数据质量（干声、统一采样率、足够时长）比参数更重要。
- 建议的准备顺序：先在 xVASynth 里确认目标音色确实不存在 →
  收集**干净的单一说话人音频** → 按工具文档切分与标注 → 训练 → 把产物按
  `xVASynth/resources/app/models/<游戏>/` 的结构放好 → 在应用里验证。
- **算力**：训练比推理重得多，GPU 是实际前提。

## 授权与伦理（必须写进流程的一步）

- 用**真实配音演员**的声音做克隆，在多数社区属敏感甚至被禁止的行为——
  发布前务必确认：原作者的授权、所使用 mod 的 permissions、
  以及目标平台的规则。
- 用**自己录制**的声音训练是最干净的做法。
- 生成的内容若再分发给他人，还需要考虑**训练数据来源**的许可链。

## 相关

- [xVASynth（AI 语音合成）](../10-audio/xvasynth.md)（推理侧与音色安装路径）
- [配音制作完整链路（wav → lip → fuz）](../10-audio/lip-fuz-workflow.md)（生成完音频之后的完整链路）
- [Creation Kit（官方创作工具）](../08-creation/creation-kit.md)（把音频接入对话）
