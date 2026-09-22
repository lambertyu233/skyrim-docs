---
id: unreliable-sources
title: 不可信来源警示
category: 12-sources
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [来源, 不可信, 内容农场, 警示]
aliases: [别信, 假教程, CSDN, 聚合站, unreliable sources, AI生成文章]
source: https://www.nexusmods.com/skyrimspecialedition/
summary: 模改领域里几类系统性不可信的来源，以及它们在工具话题上的典型错误形态——识别特征比黑名单更重要。
---

# 不可信来源警示

黑名单永远追不上新站；**识别特征**才是可复用的。以下按"错误形态"分类。

## 一、内容农场 / AI 聚合站

典型：CSDN 的技术博客、toolify 类 AI 工具导航、`*.blogspot`/`*.xyz` 的"教程"、
以及把 Nexus 描述重新翻译一遍的选题站。

**识别特征**：

- 段落**极其工整**、小标题对称、每段长度接近——像生成物不像人写的。
- 出现**无法验证的参数**：具体到小数点的数值、不存在的命令行开关、编造的默认值。
- 引用**不给出处**，或"据某论坛"这类虚指。
- 页脚有大量 SEO 关联链接、却没有任何作者身份信息。

**已知的典型错误**（本工作区在其他库里逐条取证过）：

- 编造 OAR 的 wiki（OAR **确实没有 wiki**），编造并不存在的 `IsPlayer` 条件——
  见 [不可信来源警示（已实测的编造案例）](../../oar-kb/09-sources/unreliable-sources.md)（列出 CSDN 的 12 处编造）。
- 把 Nexus 镜像站的自写描述当作作者原话引用，进而传播错误的路径与版本号。

## 二、镜像 / 重托管站

把 Nexus 上的 mod 搬到自己站上，并**重写一段介绍**。描述里常出现：

- 错误的作者署名（作者被替换成搬运者）。
- 已经不存在的版本号（"最新版本 vX.Y"其实是三年前的）。
- 参数被"意译"成错的（例如把 `-quickautoclean` 写成 `-autoclean`）。

> 判据：**Nexus 是绝大多数工具的官方发布页**。工具作者在 Nexus 描述里写的"Requirements"
> 与 "Permissions" 段才是真话；第三方站点的转述一律视为不可信。

## 三、"看起来很像官方"的域名

模式：`de.github.com/...`、`github.org/...`、`ghub.com/...`、`x.osmenoga.com/DanRuta/...`
——这些**不是 GitHub**。它们的内容常是抓取的快照，可能停留在几年前。

**判据**：官方仓库一律形如 `https://github.com/<owner>/<repo>`。
识别真实性还可以看页面里是否出现 **Releases / Actions / Insights** 这些真 GitHub 才有的标签页。

## 四、社区经验里的"高赞但错"

论坛、Reddit、Discord 的回答属**社区经验**，可用，但必须与一手来源交叉验证。已知高发错误：

- "装完 mod 用游戏启动器进游戏就行"——**SKSE 插件不会加载**，必须用 `skse64_loader.exe`。
- "禁用 mod 就干净了"——Papyrus 脚本实例**留在存档里**，需要 FallrimTools 才清得掉。
- "LOOT 排好序就没冲突了"——LOOT 只管插件顺序，**记录级冲突它看不见**。
- "同时装 Crash Logger 和 Trainwreck 更保险"——两者**只能装一个**，同时装会互相抢钩子。

## 五、本库的引用纪律

1. 每条结论必须落到**条目路径**（如 [xEdit / SSEEdit（记录编辑器与冲突检测）](../04-loadorder/xedit.md)）。
2. 三类信息在正文里**明示可分**：一手源 / 社区经验 / 本机实测。
3. 涉及具体版本号、路径、命令行开关的陈述，**必须**可回到 L1/L2 来源；
   回不去的就写成"未确认"，或直接不写。

> 相关：[一手来源清单](../12-sources/primary-sources.md)（白名单）、[常见错误认知](../12-sources/common-misconceptions.md)（错误认知清单）。
