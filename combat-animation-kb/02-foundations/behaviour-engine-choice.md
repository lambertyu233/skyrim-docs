---
id: behaviour-engine-choice
title: 行为引擎选型：Pandora 是现役答案
category: 02-foundations
kind: concept
version: 1.0.0
updated: 2026-09-30
tags: [Pandora, Nemesis, FNIS, 选型, 行为引擎]
aliases: [行为引擎怎么选, pandora 和 nemesis, FNIS 过时, 补丁器选择, engine choice]
source: https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus
summary: FNIS（2020 停更）→ Nemesis（2021 停更）→ Pandora（现役）；本条只给结论，机制详见 behaviour-engine-kb。
---

# 行为引擎选型：Pandora 是现役答案

## 一句话

三选一：FNIS **7.6（2020-02）后停更**、Nemesis **0.84-beta（2021-12）后归档**、**Pandora 活跃（v4.4.0-beta，2026-08）**。新装选 Pandora，且与 FNIS/Nemesis 不要同时运行。

## 结论速览（均有官方页面佐证）

| 引擎 | 状态 | 关键证据 |
|---|---|---|
| FNIS | 淘汰 | LE 页最终文件 "FNIS Behavior 7_6"（2020-02-22）；BFCO 官方原话 "FNIS is outdated, please use Pandora"【一手源】 |
| Nemesis | 停更 | GitHub README：仓库已归档、"being written from scratch"；Nexus 最后更新 2021-12-13（0.84-beta）【一手源】 |
| Pandora | 现役 | 官方仓库 [Monitor221hz/Pandora-Behaviour-Engine-Plus](https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus)；作者原话 "A modular and lightweight behavior patching engine… including creatures and humanoids"、向下兼容 Nemesis 与 FNIS 两种补丁格式【一手源】 |

## 常被搞错的两点

- **Pandora 作者不是 shikyZ**：官方仓库在 **Monitor221hz**（Nexus 署名 Pandora Behaviour Engine Team）名下——与 Nemesis 作者 ShikyoKira 拼写相近容易混【一手源】。
- Pandora 是外部补丁工具，在它自己的界面里勾选要打补丁的 mod 后 Launch；**各动画 mod 的 FOMOD 安装器里才需要选 "Pandora" 选项**。MO2 下建议输出到专门的 "Pandora Output" 空 mod（README Quickstart）【一手源】。

## 深入阅读（机制、格式、排错）

- 三引擎对比与时间线：[behaviour-engine-kb/00-overview/engine-comparison.md](../../behaviour-engine-kb/00-overview/engine-comparison.md)
- Pandora 安装与排错：[behaviour-engine-kb/04-pandora/pandora-install.md](../../behaviour-engine-kb/04-pandora/pandora-install.md)
- 补丁器与替换器的分工：[behaviour-engine-kb/01-principles/patcher-vs-replacer.md](../../behaviour-engine-kb/01-principles/patcher-vs-replacer.md)
