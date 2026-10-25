---
id: autobody
title: AutoBody（AE 版身形分发）
category: 05-distribution
kind: tool
version: 2.0.0
updated: 2026-10-25
tags: [分配, AutoBody, CBBE, HIMBO, NPC 身形, ini]
aliases: [身形分发, napmouse, 给 npc 分配身形, autobody 是什么, autobodyae, rocketbun, orefit 重实现, morphs.ini faction, 分号键, regenerate actor, jbs2bg, autobody 依赖, autobody 停更, ae 身形分发, autobody 安装]
source: https://github.com/napmouse/autoBodyAE
summary: AutoBody 的作者与仓库沿革（napmouse → RocketBun-OG、2022-09 后基本停滞）、仿 BodyGen 的 morphs.ini 语法与 faction/EditorID 匹配、ORefit 重实现、游戏内调整菜单与 Regenerate Actor 法术、仅 Address Library 的依赖，及与 OBody NG 的对比。
---

# AutoBody（AE 版身形分发）

> **一句话**：一个 SKSE 插件，把 **CBBE 与 HIMBO 预设**分发给 NPC——
> 用**仿 RaceMenu BodyGen 的 `morphs.ini`** 配置，**重新实现了 OBody 的 ORefit 算法**，
> 而且**只依赖 Address Library**（不需要 MCM Helper / UIExtensions / RaceMenu 生态）。

## 速览

| 项 | 内容 |
|---|---|
| 作者 | **napmouse**（VR 移植致谢 alandtse） |
| 仓库 | `github.com/napmouse/autoBodyAE`（GitHub 现解析到 **`RocketBun-OG/autoBodyAE`**，账号变更/迁移） |
| Nexus | **AE：61321** · VR：61690 |
| 许可证 | **GPL-3.0** |
| 编译 | **CommonLibSSE**（非 NG）→ DLL 按游戏版本分档；提供 AE / SSE / VR 三套构建预设 |
| 依赖 | **仅 Address Library for SKSE Plugins**（VR 用 VR Address Library） |
| 配置 | `morphs.ini`，语法仿 BodyGen；**EditorID / faction / race** 匹配 |
| 游戏内 | **`;` 键** actor 调整菜单 + **Regenerate Actor 法术** |
| 维护状态 | 最后提交 **2022-09**，此后基本停滞；**不支持 1.7.x** |

要点：

- **依赖链是它最大的卖点**：不碰 RaceMenu / MCM Helper / UIExtensions，
  装上 Address Library 就能跑。
- **语法仿 BodyGen**：见过 `morphs.ini` 的人直接上手；但它是**独立的 mod**，不要与
  RaceMenu BodyGen 混装。
- **ORefit 是重实现的**：作者 credits 明写参考并部分照搬了 Sairion350 的 OBody
  （事件处理与 ORefit）。
- **男性支持**：分发 **HIMBO** 预设。
- **维护基本停滞**：2022-09 后无提交；选它等于接受"没有后续版本适配"。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| 2022-01-05 | 仓库提交 "Changed license, added new config options" | 许可证定为 GPL-3.0；配置选项扩充 |
| 2022-01-11 | 版本 **1.3.1**；"Add VR compilation" | AE / SSE / VR 三套 CMake 预设成型 |
| 2022-09-28/29 | 最后两次提交："fix for in-game menu page limit"、"version bump" | **此后仓库基本停滞** |
| 2026（现状） | 仓库解析到 `RocketBun-OG/autoBodyAE`；README 构建说明仍写 `napmouse/autoBodyAE` | 账号变更/迁移；**是否有新维护者未确认** |

### 它从哪来

它瞄准的是 AE 早期的一个具体空档：**OBody 原版挂在 OStim 生态上**（要装 OStim），
而 RaceMenu 系的分配工具依赖链越滚越长。AutoBody 的思路是"**只要 Address Library**"：
用 CommonLibSSE 写一个轻插件，配置语言直接借用社区已经熟悉的 BodyGen `morphs.ini`，
再把 OBody 的 ORefit（穿衣重算）重新实现一遍。

### 中间经历了什么

开发集中在 2022 年：1.3.1 定版 AE/SSE/VR 三预设；VR 版由 alandtse 贡献；
9 月修了游戏内菜单分页问题后停止提交。**没有跟进 2026-08 的 1.7.x。**

### 现状

仍可用（停在 1.6.x 链），Nexus AE 页 61321 在线；但在" RaceMenu 缺席 1.7.x"的当下，
它同样上不了 1.7.x（CommonLibSSE 老档，按游戏版本分 DLL）。生态位上，它被
**OBody NG**（CommonLibSSE NG 单 DLL、活跃维护）覆盖了大部分需求。

## 它解决什么问题

| 需求 | AutoBody 的答案 |
|---|---|
| 想分发 CBBE / HIMBO 预设给 NPC | 核心功能 |
| 不想装 OStim / 不想拖一长串依赖 | **只依赖 Address Library** |
| 想按 **faction / race** 分配（如只让Whiterun镇民用某组预设） | `morphs.ini` 里 EditorID 匹配 |
| 男性 NPC 也要多样身材 | **HIMBO** 预设支持 |
| 权重想要随机 / 指定 / 跟随 actor | 三种 weight 模式 |
| 不满意某个 NPC 的体型 | **`;` 键**当场换；或 **Regenerate Actor 法术**重摇 |

## 工作原理

```
morphs.ini：左侧 = 匹配键（All|Female|TownWhiterunFaction / All|Female|NordRace …）
           右侧 = 预设（多预设可权重随机）
   ↓
扫描预设：SliderPresets 目录，或专门的 mod 预设文件夹（两处可选）
   ↓
分配：随机 / 权重随机 / 按 faction 优先（可选）
   ↓
施加：morph + ORefit（重实现）——衣服贴身
   ↓
 clothed 预设：自动排除（"Automatically prevents ALL clothed presets from loading"）
```

与 BodyGen 的差异（作者 README 归纳）：更丰富的配置项、faction 身形、两处预设加载位置、
faction 身形是否优先可选、自动排除 clothed 预设、男性支持、weight 三模式。

## 安装

1. **确认游戏版本与 Address Library**（AE 档）。验证点：`Data\SKSE\Plugins\` 有地址库文件。
2. **装 AutoBody 主文件**（Nexus 61321；VR 用 61690 + VR Address Library）。
   验证点：`Data\SKSE\Plugins\` 下出现 AutoBody 的 DLL。
3. **放置 `morphs.ini`**（配置形态见下节）。验证点：文件在预期路径、
   语法与 BodyGen 一致（ini 末尾同样建议留空行——社区经验）。
   `morphs.ini` 通常随预设包或整合清单提供；自己写时注意**匹配键的 EditorID 不能凭印象编**，
   用 xEdit / CK 查实际 EditorID。
4. **进游戏验证**：准星对准 NPC 按 **`;`**。验证点：弹出 actor 调整菜单，
   能改预设且**改动会保持**。

> ⚠️ AutoBody **不需要** MCM Helper / UIExtensions / PapyrusUtil / RaceMenu——
> 看到"要求装这些"的教程，是把 OBody NG 的依赖错安到了它头上。
>
> ⚠️ 它与 RaceMenu 可以共存于同一加载列表（不冲突），但**不要同时启用两套分配**
> （AutoBody + RaceMenu BodyGen，或 AutoBody + OBody NG）。

## 使用与配置

### `morphs.ini`（语法有意仿照 RaceMenu BodyGen）

匹配键用 **EditorID**，支持 **faction 与 race**：

```
All|Female|TownWhiterunFaction=...
All|Female|NordRace=...
```

能力清单（README）：

- 按 **faction / race** 匹配；
- 支持**男性**（HIMBO 预设）；
- 支持**权重随机**；
- 两处预设加载位置：仅 `SliderPresets`，或专门的 mod 预设文件夹；
- faction 身形是否优先，可配置。

### 游戏内工具

| 功能 | 说明 |
|---|---|
| **`;` 键** | 打开 actor 调整菜单；不喜欢当前预设就换，**改动会保持** |
| **Regenerate Actor 法术** | 对任意 actor 重跑分配算法 |

### 预设从哪来

AutoBody 分发的素材就是普通 BodySlide 预设，两个来源：

- **你自己在 BodySlide 里做的 / 从 Nexus 下的预设包**（落在
  `Data\CalienteTools\BodySlide\SliderPresets\` 的 `.xml`）——这也是 OBody NG 读的同一批文件；
- **专门的 mod 预设文件夹**（AutoBody 支持的第二处加载位置，README 明示）。

女性预设来自 CBBE 系（含 3BA 变体，见 [cbbe.md](../03-body/cbbe.md) /
[cbbe-3ba.md](../03-body/cbbe-3ba.md)），男性来自 **HIMBO**（见
[himbo.md](../03-body/himbo.md)）。**前提仍然是 `.tri`**：预设只是"数值"，
 morph 数据要靠 BodySlide 的 `Build Morphs` 构建出来（见
[morph-runtime-vs-bake.md](../03-body/morph-runtime-vs-bake.md)）。

## 兼容与冲突

| 对象 | 结论 |
|---|---|
| **RaceMenu BodyGen** | 语法仿照但**是两个 mod**，不要混装 |
| **OBody NG** | **二选一**：都装会争同一批 actor 的 morph；社区"OBody NG 是 AutoBody 继任者"的说法**先后关系未确认**（作者不同、都在维护/曾维护） |
| **依赖面** | 仅 Address Library —— 比 OBody NG（RaceMenu/skee 生态 + MCM Helper + UIExtensions + PapyrusUtil）轻得多 |
| **1.7.x** | **不支持**（CommonLibSSE 老档，2022-09 后无提交）；1.7.x 上想分配看 [OBody NG](obody-ng.md) 5.0 |
| **CBBE / HIMBO** | 分发的就是这两族预设；其他身形（3BA 变体、BHUNP 等）的支持以预设实际形态为准 |

## 排错

| 症状 | 判据（看到 X 说明是 Y） | 处理 |
|---|---|---|
| `;` 键无菜单 | Address Library 缺失或档位错 | 核对 ADL 版本与游戏匹配 |
| 分发的 morph 不生效 | 没做 `Build Morphs` 基础构建（没有 `.tri`） | 先补 Zeroed Sliders + Batch Build（[morph-runtime-vs-bake.md](../03-body/morph-runtime-vs-bake.md)） |
| 想要 clothed 预设却不出现 | **设计如此**：自动排除全部 clothed 预设 | 改用裸体系预设 |
| faction 规则不生效 | EditorID 写错 / 加载位置没选对 | 核对 EditorID 与预设目录配置 |
| 男性 NPC 没变化 | `morphs.ini` 没给男性配 HIMBO 预设，或 HIMBO 侧没构建 `.tri` | 补 HIMBO 预设条目并构建（[himbo.md](../03-body/himbo.md)） |
| 与 OBody NG 同装后行为混乱 | 两个分配系统争同一批 actor | **二选一** |
| 在 1.7.x 上起不来 | DLL 按游戏版本编译，未跟进 1.7.x | 回 1.6.x 或换 OBody NG |

## 取舍与建议

| | **AutoBody** | **OBody NG** |
|---|---|---|
| 配置 | `.ini`（仿 BodyGen） | `.json` |
| 男性身形 | **HIMBO** | 支持（受支持男性身形清单） |
| 界面 | 游戏内菜单 + 法术 | MCM |
| 依赖 | **仅 Address Library** | RaceMenu/skee 生态 + MCM Helper + UIExtensions + PapyrusUtil |
| 版本适应 | 按游戏版本分档；**2022-09 后停滞** | **单 DLL 通吃；5.0 支持 1.7.x** |
| 作者 | napmouse | Aietos |

- **选 AutoBody 的理由**：依赖洁癖、只装一个 DLL、熟悉 BodyGen ini 语法、要 faction 匹配。
- **不选的理由**：维护停滞（无 1.7.x、无后续修复）、无 MCM、文档只有 README。
- **默认建议**：2026 年的新配置，**优先 [OBody NG](obody-ng.md)**；AutoBody 适合
  "已经有一个 1.6.x 稳定环境、想最小依赖"的场景。
- **共同前提不变**：无论哪个分配工具，都要先有 `.tri` 地基
  （[morph-runtime-vs-bake.md](../03-body/morph-runtime-vs-bake.md)）。

## 来源

- **作者、仓库、GPL-3.0、ORefit 重实现、`morphs.ini` 语法与 EditorID/faction/race 匹配、
  faction 优先可选、两处预设加载位置、自动排除 clothed 预设、男性/HIMBO 支持、
  weight 三模式、`;` 键与 Regenerate Actor 法术、依赖 Address Library、AE 61321 / VR 61690、
  credits（Sairion350 / Ryan-rsm-McKenzie / Scrab / alandtse）、CommonLibSSE 构建与
  2022-01/09 提交时间线、仓库现位于 RocketBun-OG**：
  **GitHub 官方 README 与仓库记录** —— **一手**
  `https://github.com/napmouse/autoBodyAE`（现解析到 `RocketBun-OG/autoBodyAE`）
- **Nexus mod id 61321**：AutoBody README 内链 —— **一手**
- **与 OBody NG 的继任关系**：**社区说法，未确认**
- **未确认**：RocketBun-OG 与 napmouse 的关系（账号变更或转移）、2022-09 之后是否存在
  其他维护渠道、Nexus 61321 页的当前版本号（本库未逐条核对）
