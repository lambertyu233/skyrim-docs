---
id: version-and-support
title: 版本与支持策略
category: 00-overview
version: 1.0.0
updated: 2026-09-21
tags: [概览, 版本, 支持, VR, Linux, 更新]
source: https://www.nexusmods.com/skyrimspecialedition/mods/86492
summary: 官方构建政策、支持的游戏版本、VR / Linux 现状、功能并入核心的时间线，以及该找谁求助。
---

# 版本与支持策略

这一页回答「我该装哪个版本、我的环境受不受支持、出了问题谁能管」。这些规则很硬，踩错通常直接表现为「没人理你」。

## 版本号现状（截至 2026-09）

| 渠道 | 版本 | 说明 |
|------|------|------|
| **Nexus 发布页** | 稳定正式版（1.8.x 系列，最新补丁 1.8.4 于 2026-08-26） | **唯一受支持**的玩家版本。想稳定就用它 |
| GitHub Releases | `1.9.0-prXXXX` 形式的 PR 构建（2026-09 仍在迭代，最新一批 2026-09-20） | 开发构建，**只**在 Discord 对应线程受支持 |
| Discord 的 Jiaye / post-processing 构建 | 非官方 | 见下 |

> 判断自己装的是哪版：游戏内按 **END** 打开 CS 菜单，版本号在界面上直接可见。

### 关于「开发构建」

- 官方明确定义：**只有官方构建受支持**；第三方构建与分叉（fork）不受支持；开发构建只在 Discord 对应线程里受支持。
- **Jiaye / post-processing 构建**：官方 FAQ 专门澄清过——**这不是官方 CS 产品**，未经 CS 开发团队审核，也**不以性能为目标**。除了 `#jiaye` 前缀的频道，别处问会被请回去；发不出帖说明你得进那个「下载构建的帖子」里说话。
- 想要设置预设（Presets）：官方 Vanilla 设置指南说明，预设目前**只在实验构建**里可用，在官方 Discord 获取。

### 官方一键安装：Vortex Collection

Vortex 用户可以直接用官方 **Community Shaders Collection**（Nexus Collections 编号 `62eesj`）一键装齐 CS 与全部附加特性。**用了合集就整体更新**，不要单独去更新其中某一个特性——两边版本错开会直接导致着色器编译失败。

## 支持的游戏版本（硬性）

| 版本 | 是否支持 |
|------|---------|
| Skyrim SE/AE **1.6.1170**（Steam） | ✅ 支持 |
| Skyrim AE **1.6.1179**（GOG） | ✅ 支持 |
| Skyrim SE **1.5.97** | ✅ 长期支持（唯一保留的旧版本） |
| LE（传奇版） | ❌ 不支持 |
| VR | ❌ 主版本已停止支持，见下 |
| 其它 AE 版本，如 **1.6.640、1.7.99、1.7.104** | ❌ 不支持 |
| Steam 刚推送的新版本 | ⏳ 团队会跟进，但需等待 |

官方立场：**只计划支持 Steam 最新版与 1.5.97**。除 1.5.97 之外，**对旧版本没有任何长期支持（LTS）承诺**。

- 游戏刚更新导致 CS 不能用时，官方 FAQ 给的办法是**降级游戏版本**（用 downgrader），并把 `appmanifest_489830.acf` 设为只读来锁版本；恢复更新则取消只读 + 校验文件。
- 降级后别忘了同步更新 **CommonLibSSE / Address Library / Engine Fixes**，否则会报 Address Library 相关错误。

## VR：已停止支持

**CS 主版本不再支持 VR。** 想要在 VR 里用 CS（或继续 VR 方向的开发），请转投社区分支 **Open Shaders**。

> 这也是为什么 [功能对照矩阵](feature-matrix.md) 里会单独有一列 `CS VR`——历史与分支的差异仍然记录着。

## Linux：不官方支持，但有活跃社区

- 开发团队**不官方支持 Linux**（安装问题请找社区）。
- 官方指路的发行版/管理器：**Fluorine**（`SulfurNitride/Fluorine-Manager`）。官方 FAQ 在多处（安装、排错）都指向它。
- Nexus 页面另提到 Linux 用户可跟随 `SulfurNitride/NaK` 指南。

## 功能并入核心的时间线

CS 会把成熟的附加特性**收进基础安装（Core）**。这带来一个高频事故：**升级 CS 后没删掉那个已并入核心的附加 MOD → 文件互相覆盖 → 着色器编译失败**。所以升级时务必对照下表清理。

| 纳入版本 | 并入核心的功能 |
|---------|--------------|
| **1.0+** | Dynamic Cubemaps、Complex Parallax Materials、Water Parallax、Tree LOD Lighting |
| **1.4+** | Light Limit Fix、Frame Generation |
| **1.4.7+** | Terrain Shadows、Inverse Square Lighting、Water Effects、Interior Sun、Extended Translucency |
| **1.5.0+** | Screenspace Shadows、Grass Collision、Grass Lighting、Subsurface Scattering |
| **1.7.0+** | Sky Sync |
| **1.8.0+** | Cloud Shadows |

> 完整的「达到某版本必须移除哪些 MOD」清单（含更早的并入项）见 [不兼容 MOD - 版本演进](../03-reference/incompatible-mods.md)。

## 官方团队与常驻贡献者

CS 是纯社区项目（GPL-3.0，永不闭源）。以下名字散见于各功能页的 Contributors，便于你知道「这项功能是谁做的、该找谁」：

- **核心 / 维护**：doodlum（创建者、主要负责人、仓库维护）、Nukem（原版着色器与渲染管线逆向）、aers（逆向与引擎修复）、Jonahex（TruePBR、逆向、最早的分片缓存）
- **主要贡献**：alandtse（VR 支持、后端系统）、FlayaN（UI、VR）、ProfJack（TruePBR glints、云影、地形阴影、优化）、hakasapl（PGPatcher、Terrain Helper）、sicsix（平方反比光照、天空同步）、jiaye（动态立方体贴图、次表面散射、水体）、davo0411（水体、UI、Nexus 页维护）、SkrubbySkrubInAShrub（UI 与修复）、ffarrell17 / Dlizzio / Bottle / soda（UI）、RealExist（优化）、Ersh、Maxsu、powerofthree、sheson（xLODGen）
- **外部/前置作者**：sheson（DynDOLOD / xLODGen）、powerofthree（CommonLibSSE）、mindflux / rudy102 / fadingsignal（粒子光照资料）

> 上表依据官方 wiki 各功能页署名整理，非完整名单；权威名单见 Nexus 发布页的 Credits。

## 出问题该找谁

1. 先读 [FAQ](../03-reference/faq.md) 与 [常见坑](../06-community/common-pitfalls.md)。
2. 再不行 → **官方 Discord**（实时求助、功能预览、测试反馈都在这里）。
3. 确认是 bug → 才去 GitHub 开 Issue（功能请求请走 Discord 的 `#cs-feature-request`，别开 Issue）。
4. 官方明确划出的渠道边界：测试构建的问题**不要**发到 `#support`，要回原帖/原线程。

> 信息源里哪些可信、哪些是内容农场，见 [可信信息源](../06-community/community-resources.md)。

## 相关条目

- [官方功能对照矩阵与路线图](feature-matrix.md)
- [系统与环境需求](../01-installation/requirements.md) · [安装指南](../01-installation/installation-guide.md)
