---
id: wabbajack
title: Wabbajack（自动安装整合）
category: 07-workflow
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [安装, Wabbajack, 整合包, modlist]
aliases: [自动安装整合, 一键整合, 安装列表]
source: https://wiki.wabbajack.org/
summary: Wabbajack 是什么、它对捏脸/身形这套复杂前置链的独特价值、四条限制（版本敏感、封闭实例、限速、更新清 mod），以及官方安装要点。
---

# Wabbajack

## 是什么

一个**开源的 modlist 自动安装器**：读取 `.wabbajack` 文件，
自动从 Nexus 等来源下载并按作者设定排序/配置，最终产出一个**自带 MO2 实例**的完整可玩环境。

本质是"**把别人的 MO2 配置克隆到你的机器**"，不分发版权文件。

- 官方站：`https://www.wabbajack.org/`
- 官方文档：`https://wiki.wabbajack.org/`
- GitHub：`https://github.com/halgari/wabbajack`

## 对捏脸/身形的独特价值

这正是新手最容易翻车的地方 —— 而 Wabbajack 列表**通常已经把这些做完了**：

| 新手最容易错的 | Wabbajack 列表通常已处理 |
|---|---|
| BodySlide 身形与服装没构建 | **已构建** |
| 骨骼 / SKSE 版本不对 | **已锁定** |
| NPC 美化的 FaceGen 没对齐 | **已对齐** |
| 物理 XML 冲突 | **已配好** |
| 身形与皮肤不同族 | **已匹配** |

所以"我只想好好地玩一个有捏脸有身形的游戏"，Wabbajack 是**最省事的路径**。

## 四条限制（与捏脸相关）

1. **版本极度敏感** —— 很多列表要求特定游戏版本（1.5.97 或 1.6.640 等），
   Steam 自动更新会破坏它；
2. **封闭实例** —— 装完是"成品"，个性化魔改需要 MO2 知识；
   叠加自己的身形/服装**极易冲突**；
3. **无 Nexus Premium 时下载极慢**（被限速）；
4. **列表更新会删除列表外自行添加的 mod**。

## 官方安装要点

- 安装位置 **不能在** Windows 受保护目录（Program Files / Desktop / Documents /
  Downloads / OneDrive 等）；
- 安装位置**不能与游戏目录或另一个列表合并**；
- 失败**先重跑**（支持断点续传）；
- 缺文件可**手动下载放进 `downloads` 文件夹**；
- 需要拥有对应商店的 AE DLC。

## 决策建议

| 你的目标 | 建议 |
|---|---|
| 想尽快玩到"好看的捏脸 + 身形" | 用 Wabbajack |
| 想自己决定每一个 mod | 手动装（从 [`install-order.md`](install-order.md) 开始） |
| 想用别人的底子再自己加 | 可以，但**先学会 MO2 覆盖规则**，见 [`mo2-override-rules.md`](mo2-override-rules.md) |

## 来源

- 定义、开源性质、GitHub：官方站与仓库 README —— **一手**
- 安装位置限制、断点续传、手动下载、AE DLC：Wabbajack 官方文档 —— **一手**
  `https://wiki.wabbajack.org/user_documentation/Installing%20a%20Modlist.html`
- 排错 FAQ：`https://wiki.wabbajack.org/user_documentation/Troubleshooting%20FAQ.html` —— **一手**
- "列表已构建好 BodySlide/FaceGen/物理"与四条限制：官方限制说明 + **社区经验**（限制类）
