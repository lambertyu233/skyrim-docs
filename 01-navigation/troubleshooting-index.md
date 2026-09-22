---
id: troubleshooting-index
title: 排错索引：从症状找答案
category: 01-navigation
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [排错, 索引, 症状, 导航, 入口]
aliases: [排错索引, 症状索引, 症状对照, 问题排查, 从症状找, 故障对照, troubleshooting, error, issue]
source: 本工作区七库汇总（条目路径见下）
summary: 全工作区的排错入口——按"你看到的现象"组织，每条症状直接给出该读哪个库的哪一条，并标出最容易误判的分叉点。
---

# 排错索引：从症状找答案

本工作区七个资料库按**主题**组织（捏脸与身形 / OAR / 动作引擎 / Community Shaders / Creation Kit / MO2，外加一个入口索引）。
但你出问题时手里拿的是**症状**，不是主题。这页就是那座桥。

> 用法：直接搜你的现象（如"T-Pose""贴图糊""改了没反应"）。
> 每条给出**该读的条目路径**，以及**最容易被误判的分叉点**——后者比前者更值钱。
> 路径均为相对工作区根目录的形式，例如 `oar-kb/05-editor/troubleshooting.md`。

---

## 一、动画、动作、姿势

| 你看到的 | 该读 | 关键分叉（别搞错方向） |
| --- | --- | --- |
| **角色摆大字（T-Pose / A-Pose）** | `oar-kb/05-editor/troubleshooting.md`（T-Pose 专项诊断）<br>`behaviour-engine-kb/06-practices/troubleshooting-common.md` | **先分类再动手**：开局几秒 = 正常预加载；一直摆且 OAR 的 Replacement Animations 面板为空 = OAR 侧问题；一直摆且行为文件坏了 = 补丁器侧问题。**OAR 的锅不会靠刷 Pandora 解决，反之亦然** |
| **换了动画完全没反应** | `oar-kb/05-editor/troubleshooting.md`<br>`oar-kb/08-practices/animation-key-model.md` | 顺序：①文件名是不是游戏请求的那个（换错文件名是头号原因）②旧 DAR 结构是否还在 `meshes\` 下③有没有重启游戏 |
| **动画换了，但某个状态掉回原版** | `oar-kb/08-practices/animation-key-model.md` | 那个状态请求的是**另一个文件名**。最常见的就是"一移动就掉回原版"——移动是独立的一套事件名 |
| **不该换的状态也被换了** | `oar-kb/03-conditions/conditions-list.md`（`AttackState`）<br>`oar-kb/05-editor/troubleshooting.md` | 条件太宽。典型修法：用 `AttackState` 而不是 `IsAttacking`（后者在整个攻击过程都为真，不区分阶段） |
| **拉弓拉一半移动就跳成满弓姿势** | `oar-kb/03-conditions/conditions-list.md`<br>`oar-kb/08-practices/authoring-workflow.md`（进阶技巧） | 需按 `AttackState` 阶段拆成多个 submod 并开 `interruptible: true`，靠阶段交接 |
| **有个随机动画在跟我的抢** | `oar-kb/02-structure/config-and-priority.md`<br>`oar-kb/05-editor/troubleshooting.md` | 比优先级；**同优先级**会让编辑器报警告 |
| **改了配置但编辑器里没变** | `oar-kb/05-editor/in-game-editor.md` | 忘了保存（User 模式看左上角有没有橙色 `*`） |
| **FNIS/Nemesis 报 hkx 不兼容** | `behaviour-engine-kb/06-practices/troubleshooting-common.md`<br>`oar-kb/08-practices/animation-key-model.md` | LE 的 32 位 hkx 丢进了 SE。**判定不能看 hkx 标签头**（LE/SE 共用），只能与已知可用的 SSE 文件逐字节比对 |

## 二、MO2 与文件覆盖

| 你看到的 | 该读 | 关键分叉 |
| --- | --- | --- |
| **文件里有两份，不知道游戏用了哪个** | `mo2-usvfs-kb/05-usage/conflict-resolution.md` | mod 列表**越靠下优先级越高**。想确认到底读的哪份，开 `mo2-usvfs-kb/04-debugging/debugging-usvfs.md` 的调试日志看 `reroute.fileName()` |
| **游戏目录里找不到我装的 mod 文件** | `mo2-usvfs-kb/05-usage/usage-faq.md`<br>`mo2-usvfs-kb/01-mechanism/process-local-links.md` | **这是正常的**，不是故障。mod 物理在 `mods\`，只在被注入的进程内可见 |
| **工具（LOOT/xEdit/BSA Browser）看不到 mod** | `mo2-usvfs-kb/06-reference/faq.md` | 必须**从 MO2 内启动**该工具，直接双击 exe 看不到虚拟视图 |
| **装完 mod 没生效** | `mo2-usvfs-kb/05-usage/enable-and-activate.md` | 两步：先勾选启用 mod，**再**去 Plugins 页激活其 esp/esm。**插件放在子文件夹里不会被识别** |
| **MO2 怪问题/注入似乎没生效** | `mo2-usvfs-kb/06-reference/troubleshooting-vfs.md` | 按顺序查：杀软拦截（常无提示）→ HVCI/Core Isolation → Windows Event Log 服务 → 系统日志被清后需**"重启"而非关机** |
| **profile 切换时 MO2 崩溃** | `mo2-usvfs-kb/05-usage/profile-switching.md`<br>`mo2-usvfs-kb/06-reference/troubleshooting-vfs.md` | 先排杀软与 Event Log 服务，别急着重建 profile |
| **警告图标说 mod 顺序有问题** | `mo2-usvfs-kb/05-usage/warnings-and-order-problems.md` | **它管的是资源（贴图/网格）覆盖顺序，不是 esp 加载顺序**——后者归 LOOT/Plugins 页的 Sort |

## 三、画质与着色器

| 你看到的 | 该读 |
| --- | --- |
| **装完 CS 后游戏变亮/变暗、光照不对** | `community-shaders-kb/01-installation/installation-guide.md`、`community-shaders-kb/03-reference/faq.md` |
| **从 ENB 迁到 CS 或想两者共存** | `community-shaders-kb/01-installation/enb-migration.md` |
| **某个效果与已有 mod 冲突** | `community-shaders-kb/03-reference/incompatible-mods.md` |
| **不知道某功能该不该开、吃多少性能** | `community-shaders-kb/00-overview/feature-matrix.md`、`community-shaders-kb/03-reference/faq.md` |
| **闪烁 / 阴影异常 / 贴图噪点** | `community-shaders-kb/06-community/common-pitfalls.md` |

## 四、Creation Kit 与脚本

| 你看到的 | 该读 |
| --- | --- |
| **Papyrus 脚本不编译 / 报编译错** | `creation-kit-kb/04-scripting/compiling-scripts.md`、`creation-kit-kb/04-scripting/papyrus-language.md` |
| **某个事件/函数不知道怎么写** | `creation-kit-kb/04-scripting/events-reference.md`、`creation-kit-kb/04-scripting/function-reference.md` |
| **CK 启动异常 / 找不到 ini** | `creation-kit-kb/01-installation/ini-files.md`、`creation-kit-kb/01-installation/install-and-launch.md` |

## 五、动作引擎侧（重刷与补丁）

| 你看到的 | 该读 |
| --- | --- |
| **到底该不该重刷 Nemesis/Pandora？** | `behaviour-engine-kb/01-principles/patcher-vs-replacer.md`——**OAR 是 Replacer，改动画不需要重刷**；新增动画命令才需要 Patcher |
| **引擎跑出 0 animations added / 无输出** | `behaviour-engine-kb/06-practices/troubleshooting-common.md` |
| **Nemesis 报 2006 / 1210 / 6001** | `behaviour-engine-kb/06-practices/troubleshooting-common.md`（含三个编号的对策） |
| **读档 CTD** | `behaviour-engine-kb/06-practices/troubleshooting-common.md` |
| **FNIS / Nemesis / Pandora 该选哪个** | `behaviour-engine-kb/06-practices/choosing-engine.md` |
| **Pandora 输出只有 txt** | `behaviour-engine-kb/04-pandora/pandora-troubleshooting.md`（查 .NET 7 Desktop Runtime 与 `Engine.log`） |

---

## 六、捏脸与身形

| 你看到的 | 该读 | 关键分叉 |
| --- | --- | --- |
| **捏的脸进游戏是黑的** | `character-appearance-kb/06-troubleshooting/dark-face.md` | 真因常是**左栏资产优先级与右栏插件顺序不一致**，不是某个美化 mod 坏了。先用 Face Discoloration Fix 应急，再用 CK 的 `Ctrl+F4` 正本清源 |
| **脖子/手腕一圈接缝** | `character-appearance-kb/06-troubleshooting/neck-seam.md` | 先查**头/手/身体是不是同一套皮肤同一档**，再查皮肤与身形是否同族（CBBE 与 UNP 的 UV 不通用）。**脖缝修补 mod 是创可贴，不是解法** |
| **裸体调好了，穿上衣服又变样** | `character-appearance-kb/03-body/morph-runtime-vs-bake.md` | 那件衣服**没被 3BA 化、不带同名 morph**，所以运行时它不动。不是你的操作错了，是那件衣服不支持 |
| **换了 BodySlide 预设后衣服穿模** | `character-appearance-kb/06-troubleshooting/clipping.md`<br>`character-appearance-kb/03-body/morph-runtime-vs-bake.md` | **根因是「构建是烘焙、滑块是运行时」**：换预设只重烘了身体。正解是 Zeroed Sliders + Build Morphs + Batch Build 全部服装 |
| **RaceMenu 里没有身形滑块** | `character-appearance-kb/06-troubleshooting/racemenu-sliders-missing.md` | 顺序：① SKSE 版本是否匹配 ② BodySlide 有没有勾 `Build Morphs` ③ `RaceMenuMorphs*.esp` 是否启用 ④ 构建产物是否被别的 mod 覆盖 |
| **身形装了但完全没物理** | `character-appearance-kb/06-troubleshooting/physics-not-working.md` | 先跑 `smp report`；再查**身形装的是不是 physics 变体**（最易忽略）；再查 SMP 与 CBPC 是否在抢同一批骨骼 |
| **NPC 身材全都一样** | `character-appearance-kb/05-distribution/obody-ng.md` | 运行时 morph **只作用于玩家**。NPC 需要分配工具，且它要求你先做过 Zeroed Sliders 的基础构建 |
| **黑脸 / 穿模 / 脖缝同时出现** | `mo2-usvfs-kb/05-usage/conflict-resolution.md`<br>`character-appearance-kb/07-workflow/mo2-override-rules.md` | **跨库问题**：这些症状共同的**上游**是 MO2 的覆盖关系。先理顺左右栏，再回各专项条目 |

---

## 通用排查纪律（跨库都适用）

1. **先读日志，再猜原因**。每个子系统都有唯一的权威日志：
   - OAR → `Documents\My Games\Skyrim Special Edition\SKSE\OpenAnimationReplacer.log`
   - Pandora → `Engine.log`
   - MO2 / usvfs → 开调试日志看 `hook_*` 与 `reroute.fileName()`
   - Community Shaders → 见 `community-shaders-kb/04-development/testing-and-debugging.md`
   **没有日志证据的结论只是猜测。**
2. **区分"没加载"和"加载了但没生效"**。这两类的修法完全不同：前者查文件/路径/冲突，后者查条件/优先级。日志是唯一能区分的手段。
3. **别跨层归因**。OAR 的问题不会靠重刷补丁器解决，补丁器的问题也不会靠改 OAR 条件解决；MO2 的覆盖问题更不归 LOOT 管。
4. **一次只改一个变量**，改完重启游戏。

> 本页是索引，不是正文。条目内容的权威版本始终在各库原文件；改动请改原条目，不要在此处复制正文。
