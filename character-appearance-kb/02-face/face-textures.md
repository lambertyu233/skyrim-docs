---
id: face-textures
title: 脸部皮肤与纹理
category: 02-face
kind: reference
version: 2.0.0
updated: 2026-10-25
tags: [捏脸, 皮肤, 纹理, 贴图, UV]
aliases: [脸皮, skin texture, fair skin, 皮肤贴图, 脖子接缝原因, 脸部贴图, 皮肤 mod, 皮肤推荐, 怎么选皮肤, 皮肤 UV, 脖缝, 脸身不同色, 面部皮肤, 皮肤不通用, cbbe 皮肤, unp 皮肤]
source: https://www.nexusmods.com/skyrimspecialedition/mods/798
summary: 脸部/身体皮肤贴图的选择原则——皮肤 UV 必须与身形同族这条硬约束、头身必须同源同档、常见皮肤 mod 盘点，以及它与脖缝、黑脸这两大症状的交叉关系。
---

# 脸部皮肤与纹理

> **一句话**：脸部皮肤看起来是"换张贴图"，实际是**换掉一整套 UV 体系里的一环**。
> 选错家族不是"不好看"，而是直接产出**脖缝、手脚接缝、色差**。

---

## 速览

| 项目 | 值 |
|---|---|
| 适用层 | 头部（脸/头颈）、身体、手、脚的 diffuse / normal / specular 贴图 |
| UV 家族 | **CBBE 族** vs **UNP 族（UNP / UNPB / UUNP / BHUNP 共用原版延伸 UV）**，互不通用 |
| 常见分辨率 | 2K / 4K / 8K（8K 脸 + 4K 身是常见搭配） |
| 是否需补丁 | 换 **HPH / CotR / UBE** 头模时看情况：HPH 沿用原版头 UV，**一般不需要**专门的脸部皮肤 |
| 硬前置 | 无；但**必须先定身形**，再在这个家族里选皮肤 |
| 影响范围 | 玩家与 NPC 都受影响（贴图是被动资源，谁用这套网格谁就变） |
| 常见症状 | 脖缝、手脚接缝、脸黑、油光 |

要点：

- **皮肤必须与身形同族**：CBBE 皮肤配 CBBE 身形，UNP 系皮肤配 UNP 系身形。
- **头、身、手、脚要用同一套的同一档**——混档是脖缝的**第二大成因**。
- **换头模不等于换皮肤**：HPH 官方称兼容基于原版头部的纹理，不需要专门为它找脸皮。
- ⚠️ **脖缝修补 mod 是创可贴**，根因永远是"头颈贴图不同源"。

---

## 前世今生

### 时间线（可核实部分）

| 时间 | 事件 | 意义 |
|---|---|---|
| 原版 | Bethesda 自带低分辨率皮肤贴图，头/身共用一套原版 UV | 一切皮肤 mod 的基线 |
| 未确认 | 社区开始做皮肤替换，出现 **ECE 系纹理**这一类早期流派 | 后来的 Fair Skin 等被归类为"基于 ECE 的纹理" |
| 未确认 | **CBBE** 另起一套 UV；UNP 系沿用原版延伸 UV | **皮肤家族从此分裂**，这是后续所有接缝问题的源头 |
| 未确认 | 4K 成为主流，8K 脸 + 4K 身成了常见配置 | 分辨率不是越高越好，见"取舍与建议" |
| 当前 | 主流皮肤普遍**同时提供 CBBE 与 UNP 两个版本**，FOMOD 里选 | 家族约束从"找不到"变成了"**别选错**" |

> ⚠️ 上表中标「未确认」的年份**本轮未能取得可靠出处**，宁可留白也不补。

### 为什么家族会分裂

身形 mod 改的是**网格**，而贴图是靠 **UV 展开**贴到网格上的。CBBE 重新展了一套 UV，
UNP 系则在原版 UV 上延伸。于是出现了一个硬事实：

> **同一张 PNG/dds，贴到 CBBE 网格和贴到 UNP 网格上，落到身体不同位置。**

所以"为 CBBE 做的身体皮肤"用在 UNP 上不是"稍微错位"，而是**整张图对不上**。
这条约束在 [`../03-body/cbbe.md`](../03-body/cbbe.md) 与
[`../03-body/unp-bhunp.md`](../03-body/unp-bhunp.md) 里从身形侧有对称的记述。

### 一条容易被搞混的细节：脸的 UV 其实没分裂

值得单独说清，因为它是很多"我明明同族了还是有缝"的困惑来源：

- **头/脸用的是原版头部 UV**。这也正是 HPH 官方敢写"兼容基于原版头部的纹理"的原因
  （HPH 是在原版头网格上加密，UV 没换）。
- 真正分裂的是**身体、手、脚**。
- 因此**脖缝发生在两套 UV 的交界处**：脖子那一圈的颜色/法线，一半来自头部贴图，
  一半来自身体贴图。

> **辨析结论（本工作区推断）**：由「HPH 兼容原版头纹理」与「皮肤包普遍把头/身分开打包」
> 两点交叉得出——**脸部贴图本身大多跨身形通用**，被家族约束的是**身体那一半**。
> 实务上仍然建议**整包同族同档**，因为你几乎总是同时换头身手脚本。

---

## 它解决什么问题

### 没有它之前

- 原版皮肤分辨率低、细节糊，毛孔与皮下血色全无；
- 男女共用同一套观感，女性角色普遍显老显脏；
- 兽族（亚龙人 / 虎人）的鳞片与毛发贴图更粗糙。

### 它怎么解决的

| 层次 | 皮肤 mod 提供什么 |
|---|---|
| diffuse（`_d` / `_1`） | 肤色、斑点、血管、妆面底色 |
| normal（`_n` / `_msn`） | 肌肉线条、皮肤起伏。**肌肉感的来源，不是 diffuse** |
| specular / subsurface（`_s` / `_sk`） | 油光、湿润感。**油光类 bug 的高发区** |
| 可选覆盖层 | 雀斑、体毛、血管、war paint 等叠加层 |

> **换皮肤 = 同时换掉这四层。** 只换 diffuse 不换 normal，会得到"很平的脸"；
> 反过来 specular 没跟上，就会出现脸泛油光。

---

## 它包含什么

一个典型的女性皮肤 mod 的 FOMOD 大致这样分：

```
身形家族：  CBBE  /  UNP(含 UNPB / UUNP / BHUNP)
部位分档：  头 / 身体 / 手 / 脚
风格选项：  光滑 / 真实 / 肌肉 / 汗湿 / 体毛
分辨率：    2K / 4K / 8K
可选：      私密处样式、妆面、覆盖层
```

**规则只有一条：全部选同一档。**

| 错法 | 后果 |
|---|---|
| 头用 A 皮肤、身体用 B 皮肤 | **脖缝**（最常见） |
| 头用 High、身体用 Low | 色深不一致 → 脖缝 / 脸身不同色 |
| CBBE 皮肤 + UNP 身形 | 手、脚、身体接缝，纹理错位 |
| 只换 diffuse 不换 normal | 脸变平、肌肉感消失 |

---

## 安装

1. **先定身形家族**（CBBE 系还是 UNP 系），这是第 0 步，决定了后面所有选项。
   家族判断见 [`../03-body/cbbe.md`](../03-body/cbbe.md) / [`../03-body/unp-bhunp.md`](../03-body/unp-bhunp.md)。
2. **在该家族里挑一个皮肤 mod**，FOMOD 里选对应的身形分支。
   验证点：安装器里出现的是 `CBBE` 还是 `UNP`，不要凭 mod 名猜。
3. **头 / 身 / 手 / 脚全部选同一档**（分辨率一致、风格一致）。
4. **装完后检查覆盖顺序**：皮肤贴图是纯资源，靠 MO2 左右栏覆盖决定谁生效
   （覆盖规则见 `mo2-usvfs-kb`）。
   本库内的顺序建议见 [`../07-workflow/install-order.md`](../07-workflow/install-order.md)。
5. **进游戏验证**：新建角色，看**脖子一圈**、**手腕**、**脚踝**有没有色差或硬边。
   有 → 回第 3 步查是否混档，不要急着装脖缝补丁。

---

## 使用与配置

### 与 tint / 妆面的关系

皮肤是"底"，tint mask 是"上层着色"。两者叠加，所以：

- **换了皮肤后，妆面（makeup / warpaint）观感会变**——底色变了；
- 在 Creation Kit 里改过肤色的 NPC，需要在 **Face Tinting Color** 上同步调整，否则脸身脱色；
- RaceMenu 预设里的 `skinOverrides` 也和皮肤相关，**缺失会出现油光类 bug**。

### 与头模的关系

| 头模 | 皮肤要求 |
|---|---|
| **原版头** | 任意原版 UV 皮肤 |
| **High Poly Head** | **兼容基于原版头部的纹理**，不需要专门为 HPH 找皮肤（官方说明）。见 [`high-poly-head.md`](high-poly-head.md) |
| **CotR / UBE** | 头部拓扑与 UV 都不同，**预设与皮肤不通用**，需要专门版本 |
| **Citrus Heads** | 同上，需对应版本 |

### 与身体皮肤的关系

脸部条目和 [`../03-body/body-textures.md`](../03-body/body-textures.md) 是同一件事的两半：
**皮肤包几乎总是头身一起发**，所以两边要一起看，别只改一半。

---

## 兼容与冲突

| 交叉点 | 说明 |
|---|---|
| **与身形** | **必须同族**，这是硬约束 |
| **与脖缝** | 头身不同源 = 脖缝第一成因；混档 = 第二成因。见 [`../06-troubleshooting/neck-seam.md`](../06-troubleshooting/neck-seam.md) |
| **与黑脸** | 黑脸是 **FaceGen 贴图与网格不匹配**（通常是覆盖/加载顺序问题），**换皮肤不能解决黑脸**。见 [`../06-troubleshooting/dark-face.md`](../06-troubleshooting/dark-face.md) |
| **与 HPH** | 兼容原版 UV 纹理，无需专门皮肤 |
| **与 tint mask** | 皮肤是底、tint 是上层；改肤色要在 CK 同步 Face Tinting Color |
| **与 RaceMenu 预设** | 预设的 `skinOverrides` 与皮肤相关，缺失导致油光 |
| **与兽族** | 人类系皮肤**不覆盖**亚龙人/虎人，需要专门的兽族皮肤包 |

> **别把黑脸当皮肤问题。** 黑脸的脸是"贴图没对上网格"，皮肤是"贴图内容"——
> 两者的排查路径完全不同，混着查会浪费大量时间。

---

## 排错

| 症状 | 判据（看到 X 说明是 Y） | 处理 |
|---|---|---|
| **脖子一圈有明显色差/硬边** | 头身来自不同皮肤或不同档 | 头身同源同档；**别先装脖缝补丁** |
| **手腕 / 脚踝接缝** | 手、脚贴图与身体不同源 | 同一个包的同一档一起装 |
| **纹理整体错位、花纹跑位** | **身形与皮肤不同族**（CBBE 皮肤 + UNP 身形） | 换同族皮肤 |
| **整张脸发黑** | 与皮肤无关，是 FaceGen 未匹配 | 走 [`../06-troubleshooting/dark-face.md`](../06-troubleshooting/dark-face.md) |
| **脸泛油光 / 像打了蜡** | specular 层没跟上，或预设 `skinOverrides` 缺失 | 补齐 `_s` / `_sk`；检查预设 |
| **脸很平、没有肌肉感** | 只换了 diffuse，没换 normal | 一并装 `_n` / `_msn` |
| **换妆后细线妆断裂** | 头部 UV 被头模/morph mod 改过（如 EFM 修过头部 UV） | 换妆容贴图，见 [`expressive-morphs.md`](expressive-morphs.md) |
| **装了很多皮肤但只生效一个** | MO2 覆盖顺序 | 检查左右栏覆盖 |
| **NPC 和玩家皮肤不一致** | NPC 用了自己的 FaceGen 贴图 | 正常；NPC 贴图是预生成的 |

---

## 取舍与建议

1. **先定身形，再选皮肤** —— 顺序反了必然返工。
2. **CBBE 皮肤配 CBBE 身形，UNP 皮肤配 UNP 身形**，不要跨界。
3. **头 / 身 / 手 / 脚保持同档**（同一风格、同一分辨率档位）。
4. **8K 只用在脸上就够了**。身体 4K 通常足够，全 8K 换来的观感提升远小于显存代价。
5. **出现脖缝先怀疑同源问题**，而不是去找"脖缝修补 mod"——那是创可贴。
6. **兽族要单独找皮肤包**，人类系皮肤不覆盖亚龙人 / 虎人。
7. **记录你用的是哪一套**。预设分享时，"用了哪个皮肤"是必需信息——
   别人装了同一张预设但皮肤不同，脸就是两个样。

### 常见皮肤 mod 盘点

| mod | Nexus（SE） | 作者 | 备注 |
|---|---|---|---|
| **Fair Skin Complexion** | **798** | **HHaleyy** | 同时提供 **CBBE 与 UNP** 选项；EFM 的嘴部纹理就取自它。CBBE 装完后最常被推荐的脸皮之一 |
| **The Pure** | 未确认 | **Anini / Regenbot03 / Shiva182** | CBBE 与 UNP 双版本，4K / 8K（整合包记录 v1.3.1） |
| **Demoniac** | 未确认（SE 版由 **Rektas** 移植） | 原作 **regenbot03**（LE 70834） | 8K/4K/2K，光泽感强，偏暗 ENB 下表现好 |
| **Mature Skin** | 未确认 | **Maevan2** | 写实向，覆盖 UNP / UNPB / 7Base / CBBE / Vanilla |
| **Leyenda Skin** | 未确认 | **HeroedeLeyenda** | 白皙向，U 身 C 身皆有 |
| **Reverie Skin** | 未确认 | **Novelyst** | 较新的女性皮肤，常见于新预设的 credits |
| **Bijin Skin（UNP and CBBE）** | 未确认 | **rxkx22** | **EFM 作者本人推荐**的脸皮 |
| **Tempered Skins for Males** | 未确认 | **traa108** | 男性皮肤的代表作，有 Vanilla 与 SOS 两版 |
| **SkySight Skins** | 未确认 | **fadingsignal** | 男性 4K / 2K，写实肌肉向 |
| **Fine Face Textures for Men** | LE 27815 | **urshi** | **EFM 作者本人推荐**的男性脸皮 |
| **Feminine Argonian / Khajiit Textures** | 未确认 | **MONSTERaider** | 兽族女性皮肤 |
| **Male Dragonic Argonian Textures** | 未确认 | **ChaserTech** | 兽族男性皮肤（SOS / Vanilla 两版） |
| **BnP（Female / Male Skin）** | 未确认 | 未确认 | 常见于 HIMBO 一类男性身形的推荐搭配 |

> ⚠️ **上表"未确认"的 Nexus ID 本轮未能逐一核实到位**，请以 Nexus 站内搜索为准；
> **作者名凡未确认的一律写"未确认"**，不要凭印象补全。
> 另外"最主流的皮肤清单"会随时期变化，**不宜写死**——上表只是取样，不是排行榜。

---

## 来源

**一手**

- Fair Skin Complexion（SE 798）发布页：CBBE 与 UNP 双版本 —— 一手
  `https://www.nexusmods.com/skyrimspecialedition/mods/798`
- EFM 发布页 credits：**EFM 的嘴部纹理来自 Fair Skin Complexion（HHaleyy）** —— 一手
- EFM 发布页 Recommended：**Bijin skin（rxkx22）**、**Fine Face Textures for Men（urshi）** —— 一手
- High Poly Head 官方说明：**兼容基于原版头部的纹理** —— 一手（镜像转述官方描述）
- Demoniac 原作者 **regenbot03**、LE 页 70834；SE 由 **Rektas** 移植 —— 一手（LE 发布页）+ 社区经验（移植者）

**社区经验**

- "CBBE 与 UNP 的 UV 不通用"：Nexus 发布页描述 + 社区一致确认 —— 一手 + 社区经验（一致）
- 头/身/手/脚需同一套同一档：脖子接缝排查帖（Nexus 论坛 / LoversLab）—— 社区经验
- Tempered Skins（traa108）、SkySight Skins（fadingsignal）、Mature Skin（Maevan2）、
  Leyenda Skin（HeroedeLeyenda）：整合包与社区皮肤讨论帖 —— 社区经验
- The Pure（Anini / Regenbot03 / Shiva182，CBBE 与 UNP 4K/8K，v1.3.1）：Nolvus 整合包条目 —— 社区文档
- 兽族皮肤（MONSTERaider / ChaserTech）、Reverie Skin（Novelyst）：整合包 credits 与社区帖 —— 社区经验

**本工作区辨析**

- **"脸用原版 UV、分裂的是身体那一半"**：由 HPH 官方"兼容基于原版头纹理"与皮肤包普遍头身分开打包
  两点交叉推出 —— **推断结论，未取得直接的一手表述**

**未确认**

- **The Pure / Demoniac SE / Mature Skin / Leyenda Skin / Reverie / Bijin Skin / Tempered Skins / SkySight Skins 的 SE 版 Nexus ID**
- **BnP 皮肤的作者与 SE 版 ID**
- 各皮肤 mod 的首发年份与当前版本
- "ECE 系纹理"这一分类的确切由来与首款代表 mod
