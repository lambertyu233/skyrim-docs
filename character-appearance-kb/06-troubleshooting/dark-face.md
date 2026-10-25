---
id: dark-face
title: 黑脸 / 黑头（Dark Face Bug）
category: 06-troubleshooting
kind: tutorial
version: 2.0.0
updated: 2026-10-25
tags: [排错, 黑脸, 黑头, FaceGen, 冲突]
aliases: [dark face, 脸变黑, NPC 黑脸, 头像变黑, face discoloration, face discoloration fix, 脸色发黑, 脸部变色, 重导 FaceGen, Ctrl+F4, 左栏右栏不一致, 黑脸修复, 脸变灰]
source: https://www.nexusmods.com/skyrimspecialedition/mods/42441
summary: 黑脸的根本成因（FaceGen 数据与 head parts 不匹配导致 tint 被丢弃）、按频率排序的成因清单与有序排查、四种修法（运行时修复 / CK 重导 / 隐藏冲突文件 / 调序打补丁），以及"这是数据缺失不是贴图问题"这条总认知。
---

# 黑脸 / 黑头（Dark Face Bug）

> **一句话**：黑脸不是"贴图坏了"，而是 **FaceGen 预生成数据与插件记录对不上**——
> 游戏重新生成脸时丢掉了 tint，于是脸变黑。修的是"把数据对上"，不是"换图片"。

## 速览

| 项 | 内容 |
|---|---|
| 症状 | NPC（偶尔也含玩家）**头部变黑 / 变灰**，身体颜色正常 |
| 高频成因 | FaceGen 数据缺失或与 head parts 不匹配；多个 mod 改同一 NPC 互相覆盖 |
| 首选判据 | 只有头黑、身不黑 ⇒ 查 `FaceGeom` / `FaceTint` 两个路径下的文件**是否存在、是否被覆盖** |
| 最短修复路径 | 治标：装 **Face Discoloration Fix**；治本：理顺覆盖关系后用 CK **`Ctrl+F4`** 重导 |

要点：

- **第一性事实**：NPC 的脸是**预生成**的静态文件，不是实时算的——
  "插件记录改了、磁盘文件没跟着重导"就是黑脸（机制见
  [FaceGen 管线与 head parts](../02-face/facegen-pipeline.md)）。
- **最常见的真因是覆盖错位**：MO2 左栏（资产优先级）与右栏（插件顺序）不一致，
  某 mod 赢了 NPC 记录，FaceGen 文件却被别的 mod 覆盖。
- **`Ctrl+F4` 不是万能修复键**：它按"当前插件数据"重新生成，冲突没理顺时
  可能把脸导回原版样。
- **Face Discoloration Fix 只修变色**：load order 冲突破坏 NPC 美化这类根因还在，
  脸依然不是你想要的那张。
- **黑脸与皮肤 mod 无关**：换皮肤不能解决黑脸（见
  [脸部皮肤与纹理](../02-face/face-textures.md)）。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| LE 时代（具体日期未确认） | 引擎自带 **FaceGen 预生成机制**（CK 的 `Ctrl+F4` = Export FaceGen data） | NPC 的脸是"烘焙品"：改记录必须重导，这是黑脸的土壤（一手：CK / UESP 文档） |
| 2011-2012 | CBBE 与 UNP 分家、皮肤开始分 UV 家族 | 与黑脸无关，但同期普及的"头身分开打包"让覆盖错位更容易发生（见 [身体皮肤材质](../03-body/body-textures.md)） |
| 2013-01-08 | **RaceMenu LE 首发** | 玩家的脸第一次能导出成网格；NPC 侧仍全靠预生成 |
| 2018-08-06 | **RaceMenu SE 首发**（`skee64.dll`：CharGen + NiOverride） | 运行时 tint / overlay 体系成熟，"重新生成脸"的路径被更多 mod 触及 |
| 2019-2021（具体年份未确认） | **High Poly Head** 普及 | "换头模必须给 NPC 重导 FaceGen"成为常规动作，黑脸进入高发期（见 [High Poly Head](../02-face/high-poly-head.md)） |
| 未确认 | **Face Discoloration Fix** 发布（作者 **Parapets**，仓库所有者 **Exit-9B**，MIT） | 第一条"运行时阻止丢 tint"的路；当前版本 **1.0.4** |
| 2026-08 | 游戏 **1.7.x** 更新 | RaceMenu 未适配 + overlay nif 必崩是**另一回事**，别与本条混诊（见 [overlay-nif-ctd](../06-troubleshooting/overlay-nif-ctd.md)） |

### 它从哪来

黑脸不是某个 mod 引入的 bug，而是 **Bethesda 的 NPC 脸预生成设计**与
**mod 生态不断改记录**之间张力的必然产物。引擎为了省性能，把每个 NPC 的脸
在编辑器里算好、落盘成两个文件；而美化 mod 的工作方式就是"改插件记录"。
两边一旦不同步，游戏只能在运行时重画脸——而重画会丢 tint。

### 中间经历了什么

社区对策的演进正好三步：**早期**靠"删了重装、互相试"；
**中期**形成 CK `Ctrl+F4` 重导的标准流程与 Black-Face 补丁指南；
**近年**有了 Face Discoloration Fix 这种运行时补丁（等价于 `Ctrl+F4` 的运行时版本），
把"治本"与"治标"正式分开。

### 现状

引擎机制没变，黑脸的成因结构也没变；变化的是**触发面更宽了**——
ESL 化 / 改插件名、整合包自动排序、HPH 换头、RaceMenu 预设生态，
每一步都在增加"记录与产物对不上"的机会。

## 成因（按发生频率排序）

### ① FaceGen 数据缺失或未导出

改了 NPC 的脸（换美化、换头模），但没有在 CK 里 `Ctrl+F4` 重新导出。

**为什么**：插件记录指向新的 head parts / 染色，而磁盘上的
`FaceGeom` / `FaceTint` 还是旧的（或根本不存在），游戏只能重画脸并丢 tint。

```
Meshes\Actors\Character\FaceGenData\FaceGeom\<插件名>\<FormID>.nif
Textures\Actors\Character\FaceGenData\FaceTint\<插件名>\<FormID>.dds
```

### ② 多个 mod 改同一 NPC 且互相覆盖

两个 NPC 美化 mod 都改了同一个 NPC，或者美化 mod 与"修改该 NPC 数据"的
quest / gameplay mod 撞车。

**为什么**：后加载的记录赢，但**产物未必跟着更新**——记录与产物错配，必黑。

### ③ MO2 左栏（资产优先级）与右栏（插件顺序）不一致 ⭐ 最易误判

某 mod 赢了 NPC 记录（右栏在前），但它的 FaceGen 文件在左栏被别的 mod 覆盖。

**为什么**：这是本类问题里**回报率最高**的一条——很多人会去怀疑"某个美化 mod 坏了"，
实际是自己排完 LOOT 后右栏变了、左栏没跟着对齐。覆盖规则见
[mo2-override-rules.md](../07-workflow/mo2-override-rules.md) 与跨库的
[冲突解决](../../mo2-usvfs-kb/05-usage/conflict-resolution.md)。

### ④ 插件改名 / ESL 化导致 `<插件名>` 目录失效

FaceGen 路径里的目录名是**插件名**。ESL 化、重命名会让整个目录失效。

**为什么**：游戏按"插件名 + FormID"去找文件；目录名对不上 = 文件不存在 = 重画脸。
能不改插件名就别改，这是性价比最低的翻车方式。

### ⑤ 自定义头网格（HPH 等）未重导 FaceGen

HPH 给 NPC 用的官方流程是三步：把 HPH 设为该 NPC 所在插件的 master →
换掉原版 head parts → `Ctrl+F4`。只做前两步 = 黑脸。

**为什么**：HPH 官方明确"对带雕塑的头网格无效"（This method does not work for
sculpted head meshes）—— sculpted 头走不了这条路，需要另做。
CotR / UBE 这类拓扑、UV、morph 全变的更不用提，预设与 tint 都不通用
（见 [UBE 2.0](../03-body/ube.md)）。

### ⑥ tint mask 被改过，污染了导出或加载

**为什么**：tint mask 是"上层着色"的源。本地 `tintmasks` 被改过时，
`Ctrl+F4` 的导出结果会被污染——注意这类问题的表现是**紫、红、额头条纹**，
不是纯黑，判据不同（见「判断分叉点」）。

### ⑦ BSA 里的旧版本压住了磁盘文件

产物被 BSA 里的旧版本压住时，改磁盘文件看不出效果。

**为什么**：覆盖规则里 BSA 与 loose 文件的优先级会骗过眼睛——你以为改了，
游戏读到的还是旧的那份。

## 排查顺序（照着走）

```
1. 是"纯黑"还是"花脸"（紫 / 红 / 额头条纹）？
   纯黑  → 走 FaceGen 匹配链（第 2 步起）
   花脸  → 查 tintmasks 污染（成因⑥），导出前先移走 tintmasks

2. 只有一个 NPC 黑，还是一批黑？
   一个   → 该 NPC 的 FaceGen 或它的专属覆盖
   一批   → 找共同因子：同一个美化 mod / 同一个皮肤 / 同一次自动排序

3. 最近是否装/卸了 NPC 美化、ESL 化过插件、跑过 LOOT？
   是     → 高度怀疑左栏右栏不一致（成因③），直接查 Conflicts

4. 在 MO2 里按 FormID 搜该 NPC 的 FaceGeom.nif / FaceTint.dds
   看到 X：覆盖者不是该美化的文件  → 说明是 Y：左栏覆盖错位，hide 掉覆盖者

5. 是否换了头模（HPH 等）却没 Ctrl+F4？
   是     → 按 HPH 官方三步重导；带雕塑的头网格这条路无效

6. 以上都排完还黑 → Face Discoloration Fix 治标 + CK 重导治本
```

> **经验法则**：黑脸问题 90% 能在"两个路径上的文件是否存在、是否匹配"里定位，
> 再怀疑 mod 冲突。先查文件，再查排序。

## 修法

### ① 运行时修复（最快，治标）

装 **Face Discoloration Fix**（作者 **Parapets**，仓库所有者 **Exit-9B**）：

- Nexus：`https://www.nexusmods.com/skyrimspecialedition/mods/42441`
- 仓库：`https://github.com/Exit-9B/Face-Discoloration-Fix`（**MIT**）
- 版本 **1.0.4**（更新到 Address Library 12，静态链接 VC++ Runtime）；
  历史：1.0.3 支持 1.6.629+，1.0.2 支持 1.6.318+，
  1.0.1 修了坏 race（RNAM）数据导致的启动崩溃并加 VR 支持。

**它的做法**：阻止游戏在重新生成脸时丢弃 tint 数据，让重生成的颜色正确。
等价于 **CK 的 `Ctrl+F4` 的运行时版本**。

**代价**：实时生成 FaceGen 比加载预处理慢——
作者测得预处理约 **0.2 ms/NPC**，实时生成约 **30–70 ms/NPC**。

**限制**：它**只修变色**。如果 load order 冲突破坏了 NPC 美化 mod，
它无法恢复原貌——**根因还在**。

### ② Creation Kit 正本清源（治本）

1. 加载相关插件（`CreationKit.ini` 需允许加载多个 master）；
2. Objects → Actors → Actor，**在子树里直接选中**目标 NPC
   （不要用搜索选 `*All*`）；
3. **`Ctrl+F4`** 导出 FaceGen。

导出前技巧（社区经验）：若 tintmask 被改过，先临时把
`Textures\Actors\Character\Character Assets\tintmasks` 改名/移走，
导完再改回，否则导出结果被污染。

### ③ MO2 隐藏冲突 FaceGen

- 在 MO2 的 **Conflicts** 里找覆盖者；
- 按 FormID 搜冲突的 `.nif` / `.dds`，把它们 **hide** 掉
  （隐藏文件的方法见跨库 [hide-files-and-filetree](../../mo2-usvfs-kb/05-usage/hide-files-and-filetree.md)），
  确保 FaceGen 来自正确的美化 mod；
- 同时检查插件顺序，让该美化 mod 的 NPC 记录优先。

### ④ 调序 / 打补丁

- 让 NPC 美化 mod 位于"修改该 NPC 数据"的 mod **之后**；
- 多个 NPC 美化共存时，用 SSEEdit 逐个做 patch（合并外观记录 + 对齐 FaceGen）。

社区另有一份专门的 **Black-Face Patching Guide**（Nexus `mods/17004` 的 PDF 附件）。

## 判断分叉点（别误诊）

| 看起来像 | 其实 |
|---|---|
| "皮肤 mod 坏了，换皮肤试试" | **黑脸与皮肤无关**：脸是"贴图没对上网格"（数据缺失），皮肤是"贴图内容"。混着查浪费大量时间 |
| "RaceMenu / EFM 出问题了" | EFM **只影响玩家**；NPC 黑脸走 FaceGen 路线。EFM morph 也不适用于 HPH（见 [EFM](../02-face/expressive-morphs.md)） |
| "游戏崩了 / 1.7.x 的锅" | overlay nif 崩溃是**启动或进捏脸时直接崩**，不是黑脸；两回事（见 [overlay-nif-ctd](../06-troubleshooting/overlay-nif-ctd.md)） |
| "脸是紫的 / 红的 / 额头有条纹" | tintmasks 污染导出结果，不是黑脸成因链；导出前移走 tintmasks |
| "随从的脸在别人机器上不对" | `.dds` 没按 **BaseID** 命名，或没放进正确的 `<插件名>` 目录 |
| "改了 `.dds` 却没变化" | 被 BSA 或别的 mod 覆盖——查覆盖优先级，别急着重装 |

## 取舍与建议

- **先治标再治本**：不确定根因时，先装 Face Discoloration Fix 让脸能看，
  再按排查顺序理顺覆盖；但永远记得"根因还在"。
- **能不改插件名就别改**：ESL 化前先想清楚 FaceGen 目录的连带失效。
- **HPH 给 NPC 用是重活**：master + 换 head parts + `Ctrl+F4` 三步，
  批量改造用官方 xEdit 脚本（`KL Swap Headparts`），带雕塑的头网格这条路无效。
- **记录你的环境**：黑脸复发时，"最近动了什么"比任何日志都有用。

## 来源

- **成因（FaceGen 与 head parts 不匹配 → 丢 tint）与运行时代价（0.2 ms vs 30–70 ms/NPC）**：
  Face Discoloration Fix Nexus 页描述 + GitHub README —— **一手**
  `https://www.nexusmods.com/skyrimspecialedition/mods/42441`
  `https://github.com/Exit-9B/Face-Discoloration-Fix`
- **FaceGen 路径与 `Ctrl+F4` 流程、`<插件名>` 目录与插件改名的后果、
  "只做第一步 = 必定黑脸"、tintmasks 污染（紫/红/额头条纹）**：
  CK wiki / UESP + [facegen-pipeline.md](../02-face/facegen-pipeline.md) —— **一手 + 本库整理**
- **HPH 给 NPC 用的三步与"对雕塑头网格无效"、官方 xEdit 脚本、
  High Poly NPCs 的黑脸警告**：[high-poly-head.md](../02-face/high-poly-head.md)（官方说明经镜像转述）—— **一手（经转述）**
- **"左栏右栏不一致"这一成因**：Nexus 论坛帖 —— **社区经验（多帖一致）**
- **MO2 隐藏冲突 FaceGen**：Black-Face Fix Guide（Nexus `mods/77338`、`mods/17004`）—— **社区经验**
- **"`Ctrl+F4` 会重置为当前数据描述的脸"**：**机制推论 + 社区一致经验**
- **EFM 只影响玩家、EFM morph 不适用于 HPH**：EFM Nexus 发布页 —— **一手**
