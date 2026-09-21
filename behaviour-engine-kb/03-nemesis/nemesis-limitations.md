---
id: nemesis-limitations
title: Nemesis 的局限：文档缺失、大列表崩溃、更新停滞
category: 03-nemesis
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [Nemesis, 局限, 崩溃, 文档, overwrite]
source: https://www.nexusmods.com/skyrimspecialedition/mods/60033
summary: Nemesis 最大的短板是"中级以上无公开文档"，叠加超大 modlist 下崩溃与更新不活跃，促成了 Pandora 的接替。
---

# Nemesis 的局限：文档缺失、大列表崩溃、更新停滞

## 1. 文档缺失（最致命的短板）

Nemesis 官方描述页原话：

> For use case that is above *Intermediate* level, as there is no public documentation available atm, so please contact Shikyo Kira through discord directly or ask in the discord server.
> （对于**中级以上**的使用场景，目前**没有公开文档**，请直接通过 Discord 联系 Shikyo Kira，或在 Discord 服务器中提问。）

对比：Pandora 有官方 GitHub Wiki（[本库主要来源](../07-sources/official-sources.md)）；FNIS 有作者一手文档（FNIS for Modders Documentation）。**只有 Nemesis 的作者层用法没有公开文档**——这是它最常被诟病之处。

## 2. 超大 modlist 下易崩溃

- 社区大量反馈：动画数量极大时 Nemesis 可能**在打补丁过程中崩溃**，需要**反复重跑**才成功。
- 常见对策：定位冲突 mod 移除，**或直接改用 Pandora**。

相关社区反馈（Nexus 论坛 "PANDORA behaviour engine as a NEMESIS replacement?"）：

> i use pandora it's absolute amazing. **Nemesis is death to me, constant crash, beast animations troubles all the time** etc.

> 来源：https://forums.nexusmods.com/topic/13471680-pandora-behaviour-engong-as-a-nemesis-replacement

## 3. 更新不活跃

Nemesis 由个人作者维护（Shikyo Kira），更新节奏慢；社区普遍视其为"事实上的收尾项目"，并预期 Pandora 接替。作者当年也自认"仍处于 beta 阶段"。

## 4. 输出落在 overwrite（管理体验差）

- MO2 下 Nemesis 生成的补丁默认写入 **overwrite 文件夹**，需手动整理进命名 mod（如 "Nemesis Output"）才能在切换 profile 时保留。
- 社区经验（烽火 MOD 指南）：
  - **每次运行前清空 overwrite 文件夹**，否则易导致动作不生效；
  - **卸载后也要清空 overwrite** 并重装整合包，否则动作不生效。

> 来源：https://magicskyrim.net/archives/23507

## 5. 相关报错编号

中文社区整理的 Nemesis 常见报错（见 [常见报错](../06-practices/troubleshooting-common.md)）：

- **2006** → 装 Creature Behaviour – WereWolf Addon 后重刷；
- **1210** → 删除 mod 目录下所有 `werewolfbeast` 文件夹；
- **6001 / 攻击移动莫名弯腰** → 社区有修复版（0.84）可用。

## 结论

Nemesis 仍能胜任"中等规模、以人形动画为主"的 modlist；但当规模变大、或需要完整生物支持时，Pandora 在**稳定性、性能与文档**三方面都更有优势——这也是本库把它列为"上一代"的原因。

## 相关

- [Nemesis 概览](nemesis-overview.md)
- [Pandora 概览](../04-pandora/pandora-overview.md)
- [如何选择引擎](../06-practices/choosing-engine.md)
