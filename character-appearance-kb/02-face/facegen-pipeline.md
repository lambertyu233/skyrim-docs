---
id: facegen-pipeline
title: FaceGen 管线与 head parts
category: 02-face
kind: concept
version: 2.0.0
updated: 2026-10-25
tags: [捏脸, FaceGen, head part, HDPT, tint, 导出]
aliases: [facegen 数据, 面部预生成, ctrl f4, tintmask, facegeom, facetint, NPC 脸, 黑脸原理, 导出脸, 随从脸, FaceGen 是什么, facegen 路径, 重导脸, 脸部烘焙]
source: https://en.uesp.net/wiki/Skyrim_Mod:Mod_File_Format/RACE
summary: 脸部在插件里的数据模型（HDPT / RACE / NPC 记录）与运行时的两条文件路径（facegeom / facetint），Ctrl+F4 导出流程、做自定义随从脸的做法、官方 HeadPart Papyrus 接口，以及"NPC 的脸是预生成的"这条决定了整条排错思路的第一性事实。
---

# FaceGen 管线与 head parts

> **理解这一层，才能理解黑脸、脖缝、"EFM 对 NPC 无效"、"装了高模头 NPC 没变"这些现象。**
> 它们看起来毫不相干，其实是同一件事：**NPC 的脸不是实时生成的。**

---

## 速览

| 项目 | 值 |
|---|---|
| 作用层 | **插件记录（RACE / NPC / HDPT） + 磁盘上的预生成产物**两层 |
| 依赖 | 无（这是引擎原生机制，不是 mod 引入的） |
| 影响范围 | 所有 NPC 的脸网格与脸色调；玩家脸**不走**这条路径（玩家是实时生成的） |
| 关键限制 | **预生成产物与插件记录必须对得上**，对不上就是黑脸；产物是静态的，**改了记录就要重导** |
| 导出工具 | Creation Kit：**`Ctrl+F4`（Export FaceGen data）** |
| 产物 | `FaceGeom\<插件名>\<FormID>.nif` + `FaceTint\<插件名>\<FormID>.dds`（另有一份 `.tga`） |

要点：

- **玩家 vs NPC 是两条路**：玩家的脸在运行时由 head parts + morph 合成；
  NPC 的脸是**提前烘焙好的网格与贴图**，游戏只是加载它。
- 因此**任何"改 NPC 脸"的 mod，本质都是"改记录 + 重新烘焙"两步**，只做第一步没用。
- 路径里的 **`<插件名>` 目录名**是最关键的判据：黑脸 = 这个目录里的数据与记录对不上。
- **`Ctrl+F4` 会同时生成一份 `.tga` 和一份 `.dds`** —— CK wiki 原文说 `.tga` 是
  "unnecessary"（不用分发），`.dds` 才是要随 mod 发布的。

---

## 前世今生

### "FaceGen"这个名字

Creation Kit 里对应的命令就叫 **"Export FaceGen data"**（`Ctrl+F4`），
可见这是引擎/编辑器自带的一套概念，不是 mod 生态发明的。
**这套技术最初来自哪、是不是某个商业中间件，本库未确认** —— 下面只讲它在
Skyrim mod 生态里演化出的那条脉络。

### 这条管线是怎么被 mod 生态"撞开"的

| 阶段 | 状况 | 后果 |
|---|---|---|
| 原版设计 | 玩家脸**实时生成**（head parts + RACE 的 chargen morph 现算）；**NPC 脸全部预烘焙** | 玩家能捏，NPC 固定；运行时开销可控 |
| RaceMenu 出现 | 给玩家提供 **Export head mesh**，把实时生成的脸**导出成网格** | 第一次能把"玩家的脸"变成"某人的脸" |
| 高模头 / 自定义头模普及 | 换掉 head part 指向的网格 | **NPC 的预烘焙产物还是旧头** → 必须 `Ctrl+F4` 重导 |
| EFM 等 morph 类 mod | 替换 chargen / race morph 并加滑块 | **只影响玩家**（NPC 是预生成网格，不走实时 morph）；这也解释了"EFM 对 NPC 无效" |
| 预生成 preset / 随从包流行 | 直接分发 `FaceGeom` + `FaceTint` 产物 | 好处是所见即所得；代价是**对插件名/FormID 极度敏感** |

> 一句话概括这条演化：**mod 生态不断往"实时生成"那一侧加东西，
> 而 NPC 那一侧始终是"烘焙品"，于是"重导 FaceGen"成了一个绕不开的常规动作。**

---

## 它解决什么问题

### 为什么不实时生成 NPC 的脸

因为实时生成要走一整套流程：按 RACE 取默认 head part → 套 chargen morph →
按 NPC 记录的部件与染色层合成 tint → 生成网格与贴图。全 Skyrim 上千个 NPC
每次加载都算一遍，代价不可接受。

于是 Bethesda 的做法是：**编辑器里一次性算好，落盘成两个文件，游戏只负责加载。**

### 代价（也就是所有 FaceGen 类故障的总根源）

> **产物是静态的，且与"插件名 + FormID"强绑定。**
> 只要插件记录里的 head parts / 种族 / 染色变了，而磁盘上的产物没跟着重生成，
> 二者就对不上 —— 表现就是**黑脸**（见
> [`../06-troubleshooting/dark-face.md`](../06-troubleshooting/dark-face.md)）。

---

## 工作原理

### 一、脸部在插件里的数据模型

### HDPT：Head Part（面部部件）

一个 HDPT 记录代表一类面部特征（头发、眼、胡须、疤痕…），包含：

- 基础模型信息；
- 按用途（**chargen** / **other**）分组的字段，各自指向一个 `.tri` 文件；
- 一个 FormList 给出可选部件数据（`NAM0` / `NAM1` 成对重复）。

### RACE：种族的 chargen 数据

以 `NAM0` 开始，按性别分成 `MNAM`（男）/ `FNAM`（女）：

| 字段 | 含义 |
|---|---|
| `HEAD` | 默认 headpart（引用 HDPT） |
| `MPAI` / `MPAV` | **Morph 索引与取值**（出现 4 次，对应**鼻 / 眉 / 眼 / 唇**） |
| `RPRM` / `RPRF` | Race Presets（男女） |
| `AHCM` / `AHCF` | 可用发色（→ CLFM） |
| `FTSM` / `DFTM` | Face Details / Default Face Texture（→ TXST） |

Morph 的类型标志为：`NoseType0-31`、`BrowType0-20`、`EyesType0-38`、`LipType0-31`。

### 染色（tint）字段组

| 字段 | 含义 |
|---|---|
| `TINL` | Tint Index Number |
| `TINT` | tint mask 纹理路径（`.dds`） |
| `TINP` | **Mask Type**，见下表 |
| `TINC` / `TIND` | 关联的颜色预设（→ CLFM） |
| `TINV` | 默认值（float） |

`TINP` 的取值表：

```
1=Lip Color   2=Cheek Color   3=Eyeliner       4=EyeSocket Upper
5=EyeSocket Lower  6=Skin Tone   7=Paint       8=Laugh Lines
9=Cheek Color Lower  10=Nose    11=Chin        12=Neck
13=Forehead   14=Dirt
```

### NPC：脸上的部件与色层

- `PNAM` = Head Parts（头发、眼、疤痕…）
- `HCLF` = Hair Color
- 面部染色层子记录：`TINI` / `TINC` / `TINV` / `TIRS`，以及第二套 `TINT` / `TINP` / `TIND`（枚举 1–69）

### 二、运行时文件路径

| 内容 | 路径 |
|---|---|
| 头网格 | `Meshes\Actors\Character\FaceGenData\FaceGeom\<插件名>\<FormID>.nif` |
| 头色调 | `Textures\Actors\Character\FaceGenData\FaceTint\<插件名>\<FormID>.dds`（另有一份 `.tga` 供 LOD 用） |
| 原版 tint mask 源 | `Textures\Actors\Character\Character Assets\tintmasks\` |

**注意路径里的 `<插件名>`** —— 黑脸的本质就是"这个目录里的数据"与"插件记录里的 head parts"对不上。
插件改名（例如 ESL 化、换文件名）会让整个 `<插件名>` 目录失效，这是很常见的翻车点。

### 玩家为什么不一样

玩家的脸由 **RACE 的 chargen 数据 + 选中的 head parts + morph** 在运行时合成，
**没有** `FaceGeom` 产物。所以：

- 拖 RaceMenu 滑块 → **只改玩家**；
- 想让 NPC 也变 → 走**分配/预构建**路线（见
  [`../03-body/morph-runtime-vs-bake.md`](../03-body/morph-runtime-vs-bake.md) 与
  [`../05-distribution/obody-ng.md`](../05-distribution/obody-ng.md)）。

---

## 安装

这一层没有"安装"，要做的是**把环境准备好**：

1. **让 Creation Kit 能加载多个 master**：在 `CreationKit.ini` 里允许多 master 加载
   （INI 相关见 [`../../creation-kit-kb/01-installation/ini-files.md`](../../creation-kit-kb/01-installation/ini-files.md)）。
   验证点：CK 能同时打开你的插件与它依赖的 esm，且不报 master 数超限。
2. **确认目标插件是 Active File**：`Ctrl+F4` 只会为**当前活动插件**里的 NPC 导出。
   验证点：CK 标题栏/Object Window 里目标插件处于激活状态。
3. **若你要在 CK 里给高模头导脸**：必须装 HPH 的 **01 号 FOMOD 选项**
   （"Loose files needed for FaceGen creation in CK"），否则 CK 找不到松散网格文件。
   见 [`high-poly-head.md`](high-poly-head.md)。
4. **备份 `tintmasks`**（可选但强烈建议，见下节技巧）。

---

## 使用与配置

### 一、CK 导出流程（`Ctrl+F4`）

`Ctrl+F4` 在 CK 的键盘映射里的定义是 **Export FaceGen data**，官方说明为：

> *"Builds temporary .tga (unnecessary) and permanent .dds (to distribute) of FaceGen data for all selected NPCs"*

—— 即**生成一份临时 `.tga`（不需要分发）和一份 `.dds`（这个才随 mod 发布）**。
出处：[`../../creation-kit-kb/02-features/keyboard-mapping.md`](../../creation-kit-kb/02-features/keyboard-mapping.md)。

步骤：

1. 在 Creation Kit 里加载相关插件（需要 `CreationKit.ini` 允许加载多个 master）；
2. **不要用搜索框选 Actor**，要在 Object Window 的 **Actors 子树里直接点中**目标 NPC
   （可以多选）；
3. 按 **`Ctrl+F4`** 导出，生成 `FaceGeom` 下的 `.nif` 与 `FaceTint` 下的 `.dds`。

> **导出前的一个技巧（社区经验）**：如果你的 tintmask 曾经被改过，先临时把
> `Textures\Actors\Character\Character Assets\tintmasks` 改名/移走，
> 否则会"污染"导出结果（表现为紫、红、额头条纹）。导完再改回。

### 二、做自定义随从的脸

1. 在 RaceMenu 捏好脸 → **Sculpt 页 F5 Export head** →
   `Data\SKSE\Plugins\CharGen\<name>.nif` 与 `.dds`；
2. 把 `.dds` 复制到 `FaceTint\<你的 esp>\` 并**重命名为该 NPC 的 BaseID**
   （前两位补 0，例如 `0001C197.dds`）；
3. 若改过肤色，还要在 CK 的 **Character Gen Parts → Face Tinting Color** 填上对应 RGB。

对应的预设流程（`.jslot` + 雕塑 `.nif`）见 [`racemenu-presets.md`](racemenu-presets.md)。

### 三、官方 Papyrus 接口

Creation Kit wiki 的 **HeadPart Script** 明确标注 *"This type requires SKSE"*，继承 `Form`：

| 类型 | 函数 |
|---|---|
| SKSE Global | `HeadPart GetHeadPart(String name)` |
| SKSE Member | `Int GetType()`、`Int GetNumExtraParts()`、`HeadPart GetNthExtraPart(Int n)`、`Bool HasExtraPart(HeadPart part)`、`Int GetIndexOfExtraPart(HeadPart part)`（非 extra 返回 `-1`）、`FormList GetValidRaces()`、`SetValidRaces(FormList races)` |

CK wiki 示例里还出现 `Player.GetNthHeadPart(0).GetType()`，
说明 Actor 侧有 `GetNthHeadPart` / `SetNthHeadPart`（**该函数页未单独确认，标注为"示例引用"**）。

> **澄清**：`showracemenu` 与 `setnpcweight` 是**引擎/控制台命令**，不是 Papyrus 函数。
> 提到"chargen 的脚本接口"时，指的其实是上面这组 HeadPart Script。

---

## 兼容与冲突

| 对象 | 关系 |
|---|---|
| **High Poly Head / 任何换头模的 mod** | 只改记录 **不够**，必须 `Ctrl+F4` 重导；且**带雕塑的头网格走不通**。见 [`high-poly-head.md`](high-poly-head.md) |
| **EFM** | 替换 chargen / race morph，**只影响玩家**；NPC 是预生成网格，不吃这套 morph。见 [`expressive-morphs.md`](expressive-morphs.md) |
| **改 tintmasks 的 mod** | 会污染 `Ctrl+F4` 的导出结果（皮肤/额头条纹异常） |
| **插件改名 / ESL 化** | `<插件名>` 目录失效 → 黑脸 |
| **BSA vs loose** | 产物被 BSA 里的旧版本压住时，改磁盘文件看不出效果 —— 覆盖规则见 [`../07-workflow/mo2-override-rules.md`](../07-workflow/mo2-override-rules.md) |
| **多个 mod 改同一个 NPC** | 后加载的记录赢，但**产物未必跟着更新** → 记录与产物错配 |

---

## 排错

| 症状 | 判据（看到 X 说明是 Y） | 处理 |
|---|---|---|
| **黑脸** | `FaceTint\<插件名>\<FormID>.dds` 缺失或与记录不符 | 见 [`../06-troubleshooting/dark-face.md`](../06-troubleshooting/dark-face.md)：运行时修复 / CK 重导 / 隐藏冲突文件 / 调序 |
| 脸是紫的、红的、**额头有条纹** | 导出被本地改过的 `tintmasks` 污染 | 导出前临时移走 `tintmasks` 目录，导完改回 |
| 换了头模但 **NPC 脸没变** | 只改了记录，没重导 | `Ctrl+F4`；带雕塑的头网格**无效**，需另做 |
| 装了 EFM，NPC 表情没变 | EFM 只作用于玩家 | 这是设计而非 bug |
| 脖子上有一圈色差 | 头身皮肤不同源 / UV 错配 | 见 [`../06-troubleshooting/neck-seam.md`](../06-troubleshooting/neck-seam.md) |
| 手动改了 `.dds` 却没变化 | 被 BSA 或别的 mod 覆盖 | 检查覆盖优先级 |
| 随从脸在别人机器上不对 | `.dds` 没按 **BaseID** 命名，或没放进正确的 `<插件名>` 目录 | 检查文件名与目录 |
| 导出后 `FaceTint` 下只有 `.tga` 没有 `.dds` | 导出未正常完成 | CK wiki 说 `.tga` 是临时的、`.dds` 才是要分发的；两者都在说明导出成功了，分发只带 `.dds` |

---

## 取舍与建议

- **改 NPC 脸的正确心智模型是"两步"**：① 改插件记录（head part / 种族 / 染色）；
  ② `Ctrl+F4` 重新烘焙。**只做第一步 = 必定黑脸。**
- **能不改插件名就别改**。改名会让整个 `<插件名>` 目录失效，是性价比最低的翻车方式。
- **分发 mod 时只带 `.dds`，不带 `.tga`**（CK wiki 明确 `.tga` 是 unnecessary）。
- **做随从优先走 RaceMenu 导出 + BaseID 命名**这条路，比在 CK 里手捏精确得多。
- **遇到"为什么这个 NPC 的脸和别人不一样"**，先查两条路径上的文件是否存在、是否匹配，
  再怀疑 mod 冲突 —— 90% 的问题在这两层里就能定位。
- **理解 morph 与 FaceGen 的分工**：morph 是运行时/构建时的顶点位移（见
  [`../00-overview/morph-and-nif-basics.md`](../00-overview/morph-and-nif-basics.md)），
  FaceGen 是"把最终那张脸固化成文件"。两者不是一回事，别混着排查。

---

## 来源

**一手**

- HDPT / RACE / NPC 的字段与 `TINP` 枚举：UESP「Skyrim Mod:Mod File Format」
  `https://en.uesp.net/wiki/Skyrim_Mod:Mod_File_Format/HDPT`、`/RACE`、`/NPC`
- HeadPart 对象字段与 HeadPart Script：Creation Kit wiki
  `https://ck.uesp.net/wiki/HeadPart`、`https://ck.uesp.net/wiki/HeadPart_Script`
- **`Ctrl+F4` = Export FaceGen data，且会生成"临时 .tga（unnecessary）与用于分发的 .dds"**：
  Creation Kit wiki「Creation Kit Keyboard Mapping」（本工作区 `_raw` 原文）
  → [`../../creation-kit-kb/02-features/keyboard-mapping.md`](../../creation-kit-kb/02-features/keyboard-mapping.md)
- FaceGen 运行时路径（`FaceGeom` / `FaceTint`）与 `Ctrl+F4` 流程：Creation Kit wiki / UESP +
  Nexus 论坛被广泛引用的答复 —— **一手路径 + 社区流程**
- High Poly Head 官方说明：NPC 需先加为 master、换 head part、再 `Ctrl+F4`，
  且**对雕塑头网格无效** —— 一手（经镜像转述）

**社区经验**

- 导出前临时移走 `tintmasks` 以避免污染（紫/红/额头条纹）
- F5 导出头网格后按 BaseID 命名 `.dds` 的做法
- 不要用搜索框选 Actor、要在 Actors 子树里直接点中

**未确认**

- Actor 的 `GetNthHeadPart` / `SetNthHeadPart` **函数页**（仅见于 CK wiki 示例，未单独确认）
- "FaceGen"这一名称背后所用技术的**具体来源/供应商**
- 本页列出的各 mod 具体发布日期（未逐一核实）
