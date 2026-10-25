---
id: wabbajack
title: Wabbajack（自动安装整合）
category: 07-workflow
kind: tool
version: 2.0.0
updated: 2026-10-25
tags: [安装, Wabbajack, 整合包, modlist]
aliases: [自动安装整合, 一键整合, 安装列表, wabbajack 是什么, wabbajack 怎么用, modlist 安装, wabbajack 限制, wabbajack 磁盘空间, wabbajack 前置, 杀软误报, wabbajack 作者, halgari, 一键安装 modlist, wabbajack 失败]
source: https://wiki.wabbajack.org/
summary: Wabbajack 是什么（作者 Halgari、与 Automaton 的渊源）、它对捏脸/身形这套复杂前置链的独特价值、四条限制，以及官方安装要点（.NET 与 VC++ 运行时、磁盘空间、位置限制、杀软误报）与决策建议。
---

# Wabbajack

> **一句话**：Wabbajack 是一个**开源的 modlist 自动安装器**——读取 `.wabbajack` 文件，
> 自动从 Nexus 等来源下载并按作者设定排序/配置，最终产出一个**自带 MO2 实例**的完整可玩环境。
> 本质是"**把别人的 MO2 配置克隆到你的机器**"，不分发版权文件。

## 速览

| 项 | 内容 |
|---|---|
| 作者 | **Halgari**（GitHub `halgari`，Patreon 同 ID；前 **Automaton** 项目开发者） |
| 性质 | 开源 **modlist 自动安装器**；产出 = 自带 MO2 实例的完整环境 |
| 许可证 | **GPL-3.0**（original code；所用库各自保留原许可证） |
| 官方站 | `https://www.wabbajack.org/` |
| 官方文档 | `https://wiki.wabbajack.org/`（wiki 源码仓库 `wabbajack-tools/wiki`） |
| 源码仓库 | `https://github.com/halgari/wabbajack` |
| 支持游戏 | Skyrim LE / SE、Fallout 3 / NV / 4 等（官方 README 与 Patreon 页） |
| 硬性前置 | **.NET 8 Desktop Runtime** + **VC++ 2019 Runtime**（官方 troubleshooting FAQ） |
| 磁盘前提 | 除 modlist 本身外**另备 40-60GB** 空闲空间（官方 troubleshooting FAQ） |
| 维护状态 | 活跃；代码签名证书与构建服务器由 Patreon 支持 |

要点：

- **它不分发任何版权文件**：官方 FAQ 原话式的设计是"给定一个 MO2 文件夹与 profile，
  生成一组指令，让程序在另一台机器上复现其内容"——是**复刻，不是同步，也不是分发**。
- **modlist 必须免费**：官方 FAQ 明令禁止对 `.wabbajack` 安装器收费、paywall、
  "付费抢先"等任何等价结构（Wabbajack 团队保留软件层面禁止付费列表安装的权利）。
- **对捏脸/身形的独特价值**：它把新手最容易翻车的那几步（BodySlide 构建、FaceGen 对齐、
  版本锁定、物理配置）全部预制——见下文。
- **四条限制**与官方安装要点是安装前必读，见下文两节。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| 未确认 | Wabbajack 的确切首发日期（GitHub 仓库早期历史本轮未逐条核实） | —— |
| 作者自述 | Halgari **曾是 Automaton 的开发者**，因"开发速度太慢、想要完全重写"而独立做出 Wabbajack（重写还带来了 BSA 打包等特性） | 官方 FAQ 对"How does Wabbajack differ from Automaton?"的回答——**一手（作者原话）** |
| 2019 前后 | 社区讨论帖已列出其完整能力：支持 LE/SE/F4/FNV，来源含 Nexus / Dropbox / Google Drive / Mega / ModDB / 直链，归档格式 `.zip`/`.7z`/`.rar` | 早期形态已与今天一致（**社区经验，2019 年论坛帖**） |
| 2020 之后 | Wabbajack 成为 Skyrim 大型 modlist 的**事实标准分发方式** | "网盘整合包"逐步被"可验证的指令清单"取代（社区经验） |
| 现状 | 官方站 + Gallery + Discord + Patreon（维持代码签名证书与构建服务器） | 仍是活跃项目；许可纪律（免费）由团队主动执行 |

### 它从哪来

动机在官方 FAQ 里写得很直白：Halgari 当时在开发 **Automaton**（同类工具），
觉得进展太慢，认定"完全重写能实现一些很不错的特性（比如 BSA 打包）"，
于是**先让东西能跑、再让它好看**（"make it work, then make it pretty"）。
这句话也解释了 Wabbajack 此后的形态：功能极其完整，UI 被作者自嘲"不够专业"。

### 中间经历了什么

最大的环境变化不是工具本身，而是**生态对它的吸收**：MO2 成为事实标准 →
Wabbajack 以"MO2 文件夹 + profile → 指令清单"为设计前提 → 列表作者把
BodySlide 构建、MCM 配置、INI 调整全部固化进安装流程 → 用户侧"装 mod"
这件事被压缩成"选列表、点安装、读 README"。

第二个变化是**来源协议的丰富**：从 Nexus API 扩展到 Google Drive / Mega / Dropbox /
ModDB / 直链（官方 meta files 文档列出全部可下载站点），非 Nexus 资源也能进列表。

### 现状

活跃维护中。截至 2026-10-25，本库未核实其"最新版本号"与发布节奏——
版本信息以 GitHub Releases 与官方站为准（**未确认项，见来源节**）。

## 它解决什么问题

**没有它之前**，分享一套调好的环境只有两条路，两条都烂：

| 旧方式 | 烂在哪 |
|---|---|
| 网盘整合包 | 分发版权文件（违规）、体积巨大、来源不可验证、版本冻结即报废 |
| 文字教程 | 步骤随上游版本过期；读者环境稍有不同就走样；排错全靠读者自己 |

**它的解法**是"指令清单复刻"：`.wabbajack` 文件记录每个 mod 的来源、版本、安装方式、
目标 mod 文件夹、排序位置与配置改动，安装时逐条执行。**版权文件始终从官方来源下载**，
作者只是分享了"怎么装"。

### 对捏脸/身形的独特价值

这正是新手最容易翻车的地方 —— 而 Wabbajack 列表**通常已经把这些做完了**：

| 新手最容易错的 | Wabbajack 列表通常已处理 |
|---|---|
| BodySlide 身形与服装没构建 | **已构建** |
| 骨骼 / SKSE 版本不对 | **已锁定** |
| NPC 美化的 FaceGen 没对齐 | **已对齐** |
| 物理 XML 冲突 | **已配好** |
| 身形与皮肤不同族 | **已匹配** |

所以"我只想好好地玩一个有捏脸有身形的游戏"，Wabbajack 是**最省事的路径**。
它替你守住的正是 [`install-order.md`](install-order.md) 里那 14 步的全部覆盖关系
与 [`mo2-override-rules.md`](mo2-override-rules.md) 里两栏一致性的全部细节。

## 工作原理（它包含什么）

### 一个 `.wabbajack` 文件里有什么

- **manifest**：安装开始前用户即可查看的清单，含每个 mod 的标题、作者、版本、大小、链接等元数据；
- **来源指令**：从 Nexus（官方 API）、Google Drive、Mega、Dropbox、ModDB、直链等下载；
- **安装指令**：FOMOD 选项、重命名/删除/移动的文件、多 mod 合入同一文件夹等处理；
- **排序与配置**：产出 MO2 实例内的 mod 顺序与 profile。

### 安装时你会看到什么

安装过程可能从几分钟到几小时（取决于列表大小、网速与硬件）；
期间播放的 **Slideshow** 会随机展示列表内各 mod 的标题、作者、图片、版本与 Nexus 链接——
这也是"**你装的到底都有什么**"的第一手答案。

### 两条安装路径（官方文档）

1. **Gallery 路径**：打开 Wabbajack → 进 Gallery → 选列表 → 点下载（等 `.wabbajack` 文件下载完）→
   点播放按钮 → 读该列表的 README → 下载第三方/外部文件 → 选路径 → 等待 → 完成 README 里的收尾步骤。
2. **本地文件路径**：`install from disk` → 选 `.wabbajack` 文件 → 之后的步骤与上面相同。

> **每个列表都有自己的 README**，官方文档的原话是"想装成功就该读"。

## 安装

### 前置（官方 troubleshooting FAQ，一手）

报 `texconv` 相关错误 = 缺运行时，装齐这两样再重启电脑：

```
Microsoft Windows Desktop Runtime .NET 8
https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-8.0.4-windows-x64-installer

Microsoft Visual C++ 2019 Runtime
https://aka.ms/vs/16/release/vc_redist.x64.exe
```

### 磁盘空间（官方 troubleshooting FAQ，一手）

> "这个错误通常出现在磁盘空闲空间不足时。装之前确保有足够空间；
> 此外你应该**另有 40-60GB 可用**，否则可能遇到其它问题。"

hash 不匹配（`menYUTfbRu8=` 那类报错）的第一嫌疑人就是**空间不足**，不是文件损坏。

### 安装位置限制（官方文档，一手）

| 路径 | 限制 |
|---|---|
| **Installation Location**（安装位置） | 不能是 Wabbajack 自身位置 · 不能是游戏位置 · 不能与另一个列表共用（**列表不能合并**）· **不能在 Windows 受保护目录** |
| **Download Location**（下载缓存） | 可与其它列表的 downloads 文件夹共用（避免重复下载）；若打算自制并分享列表则**别合并**（Wabbajack 无法区分哪些归档是它需要的） |

Windows 受保护目录清单（官方列举）：

```
C:\Windows
C:\Users\<用户名>\Documents
C:\Users\<用户名>\Images
C:\Users\<用户名>\Videos
C:\Users\<用户名>\OneDrive
C:\Program Files
C:\Program Files (x86)
```

官方原话式建议：**游戏、Wabbajack、modlist 与下载缓存都不要放在上述任何目录里。**

### 步骤与每步验证

1. **确认游戏为对应商店正版、且有所需 DLC**（多数 Skyrim 列表要求 AE 升级 DLC；官方文档与列表 README 为准）。
   验证点：Wabbajack 能自动识别游戏文件夹；识别不了先重启电脑再试。
2. **装好 .NET 8 与 VC++ 2019 运行时**（见上）。验证点：Wabbajack 能正常启动、不报 texconv。
3. **下载目标列表的 `.wabbajack` 文件**（Gallery 内或列表作者给的链接）。
4. **读列表 README**，把其中要求的**第三方/外部文件先下好**。验证点：README 里点名要的文件都在 downloads 文件夹里。
5. **选路径**（遵守上表的位置限制）。验证点：安装位置是**全新空目录**，不与任何既有列表共用。
6. **点安装，等待**。失败**先原样重跑**——支持断点续传，不会丢进度（社区经验，多个列表 wiki 一致）。
   验证点：安装结束无报错；Slideshow 放完。
7. **回到 README**（装完会自动打开），完成其中所有收尾步骤（MCM 配置、INI、启动器等）。
8. **首次启动**：用列表自带的 MO2 + 对应的 SKSE 启动方式进入游戏。
   验证点：能进主菜单、能新开游戏、捏脸界面是列表配置的样子（RaceMenu 而非原版菜单）。

### 杀软误报（社区经验）

- 已知误报：**Windows Defender 自动隔离 MO2 的 `usvfs_proxy_x86.exe`**，
  **MO2 开发者已确认是误报**；解法是给 MO2 文件夹加例外（多个列表 wiki 记录一致）。
- 更一般的规律（modlist 作者长期总结）：**给 Wabbajack 文件夹与 modlist 安装目录加例外**；
  过期/不用的杀软**卸载**而不仅是关闭（驻留的也会 interference）；
  装完仍出现怪症状时，临时关闭实时防护重装一次做对照。
- Webroot / Bitdefender / McAfee / Norton / Avast 等各有具体症状与解法
  （详见来源中的 FG's Modlists 专页）。**判据**：安装或游戏出现"文件自己消失"、
  `skse64_loader.exe does not exist`、hash 不匹配、启动即崩，先怀疑杀软再怀疑列表。

## 使用与配置

- **装完先读 README**：MCM 该开什么、INI 该改什么、用什么启动器，列表作者都写好了。
  官方 FAQ 也点名：需要大量配置的 mod 通常会被写进列表的 instructions。
- **加自己的 mod 之前先学 MO2**：封闭实例里叠加自有内容极易冲突，
  而列表更新会清掉列表外添加的 mod——**先读 [`mo2-override-rules.md`](mo2-override-rules.md)**。
- **想改身形/皮肤**：确认列表用的身形家族（3BA / BHUNP / HIMBO），
  加同族资源；换家族等于重做构建层，见 [`install-order.md`](install-order.md)。
- **备份 profile**：动结构之前备份，回滚成本最低。

## 兼容与冲突：四条限制（与捏脸相关）

1. **版本极度敏感** —— 很多列表要求特定游戏版本（1.5.97 或 1.6.640 等），
   Steam 自动更新会破坏它；
2. **封闭实例** —— 装完是"成品"，个性化魔改需要 MO2 知识；
   叠加自己的身形/服装**极易冲突**；
3. **无 Nexus Premium 时下载极慢**（被限速）；
4. **列表更新会删除列表外自行添加的 mod**。

> 还有一条常被忘的**软限制**：列表把"版本决策"替你做了——
> 2026-10 的当下，人物向列表多数锁在 **1.6.1170** 而非 1.7.x
> （RaceMenu 在 1.7.x 下不可用，见 [`../02-face/racemenu.md`](../02-face/racemenu.md)
> 与 [`../00-overview/game-version-1-7-x.md`](../00-overview/game-version-1-7-x.md)）。
> 升级游戏版本前，先确认你的列表支持。

## 排错

| 症状 | 判据（看到 X 说明是 Y） | 处理 |
|---|---|---|
| 报 `texconv` 错误 | 缺 .NET 8 Desktop Runtime 或 VC++ 2019 Runtime | 装齐两个运行时，重启，重装列表（官方 FAQ） |
| hash 不匹配（`menYUTfbRu8=`） | **磁盘空间不足**（第一位嫌疑人） | 清理出列表体积 + 额外 40-60GB；重跑 |
| `Could not download x` | 上游 mod 更新后旧文件被删 | 等列表作者更新（社区经验） |
| `x is not a whitelisted download` | 列表更新后校验源变化 | 等列表更新（社区经验） |
| 找不到游戏文件夹 | 游戏未正确安装 / Wabbajack 运行中装的游戏 / 非正版 | 重启电脑；确认正版与安装顺序（社区经验） |
| 文件装完"自己消失"、启动即崩 | 杀软干扰（隔离/实时扫描） | 加例外或临时关防护，重装覆盖同一目录（社区经验） |
| `Unable to download openvr_api.dll` | 游戏文件缺失 | Steam 校验游戏文件完整性后重跑（社区经验） |
| 装成功但进游戏各种怪症状 | 同上，杀软事后干扰 | 关闭实时防护做对照测试 |

## 取舍与建议

| 你的目标 | 建议 |
|---|---|
| 想尽快玩到"好看的捏脸 + 身形" | 用 Wabbajack |
| 想自己决定每一个 mod | 手动装（从 [`install-order.md`](install-order.md) 开始） |
| 想用别人的底子再自己加 | 可以，但**先学会 MO2 覆盖规则**，见 [`mo2-override-rules.md`](mo2-override-rules.md) |

- **即使走 Wabbajack，排错能力仍是必需品**：列表替你装，不替你排查
  （本库 [`../06-troubleshooting/`](../06-troubleshooting/) 的七篇症状条目全部适用）。
- **把"读 README"当成安装的一部分**：官方文档明确说它是成功安装的条件，不是可选阅读。
- **中文用户对照读** [`chinese-modpacks.md`](chinese-modpacks.md)：Wabbajack 列表的
  可验证性远高于论坛网盘整合包——这是选择它的核心理由之一。

## 来源

**一手**

- Wabbajack 官方站（"automated modlist installer"、三步流程、平台要求 Windows 10/11）：
  `https://www.wabbajack.org/`
- Wabbajack 官方 wiki 首页 FAQ（**作者 Halgari 自述与 Automaton 的渊源**、
  "modlist 必须免费/禁止 paywall"的许可纪律、Nexus API 下载机制、manifest 与 Slideshow、
  GPL-3 许可）：`https://wiki.wabbajack.org/`
- 官方 wiki **Installing a Modlist**（两条安装路径、位置限制与受保护目录清单、
  "列表不能合并"、downloads 目录共用规则、安装时长与 Slideshow）：
  `https://wiki.wabbajack.org/user_documentation/Installing%20a%20Modlist.html`
- 官方 wiki **Troubleshooting FAQ**（**texconv 错误 = 缺 .NET 8 Desktop Runtime +
  VC++ 2019 Runtime**；**hash 不匹配 = 空间不足、另备 40-60GB**）：
  `https://wiki.wabbajack.org/user_documentation/Troubleshooting%20FAQ.html`
- GitHub `halgari/wabbajack`（源码、GPL-3、FAQ）：`https://github.com/halgari/wabbajack`
- Patreon `halgari`（"给定 MO2 文件夹与 profile 生成指令、复刻而非同步/分发"的设计描述）：
  `https://www.patreon.com/u11907933/about`

**社区经验**

- "失败先重跑、断点续传不丢进度"与 `Could not download x` / `not a whitelisted download` /
  `openvr_api.dll` / 盗版找不到游戏文件夹 等报错处理：FUS 等列表的 Wabbajack Troubleshooting wiki
  （多个列表 wiki 一致）：`https://github.com/Kvitekvist/FUS/wiki/Wabbajack-Troubleshooting`
- **杀软误报与各杀软的具体症状**（Defender 隔离 `usvfs_proxy_x86.exe`、MO2 开发者确认误报；
  Webroot / Bitdefender / McAfee / Norton / Avast / Malwarebytes 各自表现）：
  FG's Modlists 杀软专页 + 各列表 wiki（多来源一致）：
  `https://fgsmodlists.com/news-articles/antivirus-troubleshooting`
- "无 Premium 限速""版本极度敏感""封闭实例"：社区长期使用结论（多帖一致）

**未确认**

- **Wabbajack 的确切首发日期与最新版本号**（GitHub 早期历史未逐条核实，以 Releases 页为准）
- **"多数 Skyrim 列表锁 1.6.1170"**：为本库基于 RaceMenu 1.7.x 现状的推断，
  具体列表的版本要求以其 README 为准
- **官方 wiki 中是否有独立的"System Requirements"专页**（本轮检索未定位到，
  .NET/VC++/空间要求引自 Troubleshooting FAQ）
