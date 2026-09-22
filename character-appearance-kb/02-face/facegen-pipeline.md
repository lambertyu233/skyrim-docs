---
id: facegen-pipeline
title: FaceGen 管线与 head parts
category: 02-face
kind: concept
version: 1.0.0
updated: 2026-09-22
tags: [捏脸, FaceGen, head part, HDPT, tint, 导出]
aliases: [facegen 数据, 面部预生成, ctrl f4, tint mask]
source: https://en.uesp.net/wiki/Skyrim_Mod:Mod_File_Format/RACE
summary: 脸部的数据模型（HDPT / RACE / NPC 记录）、FaceGen 的运行时文件路径与 CK 导出流程，以及为什么"NPC 的脸是预生成的"决定了整条排错思路。
---

# FaceGen 管线与 head parts

理解这一层，才能理解黑脸、脖缝、"EFM 对 NPC 无效"这些现象。

## 一、脸部在插件里的数据模型

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

## 二、运行时文件路径

| 内容 | 路径 |
|---|---|
| 头网格 | `Meshes\Actors\Character\FaceGenData\FaceGeom\<插件名>\<FormID>.nif` |
| 头色调 | `Textures\Actors\Character\FaceGenData\FaceTint\<插件名>\<FormID>.dds`（另有一份 `.tga` 供 LOD 用） |
| 原版 tint mask 源 | `Textures\Actors\Character\Character Assets\tintmasks\` |

**注意路径里的 `<插件名>`** —— 黑脸的本质就是"这个目录里的数据"与"插件记录里的 head parts"对不上。

## 三、CK 导出流程（`Ctrl+F4`）

1. 在 Creation Kit 里加载相关插件（需要 `CreationKit.ini` 允许加载多个 master）；
2. **不要用搜索框选 Actor**，要在 Object Window 的 Actors 子树里**直接点中**目标 NPC；
3. 按 **`Ctrl+F4`** 导出，生成上面两个目录下的 `.nif` 与 `.dds`。

> **导出前的一个技巧（社区经验）**：如果你的 tintmask 曾经被改过，先临时把
> `Textures\Actors\Character\Character Assets\tintmasks` 改名/移走，
> 否则会"污染"导出结果（表现为紫、红、额头条纹）。导完再改回。

## 四、做自定义随从的脸

1. 在 RaceMenu 捏好脸 → Sculpt 页 **F5 Export head** →
   `Data\SKSE\Plugins\CharGen\<name>.nif` 与 `.dds`；
2. 把 `.dds` 复制到 `FaceTint\<你的 esp>\` 并**重命名为该 NPC 的 BaseID**
   （前两位补 0，例如 `0001C197.dds`）；
3. 若改过肤色，还要在 CK 的 Character Gen Parts → **Face Tinting Color** 填上对应 RGB。

## 五、官方 Papyrus 接口

Creation Kit wiki 的 **HeadPart Script** 明确标注 *"This type requires SKSE"*，继承 `Form`：

| 类型 | 函数 |
|---|---|
| SKSE Global | `HeadPart GetHeadPart(String name)` |
| SKSE Member | `Int GetType()`、`Int GetNumExtraParts()`、`HeadPart GetNthExtraPart(Int n)`、`Bool HasExtraPart(HeadPart part)`、`Int GetIndexOfExtraPart(HeadPart part)`（非 extra 返回 `-1`）、`FormList GetValidRaces()`、`SetValidRaces(FormList races)` |

CK wiki 示例里还出现 `Player.GetNthHeadPart(0).GetType()`，
说明 Actor 侧有 `GetNthHeadPart` / `SetNthHeadPart`（**该函数页未单独确认，标注为"示例引用"**）。

> **澄清**：`showracemenu` 与 `setnpcweight` 是**引擎/控制台命令**，不是 Papyrus 函数。
> 提到"chargen 的脚本接口"时，指的其实是上面这组 HeadPart Script。

## 来源

- HDPT / RACE / NPC 的字段与 `TINP` 枚举：UESP「Skyrim Mod:Mod File Format」——
  **一手（官方 wiki 原文，本节由 MediaWiki API 抓取）**
  `https://en.uesp.net/wiki/Skyrim_Mod:Mod_File_Format/HDPT`、`/RACE`、`/NPC`
- HeadPart 对象字段与 HeadPart Script：Creation Kit wiki —— **一手**
  `https://ck.uesp.net/wiki/HeadPart`、`https://ck.uesp.net/wiki/HeadPart_Script`
- FaceGen 路径与 `Ctrl+F4` 流程：Creation Kit wiki / UESP + Nexus 论坛被广泛引用的答复 —— **一手路径 + 社区流程**
- tintmask 改名技巧、F5 导出与 BaseID 命名：**社区经验（Nexus 论坛 / LoversLab）**
- `GetNthHeadPart` / `SetNthHeadPart`：**未单独确认函数页，仅见于 CK wiki 示例**
