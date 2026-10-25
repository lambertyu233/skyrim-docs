---
id: preset-not-applied
title: 预设不生效 / 脸变回默认
category: 06-troubleshooting
kind: tutorial
version: 2.0.0
updated: 2026-10-25
tags: [排错, 预设, jslot, 存档, 依赖]
aliases: [预设不生效, 脸变回默认, 脸变默认, 预设没用, preset 不加载, 导入预设无效, 导入预设脸不对, 预设一半生效, 存档脸变了, 读旧档变默认, jslot 路径, co-save 不一致, 预设走了样]
source: https://www.nexusmods.com/skyrimspecialedition/mods/19080
summary: 预设不生效的十一条检查清单（依赖资源、.jslot 路径、旧 .slot、HPH 未切、未保存应用、morph 未构建、co-save 不一致、雕塑未导入、种族、EFM/HPH 改脸、keys[].key 绑定）、"缺什么文件对应什么症状"核对表，以及 .jslot 与旧 .slot、EFM/HPH 改脸两组常被搞混的点。
---

# 预设不生效 / 脸变回默认

> **一句话**：预设只管"数值"，不管"资源"——**缺一样就走样**是这个生态的默认状态，
> 不是 bug。排查的第一永远是"作者用的东西我装齐了吗"。

## 速览

| 项 | 内容 |
|---|---|
| 症状 | 导入 `.jslot` 后没反应 / 脸变回默认 / 只有一部分生效 / 读旧档脸变了 |
| 高频成因 | 依赖资源缺失（发/眼/眉/皮/HPH）；`.jslot` 放错目录；存档 co-save 不一致 |
| 首选判据 | 新角色正常、**读旧档变默认** ⇒ co-save 与当前配置对不上 |
| 最短修复路径 | 照作者依赖清单装齐 + `.jslot` 放对目录 + 用新档验证 |

要点：

- **预设只存"滑块值与 head parts 引用"**：它引用的头发 / 眼睛 / 眉毛 / 皮肤 /
  HPH 必须已经安装并启用——**预设作者的要求清单就是必装清单**。
- **`.jslot` 绑定身形家族**：`keys[].key` 写死提供 morph 的 esp 名，
  没有这个 esp 就**静默失效**（不报错，只是那一维不动）。
- **morph 与 tint 状态存在 SKSE co-save 里**：中途增删 mod 后旧档可能对不上。
- **"预设不生效"和"效果和截图不一样"是两回事**：前者查清单，后者查资源版本。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| ECE 时代 | 手动复制 `CME_save` 文件夹，游戏内用 Body 分类的 **"Slot Load" 滑块**翻页加载 | 预设的雏形；**与 RaceMenu 完全不通** |
| RaceMenu 早期 | **Save/Load presets to and from Windows clipboard**（剪贴板） | 只能用一次，没法当文件分享 |
| CharGen v2.0.0 | 官方功能改为 *"Save/Load preset to and from a slot file"*（replaces clipboard save/load） | 预设第一次成为**可分发的文件** |
| SE 0.4.x | 格式改为 **JSON**，扩展名 **`.jslot`**；旧二进制 `.slot` **保留读取但不再写出** | 现行格式；也是"旧 `.slot` 加载了但下拉里可能不列"的由来 |
| 0.4.13 | 加入 `skee preset-save` / `preset-load` 控制台命令 | 预设可脱离界面，还能**套到 NPC 上** |
| 0.4.19.15 | *"Exposed programmer interface for Presets"* | 其他插件能直接读写预设 |
| 2026-04-20/21 | **0.4.20.0** 部件标签 | 与预设无关，但让"几百个发型里找到作者用的那个"变容易 |

> 0.4.13 / 0.4.19.15 / 0.4.20.0 的**内容**来自官方 changelog，但除
> 0.4.19.15（2023-12-10）与 0.4.20.0 外，**日期未确认**。

### 它从哪来

预设机制要解决的是"捏好的脸无法复现、无法分享"。文件格式换过三代
（`CME_save` → 剪贴板 → slot 文件 → JSON），**很多老教程失效就失效在这里**——
照着 ECE 时代的步骤在现代 RaceMenu 上操作，什么都对不上。

### 中间经历了什么

从二进制 `.slot` 到 JSON `.jslot` 是关键一跃：不可读的二进制让
"把 A 身形的预设改成 B 身形"只能靠工具猜；JSON 之后预设可以被人肉检查，
`keys[].key` 这类字段才成了排查"为什么一半生效"的判据。

### 现状

Nexus 搜 "Racemenu preset" 有 **2000+** 结果（社区统计，2025）。
生态越大，"缺依赖"越是最常见故障——这是结构性的，不是某个预设的错。

## 检查清单

### 1. 预设依赖的资源是否装齐 ⭐ 第一位

预设只存"滑块值与 head parts 引用"，它引用的**头发 / 眼睛 / 眉毛 / 皮肤 /
HPH** 必须已经安装并启用。

- 缺头发 → 发型回退默认或变光头；
- 缺眼睛/眉毛 → 对应部件丢失或变紫红；
- 缺皮肤 → 脸色不对。

**预设作者的要求清单就是必装清单。**

### 2. `.jslot` 是否放对目录

```
Data\SKSE\Plugins\CharGen\Presets\
```

放错目录 → 预设下拉里根本看不到它。带雕塑的配套 `.nif`（+ 有时 `.dds`）
要放 `Data\SKSE\Plugins\CharGen\`。`.jslot` 的完整格式与分享生态见
[racemenu-presets.md](../02-face/racemenu-presets.md)。

### 3. 是不是旧 `.slot` 格式

二进制 `.slot` **仍能加载，但 CharGen 不再写出这种格式**，
下拉列表里可能不列。别把"下拉里没有"当文件损坏——先看扩展名。

### 4. High Poly Head 是否被选中

HPH 预设的常见现象是"**脸是尖的 / 不像截图**"——
解决：到 Head 页把 **Face part 从 1 切到 3（HPH）**。
社区经验写"拉到 3"，官方未给编号。HPH 的使用前提与坑见
[high-poly-head.md](../02-face/high-poly-head.md)。

### 5. 是否真的保存并应用了

在 RaceMenu 里调完滑块后**没有 Save / 应用** → 当然不生效。
导入时先**把种族切到预设支持的那个种族**（常被跳过）；
加载后**等肤色完全加载完**再做下一步（社区经验）。

### 6. 身形 morph 是否已构建

预设里的身形部分依赖 `.tri`。
BodySlide 没勾 `Build Morphs` → 身形部分无效（但脸的部分可能正常）。
机制见 [morph-and-nif-basics.md](../00-overview/morph-and-nif-basics.md)，
构建操作见 [bodyslide-outfit-studio.md](../03-body/bodyslide-outfit-studio.md)。

### 7. 存档与当前 mod 是否一致 ⭐

**morph 与 tint 状态存在 SKSE co-save 里。**
中途增删身形 / 皮肤 / 预设类 mod，旧档可能与新配置对不上。

表现：新角色用预设正常，**读旧档就变回默认**。
排查时用新档对照是最省事的二分法。

### 8. 带雕塑的预设是否导入了几何

若预设附带 `.nif`（雕塑几何），需要去 **Sculpt → Import Head** 手动导入
（**Import Part Matcher 保持默认**）。只加载 `.jslot` 会得到"大体对但不像"的脸。
导入顺序：**先 `.jslot`，后同名 `.nif`**（社区反复出现的 TL;DR）。

### 9. 种族切对了吗

社区经验规则：**人类之间（帝国/诺德/布雷顿/红卫）可互用；
精灵之间（高/木/暗）可互用；兽人、虎人、亚龙人最好只在同族内用。**

### 10. 是否被 EFM / HPH 改了脸

- **EFM 主文件不兼容现有预设**（会改脸）——想保留现有脸用可选的
  *EFM - Racemenu Plugin*（只有滑块）；
- **EFM morph 不适用于 High Poly Head**（作者明确暂无支持计划）；
- 两者都会让"预设明明导入了，脸却不是那张脸"。

见 [expressive-morphs.md](../02-face/expressive-morphs.md)。

### 11. `keys[].key` 指向的 esp 在不在

`.jslot` 里每条 morph 都写死提供它的 esp：

```json
{ "keys": [ { "key": "RaceMenuMorphsCBBE.esp", "value": 0.50000 } ], "name": "Breasts" }
```

你的环境里没有这个 esp（比如你装的是 UNP 系身形），这条 morph 就
**静默失效**——于是"预设套上去一半生效"是最典型的症状。

## 一张核对表（缺什么 → 对应症状）

| 缺什么 | 症状 |
|---|---|
| 依赖的头发资源 | 发型回退默认或变光头 |
| 眼睛 / 眉毛 head parts | 部件丢失或变紫红 |
| 皮肤资源 | 脸色不对 |
| HPH（Face part 未切） | 脸是尖的 / 不像截图 |
| 同名雕塑 `.nif`（未 Import Head） | 大体对但不像 |
| `.tri`（没勾 `Build Morphs`） | 身形部分无效，脸的部分可能正常 |
| 提供 morph 的 esp（`keys[].key`） | 那一维静默失效，预设一半生效 |
| co-save 与当前配置一致 | 新角色正常，读旧档变回默认 |

## 一个常被搞混的点

> **".jslot" 与旧 ".slot" 是两代格式，不是坏档。**
> 二进制 `.slot` 仍能被读取，但 CharGen 不再写出这种格式；
> 如果你下载到的预设下拉里看不到，先确认扩展名与路径。

同时记住另外三组高频混淆：

1. **EFM / HPH 会改脸**：它们改变 morph 基础或头网格，
   "预设失效"很可能是它们生效了，而不是预设坏了；
2. **"预设不生效" ≠ "效果和截图不一样"**：后者通常是**资源版本不同**
   （作者的眉毛是 v2.1、你装的是 v4.0）或**资源缺失导致部分回退**，
   仔细比对作者的要求清单；
3. **BodySlide 预设（`.xml`）与 RaceMenu 预设（`.jslot`）不能互导**：
   格式、刻度、生效方式都不同（见
   [morph-runtime-vs-bake.md](../03-body/morph-runtime-vs-bake.md)）。

## 判断分叉点（别误诊）

| 看起来像 | 其实 |
|---|---|
| "预设文件坏了" | 九成是路径 / 格式 / 依赖问题，文件本身没坏 |
| "加载后完全没反应" | SKSE / RaceMenu 版本不符——转 [racemenu-sliders-missing.md](../06-troubleshooting/racemenu-sliders-missing.md)；RaceMenu 本身的安装与版本问题见 [racemenu.md](../02-face/racemenu.md) |
| "一半生效" | `keys[].key` 指向的 esp 缺失，或部分资源没装 |
| "读旧档脸变了" | co-save 不一致；用新档对照验证 |
| "身形没跟着变" | 该身形的 `.tri` 未构建 |
| "脸变黑" | 与预设无关，是 FaceGen——转 [dark-face.md](../06-troubleshooting/dark-face.md) |

## 取舍与建议

- **下载预设前先看依赖清单的长度**：依赖越多的预设越漂亮，也越脆弱。
- **导入顺序有讲究**：先 `.jslot`，后同名 `.nif`；等肤色加载完再下一步。
- **分享礼仪**（社区惯例）：列全依赖 mod 与版本；注明支持的种族与身形；
  注明是否用了 HPH / EFM / CotR / UBE；**不要二次分发别人的预设文件**。
- **排查用新档**：co-save 本身就是混淆源，旧档对比只会更乱。

## 来源

- **依赖资源缺失、放错目录、HPH 未选、需重开 `showracemenu`、等肤色加载完、
  种族匹配经验规则、导入顺序 "jslot first, then nif"**：
  LoversLab 与 Nexus 论坛预设帖 —— **社区经验（多帖一致）**
- **`.jslot` 路径与 `skee preset-save/load`、CharGen v2.0.0 slot file
  （replaces clipboard save/load）、旧 `.slot` 只读不写、0.4.19.15 编程接口**：
  RaceMenu 发布页与 changelog —— **一手**
  `https://www.nexusmods.com/skyrimspecialedition/mods/19080`
- **需要 Import Head（Import Part Matcher 默认）**：
  RaceMenu 发布页（Sculpt 的 Import Geometry 功能）+ 多份预设说明 —— **一手 + 社区经验**
- **`keys[].key` 指向提供 morph 的 esp、`.jslot` 结构示例**：
  Nexus 论坛 scorrp10 的详细解答（附实际文件片段）—— **社区经验（引用了实际文件内容）**
- **co-save 存储 morph 状态**：BodyGen 文档与 NiOverride 机制 ——
  **社区文档（引作者原话）+ 一手机制**
- **EFM 主文件不兼容现有预设、EFM - Racemenu Plugin、EFM 不适用 HPH**：
  EFM 发布页描述 —— **一手**（本库整理见 [expressive-morphs.md](../02-face/expressive-morphs.md)）
- **"预设效果不同"与"预设不生效"要分开**：**机制推论**
- **Nexus 预设数量 2000+（2025）**：社区统计 —— **社区经验**
- **"Face part 拉到 3"的具体档位**：官方未给编号 —— **未确认**
