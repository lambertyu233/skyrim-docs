---
id: unreliable-sources
title: 不可信来源警示（已实测的编造案例）
category: 09-sources
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 来源, 警示, 辟谣, CSDN]
source: https://github.com/ersh1/OpenAnimationReplacer
summary: CSDN 等站点的 OAR 文章已被逐条验证为编造：不存在的 Data\OAR\ 目录、OAR.json 全局配置、oar list/log 控制台命令、.kf/.nif/.fbx 动画格式、OAR v5.0 与 State Override 功能——全部不实。
---

# 不可信来源警示（已实测的编造案例）

## 结论先行

**不要参考 CSDN 上的 OAR 文章。** 本库在检索过程中命中多篇，并把它们的每一条技术断言都拿去与官方源码 / 描述页对比 —— **全部不成立**，而且编造方式高度一致（看起来"细节丰富"，实则每一条都能被现有事实否定）。

同类的 mod 聚合站（toolify 一类）也不要作为技术依据。

## 已实测的编造清单

| 被编造的东西 | 事实 |
| --- | --- |
| **`Data\OAR\` 目录**（"动画以原始格式躺在 `Data\OAR\` 目录下"） | **不存在**。OAR 的目录是 `Data\Meshes\...\OpenAnimationReplacer\<Mod>\<Submod>\`——**必须在 `Meshes` 里面**。 |
| **`Data\OAR.json` / `SkyrimSE/Data/OAR.json` 全局配置** | **不存在**。OAR 没有全局 `OAR.json`。配置是**每个 submod 一份 `config.json`**，加上 `Data\SKSE\Plugins\OpenAnimationReplacer.ini`。 |
| **`OAR.json` 里的 `"animations"` 数组 / `"type": "RunForward"` 字段** | **不存在**。官方明确说明条件与动画写在 submod 的 `config.json` 里，且**不推荐手改**。 |
| **控制台命令 `oar list`、`oar log`** | **不存在**。OAR **没有任何控制台命令**。它的入口是 **`Shift + O`** 的游戏内 UI。 |
| **"日志里会出现 `Matched RunForward for Player with priority 100`"** | 编造的日志格式。真实的日志是 `Documents\My Games\Skyrim Special Edition\SKSE\OpenAnimationReplacer.log`，而且是文件 + 游戏内 overlay，不是控制台输出。 |
| **替换 `.kf` 文件 / `MainMenu.kf`** | **Skyrim SE 不用 `.kf`**。`.kf` 是旧 Gamebryo/NetImmerse 时代的动画格式，Skyrim 用 **`.hkx`**。 |
| **`.fbx` / `.nif` 动画文件**（"你扔进去的 `.fbx` 或 `.nif` 动画文件……"） | **不存在**。OAR 处理的替换动画一律是 **`.hkx`**。`.nif` 是模型网格，`.fbx` 是 DCC 交换格式，都不是游戏要播的动画文件。 |
| **"OAR v5.0"** | **不存在**。截至 2026-09，当前版本是 **3.2.1**，历史版本号从未到 5。 |
| **"OAR v1.3，2019 年测试"** | **不成立**。OAR 的**首次上传是 2023-06-01**，0.x 系列是 2023 年的测试版。2019 年 OAR 还不存在。 |
| **"State Override" 功能** | **不存在**。OAR 没有这个功能。 |
| **"按 `Ctrl+Shift+R` 就能刷新动画"** | **不存在**。官方明确：**运行时不能物理增删动画文件或 mod，改动只在重启后生效**。没有热刷新快捷键。 |
| **"OAR 不走 Bethesda 的 .esm/.esp 加载管线，它把动画数据塞进内存里的 Animation Graph 节点"** | 半真半假的拼接。OAR 是 **SKSE 插件**（绕过 esp 是对的），但它**不操作 Animation Graph 节点树**，也不注入骨骼/重映射动画曲线。它是**在动画请求这一层做文件重定向**。 |
| **"OAR 可以插入 Blend Space / State Machine / Transition Rule"** | **不成立**。那是 Unreal 的动画蓝图概念。OAR 做的是**替换文件**，不是编辑行为图结构。 |
| **"FNIS 生成预编译 `.kf` 序列帧文件"、"NISS"** | **不成立**。FNIS 生成/更新的是 **`.hkx` 行为文件与动画数据库条目**；"NISS" 这个工具名也不存在（应为 Nemesis）。 |

> 判定依据：官方描述页 <https://www.nexusmods.com/skyrimspecialedition/mods/92109>；源码 `github.com/ersh1/OpenAnimationReplacer`（`src/` 中无任何 `.kf` / `oar` 控制台命令 / `OAR.json` 相关实现，且 `src/Parsing.cpp` 就是 `config.json` 的解析器）；本工作区实测记录 `OAR/`。

## 这些文章的"毒性"为什么大

1. **形式上很专业**：有"技术原理"、有 JSON 片段、有命令输出、有版本号，还带"我 2019 年就测试过"式的资历铺垫。
2. **错得可执行**：照着做会去建一个**永远不会被读取的目录**、改一个**不存在的文件**、敲一个**不存在的命令**——然后得出"OAR 好难用/不工作"的结论。
3. **能自我解释失败**："动画没换？那是你没刷新（Ctrl+Shift+R）"——用编造的机制解释真实的问题，把人往错误方向推。

## 怎么快速鉴别一篇 OAR 文章

看到下列任一条，**立刻提高警惕**：

- 提到 `Data\OAR\`、`OAR.json`、`oar list`、`oar log`、`Ctrl+Shift+R`
- 提到 `.kf`、`.nif`、`.fbx` 作为**动画**文件
- 提到 OAR 版本 ≥ 4，或 2019–2022 年的 OAR 经历
- 提到 Blend Space / State Machine / Transition Node / Animation Blueprint
- 通篇不提 `Shift + O`、不提 `config.json` / `submod` / `replacer mod`、不提 DAR 兼容
- 把 OAR 描述成"另一个动作引擎"，不讲它与 FNIS/Nemesis/Pandora 的区别

**正确的核对姿势**（按成本从低到高）：

1. 在**游戏内编辑器**里找这个条件/字段/开关——找不到就是没有；
2. 在 **Nexus 描述页**搜关键词；
3. 在**源码**里搜（`src/Parsing.cpp` 找 JSON 字段、`src/Conditions.h` 找条件名、`src/Settings.h` 找 ini 键）。

## 关于 AI 聚合站

toolify 一类的"AI 工具导航/聚合"站会对 mod 页面做机器改写，产出的"说明"常常**混合了多个 mod 的信息、凭空补全参数、版本号错乱**。它们对**发现**新工具或许有用，但**绝不能**作为版本号 / 目录 / 命令的依据。

## 一个正面例子（说明什么才叫可核对的二手来源）

Nexus 论坛 scorrp10 的回复之所以可信，是因为他**引用了可验证的具体对象**：原版动画数据库里 `ChairIdle` 对应 `meshes/actors/character/animations/female/chair_idlebasevar1.hkx`；`"7GOM34"` 对应 `GomaPeroPero1\7GOM34.hkx`。**你可以自己打开行为文件核对。** 这才是社区来源的正确形态。

> 来源：<https://forums.nexusmods.com/topic/13487504-for-animations-what-is-the-difference-between-fnisnemesis-and-oar/>

## 相关

- [官方来源清单](official-sources.md)
- [社区来源清单](community-sources.md)
- [排错对照表](../05-editor/troubleshooting.md)
