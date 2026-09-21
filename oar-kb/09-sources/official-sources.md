---
id: official-sources
title: 官方来源清单
category: 09-sources
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 来源, 官方, 清单]
aliases: [OAR 官方来源, Nexus 页面, official sources]
source: https://github.com/ersh1/OpenAnimationReplacer
summary: OAR 没有 wiki——最权威的一手来源是源码仓库、Nexus 描述页（唯一手册）与作者 Patreon 开发日志；本页给出各自能回答什么问题及核对方式。
---

# 官方来源清单

## 首要事实：**OAR 没有 wiki**

本库建立时确认：`ersh1/OpenAnimationReplacer` 仓库**没有 `docs/` 目录、没有 GitHub Wiki**。仓库里只有 `README.md`（很短，面向**编译者**）与 `src/` 源码。

所以「官方文档」实际由三块拼成：

| 来源 | 性质 | 能回答什么 |
| --- | --- | --- |
| **Nexus 描述页** | **唯一的使用者手册** | 结构规则、条件清单、变体、预设、编辑器、函数、实验设置、FAQ、兼容性 |
| **源码仓库** | 事实的**终极出处** | 条件名全集、API 形状、枚举值、版本常量、变更的真实语义 |
| **作者 Patreon 开发日志** | 设计与历史的**动机解释** | 为什么是这个形状、某些机制只在这里解释过 |

## 一、Nexus 描述页（mod 92109）

- **链接**：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>
- **作者**：Ersh（Nexus 用户名 Ershin）｜ **当前版本 3.2.1**（2026-09-01）
- **首次上传**：2023-06-01

**页面里有什么**（本库核对过的完整清单）：

1. 功能列表（Features）
2. **STRUCTURE 节**：目录结构、路径插入规则、Legacy 兼容、运行时限制
3. 变体（Variants）——含 1.2.0 随机与 2.2.0 顺序模式
4. 预设（PRESETS）——2.2.0 起
5. 编辑器说明（Inspect / User / Author 三模式）
6. 动画日志说明
7. **完整条件清单**（按 `Added in X.X.X` 分组，从 1.1.0 到 3.2.0）
8. **完整函数清单**（从 3.0.0 到 3.2.0）
9. DAR 旧条件改名/合并对照
10. 实验性设置（65534 动画上限的技术解释、禁用预加载）
11. 需求、兼容性、FAQ
12. miscellaneous notes（示例 replacer mod、迁移建议、路径长度、interruptible 警告）

**本库已核对**：描述页的条件清单与源码 `src/Conditions.h` 注册的 **125 个条件名逐条比对无遗漏**。见 [条件全清单](../03-conditions/conditions-list.md)。

## 二、源码仓库

- **链接**：<https://github.com/ersh1/OpenAnimationReplacer>
- **许可**：GPL-3.0-or-later **WITH** Modding Exception **AND** GPL-3.0 Linking Exception (with Corresponding Source)

### 最有价值的文件

| 文件 | 为什么值得看 |
| --- | --- |
| `src/Conditions.h` | **全部条件名的权威列表**（含 `GetName()` 返回的 125 个名字、每个条件的组件与 tooltip 文本）。判断"某条件到底存不存在"看这里 |
| `src/BaseConditions.h` | 基础条件与 DAR legacy 解析入口 |
| `src/Functions.h` / `BaseFunctions.h` | 函数清单与实现 |
| `src/API/OpenAnimationReplacerAPI-*.h` | **插件 API**（Animations / Conditions / Functions / UI），头文件里有完整注释 |
| `src/API/OpenAnimationReplacer-ConditionTypes.h` | 条件组件类型与 `EssentialState` 等枚举 |
| `src/API/OpenAnimationReplacer-FunctionTypes.h` | 函数组件类型与 `FunctionAPIVersion` |
| `src/Variants.h` | 变体实现 |
| `src/ReplacerMods.h` | replacer mod / submod 的数据结构 |
| `src/Parsing.h` / `Parsing.cpp` | `config.json` 的**字段名真相**（想知道某个 JSON 键叫什么，搜这里） |
| `src/Settings.h` | ini 设置项 |
| `src/OpenAnimationReplacer.h` | 主类，含设置与全局状态 |
| `src/Hooks.cpp` | 拦截点（理解"它在哪一步介入"） |

> **本库的用法**：凡涉及"条件名 / 枚举值 / API 形状 / 配置字段"的断言，优先在源码里核一遍，而不是转述二手说法。

### 已知问题（GitHub Issues）

值得知道长期 open 的几条：

- Fix for paths over 260 characters（路径超长）
- Unicode support（Unicode 支持）
- The IdleTime condition doesn't work（`IdleTime` 不工作）
- CTD at combat start / Idle animations not playing. Potential SCAR/OAR Conflict

> 链接：<https://github.com/ersh1/OpenAnimationReplacer/issues>

### README 面向谁

仓库 `README.md` 是**给编译者**的：CMake / PowerShell / Vcpkg / VS2019 / CommonLibSSE-NG 的构建步骤，以及"用户需求 = Address Library（SSE/AE）或 VR Address Library（VR）"。

> 所以**别指望从 README 学到怎么用**——它不是给使用者的。

## 三、作者 Ersh 的 Patreon 开发日志

- **主页**：<https://www.patreon.com/Ershin>
- **公开可读的镜像**：<https://bakemono.app/p/patreon/25643772/>（本库抓取用的入口）

**这些帖子的价值**：OAR 在 Patreon 上迭代了很久才公开发布，很多机制的解释**只出现在这里**。本库引用过的关键帖：

| 帖子 | 关键信息 |
| --- | --- |
| `status update`（79535580） | 为什么迟迟不发版：编辑器做一半没意义；ImGui 开发中反复返工 |
| `0.5.1`（80271137） | 新结构首发、编辑器大改、`IsEquippedShout` 语义纠正、必需项目名、忽略 No Triggers 标记；**"压缩包里有 readme"这句就出自这里** |
| `0.6.1`（80648390） | 同步动画 bug（killmove/上马）的来龙去脉、legacy mod 的用户配置 |
| `0.8.0`（81916525） | `.json` 全作废重建、重复动画哈希过滤、动画文件夹覆盖、插件 API、Echo 替换 |
| `Paired Annotation Fix test`（86003539） | 配对动画注释不触发的一手分析 |
| `Released!`（83900406） | 正式发布；说明 Math Plugin 被拆出去是因为数学库体积 |
| `0.3`（77654433） | 发现"绕过动画队列"的极简改动；0.3.1 被撤、0.3.2 加互斥量 |

> ⚠️ **注意版本时效**：0.5.1 那句"压缩包里有 readme"指的是 **2023 年的测试版**，**对现在的 3.x 不适用**（当时还没有正式文档）。

## 四、实验性设置的技术说明（官方原文）

描述页里有一段非常硬的技术解释，值得原样保留：

> **提高动画数量上限到每项目 65534。** 给感兴趣的人的技术说明：一个 Havok behavior 动画剪辑里有一个 **16 位有符号整数（int16）**变量，表示该剪辑被激活时应该读取的那个巨大动画绑定数组的索引。int16 的范围是 **-32768 到 32767**。然而几乎整个负数区间都没被使用——**只有 -1 被用作特例**（比如动画剪辑未初始化时）。这个实验性设置会**把我能找到的所有按有符号处理该值的游戏代码位置**打上补丁，把指令改成按**无符号（uint16）**处理。无符号整数可取 0 到 65535。原来 -1 那个值仍然保留，所以最大值是 **65534**。之所以仍标为实验性，是因为我可能漏掉了某些要打补丁的地方，而且**没多少人真的会触及 32k 上限**。只有确实需要（或好奇）时才启用。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## 五、配套插件的官方页面

| 插件 | 链接 |
| --- | --- |
| Detection Plugin（Nonameron） | <https://www.nexusmods.com/skyrimspecialedition/mods/104806> |
| Math Plugin（Ersh） | <https://www.nexusmods.com/skyrimspecialedition/mods/92607> |
| IED Conditions（SlavicPotato） | <https://www.nexusmods.com/skyrimspecialedition/mods/98308> |
| IED Conditions 源码 | <https://github.com/SlavicPotato/OpenAnimationReplacer-IEDConditionExtensions> |
| Detection Plugin 源码 | <https://github.com/matiasmakipelto/OpenAnimationReplacer-DetectionConditions> |

## 六、抓取存档

本库 `_raw/` 下保存了：

| 文件 | 内容 |
| --- | --- |
| `gh-readme.md` | 官方仓库 README 原文（面向编译者） |
| `src/Conditions.h`、`src/BaseConditions.h`、`src/BaseFunctions.h`、`src/Functions.h`、`src/Parsing.h`、`src/ReplacerMods.h`、`src/Variants.h`、`src/Settings.h` | 关键头文件原文（条件名、函数、配置解析的结构真相） |
| `src/API__*.h` | **插件 API** 头文件原文（Animations / Conditions / Functions / UI / 类型定义） |
| `nexus-oar-description.txt` | OAR 描述页全文（含完整条件/函数清单、实验设置技术说明、FAQ、变更条目） |
| `nexus-plugin-pages.txt` | Detection / Math / IED Conditions 三个插件页面描述 |
| `patreon-ershin-posts.txt` | 作者 Ersh 的 7 篇 Patreon 开发日志 |
| `nexus-forum-threads.txt` | Nexus 论坛三帖（scorrp10 的经典解释、A-pose 帖、对话 idle 帖） |
| `bahamut-tutorials.txt` | 巴哈姆特三篇教程 |
| `misc-web.txt` | LoversLab 两帖、Gate to Sovngarde 整合文档、DAR 转换工具（Nexus / dar2oar）、**CSDN 编造案例对照** |

用 `python scripts/fetch_sources.py` 可重新抓取 GitHub 部分；网页（Nexus / Patreon / 论坛）的正文以本库存档为准。

## 相关

- [社区来源清单](community-sources.md)
- [不可信来源警示](unreliable-sources.md)
