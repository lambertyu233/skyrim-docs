---
id: high-poly-head
title: High Poly Head（高模头部）
category: 02-face
kind: tool
version: 2.0.0
updated: 2026-10-25
tags: [捏脸, 高模头, HPH, 脸部网格]
aliases: [high poly head, 高模头部, klf, 头部网格, 高聚头, 高面头, 棱角脸, 脸部拓扑, Face Part, 高模头怎么装, vectorplexus, KouLeifoh, 换头模]
source: https://vectorplexus.com/files/file/283-high-poly-head/
summary: 高模头（HPH）的作者与"为什么它不在 Nexus 主流分发"、它对原版头部网格做了什么、Face Part 切换这一使用前提、给 NPC 用必须重导 FaceGen 的流程与官方 xEdit 脚本、FOMOD 选项与已知坑，以及它与 ECE / EFM 的关系。
---

# High Poly Head

> **一句话**：HPH 是**在原版头部网格基础上加密网格**的替换件 —— 脸还是那张脸，
> 但棱角没了、可捏的细节多了。**它不是自动生效的**，必须在 RaceMenu 里切过去。

---

## 速览

| 项目 | 值 |
|---|---|
| 作者 | **KouLeifoh**（社区常缩写 **KLF**） |
| 当前版本 | **1.4**（LE 与 SE 双版本） |
| 官方分发 | **Vector Plexus**：`https://vectorplexus.com/files/file/283-high-poly-head/`（**需注册账号**） |
| Nexus 上有什么 | **只有补丁与镜像**，没有本体（详见下表） |
| 备用渠道 | **Wabbajack 白名单里的 Google Drive 作者备份**（作者授权给 Wabbajack 用于整合包） |
| 前置 | **RaceMenu（LE / SE）** —— 硬前置 |
| 可选前置 | Expressive Facegen Morphs、Expressive Facial Animation（男/女版） |
| 影响范围 | 头部网格 + brows / beards / scars / hair 的配套高模件 |
| 维护状态 | **1.4 长期未变**；1.4 之后是否有更新**未确认** |

Nexus 上能找到的（都是**补丁或镜像**，不是本体）：

| mod | Nexus | 性质 |
|---|---|---|
| High Poly Head For Custom Races | 43098 | 补丁 |
| Brows by Hvergelmir for High Poly Head - COTR - UBE | 63777 | 眉毛适配补丁 |
| Alternate High Poly Head | 148541 | 镜像，其 credits 明写 KouLeifoh 为原作者 |
| High Poly NPCs | 69604 | 用 HPH + KS Hairdos 重做一批 mod 新增 NPC（要求 HPH 1.4） |

要点：

- **别把作者认成 KS Hairdos 的 Kalilies。** KLF = KouLei**f**oh。
- **它是"加密后的原版头"**：比例与基础脸型仍然是原版的 —— 想要彻底换脸型请去看别的路线。
- **装了没效果 = 你没在 RaceMenu 里切 Face part**，这是最高频的问题。
- **给 NPC 用必须重导 FaceGen**，而且**对带雕塑的头网格无效**。

---

## 前世今生

### 为什么它不在 Nexus 主流分发

这是新人最容易困惑的一点：**搜 Nexus 搜不到本体**。原因是作者选择把主文件放在
**Vector Plexus**（一个需要注册的 mod 站），Nexus 上流通的都是他人做的补丁与镜像。

连锁后果有三个，都值得知道：

1. **下载要注册 Vector Plexus 账号**（社区普遍反映注册/登录过程比较折腾）。
2. **整合包拿不到直链** —— 于是 **Wabbajack 专门找作者要了授权**，把作者的
   **Google Drive 备份**加进了白名单，装整合包时会自动从 GD 拉。
   这也是"为什么大家都在传一个 Google Drive 链接"的由来。
3. **版本号容易被传错** —— 各处镜像标注不一，**以 Vector Plexus 页面为准**。

> 社区有"Vector Plexus 原域名失效"的说法 —— **未确认**。
> 本轮检索中，官方页地址在社区引用里同时出现 `vectorplexus.com` 与 `vectorplexis.com`
> 两种写法，**哪个为准未确认**（可能换过域名）。

### 时间线

| 时间 | 事件 | 意义 |
|---|---|---|
| 未确认 | HPH **1.0** 发布。2019-12 的社区搬运帖已在介绍"High Poly Head 1.0（SE/LE）"，并提到作者是 **SAM Light 的作者**（**社区经验，未确认**） | 进入公众视野 |
| 未确认 | 1.0 → 1.4 之间的迭代 | **各版本日期未确认** |
| 当前 | **1.4** 为现行版本，官方描述与 FOMOD 选项均以 1.4 为准；社区大量预设与 NPC 美化都以 1.4 为基准 | 事实标准 |
| 未确认 | 1.4 之后是否还有更新 | **未确认** |

### 它和"换脸型"不是一回事

HPH 的官方定位写得很清楚：**基于原版头部网格**（based on the vanilla head meshes）的
高模版本。Enderal 上一个同类竞品（Freyr）的作者在对比文章里说得最直接（**一手，该作者文章**）：

> HPH 提供更平滑、顶点更多、便于在 RaceMenu 里精修的头，**但它仍然以那个"丑陋的
> 原版头网格"为基底，因此依然继承了原版头那种奇怪的比例与平淡的形状。**

这条引文很关键：它界定了 HPH 的**能力边界** —— 想要"换一张结构更好的脸"，
HPH 解决不了，那属于换头模/换种族的范畴。

---

## 它解决什么问题

### 没有它之前

原版头部网格是**低模**的：面数少，导致

- **明显的棱角**（尤其在鼻梁、颧骨、下颌），社区俗称"棱角脸"；
- 在 RaceMenu 里做 **Sculpt** 时，笔刷一动就是一大片，捏不出细节；
- 眉、须、疤痕这些**贴着脸的部件**是按原版头的形状做的，换头模就会破皮。

### 它怎么解决的

官方描述列出的四件事：

| 改动 | 说明 |
|---|---|
| **平滑的高模男女头部** | 覆盖**全部可玩的原版种族**，基于原版头网格加密 |
| **配套的高模 brows / beards / scars / hair** | 让贴脸部件适配新头型（官方强调这块花了很多时间，不会破皮） |
| **给 RaceMenu 扩展滑块的 morph** | 高模头自己带了 morph 数据，滑块才有得改 |
| **兼容基于原版的头部纹理** | 原版 / SAM / SAM Light / SOS 一类基于原版 UV 的皮肤仍可用 |

另外官方还承诺：**兼容为原版男女头网格做的既有预设**（**但不含雕塑数据**）。

> **顶点数未确认。** 本库未能取得 HPH 头部网格的确切顶点/面数。
> 能确认的是**它与原版头的顶点数不同** —— 这正是"原版雕塑不能直接导入高模头"的根因
> （社区经验）。

---

## 安装

1. **先装好 RaceMenu**（硬前置），确认捏脸界面能用。见 [`racemenu.md`](racemenu.md)。
2. **从官方渠道拿 1.4**：Vector Plexus（需注册）或 Wabbajack 白名单的 Google Drive 备份。
   验证点：压缩包内应有 `High Poly Head.esm`（官方 xEdit 脚本要求它被载入 xEdit）。
3. **用 mod 管理器装原 zip，走安装脚本**。官方明确：**不要手动解压**
   （*"Do not manually extract anything"*）。
4. **按需勾选 FOMOD 选项**（见下）。
5. **装完后切脸**：进游戏开捏脸界面 → **Head 页 → Face Part 滑块** → 切到高模头。
   验证点：脸部棱角明显减少；同时**把眉毛/胡须/疤痕也换成 HPH 自带的版本**
   （官方使用说明明确要求）。
6. **若头变黑**：改一下 player weight，强制刷新皮肤着色器（官方给出的处理方式）。

### FOMOD 选项（官方手册安装项，00–10）

```
00 Base mod                                          必选
01 Loose files needed for FaceGen creation in CK     在 CK 里导 FaceGen 需要
02 no Dawnguard DLC
03 vampire head fix
04 remove sunken vampire face morphs
05 symmetrical eye sockets (female)                  女性眼窝 UV 对称化
06 adds Aesthetic Elves
07 adds Expressive Facegen Morphs                    与 EFM 配套
08 adds Expressive Facial Animation Male edition
09 adds Expressive Facial Animation Female edition
10 adds high poly vanilla hair as optional replacers
```

> 官方说明里 05 的作用是"让女性头部的眼窝在 UV 上对称"，并注明
> **兼容 Fair Skin Complexion 一类基于 ECE 的纹理**（本轮检索到的镜像说明如此标注）。

---

## 使用与配置

### 给自己用：切 Face part

> **HPH 不是装上就生效的。** 必须在 RaceMenu 里切：
> **Head 页 → Face Part 滑块 → 切到高模头。**

社区帖里常写"把 Face Part 拉到 3"（**社区经验，官方描述只说用 Face Part 滑块切换，
未给出具体档位编号**）。切完记得：

- 把 **brows / beard / scars** 一并换成 HPH 自带的版本；
- 头变黑 → **改 player weight** 强制刷新皮肤着色器。

### 给 NPC / 随从用：必须重导 FaceGen

NPC 的脸是**预生成**的（原理见 [`facegen-pipeline.md`](facegen-pipeline.md)），
所以换头只是换了记录，还得重新导出网格与贴图：

1. **把 HPH 设为该 NPC 所在插件的 master**；
2. **把 NPC 的原版 head parts 换成 HPH 版本**；
3. 在 Creation Kit 里选中该 NPC → **`Ctrl+F4`** 重新导出 FaceGen。

> **限制（官方原文）**：**This method does not work for sculpted head meshes.**
> 只适用于已导出的静态头网格，**带雕塑几何的头网格走不了这条路**。

### 官方附带的 xEdit 脚本（Modder Resource）

HPH 1.4 自带三个 xEdit 脚本，批量改造 NPC 时很有用：

| 脚本 | 作用 |
|---|---|
| `Skyrim - KL Filter Race.pas` | 按"HPH 支持的种族"筛选 NPC 记录 |
| `Skyrim - KL Swap Headparts.pas` | 把原版 head part 批量换成高模版本。**不支持自定义 head part**；要求 `High Poly Head.esm` 已载入 xEdit |
| `Skyrim - KL Copy NPC Protected Status.pas` | 复制 NPC 的 Protected 状态（例如配合 NPCs Protected Redux 使用） |

### 不想自己动手：现成的 NPC 美化

- **High Poly NPCs**（Nexus 69604）：给一大批 mod 新增的人类 NPC 换上 HPH 脸 + KS Hairdos，
  全部 ESL 化。要求 **HPH 1.4**。作者提醒：**别让别的东西覆盖它的插件与脸网格/贴图，
  否则会黑脸**（见 [`../06-troubleshooting/dark-face.md`](../06-troubleshooting/dark-face.md)）。
- PC Gamer 的推荐文里也提到一个把 HPH 分发给全部原版 NPC 的补充 mod
  （*High Poly Heads AND Hair for All Vanilla NPCs*）—— **其 Nexus ID 未确认**。

---

## 兼容与冲突

| 对象 | 关系 |
|---|---|
| **RaceMenu** | **硬前置**（官方 Requirements 只列了它） |
| **ECE** | **不兼容**。两者都改头部网格，方向冲突；社区共识是"装了 HPH 就别装 ECE"。另外 **ECE / RaceMenu / EFM 用的是不同的种族 morph，基础脸型不同，预设不能简单互通** |
| **EFM（Expressive Facegen Morphs）** | FOMOD 有专门的配套选项（07）。但 **EFM 的 morph 不适用于 High Poly Head**（EFM 作者明确表示暂无计划支持）。见 [`expressive-morphs.md`](expressive-morphs.md) |
| **EFA（Expressive Facial Animation）** | FOMOD 有 08/09 两个配套选项 |
| **原版头纹理 / SAM / SOS 系皮肤** | 官方称兼容（基于原版 UV 的纹理可用）；但**身形 UV 不同**造成的脖缝另说，见 [`../06-troubleshooting/neck-seam.md`](../06-troubleshooting/neck-seam.md) |
| **CotR / UBE** | 头部拓扑、UV、morph 都不同，**预设不通用**；眉毛等部件需要专门的适配补丁（如 Nexus 63777） |
| **加载顺序** | 社区（预设包作者）给出的经验顺序：**HPH 排在 EFM 之前** |

---

## 排错

| 症状 | 判据（看到 X 说明是 Y） | 处理 |
|---|---|---|
| 装了但脸没变化 | **没在 Head 页切 Face part** | 切 Face part（最高频原因） |
| 头**变黑 / 变暗** | 皮肤着色器没刷新 | **改一下 player weight**（官方给出的处理） |
| **眼睛 / 疤痕在 SE 下偏暗** | 同上 | 改 weight 通常可解（官方 Known Issues） |
| **眼睛闪烁 / 渲染异常** | 刚切到 HPH 之后出现 | **关闭 RaceMenu 再打开**（官方 Known Issues） |
| 切到**吸血鬼种族**后头被重置 | 官方已知行为 | 装 **vampire head fix**（FOMOD 03） |
| 某些**原版头发轻微穿模** | 官方已知问题 | 换发型或用 HPH 的高模香草发（FOMOD 10） |
| **眉毛错位 / 破皮** | 还在用原版 brows | 换成 HPH 配套的 high poly brows |
| NPC 换上 HPH 后**黑脸** | FaceGen 没重导 / 被别的文件覆盖 | `Ctrl+F4` 重导；检查覆盖，见 [`../06-troubleshooting/dark-face.md`](../06-troubleshooting/dark-face.md) |
| 想**把原版雕塑导进高模头**却失败/变形 | 两者**顶点数不同**，雕塑无法直接导入 | 社区做法（rentry 指南）：Outfit Studio 里导出 obj → 以原版头为参考、建 slider 到 0 → 导入 obj 作为 slider 数据 → conform → 拉回 100 → 导出 → 用 NifMerge 合并回原雕塑。**社区经验，步骤繁琐** |
| 滑块没出现 | morph 未构建 / 版本不符 | 见 [`../06-troubleshooting/racemenu-sliders-missing.md`](../06-troubleshooting/racemenu-sliders-missing.md) |

---

## 取舍与建议

- **该装**：你想消除原版脸的棱角、想在 Sculpt 里捏细节、或者你要用**绝大多数现代捏脸预设**
  （它们基本都是按 HPH 做的）—— 那 HPH 属于必装件。
- **别指望它换脸型**：它保留原版的比例与结构。想要"结构层面更好看"的脸，
  那是另一条路线（换头模 / 换种族 / SerketHeyt 式的重制），**HPH 不在那个赛道**。
- **装了就别装 ECE**，两者的头模改动会打架。
- **给 NPC 用要付出重导 FaceGen 的成本**，而且**带雕塑的头走不通**。改造一批 NPC 时
  优先用官方的 `KL Swap Headparts` + `KL Filter Race` 脚本，别手工一个个点。
- **装之前先确认渠道**：官方页要注册，整合包走 Google Drive 白名单。
  **任何第三方"HPH 下载站"都请对照 Vector Plexus 的版本号与文件大小再下手。**
- **检查补丁**：`High Poly Head UV Stretch Fix`（脖缝）、`Bone Weight Fix`、
  `Vanilla Presets Fix`、`Brows for HPH`、`LDD Better Eye Shape for HPH` 是常见的配套件
  （**这些补丁的 Nexus ID 与维护状态未确认**）。

---

## 来源

**一手**

- High Poly Head 官方页（Vector Plexus，file/283）：定位、功能、Requirements、Known Issues、
  使用方式、Modder Resource 三条 xEdit 脚本 —— 一手（本轮通过镜像站与整合包文档转述取得，
  原文需登录）
  `https://vectorplexus.com/files/file/283-high-poly-head/`
- 官方描述与安装项（00–10）、Usage、Known Issues、xEdit 脚本清单：
  AqxaroMods 与 Dwemer Mods 的 HPH 1.4 页面（**镜像转述官方描述**，多源一致）
- High Poly NPCs（Nexus 69604）页面：credits 明写 *KouLeifoh for High Poly Head*、
  要求 **HPH 1.4**、黑脸警告 —— 一手
- Alternate High Poly Head（Nexus 148541）credits：KouLeifoh 为原作者 —— 一手
- gio-gianny 整合包文档：Wabbajack 白名单与作者 Google Drive 备份的由来、FOMOD 选项分组 —— 一手（整合包作者整理）
- Freyr（Enderal）作者文章：对 HPH"仍是原版头基底、继承原版比例"的评价 —— 一手（该作者文章）

**社区经验**

- 1.0 版本与"作者是 SAM Light 的作者"（2019-12 社区搬运帖）—— **未确认**，仅社区标注
- "把 Face Part 拉到 3"的具体档位（中文社区帖）—— 官方未给编号，**未确认**
- HPH 不兼容 ECE、ECE/RaceMenu/EFM 用不同种族 morph（指南与搬运帖）
- 加载顺序 HPH 先于 EFM（预设包说明）
- 原版雕塑转高模头的 Outfit Studio + NifMerge 流程（rentry 指南帖）
- 常见配套补丁（UV Stretch Fix / Bone Weight Fix / Vanilla Presets Fix 等）的整理（多帖）

**未确认**

- **HPH 头部网格的确切顶点数 / 面数**
- **1.0 与 1.4 之间各版本的发布日期**
- **1.4 之后是否还有更新**
- **Vector Plexus 域名是否变更**（`vectorplexus.com` 与 `vectorplexis.com` 两种写法）
- **"Vector Plexus 原域名失效"**这一社区传言
- 各类第三方补丁的 Nexus ID 与维护状态
