---
id: racemenu-presets
title: 预设（`.jslot`）与分享生态
category: 02-face
kind: reference
version: 2.0.0
updated: 2026-10-25
tags: [捏脸, 预设, jslot, 存档, 分享]
aliases: [preset, 捏脸预设, 导入预设, slot 文件, 脸型文件, 预设怎么用, 预设导入失败, 分享预设, 随从脸, nif 头模, CME_save, preset-save, 预设路径, 导入头模]
source: https://www.nexusmods.com/skyrimspecialedition/mods/19080
summary: .jslot 的来历（ECE 的 CME_save → 剪贴板 → .slot → JSON）、文件结构与存放路径、导出/导入/套用 NPC 的完整操作，以及"预设导进去了脸却不对"的成因表与分享生态的惯例。
---

# 预设（`.jslot`）与分享生态

> 预设是捏脸生态的**流通货币**：它把"一组滑块数值 + 部件选择 + 肤色"打包成一个文件，
> 让别人能在自己的环境里复现同一张脸。
> **前提是你的环境和作者一致** —— 这句话是本篇全部排错内容的总纲。

---

## 速览

| 项目 | 值 |
|---|---|
| 当前格式 | **JSON 文本**，扩展名 **`.jslot`**（RaceMenu 发布页明确：预设改为 JSON 格式） |
| 旧格式 | 二进制 **`.slot`**：**仍能加载，但 CharGen 不再写出这种格式** |
| 存放目录 | `Data\SKSE\Plugins\CharGen\Presets\` |
| 控制台导出目录 | `Data\SKSE\Plugins\CharGen\Exported\<PATH>.jslot` |
| 带雕塑的配套文件 | 同名 `.nif`（有时带 `.dds`），放 `Data\SKSE\Plugins\CharGen\`，导入时走 **Sculpt → Import Head** |
| 谁能写出 | RaceMenu 的 CharGen（需 **CharGen v2.0.0+**），或控制台 `skee preset-save` |
| 能不能跨身形 | **不能直接用**。`.jslot` 里的 morph 指向**提供该 morph 的 esp**，因此预设**绑定身形家族** |
| 能不能跨捏脸框架 | **不能**。ECE 的 `CME_save` 与 RaceMenu 的 `.jslot` 是两套体系 |
| 生态规模 | Nexus 搜 "Racemenu preset" 有 **2000+** 结果（社区统计，2025） |

要点：

- **预设只管"数值"，不管"资源"** —— 缺了作者用的高模头/皮肤/眼/眉/发，导入结果必然走样。
- **`keys[].key` 指向提供 morph 的那个 esp**，这是判断"这份预设能否在我这儿完整生效"的关键字段。
- **带雕塑的预设必须额外导入 `.nif`**，只加载 `.jslot` 会得到"大体对但不像"的脸。
- **预设可以套到 NPC 上**（`skee preset-load`，官方 changelog 原话 "yes, it can be applied onto NPCs"）。

---

## 前世今生

### 从 CME_save 到 .jslot

预设这个概念不是 RaceMenu 首创，但**文件格式换过三代**，这也是很多老教程失效的原因：

| 阶段 | 存取方式 | 说明 |
|---|---|---|
| **ECE 时代** | 手动复制 `CME_save` 文件夹到 `Documents\My Games\Skyrim Special Edition\CME_save`，游戏内用 **Body 分类下的 "Slot Load" 滑块**翻页加载 | ECE 的路子；**与 RaceMenu 完全不通** |
| **RaceMenu 早期** | **Save/Load presets to and from Windows clipboard**（存到系统剪贴板） | 只能用一次，没法当文件分享 |
| **CharGen v2.0.0** | 官方功能列表改为 *"Save/Load preset to and from a slot file"*，并注明 **"replaces clipboard save/load"** | 预设第一次成为**可分发的文件** |
| **SE 0.4.x** | 预设格式**改为 JSON**，扩展名 **`.jslot`**；旧二进制 `.slot` 保留读取兼容，但不再写出 | 现行格式 |
| **0.4.13** | 加入 `skee preset-save` / `skee preset-load` 控制台命令 | 预设可以**脱离界面**、也可以**套到 NPC** |
| **0.4.19.15** | *"Exposed programmer interface for Presets"* | 其他插件能直接读写预设 |
| **0.4.20.0** | 部件标签（Part Tags） | 与预设本身无关，但让"几百个发型里找到作者用的那个"变容易了 |

> 0.4.13 / 0.4.19.15 / 0.4.20.0 的**内容**来自官方 changelog，但 changelog **未给出上传日期**，
> 除 0.4.19.15（2023-12-10）与 0.4.20.0（2026-04-20）外，其余**日期未确认**。

### 为什么现在是 JSON

二进制 `.slot` 不可读不可改，社区想"把 A 身形的预设改成 B 身形"只能靠工具猜。
改成 JSON 之后，**同一份预设可以被人肉检查和换算** —— 这也是
[`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md) 里
"BodySlide 预设与 RaceMenu 预设不能互导、只能逐滑块换算"这条结论能落地的前提。

---

## 它解决什么问题

没有预设机制时，捏脸有三个硬伤：

| 硬伤 | 后果 |
|---|---|
| 原版滑块**不显示数值** | 捏好的脸**无法复现**（重装、换机就丢） |
| 没有"导出"通道 | 玩家捏的脸**变不成 NPC/随从的脸** |
| 没有可交换的载体 | 好看的脸**无法分享**，社区只能贴截图 |

预设把"一组外观参数"变成了**可存储、可传输、可版本化**的东西，于是才有了
Nexus 上 2000+ 的预设生态、才有了"随从 mod 自带预设"这种交付形式，
也让 [`../06-troubleshooting/preset-not-applied.md`](../06-troubleshooting/preset-not-applied.md)
这类排错成为一门必须掌握的常识。

---

## 工作原理

### 文件长什么样

`.jslot` 是普通 JSON 文本，可以直接用文本编辑器打开。每条滑块大致是
"滑杆名 + 提供该 morph 的插件 + 数值"：

```json
{
  "name": "ShoulderWidth",
  "keys": [ { "key": "RaceMenuMorphsCBBE.esp", "value": 50 } ]
}
```

本库在 [`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md) 里
实测到的 `bodyMorphs` 条目是另一番样子（浮点量级）：

```json
{ "keys": [ { "key": "RaceMenuMorphsCBBE.esp", "value": 0.50000 } ], "name": "Breasts" }
```

> **两个样例的 `value` 量级不同**（50 vs 0.5），说明**不同来源/不同 morph 的刻度不一定一致**。
> 常见说法"RaceMenu 滑块是 -1 到 +1"**并不准确**；滑块上限由
> `RaceMenuMorphs*.psc` 里 `OnSliderRequest` 的 `Float factor` 决定（社区记录默认 `2.0`）。
> **以你实际界面为准。**

### 文件里还有哪些块

| 块 | 内容 |
|---|---|
| `weight` | 体重 |
| 头部件相关 | 头发 / 眼 / 眉 / 胡须 / 疤痕等 **head part** 的选择 |
| `skinOverrides` | 皮肤覆盖设置。**缺失或条目错误会导致"皮肤油光"类 bug**（社区经验） |
| `bodyMorphs` | 身形 morph 数值（上面那两个样例） |
| 雕塑几何 | **不在 `.jslot` 里**，是配套的 `.nif`（+ 有时 `.dds`） |

> **`.jslot` 的完整字段清单未确认** —— 上面列出的是本库在多份实际文件与社区讨论中
> 反复见到的块，RaceMenu 没有公布 schema。

### 为什么预设"绑定身形家族"

因为 `keys[].key` 写死了**提供 morph 的那个 esp 名**：

```
"key": "RaceMenuMorphsCBBE.esp"
```

你的环境里没有这个 esp（比如你装的是 UNP 系身形），这条 morph 就**静默失效** ——
不会报错，只是那一维不生效。于是"预设套上去一半生效"是最典型的症状。

---

## 安装

预设的安装就是**把文件放到对的位置**：

1. 下载预设包，确认里面有两类东西：
   - 一个或多个 **`.jslot`**；
   - 常带一个**同名 `.nif`**（+ 有时 `.dds`）—— 这是雕塑几何。
2. 把 `.jslot` 放进：

   ```
   Data\SKSE\Plugins\CharGen\Presets\
   ```

3. 把配套的 `.nif`（与 `.dds`）放进：

   ```
   Data\SKSE\Plugins\CharGen\
   ```

4. **照作者给的资源清单把依赖 mod 装齐**（皮肤、眼睛、眉毛、头发、高模头……
   缺一项就会走样）。这一步是"预设导入后脸不对"的**第一大成因**。
5. 验证点：进游戏开捏脸界面（`showracemenu`），预设下拉里能看到该预设的名字。
   **看不到** = 路径放错了或文件不是 `.jslot`。

---

## 使用与配置

### 导入（用别人的预设）

1. 先把种族切到预设支持的那个种族 —— **这一步经常被跳过，导致"加载后脸很怪"**。
2. 打开捏脸界面 → **Presets** 页 → 加载目标 `.jslot`。
3. **等肤色完全加载完**（社区经验：加载是分步的，急着做下一步会得到错误的肤色）。
4. 若预设**自带雕塑几何**：到 **Sculpt** 页 → **Import Head** → 选**同名**的 `.nif`
   → **Import Part Matcher 保持默认** → Accept。
5. 可选：想换瞳色时，先随便选一个"左眼盲"类的眼睛，再重复第 4 步重新选眼
   （社区经验，用于绕开预设锁定的眼睛）。

### 导出（做自己的预设 / 做随从）

1. 在 RaceMenu 里捏好脸。
2. 到 **Sculpt** 页 → **F5 Export head** →
   得到 `Data\SKSE\Plugins\CharGen\<name>.nif` 与 `.dds`。
3. 存预设：`skee preset-save <名字>`（或界面里的 Save Preset）。
4. 要把它变成 NPC/随从的脸：见 [`facegen-pipeline.md`](facegen-pipeline.md) 的
   "做自定义随从的脸"一节（把 `.dds` 按 BaseID 改名放进 `FaceTint`）。

### 控制台命令（0.4.13+）

```
skee preset-save PATH      存到 Data/SKSE/Plugins/CharGen/Exported/PATH.jslot
skee preset-load PATH      加载到当前控制台选中的 actor
```

> `preset-load` **可以作用在 NPC 上**（官方 changelog 原话）。
> 但要注意：**预设负责"滑块值"，脸部件（head parts）需要单独设置** ——
> 套到 NPC 上之后如果头发/眼睛不对，那是部件没换，不是预设失效。

---

## 兼容与冲突

| 对象 | 关系 |
|---|---|
| **身形家族** | `.jslot` 的 morph 指向具体 esp，**CBBE 系与 UNP 系不能互用**；跨家族套用只会部分生效 |
| **High Poly Head** | HPH 预设必须在 **Head 页把 Face part 切到高模头**，否则脸是尖的。见 [`high-poly-head.md`](high-poly-head.md) |
| **EFM（Expressive Facegen Morphs）** | EFM 主文件**不兼容现有预设**（会改脸）；想保留旧脸就用可选的 *EFM - Racemenu Plugin*（只有滑块）。见 [`expressive-morphs.md`](expressive-morphs.md) |
| **ECE** | `CME_save` 与 `.jslot` 是两套体系，**不能互导** |
| **CotR / UBE** | 需要各自的基础 mod（Charmers of the Reach / UBE），且**与原版/HPH 预设不互通**（头部拓扑、UV、morph 都不同） |
| **BodySlide 预设（`.xml`）** | **完全不同的东西**：格式、数值刻度、生效方式都不同，**不能互导**，只能逐滑块换算 |
| **种族** | 社区经验规则：**人类之间（帝国/诺德/布雷顿/红卫）可互用；精灵之间（高/木/暗）可互用；兽人、虎人、亚龙人最好只在同族内用** |

---

## 排错

| 症状 | 判据（看到 X 说明是 Y） | 处理 |
|---|---|---|
| 预设下拉里**看不到**它 | 文件不在 `Presets\` 目录，或扩展名不是 `.jslot` | 检查路径；旧 `.slot` 虽可读但**下拉里可能不列** |
| 加载后**完全没反应** | SKSE / RaceMenu 版本不符，或目录放错 | 见 [`../06-troubleshooting/preset-not-applied.md`](../06-troubleshooting/preset-not-applied.md) |
| 脸是**尖的**、不像截图 | **没有在 Head 页把 Face part 切到高模头** | 切 Face part（HPH 预设的最高频问题） |
| 大体对**但不像** | **雕塑几何没导** | Sculpt → Import Head 导入同名 `.nif` |
| 部分特征丢失 / 纹理**紫红** | 预设依赖的**头发/眼/眉/皮肤资源没装** | 照作者的依赖清单补齐 |
| 眉歪 / 眉毛错位 | 眉毛资源与头模不匹配，缺对应补丁 | 装与头模配套的 brows 补丁 |
| **皮肤油光** | `skinOverrides` 缺失或条目错误 | 社区经验：手工补/改该块，或换一份预设 |
| 身形没跟着变 | 该身形的 `.tri` 未构建 | BodySlide 勾 `Build Morphs` 重构建 |
| 换存档/重装后脸变了 | 运行时状态落在 **SKSE co-save** 里，co-save 不一致 | 重新导入预设（见 [`racemenu.md`](racemenu.md) 的"工作原理"） |

---

## 取舍与建议

- **永远照依赖清单装齐**。预设不是"自包含"的：作者用了什么皮肤、什么眼、什么高模头，
  你就得有什么。**"缺一样就走样"是这个生态的默认状态，不是 bug。**
- **导入顺序有讲究**：先 `.jslot`，后同名 `.nif`（社区里反复出现的 TL;DR 就是
  "load jslot first, then import nif with the same name"）。
- **导出自己的预设时一并交付 `.nif` 与 `.dds`**，否则别人只能得到"没有雕塑的版本"。
- **分享礼仪**（社区惯例）：
  - 明确列出全部依赖 mod 与版本；
  - 注明**支持的种族**与**身形**；
  - 注明是否用了高模头、EFM、CotR、UBE 等会改变基础脸型的东西；
  - **不要二次分发别人的预设文件**（RaceMenu 与多数资源 mod 的权限栏都禁止再分发）；
  - 截图最好在**同一光照**下给正脸与侧脸，方便别人判断是否真的对得上。
- 反过来说，**下载预设前先看依赖清单的长度**：依赖越多的预设越漂亮，也越脆弱。
- **去哪找预设**：Nexus 是主阵地（Body/Face/Hair 与 Presets 分类）；
  其它聚集地有 **LoversLab**（成人向预设多）、**Vector Plexus**（高模头相关）、
  以及**各 Wabbajack 整合包自带的预设包**（社区经验）。

---

## 来源

**一手**

- RaceMenu Nexus SE 发布页与 changelog：**预设改为 JSON 格式、扩展名 `.jslot`**；
  CharGen v2.0.0+ 起 *"Save/Load preset to and from a slot file（replaces clipboard save/load）"*；
  `skee preset-save/load` 命令与 `Exported` 目录；0.4.19.15 *"Exposed programmer interface for Presets"*
  `https://www.nexusmods.com/skyrimspecialedition/mods/19080`
- 作者 Nexus 帖（2026-04-20）：0.4.20.0 部件标签机制（与预设的查找相关）—— 一手
- FSC Character Presets 页面对 **ECE 侧 `CME_save` 安装路径与 "Slot Load" 滑块**的说明 —— 一手（该预设页）

**社区经验**

- `.jslot` 结构示例与 `keys[].key` 指向提供 morph 的 esp（Nexus 论坛 scorrp10 引用实际文件片段）
- 导入顺序 "load jslot first, then import nif with the same name"、等待肤色加载完、
  先选"左眼盲"再重选眼睛的做法（多个预设页安装说明一致）
- `skinOverrides` 缺失/错误导致皮肤油光（LoversLab）
- Nexus 预设数量 2000+、种族匹配经验规则（Nexus 论坛 2025 帖 + LoversLab）
- HPH 预设需切 Face part（Nexus 预设页与 HPH 说明，多源一致）
- 雕刻几何必须单独 Import Head（多份预设说明一致）

**未确认**

- `.jslot` 的**完整字段 schema**（RaceMenu 未公布）
- **`value` 的统一刻度**：本库见到的实际样例有 `50` 与 `0.50000` 两种量级
- CharGen v2.0.0 起改用 slot 文件的**具体日期**
- 0.4.13 的**上传日期**
