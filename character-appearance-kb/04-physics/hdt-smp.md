---
id: hdt-smp
title: HDT-SMP（Skinned Mesh Physics）
category: 04-physics
kind: tool
version: 2.0.0
updated: 2026-10-25
tags: [物理, HDT-SMP, SMP, Bullet, XML]
aliases: [hdt smp, skinned mesh physics, hdt, 物理引擎, hdtSkinnedMeshConfigs, hdt-smp 是什么, hdt smp 历史, hydrogensayshdt, 原版 smp, smp xml, hdt-pe 继任者, smp 原理]
source: https://github.com/HydrogensaysHDT/hdt-skyrimse-mods
summary: HDT-SMP 百科全书：原作者 hydrogensaysHDT 与 MIT 源码、作为 HDT-PE 继任者的定位、Bullet + 蒙皮网格逐顶点的原理、XML 配置方式（hdtSkinnedMeshConfigs）、官方 changelog 要点、只对 XPMSE human 骨骼生效的设计，以及与现代 fork FSMP 的分工。
---

# HDT-SMP（Skinned Mesh Physics）

> **一句话**：HDT-SMP 是"头发与衣物物理"的奠基引擎——用 Bullet 物理库对蒙皮网格
> 逐顶点求解；原作者已淡出，现代用户实际安装的是它的维护 fork
> [FSMP](faster-hdt-smp.md)，但理解配置方式与机制仍以本页为准。

- 原作者 **hydrogensaysHDT**（社区昵称"氫姐"），已淡出模改，以 **MIT** 释出源码；
  现 Nexus 上传为**社区修复合并 fork**（credits：hydrogensaysHDT 原作者，
  **ousnius** 修复与更新）。
- Nexus：`https://www.nexusmods.com/skyrimspecialedition/mods/30872`
- **HDT-PE（HDT Physics Extensions）的继任者**。

## 速览

| 项 | 内容 |
|---|---|
| 作者 / 现状 | hydrogensaysHDT（原创，已淡出，MIT 释出源码）；现为社区 fork 上传（ousnius 修复与更新） |
| Nexus | **30872** |
| 许可证 | **MIT**（源码） |
| 定位 | **HDT-PE 的继任者**；头发/衣物物理的奠基引擎 |
| 原理 | **Bullet** 物理库 + **蒙皮网格逐顶点**（skinned mesh physics）+ 碰撞体/代理体 |
| 配置 | `Data/SKSE/Plugins/hdtSkinnedMeshConfigs/*.xml`（每个使用物理的 mod 一个） |
| 前置 | SKSE64；早期需 **OpenCL 2.0**（可切 CPU 模拟）；**XPMSE**（硬挂点依赖） |
| 支持版本 | 原版主要支持 **LE 与 SE 1.5.97**；AE（1.6.x）由社区 fork 承接 |
| 维护状态 | 原创停更；现代主线是 [FSMP](faster-hdt-smp.md)（官方口径"完全取代原版"） |

要点：

- **SMP = Skinned Mesh Physics（蒙皮网格物理）**：模拟对象是网格顶点，不是骨骼。
- 相比 HDT-PE 的骨骼级方案，SMP **能做到头发与身体/地面的碰撞**——这是精度跃升。
- **"某件衣服没物理"通常不是引擎问题，而是它没带或没加载 XML**（见「使用与配置」）。
- ⚠️ 常见错误仓库名 `hydrogensaysHDT/hdt-skyrim-smp`（实测 404）；正确的是
  **`hdt-skyrimse-mods`**。
- **不要与原版和 FSMP 混装**：FSMP 官方描述明确 "replaces it totally. Do not install [原版]"。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| LE 中期（具体日期未确认） | hydrogensaysHDT 发布 **HDT-PE**（Nexus LE 53996） | 第一代实时物理：给游戏内建 Havok 加胸/臀等物理物件 |
| 2015 前后 | HDT-SMP 早期测试版流传，社区描述为 "mesh/bullet based physics / collision is baked-in / no havok object management necessary" | 技术路线定型：自带 Bullet、逐顶点、不再管 Havok 物件 |
| 2016-2018 | SMP 逐步支持 SE；`hdtSkinnedMeshConfigs` XML 体系成为 modder 标准 | 物理配置可随 mod 分发，生态起步 |
| 2018-2019 | hydrogensaysHDT 淡出模改，以 **MIT** 释出源码 | 项目转入社区维护；后续 fork 链的起点 |
| 2019-2020 | **aers**（修复与改进）→ **Karonar1**（系统修 bug）fork 链 | 修复积累期 |
| 2021-10 起 | **DaymareOn** 的 [FSMP](faster-hdt-smp.md)（Nexus 57339）成为主线 | 多线程 + ImGui 菜单；官方口径取代原版 |
| 2026 | FSMP 4.1.1；原版页面仍以社区合并 fork 形式存在 | 原版仅作历史与配置格式参考 |

### 它从哪来

hydrogensaysHDT 先做了 HDT-PE：不动引擎架构，给游戏内建 Havok 挂物理物件。
这解决了"从无到有"，但骨骼级方案精度有限，且动画师/用户仍受 Havok 物件管理限制。
SMP 换掉整个技术底座：**自带 Bullet 物理库，直接对蒙皮网格的顶点求解**——
碰撞可以烘焙进网格，不需要 Havok 物件管理。BHUNP 作者的科普博客概括这一差异：
"HDT-SMP allows physics way more realistic, natural compared to HDT-PE"。

### 中间经历了什么

关键是**开源与 fork**：作者淡出前以 MIT 释出源码，使得 aers → Karonar1 →
DaymareOn 的修复链成为可能。Nexus 30872 页面现在上传的是社区修复合并版
（credits 保留 hydrogensaysHDT 原作者、ousnius 修复与更新）。

### 现状

原版停在 LE 与 SE 1.5.97；**AE（1.6.x）与当代 SE 的实际用户都用 FSMP**。
本页仍然重要，因为：**全部物理 mod 的 XML 配置格式源自这一版**，
FSMP 只是换了引擎实现与全局配置层（JSON），逐物品 XML 仍按 SMP 规范写。

## 它解决什么问题

**没有它之前**（HDT-PE 时代及更早）：

- 物理是**骨骼级**的：胸/臀整体摆动，细节粗糙；
- 动画师要为每套动画手搓 BBP/TBBP 抖动（hydrogensaysHDT 做 PE 的动机之一就是
  把动画师从这项劳动里解放出来）；
- 头发、斗篷这类"网格级形变"几乎没有实时方案。

**SMP 的解法**：

1. **逐顶点蒙皮模拟**：网格的每个顶点都是 Bullet 里的粒子，受碰撞体/代理体约束；
2. **真碰撞**：头发可以撞到身体、斗篷可以垂到地面——PE 时代做不到；
3. **配置随 mod 分发**：每个物理物品自带 XML，装上加物理，卸了即消失，不动引擎。

## 工作原理（它包含什么）

```
一个物理发型（.nif，蒙皮网格，挂在 XPMSE 头部节点下）
  + 一个配置文件（Data/SKSE/Plugins/hdtSkinnedMeshConfigs/<mod>.xml）
      ├─ 把碰撞体（sphere / capsule / triangle）挂到指定骨骼
      ├─ 定义顶点权重/约束（哪些顶点跟哪些骨、多硬）
      └─ 重力、阻尼、风力等参数
  = FSMP/HDT-SMP 每帧用 Bullet 求解 → 顶点位移 → 游戏渲染
```

- 引擎本体：`hdtSMP64.dll`（SKSE 插件）；
- **碰撞体/代理体（collision proxies）**：定义在 XML 里，可挂骨骼或随网格；
- 全局默认身体配置通常叫 **`defaultBBPs.xml`**（或 `configs.xml`）——
  这也是 SMP 与 CBPC "分腔"时要编辑的文件（见 [physics-overview.md](physics-overview.md)）。

## 安装

### 前置

- **SKSE64**（版本与游戏匹配，见 [skse64.md](../01-prerequisites/skse64.md)）；
- **XPMSE**：SMP 只把网格附加到 XPMSE 的 human skeleton（见 [xpmse-skeleton.md](xpmse-skeleton.md)）；
- 早期版本需 **OpenCL 2.0**（GPU 计算）——注意所谓"关闭 OpenCL"实际上是
  **切到 CPU 模拟**，不是完全关掉物理计算；现代 fork 已不强制。

### 步骤与验证点

1. 装 SKSE64 + XPMSE（FOMOD 选 Physics Extensions）。
   - 验证点：XPMSE 骨架在位，`skeleton_female.hkx` 未删。
2. 装 HDT-SMP 主文件（**SE 1.5.97 用户**；AE/新 SE 用户请装
   [FSMP](faster-hdt-smp.md) 并跳过本步）。
   - 验证点：`Data\SKSE\Plugins\hdtSMP64.dll` 存在。
3. 装带物理的衣物/发型（每个都应自带 `hdtSkinnedMeshConfigs` 下的 XML）。
   - 验证点：`Data\SKSE\Plugins\hdtSkinnedMeshConfigs\` 下出现对应 XML。
4. 进游戏看效果；不抖/穿模按
   [physics-not-working.md](../06-troubleshooting/physics-not-working.md) 排，
   先跑 `smp report`。

> ⚠️ **原版与 FSMP 不要同时安装**（同名 dll 互相覆盖，且官方明确取代关系）。

### 怎么认出你装的是哪一代 SMP

原版与 FSMP 的 dll 同名（`hdtSMP64.dll`），靠以下特征区分：

| 特征 | 原版 HDT-SMP | FSMP（4.x） |
|---|---|---|
| 配置菜单 | SkyUI MCM（需 SkyUI/JContainers/PapyrusUtil/ConsoleUtil） | DLL 内置 **ImGui** 菜单（SKSE Menu Framework） |
| 全局配置文件 | `configs.xml` | **`configs.json` / `userConfigs.json`** |
| 控制台命令 | 少（`smp reset` 等） | `smp detail` / `dumptree` / `list` / `report` / `reset` |
| 支持的游戏版本 | LE、SE 1.5.97 | SE 1.5.97 ~ AE 1.6.1170、GOG、VR 全档位 |

> 看到 `configs.json` 和 ImGui 菜单 = 装的是 FSMP；看到 MCM 里的旧样式面板 =
> 可能是原版或早期 fork。选错版本的典型后果是物理不生效或开局崩溃。

## 官方 changelog 要点

自 hydrogensaysHDT 最后一版起，社区维护版的 changelog 记录（Nexus Files 页）：

- 支持 **`.` 与 `,` 两种小数点**（地区格式兼容）；
- **正确移除骨骼不在场景中的护甲**（解决护甲残留/鬼畜问题）；
- **暂停时写入变换**；
- **读盘时重置系统**；
- 更好的暂停判定；
- **旋转钳制（rotation limits）选项**；
- **只对 XPMSE "human" 骨骼生效**——修 Lurker 骨骼被物理破坏的问题。

> 最后一条同时是设计约束：SMP 的模拟对象**仅限人类骨架（XPMSE human skeleton）**，
> 非人种族不受影响，这也是"必须装 XPMSE"的根本原因。

## 使用与配置

### 配置目录与文件

```
Data/SKSE/Plugins/hdtSkinnedMeshConfigs/
  ├─ <某物理发型mod>.xml      ← 每个使用物理的 mod 一个
  └─ defaultBBPs.xml          ← 身体默认配置（与 CBPC 分腔时改它）
```

XML 的作用是**把碰撞体（sphere / capsule / triangle）挂到骨骼上**并定义顶点约束。
因此：

> **"某个衣服/发型没物理"的第一嫌疑不是引擎，而是它没带 XML、XML 没被加载、
> 或被其他 mod 覆盖。** 排查用 `smp report`（见 [FSMP](faster-hdt-smp.md) 条目）。

- modder 侧：遵循官方 **SMP Modder Guide** 的 XSD/Schematron schema 写 XML；
- 玩家侧：一般不需要手写 XML；改 `defaultBBPs.xml` 只发生在"SMP/CBPC 分腔"场景。

## 兼容与冲突

| 关系 | 结论 |
|---|---|
| 与 XPMSE | **硬依赖**；只附加 human skeleton |
| 与 CBPC | 争同一批骨骼；共存须分腔（[physics-overview.md](physics-overview.md)） |
| 与原版 HDT-SMP | 不要与 FSMP 混装（同名 dll） |
| 与 AE 1.6.x | 原版不支持；用 FSMP |
| 与 OpenCL | 早期版本需 OpenCL 2.0；"关 OpenCL"实为切 CPU |
| 与非人种族 | 设计上不生效（只认 human 骨骼），这是特性不是 bug |

## 排错

| 症状 | 判据 | 处理 |
|---|---|---|
| 某件衣服/发型完全不飘 | 它没有 XML，或 XML 没加载 | 确认 `hdtSkinnedMeshConfigs` 有对应文件；跑 `smp report` |
| 全部物理不动 | SKSE 版本不匹配 / 没装 XPMSE / dll 被覆盖 | 查 SKSE-游戏版本对；查覆盖（[mo2-override-rules.md](../07-workflow/mo2-override-rules.md)） |
| 开局 CTD | 版本档选错（AE 用户装了原版档） | 改装 FSMP 并选对版本档 |
| CPU 占用爆炸 | 原版单线程 + 高精度网格 | 换 FSMP；用 Performance 预设压档 |
| 某护甲在 NPC 身上鬼畜/残留 | 旧版的"骨骼不在场景中不移除护甲"问题 | 升级到含该修复的社区版 |
| Lurker 等非人生物骨架被物理破坏 | 低于"只对 human 骨骼生效"的版本 | 升级 |

## 取舍与建议

- **装 SMP 就是为了头发/衣物**：身体部位交给 [CBPC](cbpc.md) 更省 CPU
  （见 [physics-overview.md](physics-overview.md) 的选型）；
- **版本选择**：SE 1.5.97 可用原版；**其余一律 FSMP**；
- **不要手撕 XML** 除非在做分腔配置或修特定物品；玩家级问题先用 `smp report` 定位；
- **想深究机制**：源码在 `github.com/HydrogensaysHDT/hdt-skyrimse-mods`（MIT），
  FSMP 在 `github.com/DaymareOn/hdtSMP64`。

## 来源

- **作者 hydrogensaysHDT、MIT 释出源码、现为社区修复合并 fork（ousnius 修复与更新）、
  HDT-PE 继任者定位、SMP=Skinned Mesh Physics、Bullet + 蒙皮网格逐顶点、
  XML 目录 `hdtSkinnedMeshConfigs` 与 `defaultBBPs.xml`、只附加 XPMSE human skeleton
  （修 Lurker）、changelog 全部要点（两种小数点 / 移除不在场景护甲 / 暂停写变换 /
  读盘重置 / 旋转钳制）**：HDT-SMP Nexus 30872 发布页与 GitHub 仓库 —— **一手**
  `https://www.nexusmods.com/skyrimspecialedition/mods/30872`
  `https://github.com/HydrogensaysHDT/hdt-skyrimse-mods`
- **"正确仓库名是 hdt-skyrimse-mods，hdt-skyrim-smp 返回 404"**：
  **本工作区实测（2026-09-22）**
- **OpenCL 2.0 与"关 OpenCL 实为切 CPU"**：Nexus 描述与社区指南 —— **一手 + 社区经验**
- **HDT-PE = HDT Physics Extension（Nexus LE 53996）、用游戏内建 Havok、
  PE 时代动画师须手搓胸臀动画、SMP 比 PE 更自然**：BHUNP 作者 Bakafactory 科普
  博客（2019-10）—— **一手（作者博客）**
  `https://babofactory.blogspot.com/2019/10/what-is-hdt-pe-hdt-smp-bbp-tbbp-3bbb.html`
- **SMP 早期 "mesh/bullet based / collision baked-in / no havok object management"**：
  LoversLab 2015 年测试帖（crusher）—— **社区经验（早期用户实测）**
- **支持 LE 与 SE 1.5.97、AE 靠 fork**：**社区经验（多源一致）**
