---
id: three-engines-timeline
title: 三引擎脉络：FNIS → Nemesis → Pandora
category: 00-overview
kind: concept
version: 1.0.0
updated: 2026-09-21
tags: [FNIS, Nemesis, Pandora, 历史, 脉络]
aliases: [FNIS 历史, 动作引擎发展史, Nemesis 替代 FNIS, Pandora 由来, timeline, 演进史, fore Shikyo Kira]
source: https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/wiki
summary: 从 fore 的 FNIS 到 Shikyo Kira 的 Nemesis 再到社区共治的 Pandora，十年三代引擎的演进主线。
---

# 三引擎脉络：FNIS → Nemesis → Pandora

## 演进主线（官方口径）

Pandora 官方 wiki 用一句话概括了三代关系：

> First pioneered by Fore through FNIS for Skyrim, then further developed through Nemesis, Pandora is the latest culmination of the decade of work that has gone into the relatively underrecognized field of behaviour.
> （最初由 Fore 通过 FNIS 开创，经 Nemesis 进一步发展，Pandora 是这十年行为领域工作的最新成果。）

| 代次 | 引擎 | 作者 | 出现 | 状态 |
| --- | --- | --- | --- | --- |
| 1 | FNIS（Fores New Idles in Skyrim） | fore | 2012-03 首传，最终版 **7.6**，2020-02-21 更新 | 已停更、已淘汰 |
| 2 | Nemesis Unlimited Behavior Engine | Shikyo Kira | 2019 | 仍可用，但更新不活跃、文档缺失 |
| 3 | Pandora Behaviour Engine+ | Pandora Behaviour Engine Team（Monitor221hz 上传） | 2023-2024 | 活跃开发中，Nexus 版本 v4.4.0-beta |

## 每一代解决了什么

### FNIS（第一代，2012）：开创"补丁"思路

- 由 **fore** 开创了"读补丁、合并输出"的整套范式。
- **闭源**，版本与结构严格由 fore 本人掌控；任何 mod 想支持新行为都要等 fore 更新 FNIS。
- 动画注册走**声明式**（declarative）的 AnimList 文本格式。
- 硬伤：受限于作者维护节奏与硬编码的动画类型，无法跟上现代战斗框架（如 MCO/ABR）。

### Nemesis（第二代，2019）：模板化 + 开源

- 由 **Shikyo Kira** 开发，开源（GPLv3），**向后兼容绝大多数 FNIS mod**。
- 引入**模板（template）机制**：任何人可以制作"行为模板/动画模板"，让社区自行扩展新动画类型，不再等作者发版。
- 每个用户的 Nemesis 有**自己的引擎版本**：装了带 Nemesis 提取文件的 mod 后，会提示"更新引擎"（< 1 分钟），无需等作者更新工具。

### Pandora（第三代，2024）：性能 + 容错 + 全生物支持

- 直接支持 FNIS 与 Nemesis 两套补丁格式，并有自己更高效的新格式。
- **全生物（creature）支持**，跨平台（Windows/Linux/MacOS）。
- **强容错**：非法编辑被隔离并回退到原版，不会拖垮整轮刷补丁。
- 性能提升来自架构（增量(反)序列化、预加载、克制的并行），详见 [Pandora 架构与性能](../04-pandora/pandora-architecture.md)。

## 作者层面的口径

Nemesis 作者 Shikyo Kira 在其 2019 年的说明中对比过 FNIS 与 Nemesis（社区转录，非官方页面）：

> FNIS 是一个补丁工具，其版本和结构严格由 Fore 本人控制……Nemesis 则是开源平台，目标是随时支持任意 mod。Nemesis 自带所有既有动画类型（b、s、so、km…），并可接受自定义行为模板——这意味着 mod 作者能创建的动画类型是**无限的**，这一点与 FNIS 的硬编码不同。FNIS 对用户可安装的动画数量有**硬上限**，Nemesis 则是**软上限**（可远超 20,000，但会被警告）。

> 转引自社区转录：https://ik63.ru/nemesis-unlimited-behavior-engine-ne-rabotaet （原始出处为作者 Discord/论坛发言）

## 相关

- [官方三引擎对比表](engine-comparison.md)
- [FNIS 概览](../02-fnis/fnis-overview.md)
- [Nemesis 概览](../03-nemesis/nemesis-overview.md)
- [Pandora 概览](../04-pandora/pandora-overview.md)
