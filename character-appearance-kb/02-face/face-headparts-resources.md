---
id: face-headparts-resources
title: 眼、眉、发、须资源现状
category: 02-face
kind: reference
version: 2.0.0
updated: 2026-10-25
tags: [捏脸, 眼睛, 眉毛, 头发, 胡须, 资源]
aliases: [eyes of beauty, brows, ks hairdos, apachii, beards, 发型包, 眼睛 mod, 眉毛 mod, 头部部件, headpart, 眼眉发须, 头发 mod, 睫毛, 眉歪, 发型补丁, 胡须 mod]
source: https://www.nexusmods.com/skyrimspecialedition/mods/16185
summary: 捏脸最常用的四类外观资源（眼/眉/发/须）的代表 mod——作者、适用头部（原版 / HPH / CotR）、是否需要补丁，外加 HPH 时代的补丁矩阵与选型建议。
---

# 眼、眉、发、须资源现状

> **一句话**：这类资源是"脸的配件"——不装也能捏脸，装了才好看。
> 它们真正的共同坑不是装不上，而是**换了头模之后对不上**：
> 眉歪、须悬空、睫毛飘在脸外，全都来自"部件按旧头型做、头已经换了"。

---

## 速览

| 部位 | 事实上的主流 | Nexus（SE） | 作者 | 适用头部 | 是否需补丁 |
|---|---|---|---|---|---|
| **眼睛** | The Eyes of Beauty SSE | **16185** | LogRaam（Gabriel Mailhot），docteure 上传 | 原版 / HPH | 一般不需要 |
| **眉毛** | Brows（Aesthetic 系列） | **1062** | Hvergelmir，lthot 上传 | 原版；**HPH 需补丁** | ✅ 38493 / 63777 |
| **头发** | KS Hairdos SSE | **6817** | Kalilies & Stealthic | 原版 / HPH | 视版本 |
| **头发** | ApachiiSkyHair SSE | **2014** | apachii | 原版 | 常配重纹理补丁 |
| **胡须** | Beards（Aesthetic 系列） | **1067** | Hvergelmir，lthot 上传 | 原版；**HPH 需补丁** | ✅ |
| **胡须** | Beards of Power | **42635** | Mharlek1 | 原版 | 视版本 |

要点：

- **先定头模再选配件**。HPH 换了头型，**眉与须几乎必须换配套版本**。
- **版本号有两套体系**：LE 与 SE 的版本号互不相干（见下"版本陷阱"）。
- **发型数量口径不一致**，别把某个数字当事实。
- RaceMenu **0.4.20.0** 起支持**部件标签（Tags）**，装了一大堆发型后靠它筛选。

---

## 前世今生

### 时间线（可核实部分）

| 时间 | 事件 | 意义 |
|---|---|---|
| LE 时代 | The Eyes of Beauty（LE 13722，LogRaam）、Brows（LE 30411）、Beards（Hvergelmir）、KS Hairdos、ApachiiSkyHair 陆续成型 | 这批资源奠定了"眼眉发须"四类分工 |
| 2016–2018 | SE 移植潮：多数资源由原作者之外的志愿者移植上传（如 EoB 由 **docteure**、Hvergelmir 系列由 **lthot** 上传） | **作者 ≠ 上传者**成为常态，查 credits 时要看 `Created by` 而不是 `Uploaded by` |
| **2018-04** | Facelight Plus SE 一类配套工具移植 | 补光生态同步跟进 |
| **2020-01-09** | **KS Hairdos - HDT SMP（31300）**首发，ousnius 移植并做物理 | 发型从"静态网格"进入"物理"时代 |
| **2020-08** | The Eyes of Beauty SSE **1.2** | 现行 SE 版本 |
| **2022-02-20** | **Vanilla hair remake（63979）**首发（jg1） | 原版发型重制，可选 FSMP 物理 |
| **2024-06-11** | Vanilla hair remake 更新到 **1.0.3** | 现行版本；明确兼容 High Poly Vanilla Hair |
| **2026-05-17** | KS Hairdos - HDT SMP **1.5.0** | 加发型标签（需 **RaceMenu 0.4.20.0+**）、UBE 碰撞、假发预览 |

> ⚠️ High Poly Head 的发布时间**未确认**（见 [`high-poly-head.md`](high-poly-head.md)）。
> 它带来的连锁反应是：**眉、须、疤痕都出现了"HPH 专用版"这一新分类**。

### 版本陷阱（最容易搞错的一点）

> **SE 移植版的版本号与 LE 原版不是同一套体系。**
> The Eyes of Beauty：**SE 官方移植是 1.2**；中文镜像站上常见的 **10.0.1 是 LE 原版的版本号**。
> 这两个数字没有换算关系，别混。

同理，Brows 的版本口径在社区里同时出现 **4.0.1 与 4.1.0**（**未确认唯一最新值**），
KS Hairdos 的发型数量同时出现 **883 与 983** 两种记录（见下）。**遇到冲突以 Nexus 页面为准。**

---

## 它解决什么问题

### 没有它之前

- 原版眼睛贴图分辨率低、虹膜平淡，且**没有异色瞳 / 渐变瞳**这类选项；
- 原版眉毛是低分辨率贴片，且与发色对不上；
- 原版发型款式少、网格是"薄片"，一动就穿模；
- 胡须款式被 Bethesda 砍掉了一批（辫须、串珠须）。

### 它怎么解决的

| 部位 | 做法 |
|---|---|
| 眼睛 | 增加高分辨率虹膜贴图 + 一批可选瞳色（含异色瞳、吸血鬼眼） |
| 眉毛 | 手绘眉型 + 多档分辨率；可选 esp 增加数量并与发色匹配 |
| 头发 | 大批量发型包（几百款），后期加入 SMP 物理 |
| 胡须 | 补质量与补款式并行，复原被砍掉的部分 |

---

## 它包含什么

### 眼睛

| mod | Nexus（SE） | 作者 | 说明 |
|---|---|---|---|
| **The Eyes of Beauty SSE** | **16185** | **LogRaam（Gabriel Mailhot）**，docteure 上传 | 官方授权 SE 移植，**版本 1.2**。按 Player / NPC / Dawnguard（吸血鬼眼）分包，含人类、亚龙人、精灵、虎人、兽人异色瞳 |
| **Mikan Eyes** | 18780 | **nerune** | 常见预设的软依赖 |
| Vanilla Makeup HD | 24482 | DomainWolf | 妆面（同属脸部上层资源） |
| SUEMR Glow & No-Glow Beast Eyes | 18147 | Ruhadre | 兽族眼睛发光/不发光两版 |
| Kala's Beast Race Eyes | 42298 | GuideThisOneKalaheria | 兽族眼睛 |
| The Witcher 3 Eyes | 未确认 | Oaristys | 老牌移植资源 |
| Improved Eyes Skyrim | 未确认 | 未确认 | 老牌资源 |

### 眉毛

**Hvergelmir's Aesthetic 系列**（作者 **Hvergelmir**，上传 **lthot**）：

- Nexus SE **1062**，LE 版 30411；
- 提供 **Ultra（2048×1024）/ High（1024×512）/ Low（512×256）** 三档；
- 可选 `.esp` 增加更多手绘眉型（含按发色匹配的深浅色）。

**HPH 兼容**：Brows 与 HPH 属于"**半兼容**"——不崩溃但**眉形略歪**，需要补丁：

| 补丁 | Nexus | 说明 |
|---|---|---|
| Brows by Hvergelmir for High Poly Head | **38493** | 原版 Brows → HPH |
| 同款 - COTR - UBE 版 | **63777** | v2.1.0，含 Headpart Whitelist 与隐藏原版眉的 `Brows - Non-playable.esp` |

其它眉部资源：**Maevan2's Eyebrows**（SE 26881，Shiva182 移植）、**Kalilies Brows**、
**LM's Dual Brows - HPH - Standalone**（LeelooMinai，**SE ID 未确认**）。

### 头发

| mod | Nexus（SE） | 作者 | 说明 |
|---|---|---|---|
| **KS Hairdos SSE** | **6817** | **Kalilies & Stealthic** | 老牌大型发型包，覆盖男女 |
| **KS Hairdos - HDT SMP** | **31300** | **ousnius - Kalilies - Stealthic**（ousnius 上传） | 物理版，**standalone，不需要本体**；需 FSMP |
| **ApachiiSkyHair SSE** | **2014** | **apachii** | 量最大，Males / Females 分文件；纹理偏旧，常有重纹理补丁 |
| **Vanilla hair remake** | **63979** | **jg1** | 重制 146 款原版发型，可选 FSMP 物理；主文件**无 ESP，只影响玩家** |
| **High Poly Vanilla Hair** | **41863** | Macxhiin | 原版发型的高模版 |
| Vanilla Hair Replacer (VHR) | 未确认 | **preeum** | 替换原版发型；与 Face Discoloration Fix 有协同 |
| HG Hairdos | 未确认 | **summerdew** | 常见于新预设 credits |
| Hallgarth's Additional (Vanilla) Hair | 未确认 | **Hallgarth** | 补原版发型 |

KS Hairdos 生态衍生：**KS Hairdos 1.7 Salt and Wind**（重纹理）、**SC - KS Hairdos Retextured**、
**KS Hairdos Male Scalp Fix**、**LDD - KS Male Hairstyle Tweaks**。

> ⚠️ **KS 发型数量口径不一致**：官方 1.9 页面的描述同时被记录为
> **883（792 女 / 91 男）** 与 **983（876 女 / 107 男）** 两种。
> **未确认唯一正确值**，写作时说"**数百款（约 880~980）**"最稳。

> **Vanilla hair remake 的两个已知边界**（作者原文）：
> ❌ **不兼容 Vanilla Hair Replacer**（后者改了发型网格路径）；
> ✅ 兼容 High Poly Vanilla Hair；HPH / EFM 的补丁由 **Mharlek1** 提供。
> 另外**物理版发型会让 Creation Kit 在加载单元格时崩溃**——进 CK 前禁用或打包成 BSA。

### 胡须

| mod | Nexus（SE） | 作者 | 说明 |
|---|---|---|---|
| **Beards（Aesthetic 系列）** | **1067** | **Hvergelmir**（上传 lthot） | 版本 **5.0.1**；5.0 用 **BC7 `.dds`** 重做全部纹理与法线，5.0.1 修 FOMOD 路径错误 |
| **Beards of Power** | **42635** | **Mharlek1** | 另一套胡须美化 |
| **BeastHHBB** | 38480 | **Mharlek1** | 兽族（亚龙人 / 虎人）的毛发、角、眉、须 |

Apachii 与 Beards 系列取向不同：**前者补量，后者补质**（并复原了被 Bethesda 砍掉的辫须 / 串珠须）。

---

## 安装

1. **先装头模相关的东西**：原版头还是 HPH？这一步决定后面所有补丁。
   见 [`high-poly-head.md`](high-poly-head.md)。
2. **装眼睛 / 眉毛 / 头发 / 胡须的本体**。
   验证点：进 RaceMenu，对应部件页签里能看到新条目。
3. **装 HPH（如适用）后立即装眉/须的 HPH 补丁**（38493 / 63777 一类）。
   验证点：切到 HPH 脸后**眉毛贴合眉骨、胡须不悬空**——歪了就是没打补丁。
4. **发型包按需装**。物理版（KS Hairdos SMP / Vanilla hair remake SMP）需要 **FSMP**，
   见 [`../04-physics/faster-hdt-smp.md`](../04-physics/faster-hdt-smp.md)。
5. **装完跑一次 RaceMenu**，确认部件列表能正常打开、没有闪退。

### 加载顺序的一般原则

- 部件类 mod 多为纯资源 + 一个小小的 esp/esl，**顺序影响主要在"谁覆盖谁的贴图"**；
- NPC 向的发型/眉毛分发 mod 应**排在改 NPC 头的 mod 之后**，否则会被覆盖；
- 具体规则见 [`../07-workflow/mo2-override-rules.md`](../07-workflow/mo2-override-rules.md)。

---

## 使用与配置

### 部件太多怎么办：用部件标签

RaceMenu **0.4.20.0** 起内置**部件标签（Part selection filter and Tags）**：

- 类型映射：**Face=1, Eyes=2, Hair=3, Beard=4, Scar=5, Brow=6**；
- 配置目录：`Data/SKSE/Plugins/CharGen/Tags/<MODNAME>/parts.json` 与 `tags.json`；
- 同一个 Form 被两个 mod 打标签时会**合并**。

KS Hairdos - HDT SMP **1.5.0** 已经自带发型标签（**要求 RaceMenu 0.4.20.0+**）。
装到上百个发型时，这是唯一能救你的筛选手段。详见 [`racemenu.md`](racemenu.md)。

### 假发（wigs）

KS Hairdos SMP 1.5.0 起提供可装备的假发，作者要求：

- 用假发时**必须装 Hair Suppression Fix**（Nexus **179400**）；
- 想让 NPC 的假发颜色对上，推荐 **Hair Colour Sync NG**（Nexus **156414**）。

Vanilla hair remake 也提供可装备发型（`HairNord01` 等，控制台获取，带种族限制）。

---

## 兼容与冲突

| 组合 | 关系 |
|---|---|
| **原版头 + 任意眼/发** | ✅ 基本通用 |
| **HPH + 原版眉毛 / 胡须** | ⚠️ **半兼容**：不崩溃但**眉歪、须悬空** → 必须打 HPH 补丁 |
| **HPH + 原版头发** | ⚠️ 部分原版发型轻微穿模 → 用 HPH 的高模香草发或换发型 |
| **CotR / UBE + 原版眉** | ❌ 头部拓扑不同，需 **CotR/UBE 专用版**（如 63777） |
| **Vanilla Hair Replacer（VHR） + Vanilla hair remake** | ❌ **不兼容**（前者改了网格路径） |
| **Vanilla hair remake + High Poly Vanilla Hair** | ✅ 兼容（谁覆盖谁都行） |
| **KS Hairdos + KS Hairdos SMP** | SMP 版是 standalone，**可不装本体** |
| **物理发型 + Creation Kit** | ⚠️ 加载单元格会让 CK 崩溃 → 打包 BSA 或进 CK 前禁用 |

> **判据**：如果**只有眉/须错位而脸本身正常** → 100% 是头模换了但部件没换；
> 如果**脸也跟着崩**，那问题在头模或 morph，不在这里。

---

## 排错

| 症状 | 判据 | 处理 |
|---|---|---|
| **眉毛歪 / 飘在眉骨上方** | 装了 HPH 但用的是原版 Brows | 装 HPH 版 Brows 补丁（38493 / 63777） |
| **胡须悬空 / 破皮** | 同上 | 换 HPH 配套胡须 |
| **原版眉毛和 HPH 眉毛同时出现** | 没装隐藏插件 | 装 63777 里的 `Brows - Non-playable.esp`（隐藏原版眉） |
| **发型穿模 / 稀碎** | 用的是低质量重纹理或旧网格 | 换发型或装重纹理补丁（Salt and Wind 一类） |
| **装了物理发型但不动** | 没装 FSMP / 装了没启用 | 见 [`../06-troubleshooting/physics-not-working.md`](../06-troubleshooting/physics-not-working.md) |
| **物理发型在 CK 里崩溃** | 加载单元格时崩 | 打包成 BSA，或进 CK 前禁用该 mod |
| **部件列表打不开 / 闪退** | 部件数量过多或某个 nif 损坏 | 逐个禁用排查；见 [`../06-troubleshooting/overlay-nif-ctd.md`](../06-troubleshooting/overlay-nif-ctd.md) |
| **NPC 换了发型但脸黑了** | FaceGen 没重导 | 见 [`../06-troubleshooting/dark-face.md`](../06-troubleshooting/dark-face.md) |
| **找不到想要的部件** | 装了几百个 | 用 RaceMenu 0.4.20.0+ 的部件标签筛选 |

---

## 取舍与建议

### 使用建议（选型顺序）

1. **先定头模**（原版 / HPH / CotR / UBE），再选配件。顺序反了必然返工。
2. **装了 HPH 就同时装眉/须的 HPH 补丁**，并且**别忘了装隐藏原版部件的那个 esp**，
   否则会出现"两套眉毛叠在一起"。
3. **眼睛优先级最高**：成本最低、收益最明显，且几乎不需要补丁。
4. **发型按需选一个主包即可**（KS 或 Apachii 二选一作为主力），
   再按预设需求补散件——装 3 个大包的收益远小于它带来的管理与 CK 成本。
5. **物理发型要算性能账**。Vanilla hair remake 作者明说它是"为所有人做的不为高端机做的"，
   优化了开销并**跳过了身体碰撞**；追求极致动态再去 KS Hairdos SMP。
6. **资源装得越多，FaceGen 缓存与部件索引负担越重**。装到上百发型时，
   留意是否需要专门的 FaceGen 缓存处理（见 [`facegen-pipeline.md`](facegen-pipeline.md)）。
7. **给 NPC 换部件必须重导 FaceGen**，`Ctrl+F4` 那条流程逃不掉。

### 不该做的

- **不要把 LE 的版本号当 SE 的版本号**（EoB 是最典型的坑：SE 是 1.2）。
- **不要装了 HPH 还留着原版眉/须**，也不要同时装多个互相改路径的发型替换（VHR vs remake）。
- **不要凭"作者名"判断**——SE 大量资源是**志愿者移植上传**，`Created by` 与 `Uploaded by` 经常不是同一个人。

---

## 来源

**一手（Nexus 发布页 / Files 页）**

- The Eyes of Beauty SSE（16185）：版本 **1.2** 为 SE 移植、分包结构、作者与上传者
  `https://www.nexusmods.com/skyrimspecialedition/mods/16185`
- Brows（SE 1062 / LE 30411）与 HPH 补丁 38493、COTR-UBE 版 63777
  `https://www.nexusmods.com/skyrimspecialedition/mods/1062`
- Beards（SE 1067）：版本 **5.0.1**、BC7 重做纹理与法线、FOMOD 路径修复
  `https://www.nexusmods.com/skyrimspecialedition/mods/1067`
- KS Hairdos SSE（6817）：作者 Kalilies & Stealthic
  `https://www.nexusmods.com/skyrimspecialedition/mods/6817`
- **KS Hairdos - HDT SMP（31300）**：`ousnius - Kalilies - Stealthic`、ousnius 上传、
  首发 2020-01-09、当前 1.5.0（2026-05-17）、完整 changelog（1.1~1.5.0）、
  standalone、假发需 Hair Suppression Fix（179400）、推荐 Hair Colour Sync NG（156414）、
  发型标签需 RaceMenu 0.4.20.0+ —— 一手
- **Vanilla hair remake（SE 63979 / LE 118021）**：作者 **jg1**、首发 2022-02-20、
  1.0.3（2024-06-11）、兼容 High Poly Vanilla Hair、**不兼容 Vanilla Hair Replacer**、
  HPH/EFM 补丁由 **Mharlek1** 提供、物理版会让 CK 崩溃 —— 一手（作者页描述）
- ApachiiSkyHair SSE（2014）：`https://www.nexusmods.com/skyrimspecialedition/mods/2014` —— 一手
- Beards of Power（42635，Mharlek1）、BeastHHBB（38480，Mharlek1）、
  Vanilla Makeup HD（24482，DomainWolf）、SUEMR（18147，Ruhadre）、
  Kala's Beast Race Eyes（42298）：各发布页与社区 credits —— 一手（页面）

**社区经验**

- Hvergelmir 系列由 **lthot** 上传、EoB 由 **docteure** 上传（SE 移植者与作者不同）
- KS 发型数量的 883 / 983 两种口径（整合包记录与 MO2 导出记录）
- "Brows 与 HPH 半兼容，不崩溃但眉形略歪"（本库既有结论 + 补丁页互相印证）
- HG Hairdos（summerdew）、Hallgarth's Additional Hair、LM's Dual Brows（LeelooMinai）
  等资源的作者归属：整合包 credits —— 社区经验（**其 SE 版 Nexus ID 未确认**）

**未确认**

- **Brows 的当前版本**（4.0.1 与 4.1.0 两种记录）
- **KS Hairdos 的确切发型数量**（883 与 983 两种记录）
- **Vanilla Hair Replacer（VHR）、The Witcher 3 Eyes、Improved Eyes Skyrim 的 SE 版 Nexus ID**
- **HG Hairdos、Hallgarth's Additional Hair、LM's Dual Brows 的 SE 版 Nexus ID**
- **High Poly Head 的发布日期**（影响了眉/须补丁生态的时间起点）
