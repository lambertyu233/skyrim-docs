---
id: troubleshooting
title: 排错对照表
category: 05-editor
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 排错, T-Pose, 症状, 诊断]
aliases: [OAR 不生效, 换了动画没反应, OAR 排错, 动画没变, 条件对了但没用]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: 按"症状 → 优先排查"组织的排错表；含 T-Pose/A-Pose 的三类成因、重复动画、路径过长、同优先级冲突、条件不命中等高频问题。
---

# 排错对照表

## 症状 → 原因

| 症状 | 优先排查 |
| --- | --- |
| **动画完全没换** | ① 文件名是不是游戏请求的那个（见 [心智模型](../08-practices/animation-key-model.md)）；② 旧 DAR 结构有没有移走；③ 改动后有没有重启游戏 |
| **动画换了，但某个状态掉回原版** | 那个状态请求的是**另一个文件名**——最常见的就是"移动掉回原版"（移动是另一套事件名） |
| **不该换的状态也被换了** | **条件太宽**。逐条收紧（典型修法是加更精确的状态条件，例如用 `AttackState` 而不是 `IsAttacking`） |
| **角色摆 T-Pose / A-Pose，或该动作不播放** | ① **hkx 版本/格式不对**（LE 的 32 位文件丢进 SE）；② **完整路径 > 260 字符**；③ OAR 根本没读到动画（看 Replacement Animations 面板是否为空） |
| **有个随机动画在跟我的抢** | 优先级对比，或收窄条件；**同优先级**会让编辑器报警告 |
| **改了没生效但日志里有** | 条件没命中——用 `Shift+O` 看每一条的图标和实时值 |
| **设置重置了** | 删掉了插件生成的 `.ini`（MO2 下默认在 overwrite 里） |
| **主菜单崩溃** | 在 `Data\SKSE\Plugins\OpenAnimationReplacer.ini` 里把 `bLoadDefaultBehaviorsInMainMenu` 设为 `false` |
| **编辑器报"缺少插件/需要更高版本"** | 某个条件要求的 OAR 或扩展插件版本不够。**点编辑器底部的错误栏**看详情；或该插件没装 |
| **预览按钮不出现** | **没有选中求值目标**——先控制台点自己（`prid 14`） |
| **配置改了但编辑器里没变** | 忘了按保存（User 模式看左上角有没有橙色 `*`） |

> 来源（症状表骨架）：本工作区实测记录 [实战](../../oar-kb/08-practices/)（原 `OAR/` 目录的内容已并入本库）；官方 FAQ 部分见 <https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## T-Pose / A-Pose 专项诊断

这是社区里最常见、也最容易误诊的问题。**先分类，再动手**：

| 表现 | 判断 | 处理 |
| --- | --- | --- |
| **开局头几秒** T-Pose，随后恢复 | OAR 在**预加载动画**，正常 | 等它读完。装了大量动画包时会更久 |
| **一直** T-Pose，且 OAR 的 **Replacement Animations 面板是空的** | OAR **没读到你的动画**——这是 OAR 侧问题 | 查条件、查文件冲突、查**路径长度**、查是否混进了 **32 位（LE）hkx** |
| 一直 T-Pose，且**行为文件本身坏了** | 补丁器侧问题 | 这时才重跑 Nemesis / Pandora / FNIS |

**关键判断**：**OAR 的锅不会靠刷 Pandora 解决，反之亦然。**

> 来源：本工作区实测记录 [Replacer 与 Patcher：OAR 与 FNIS/Nemesis/Pandora 的分工](../../oar-kb/00-overview/replacer-vs-patcher.md)；社区同一现象见 <https://forums.nexusmods.com/topic/13497416-open-animation-replacer-a-pose/>

### 社区里真实出现过的成因

同一个 A-pose 帖子里，最终有位玩家靠装独立的 **A Pose Bug Fix**（Nexus mod 168903）解决，他的描述是：

> 装了需要 OAR 的自定义动画 mod 后，它们会出现在 OAR 的 "Replacer Mods" 标签页里，但 **OAR 不会加载这些动画**（动画不出现在 "Replacement Animations" 标签页里），结果游戏里所有角色都 A-Pose。装了 A Pose Bug Fix 之后，OAR 终于加载了动画。

> 来源：<https://forums.nexusmods.com/topic/13497416-open-animation-replacer-a-pose/>

另一位玩家在同一帖里提到 **FNIS 报过 "32bit Animations incompatible with the current version of the game"**——这正是"hkx 位宽不对"的典型表现。判定方法见 [hkx 与行为文件](../08-practices/animation-key-model.md)。

## 用日志做判断（唯一权威）

**OAR 日志是唯一能区分「配置没加载」和「配置加载了但条件没命中」的手段。**

```
C:\Users\<用户名>\Documents\My Games\Skyrim Special Edition\SKSE\OpenAnimationReplacer.log
```

| 搜什么 | 判断 |
| --- | --- |
| 被替换的原动画路径 | 有没有出现在日志里 → submod 是否被扫描到 |
| `fail` / `invalid` / `could not` | 动画加载失败 |
| `Legacy` | DAR 旧 mod 被转换成什么 |
| `interruptible` | 有哪些动画会被动态替换 |

详见 [动画日志与调试](animation-log-and-debugging.md)。

## 社区反馈里最"冤"的两件事

1. **把 OAR 的问题归给补丁器**。论坛里"我换了 Pandora 之后 OAR 包不加载"的帖子，按 scorrp10 的划定，问题几乎总在 OAR 侧（mod 条件写错或冲突）。

   > 来源：<https://forums.nexusmods.com/topic/13497416-open-animation-replacer-a-pose/>

2. **找不到预览按钮就放弃**。答案只是"先选中目标"。

   > 来源：<https://forums.nexusmods.com/topic/13487504-for-animations-what-is-the-difference-between-fnisnemesis-and-oar/>

## 已知的未修复 issue（GitHub Issues）

本体仓库长期挂着的公开 issue 里，和排错相关的有：

- **路径超过 260 字符**（Fix for paths over 260 characters，open）
- **Unicode 支持**（open）——对应官方"避免非英文字符"的请求
- **`IdleTime` 条件不工作**（open）
- **战斗开始时 CTD**、**SCAR/OAR 潜在冲突**（open）

> 来源：<https://github.com/ersh1/OpenAnimationReplacer/issues>

**含义**：路径过长与 Unicode 是**已知且未修**的，遇到别怀疑自己；`IdleTime` 在报 issue 时（2025-08）仍有问题，用前先实测。

## 相关

- [动画日志、事件日志与 trace](animation-log-and-debugging.md)
- [游戏内编辑器](in-game-editor.md)
- [替换的心智模型](../08-practices/animation-key-model.md)
- [坑与代价](../08-practices/pitfalls-and-costs.md)
