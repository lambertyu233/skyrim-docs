---
id: requirements
title: 系统与环境需求
category: 01-installation
version: 1.1.0
updated: 2026-09-21
tags: [需求, 前置, 兼容性, 安装, 强烈推荐]
source: https://modding.wiki/en/skyrim/developers/community-shaders/installation-guide#requirements
summary: 支持的游戏版本、GPU/系统要求，以及必须安装的前置 MOD 清单。
---

# 系统与环境需求

安装 Community Shaders 前，必须满足以下硬性条件。

## 游戏版本

- **Skyrim 1.6.1170（Steam） / 1.6.1179（GOG） / 1.5.97**
- **不支持** LE、VR 以及其它所有 Skyrim 版本。特别地，**1.6.640、1.7.99、1.7.104 都不受支持**。
- 团队只计划支持 Steam 最新版与 1.5.97；新版本发布后会跟进支持。**除 1.5.97 外没有长期支持（LTS）承诺**。
- CS 主版本**不再支持 VR**，VR 用户请看 [Open Shaders](https://www.nexusmods.com/skyrimspecialedition/mods/180419)。
- 更完整的版本与支持策略见 [版本与支持策略](../00-overview/version-and-support.md)。

## 硬件 / 系统

- **GPU**：支持 **Vulkan 1.4 或更新**（GTX 900 Maxwell 系列、RX 5000 RDNA1 系列或更新）。
  - 不确定可查 [TechPowerUp](https://www.techpowerup.com/gpu-specs)。
- **Intel 核显不支持**；所有 CPU 均可。
- **系统**：Windows 10 创意者更新或更新（Linux 用户见 [Fluorine](https://github.com/SulfurNitride/Fluorine-Manager)）。
- **运行库**：[Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)（务必装 X64 最新版）。

## 必须安装的前置 MOD

| MOD | 说明 |
|-----|------|
| [SKSE64](https://www.nexusmods.com/skyrimspecialedition/mods/30379) | 脚本扩展，**需手动**放入游戏根目录 |
| [Address Library](https://www.nexusmods.com/skyrimspecialedition/mods/32444) | SKSE 插件地址库 |
| [Engine Fixes](https://www.nexusmods.com/skyrimspecialedition/mods/17230) | 引擎修复（含 Preloader，需手动放 `d3dx9_42.dll` 到根目录） |

## 强烈推荐（官方 Nexus 页）

这两项不是硬性需求，但官方在 Nexus 发布页专门列了出来：

| MOD | 说明 |
|-----|------|
| **Crash Logger**（SSE AE VR，PDB 支持） | 帮助诊断崩溃。官方 FAQ 反复强调：报 bug 时不带日志基本没人能帮你 |
| **Assorted Mesh Fixes** | 修复网格问题——**这些问题是 CS 会「照出来」的**（原版渲染器一直掩盖着它们，CS 把它们暴露了） |

## 新手从哪开始

官方安装指南点名推荐：**从没 mod 过 Skyrim 的人，先读 [A Dragonborn's Fate](https://dragonbornsfate.moddinglinked.com/intro.html)**（作者同时也是 *Viva New Vegas* 的作者），读到 Community Shaders 那一节再回来。整体负载构建另可参考 **STEP Modifications Guide**（见 [Vanilla 设置指南](vanilla-setup.md)）。

## 不兼容 MOD（节选）

- ENBSeries（见 [Effects 11](https://mod.pub/skyrim-se/415-effects-11) 以支持未加密预设）
- 任何阻止 CS 初始化的 MOD（如 NVIDIA Reflex、TAA Sharpen 等）

> 完整不兼容清单见 [参考-不兼容 MOD](../03-reference/incompatible-mods.md) 与 [FAQ](../03-reference/faq.md)。
