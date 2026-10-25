---
id: version-matrix
title: 版本对照表（游戏 ↔ SKSE ↔ Address Library ↔ RaceMenu ↔ 物理）
category: 00-overview
kind: reference
version: 3.0.0
updated: 2026-10-25
tags: [总览, 版本, 对照, 兼容性, 1.7]
aliases: [version matrix, 版本对照, 哪个版本, 1170 对应, skse 版本对应, 版本不匹配, 1.7.104 对应什么 skse, 2.3.1, 版本表, dll 版本不对, 降级到多少, gog 1179, skse 2.2.6, address library v13, 兼容性对照]
source: https://www.nexusmods.com/skyrimspecialedition/mods/30379
summary: 以游戏版本为主键的权威对照表：SKSE64 / Address Library / RaceMenu / Faster HDT-SMP 各自的对应版本与验证状态（已验证可用 / 作者标注 untested / 未确认 / 不能用），每条都带日期与出处。
---

# 版本对照表

**这是整个领域第一大坑**：SKSE64、RaceMenu、FSMP 都是原生 DLL 插件，
它们的版本与**游戏可执行文件版本**强绑定。一次后台自动更新就能让整套失效，
而且症状往往是**静默失效**（没有报错，但功能消失）。

## 速览

| 字段 | 内容 |
|---|---|
| 作用层 | 版本对应关系的核对表（对应 [`ecosystem-map.md`](ecosystem-map.md) 的 L0 前置层） |
| 主键 | **游戏版本号**（先知道自己站在哪一档，再看其他） |
| 涉及组件 | SKSE64、Address Library、RaceMenu、Faster HDT-SMP、BodySlide |
| 影响范围 | 任一 DLL 错配 → 该功能整体消失；SKSE 自身错配 → **全部**插件失效 |
| 关键限制 | SKSE **不支持** Microsoft Store / Game Pass 版与 Epic 版；且 SKSE 本身**不使用** Address Library |
| 版本状态标注 | ✅ 已验证可用 · ⚠️ 有限/待确认 · ❓ 未确认 · ❌ 不可用（见正文表） |

要点：

- **游戏版本决定一切**：先看 `SkyrimSE.exe` 版本，再倒查 SKSE、再倒查插件。顺序不能反。
- **Address Library v13（2026-08-27）一次性覆盖到 1.7.104.0**，是目前唯一"装新版就覆盖到最新游戏"的组件。
- **RaceMenu 停在 0.4.20.0（2026-04），官方主文件明确要求 Game Version 1.6.1170** —— 它**不是** 1.7.x 可用的分量。
- **BodySlide / Outfit Studio 是外部工具，不受游戏版本影响**，仍正常更新（5.9.1 / 2026-10-04）。
- **当下最稳的组合是 1.6.1170（Steam）或 1.6.1179（GOG）**，详见 [`game-version-1-7-x.md`](game-version-1-7-x.md)。

## 前世今生

这张表之所以会长成这样，是有原因的：

| 时间 | 事件 | 意义 |
|---|---|---|
| 2016-10 | Special Edition 发布，SKSE64 随之出现 | 从这一刻起"游戏更新 ↔ 脚本扩展器重编"成为常态 |
| 2019-11-18 | SKSE64 的 Nexus 页面建立（AE时代的更新/ changelog 渠道） | 后来核对版本最重要的依据就是它的 Changelog |
| 2020-02-07 | **Address Library** 发布（meh321） | 把"插件硬编码偏移"变成"查询数据库"，1.6.x 系列的大量小更新不再需要每个插件重编 |
| 2021-10 | Bethesda 发布 Anniversary Edition（1.6.317 起的一串更新） | 版本号频繁跳变，催生了各种"版本对照表"这种民间文档 |
| 2021-10-22 | Faster HDT-SMP 首传 | 物理层开始有自己的"最后一版面向 X"的版本台账（后来在 Files 页明确写出） |
| 2024-10-08 | FSMP 2.5.1 —— 最后一个基于 SKSE 的版本，之后转 CommonLibSSE | 物理层与新版工具链对接 |
| 2026-08-14 | SKSE 官网挂出警告："Bethesda 宣布即将更新 Skyrim" | 两年半以来的第一次更新预报 |
| 2026-08-19 | SKSE 2.2.7（仍面向 1.6.1170，主要提供插件预加载支持） | 为老版本用户做的最后准备 |
| 2026-08-20 | 游戏 **1.7.99** + SKSE **2.3.0** | 新分支开始 |
| 2026-08-21 | Address Library **v12**（面向 1.7.99.0） | 附属更新跟进 |
| 2026-08-27 | 游戏 **1.7.104** + SKSE **2.3.1** + Address Library **v13** | 同一天三件套齐更新；v13 的官方说明是"This is for ALL game versions up to 1.7.104.0" |
| 2026-08-23 | RaceMenu 作者发帖：1.7.99 已完成但被 SKSE 的 Papyrus bug 卡住；1.7.104 未做；转 CommonLibSSE-NG 重写 | **链条在这里断掉** |
| 2026-10-04 | BodySlide 5.9.1 | 外部工具链不受影响，仍在迭代 |

一句话总结：**这套生态的工程复杂度，几乎全部来自"Bethesda 会随机更新二进制"这一件事。**

## 它解决什么问题

- **症状没有报错**：版本错配最典型的表现是"功能消失"而不是"崩溃"，没有线路图就很难想到是版本不对。
- **多组件互相牵连**：SKSE 版本由游戏版本决定，插件版本由 SKSE + 游戏共同决定，Address Library
  又是另一个覆盖面维度 —— 四个变量，需要一张表把它们绑在一起。
- **民间对照表版本不一**：年代不同的表会给出互相矛盾的对应关系（本表此前就有过一次修正，见下）。
  因此本表**每条都标注了出处与核实日期**。

> ⚠️ **本表在 2026-09-30 做过一次较大修正**（保留该结论）：
> - 新增 **1.7.99 / 1.7.104** 两行（2026 年 8 月 Bethesda 更新后的新分支）；
> - 修正 **1.6.1130 → 2.2.4**（原表误写 2.2.6）、**1.6.640 / 1.6.659 → 2.2.3**（原表误写 2.2.2）。
>
> ⚠️ **2026-10-25 本轮再次修正**：依据 SKSE64 官方 Changelog 逐条核对后，补上了
> **2.2.7 / 2.2.8 仍面向 1.6.1170**、**1.6.640 的支持自 2.2.1 引入**等细节，并重新标注了
> 每一档的验证状态。原来写"1.6.1170 → SKSE 2.2.6"是不完整的（2.2.6 是**引入**该支持的版本，不是唯一可用版本）。

---

## 配置与使用

### 主表：以游戏版本为主键（2026-10-25 核实）

图例：**✅ 已验证可用**（多方一手来源一致且社区广泛使用） · **⚠️ 有限/待确认**（官方标注 untested 或存在争议） ·
**❓ 未确认**（找不到可靠出处） · **❌ 不可用**（官方明确不支持或缺核心组件）

| 游戏版本 | SKSE64 | Address Library | RaceMenu | Faster HDT-SMP | 组合状态 |
|---|---|---|---|---|---|
| **1.7.104**（Steam AE，当前） | **2.3.1**（2026-08-27） | **v13**（2026-08-27，官方说明覆盖到 1.7.104.0） | ❌ **无官方版本**：最新 0.4.20.0 面向 1.6.1170；作者另有 Patreon beta（见下） | FSMP **4.1.1**（2026-08-27）；其面向的确切游戏版本 **❓ 未确认**（社区报告互相矛盾） | ❌ **不适合依赖捏脸的用户**：核心缺件 |
| **1.7.99** | **2.3.0**（2026-08-20） | **v12**（2026-08-21） | ❌ **未发布**：作者称已完成，但被 SKSE 的 Papyrus 函数 bug 卡住（会崩游戏）；未上架 | FSMP 仓库 2026-08-23 有 "retarget UpdateHook2 for AE 1.7.99" 的 commit —— ❓ 未确认是否发版 | ❌ 同上 |
| **1.6.1170**（Steam AE） | 2.2.6（引入支持）；**2.2.7**（2026-08-19）/**2.2.8** 仍面向此版本 ⚠️（由 changelog 无新 "support for" 行推断） | v13 覆盖 | ✅ **0.4.19.16 及以上**；当前 **0.4.20.0**（主文件明示要求此版本 + SKSE64 AE 2.2.6+） | ✅ 3.5.0 / 4.x 系列皆有面向此档的构建 | ✅ **推荐的稳定组合**（本工作区判断） |
| **1.6.1179**（GOG AE） | 2.2.6（GOG 档） | v13 覆盖（bin 为统一数据库） | ⚠️ **0.4.20.0 起支持，作者原帖标注 "Added GOG 1.6.1179 though untested"** | ❓ 未确认（FSMP 侧未见针对此版本的明确声明） | ⚠️ **基本可用**，但官方明确标注 untested |
| 1.6.1130 | **2.2.4** | v13 覆盖 | 0.4.19.15+ | FSMP **2.1.3**（2024-01-04）是该分支最后一个明确声明的版本 | ✅ 旧链仍可用，但新 mod 逐步不支持 |
| 1.6.640 | 支持自 **2.2.1** 引入；该分支最后一个为 **2.2.3** | v13 覆盖 | 0.4.19.13+ | FSMP 有 1.6.640 档（更早版本不再提供） | ⚠️ 老分支；上层环境插件多数不再支持 |
| 1.6.659（GOG 旧档） | **2.2.3** | ❓ | 0.4.19.14+ | FSMP **2.2.1**（2024-02-09）为最后一个面向此版本的构建 | ⚠️ 老分支 |
| 1.6.353 | **2.1.5** | ❓ | 0.4.19.x 相应版本 | FSMP **2.1.0**（2023-12-12）为最后一个面向此版本的构建 | ⚠️ 老分支 |
| 1.5.97（pre-AE 长期版本） | **2.0.20**（SE 档；AE 档不可混用） | SE 侧 bin（与 AE **不通用**） | 0.4.19.12 及以下一支 | FSMP 有 1.5.97 档 | ⚠️ 每个组件都要用 SE 版；用途特化 |
| VR（1.4.15） | SKSEVR **2.0.12** | VR 侧 bin | RaceMenu **VR 0.4.14**（2020-08-10，Nexus 明确说明它是 VR 版） | FSMP 有 VR 档 | ⚠️ 独立分支，与 SE/AE 的档位不交叉 |

> **关于 SKSE 2.2.7 / 2.2.8**：SKSE 官方置顶帖原文是
> "2026-08-19: In preparation for the patch tomorrow, I've uploaded SKSE64 **2.2.7** for game version **1.6.1170**
> with the latest code. This is mostly so users on 1.6.1170 get plugin preloading support."
> 而 2.2.8 的 changelog 只有 "fix regression in old commonlib"，**没有出现新的 "support for <版本>" 行** ——
> 据此推断它仍面向 1.6.1170。这是**推断而非官方明示**，请以实际安装后的 `getskseversion` 与游戏能否启动为准。

### 反向对照：SKSE64 版本 → 游戏版本（依据官方 Changelog）

正查（游戏 → SKSE）上一级"主表"已经给出；这里是**反查**，依据是 SKSE64 官方 Changelog 里
明确写着 "support for X" 的那些行：

| SKSE64 | Changelog 明示的游戏版本 | 备注 |
|---|---|---|
| **2.3.1** | `support for 1.7.104` | 另含 "fix PlayerCharacter functions" 与更好的插件重编译兼容性提示 |
| **2.3.0** | `support for 1.7.99` | 新分支的第一次跟进 |
| 2.2.8 | —— （无新 support 行） | 仅 "fix regression in old commonlib" → **推断仍面向 1.6.1170** |
| 2.2.7 | —— （无新 support 行，但置顶帖明确"for game version 1.6.1170"） | 主要为插件预加载支持 |
| **2.2.6** | `support for 1.6.1170` | 长期作为 AE 稳定档 |
| 2.2.5 | —— | InputManager / 自定义文本输入修复 |
| **2.2.4** | `support for 1.6.1130` | 另有 loader 参数与 SoulGem::GetSoulSize 修复 |
| 2.2.3 | —— | 支持探测 Epic 版、改进 GOG 兼容性 |
| 2.2.2 | —— | 修收右手法器崩溃 |
| **2.2.1** | `support for 1.6.640` | **1.6.640 的支持由此引入**，该分支最后一个为 2.2.3 |
| **2.2.0** | `support for 1.6.629` | 提及 1.6.629+ 的 `SKSEPluginVersionData` 破坏性变更 |
| **2.1.5** | `support for 1.6.353` | |
| 2.1.4 / 2.1.3 | `support for 1.6.342` / `support for 1.6.323` | |
| 2.1.1 / 2.1.0 | `support for 1.6.318` / `support for 1.6.317 (anniversary edition)` | AE 起点 |
| **2.0.20** | （面向 1.5.97 的长期版本） | 官方明示：除非你主动降级/阻止更新，否则应下 AE 档 |

> 读法：**凡是 Changelog 里没有出现 "support for <版本>" 的版本，就沿用上一档的目标游戏版本。**

### 去哪里核：四项自我核对的位置

| 组件 | 最权威的核对位置 | 看什么 |
|---|---|---|
| SKSE64 | `skse.silverlock.org` 首页 + Nexus 页 `Changelogs` 标签 | 首页写"当前各档"；changelog 写某版本对应什么游戏版本 |
| Address Library | Nexus `Files` 页主文件名 | 文件名自带面向版本，如 `All in One (1.7.104.0) v13` |
| RaceMenu | Nexus `Files` 页主文件的说明文字 | 直接写 "REQUIRES SKSE64 … and Game Version …" |
| FSMP | Nexus `Files` 页的历史条目说明 | 历史条目会写 "Last FSMP version for Skyrim X"；当前版本的 FOMOD 里选对应档 |

**实践结论**：遇到不确定的插件，**先看 Files 页而不是 Posts 页** —— 作者通常把版本要求写在文件说明里，
而论坛帖里混杂着别人的二手经验。

### 不受影响的组件

| 组件 | 为什么不受影响 |
|---|---|
| **BodySlide and Outfit Studio**（5.9.1 / 2026-10-04） | 外部 Windows 工具，不注入游戏进程，因此与游戏版本无关。它仍在更新（含 morph 相关的修复） |
| 网格 / 贴图类资源 | 纯 Asset，但要注意 SE/AE 的网格格式差异（见 [`morph-and-nif-basics.md`](morph-and-nif-basics.md)） |

### Community Shaders 的口径可作旁证

同一台机器上，其他原生插件对"支持哪些游戏版本"的态度更严格：
`community-shaders-kb` 记录 CS 只支持 **1.6.1170 / 1.6.1179 / 1.5.97**，
明确**不支持 1.6.640 / 1.7.99 / 1.7.104**。这说明"版本敏感"不是个别 mod 的怪癖，
而是这套引擎生态的系统性特征 —— **装任何原生插件前，先确认自己的游戏版本号**。

### 怎么查自己的游戏版本

- Steam 版：右键游戏 → 属性 → 已安装文件，或看游戏目录里 `SkyrimSE.exe` 的详细信息；
- 更可靠的办法是看 **SKSE 启动日志**或 `Documents/My Games/Skyrim Special Edition/SKSE/` 下的插件日志，
  它们会打印运行时版本；
- 装有 SKSE 时，控制台 `getskseversion` 会直接给出版本串。

## 排错

版本错配的症状对照：

| 错配 | 症状 | 首选判据 |
|---|---|---|
| SKSE 与游戏不匹配 | 游戏起不来，或**所有 SKSE 插件静默失效**（菜单没有、滑块没有） | 控制台 `getskseversion` 无输出 / SKSE 日志打印版本不一致 |
| RaceMenu 与 SKSE/游戏不匹配 | 进游戏后捏脸界面是**原版那个**，RaceMenu 全套功能消失 | 界面样式一眼可辨；此前可用、更新后变这样 = 版本错了 |
| FSMP 选错游戏版本档 | 物理不生效，或开局 CTD | 换档重装后症状立刻消失即为佐证 |
| Address Library 装了 SE 版给 AE 用 | 依赖它的 DLL 插件全部失效（地址不通用） | 日志里出现 "failed to open address library file" 一类提示 |
| 升级后开局就崩 | 老插件全部需要重编；2026-08 起还有一个特有的 overlay nif 崩溃 | SKSE 官方建议：先清空 `Data/SKSE/Plugins` 再逐个加回；另见 [`../06-troubleshooting/overlay-nif-ctd.md`](../06-troubleshooting/overlay-nif-ctd.md) |

**推论**：遇到"某个功能整体不见"，第一件事永远是核对版本，而不是去翻冲突。

## 取舍与建议

- **依赖捏脸（绝大多数人）：留在 1.6.1170（Steam）或 1.6.1179（GOG）**，并在 Steam 里限制自动更新。
  完整的决策树的见 [`game-version-1-7-x.md`](game-version-1-7-x.md)。
- **不依赖 RaceMenu、只想用 DLL 无关的内容**：1.7.104 + SKSE 2.3.1 + Address Library v13 是可行的，
  但仍要逐个插件确认作者是否声明支持。
- **不要装跨越多个游戏版本的"通配"档**：FSMP 这类提供 FOMOD 多选设计就是因为**没有通配这回事**。
- **GOG 用户特别注意**：官方对 GOG 1.6.1179 的态度是"支持但未测试"（作者原话 "though untested"），
  遇到异常时优先怀疑这条链路。
- **升级前先做两件事**：备份存档与整套 `Data`；记录当前各 DLL 版本号（将来回滚靠它）。
- **本表会过期**：任何一项决策之前，请重新核 SKSE 官网首页、目标 mod 的 Files 页与 Address Library 的 Files 页。

## 来源

- **SKSE64 官方站（一手，SKSE 团队）**：`https://skse.silverlock.org/`
  （AE **2.3.1 = 1.7.104**、GOG **2.2.6 = 1.6.1179**、SE **2.0.20 = 1.5.97**、VR 2.0.12；
  2026-08-14 更新警告；明示不支持 MS Store / Game Pass 与 Epic 版；明示 SKSE 不使用 Address Library）
- **SKSE64 Nexus Changelog 与置顶帖（一手）**：`https://www.nexusmods.com/skyrimspecialedition/mods/30379`
  （逐条版本记录：2.1.5=1.6.353、2.2.0=1.6.629、**2.2.1=1.6.640**、2.2.4=1.6.1130、2.2.6=1.6.1170、
  **2.3.0=1.7.99**、**2.3.1=1.7.104**；2.2.7/2.2.8 的说明；2026-08-19/20/27 的置顶更新）
- **Address Library（一手，meh321）**：`https://www.nexusmods.com/skyrimspecialedition/mods/32444`
  （**v13 = "All in One (1.7.104.0)"，2026-08-27 上传；v12 面向 1.7.99.0，2026-08-21 上传**；原始发布 2020-02-07）
- **RaceMenu（一手，Nexus Files 页）**：`https://www.nexusmods.com/skyrimspecialedition/mods/19080?tab=files`
  （0.4.20.0 主文件明示 "REQUIRES SKSE64 Anniversary Edition 2.2.6 or greater and Game Version 1.6.1170"；
  GOG 可选文件要求 SKSE64 GOG AE 2.2.6+ 与 Game Version 1.6.1179；VR 0.4.14；最后更新 2026-04-20）
- **RaceMenu 未适配 1.7.x（一手，作者本人）**：Nexus RaceMenu Posts 区置顶帖（2026-08-23）
- **Faster HDT-SMP（一手，Nexus Files 页）**：`https://www.nexusmods.com/skyrimspecialedition/mods/57339?tab=files`
  （当前 **4.1.1（2026-08-27）**；3.5.0（2026-07-03）为最后一个带 MCM 的版本；
  **2.5.1（2024-10-08）为最后一个基于 SKSE 而非 CommonLibSSE 的版本**；
  2.2.1=最后一个面向 GOG 1.6.659 的版本；2.1.3=最后一个面向 1.6.1130 的版本；2.1.0=最后一个面向 1.6.353 的版本）
- **FSMP 仓库（一手）**：`https://github.com/DaymareOn/hdtSMP64`（GPL-3.0；"Initial commonlibsse support"（2026-02-22）、
  "retarget UpdateHook2 for AE 1.7.99"（2026-08-23）等 commit）
- **BodySlide（一手）**：`https://www.nexusmods.com/skyrimspecialedition/mods/201`（5.9.1，2026-10-04）
- **1.6.1130 → 2.2.4、1.6.1170 → 2.2.6 的早期佐证**：PapyrusUtil 官方 changelog
  `https://www.nexusmods.com/skyrimspecialedition/mods/13048`（4.5 / 4.6 两条）—— **一手**
- **1.6.640 / 1.7.9x 不被 Community Shaders 支持**：`community-shaders-kb` 记录 —— **一手（CS 官方）**
- **未确认项（本轮未能核实，请勿当作结论）**：FSMP 4.1.1 面向的具体游戏版本；1.6.659 / 1.6.353 对应的
  Address Library 版本；2.2.8 的面向游戏版本（由 changelog 推断）
