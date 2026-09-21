---
id: what-is-oar
title: OAR 是什么：它替换的到底是什么
category: 00-overview
kind: concept
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 入门, 定位, SKSE]
aliases: [OAR 是什么, OAR 干嘛的, Open Animation Replacer, 替换动画, 它替换什么]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: Open Animation Replacer 是一个 SKSE 框架插件，在游戏请求某个"已有动画"时按可配置条件改播另一个 hkx 文件；它不新增动画命令，因此与 FNIS/Nemesis/Pandora 是互补关系。
---

# OAR 是什么：它替换的到底是什么

## 一句话定义

**Open Animation Replacer（OAR）** 是一个 **SKSE 框架插件**：当游戏要播放某个动画时，它拦截这个请求，检查你写的条件，命中就把请求**重定向到另一个 `.hkx` 文件**。

作者（Ersh）在 Nexus 发布页上给出的原话是：

> A SKSE framework plugin that **replaces** animations depending on configurable conditions. In-game editor. Backwards compatible with more features. Extensible by other SKSE plugins. Supports SE/AE/VR. Open source.

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## 关键：替换的键是「路径 + 文件名」，不是「动作」

这是理解 OAR 的**第一性原理**，也是绝大多数「改了没效果」的根因。

游戏的行为图（behavior）里写死了一条条引用，形如：

```
Animations\Bow_IdleDrawn.hkx
Animations\SneakBow_IdleDrawn.hkx
Animations\SneakWalk_Forward.hkx
```

当游戏要播「持弓瞄准待机」时，它去请求 `Bow_IdleDrawn.hkx`。OAR 在**这一步**拦截，问：

> 在我扫描到的所有 submod 里，谁的目录下放着一个叫 `Bow_IdleDrawn.hkx` 的文件、且条件命中了？

再挑**优先级最高**的那个，把请求重定向过去。

由此推出三条铁律：

| # | 铁律 | 推论 |
| --- | --- | --- |
| 1 | 文件名必须等于**目标状态下游戏请求的原始文件名** | 文件名错 = 永远不生效，且**不会有任何报错** |
| 2 | 「换不到」优先怀疑**文件名**，而不是条件 | 条件写错最多是不命中；文件名写错是根本不会被问 |
| 3 | **一个事件名 = 一个文件**，不是「一段动作」 | 你以为的「一整套拉弓动作」底层是 4 个互不相干的文件；只换 idle，一移动就掉回原版 |

完整的展开见 [替换的心智模型](../08-practices/animation-key-model.md)。

## 核心能力（官方功能列表）

- 基于可配置条件的**动态动画替换**
- 与 DAR 制作的 mod **完全向后兼容**
- 大量**新条件**与对既有条件的改进（例如支持关键字 **EditorID**）
- 支持**成对动画（paired animations）**与**非角色动画**
- 在**动画循环（loop）**与**回声（echo）**时正确替换
- **过滤重复的替换动画**（按内容哈希去重，不改变结果，但能显著降低动画数量占用）
- **动画变体**：随机或顺序播放
- **mod 级条件预设（PRESET）**，供各 submod 复用，减少重复
- submod **附加设置**：Constant polling、循环时保留随机结果、共享随机结果、自定义混合时间、忽略 No Triggers 标记、必需项目名、动画文件夹覆盖
- **游戏内编辑器**：改条件 / 优先级 / 开关并立刻看到效果；可**预览**任何替换动画
- **动画日志**与**动画事件日志**
- 主菜单预加载动画 + 预加载进度条
- 动画数量上限提升到**每项目 32767**（实验性可到 65534）
- 增大 Havok 堆，动画多时更稳定
- 给其他 SKSE 插件用的 **API**（可注册自定义条件）
- 全部通过 SKSE 实现，**可随时安装/卸载**

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## 它**不是**什么（澄清三条）

| 常见误解 | 事实 |
| --- | --- |
| 「OAR 是另一个动作引擎，能替代 FNIS/Nemesis/Pandora」 | **不能**。OAR 只**重定向已有动画命令**；给游戏新增动画命令（poser、舞蹈、成人动画那类 `"7GOM34" → hkx` 的新条目）仍然只能靠补丁器。详见 [Patcher 与 Replacer 的分工](replacer-vs-patcher.md)。 |
| 「OAR 是 DAR 的逆向工程改版」 | **不是**。作者明确说除少数"与游戏代码交互且只能有一种实现方式"的部分外，**不包含任何 DAR 代码**。 |
| 「装 OAR 要删掉 DAR」 | **不需要删 mod**，但 **OAR 本体与 DAR 本体不兼容**（两个插件不能同时启用）。放在 `DynamicAnimationReplacer` 文件夹里的老 mod 会被照常读取并转换。 |

## 与 DAR 的取舍

作者在描述里说明了动机：DAR 长期停更且**闭源**，导致新补丁来临时社区只能给游戏降级；而且闭源意味着**没人能贡献代码**。OAR 选择开源 + 可扩展，目标是"DAR 的继任者，带完全向后兼容和新功能"。

作者同时请用户**也去给 DAR 点赞**——「最初的想法是 Felisky 的」。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## 相关

- [OAR 与 DAR：兼容策略与 Legacy](oar-vs-dar.md)
- [Replacer 与 Patcher：OAR 与 FNIS/Nemesis/Pandora 的分工](replacer-vs-patcher.md)
- [版本迭代史与关键节点](version-history.md)
- [替换的心智模型](../08-practices/animation-key-model.md)
