---
id: skse64
title: SKSE64（Skyrim Script Extender）
category: 01-frameworks
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [前置, SKSE, 脚本扩展, 运行时, 版本匹配]
aliases: [Skyrim Script Extender, skse64_loader, 启动器, 报错 Error Code 1]
source: https://skse.silverlock.org/
summary: 一切高级 mod 的地基：以 DLL 注入扩展脚本与内存能力，版本必须与 SkyrimSE.exe 精确对应，且必须用它自己的 loader 启动游戏。
---

# SKSE64

## 是什么

`skse64_loader.exe` + `skse64_<版本>.dll` + 一组 `.pex` 脚本，
通过注入 `SkyrimSE.exe` 暴露游戏原本没有的脚本函数与内存访问能力。
绝大多数"高级 mod"（SkyUI、OAR、MCM Helper、SPID、RaceMenu…）都建立在它之上。

**唯一官方分发点：`https://skse.silverlock.org/`**（含 archived builds 页）。
不要从第三方站下载——这是注入型 DLL，来源必须可信。

## 版本匹配表（官方站 / Nexus Mods Wiki）

| 游戏运行时 | 发行渠道 | 对应 SKSE64 |
|---|---|---|
| 1.5.97 | Steam | 2.0.20（异常时可退回 2.0.17） |
| 1.6.353 | Steam | 2.1.5（archived builds） |
| 1.6.640 | Steam | 2.2.3（archived builds） |
| 1.6.1170 | Steam | 2.2.6 |
| 1.6.1170 | GOG | 装机时可能尚无对应版 |
| 1.6.659 | GOG | 2.2.3 |

> 关键：**所有 SKSE 插件也必须与运行时版本匹配**。MCM Helper、PapyrusUtil、po3 系插件
> 都有分版本的下载文件，装错表现为"奇怪的行为"而不是干脆报错。

## 安装

1. 打开游戏根目录（`SkyrimSE.exe` 所在处）确认版本号：右键 `SkyrimSE.exe` → 属性 → 详细信息。
2. 下载对应 `.7z`，解压。
3. **把 `skse64_loader.exe`、`.dll` 复制到游戏根目录**（不是 `Data\`）；
   把解压包里的 `Data\Scripts\` 合并进游戏的 `Data\Scripts\`。

> 作者与社区反复强调：**99% 的安装失败源于把 loader/DLL 也丢进了 `Data\`，或整个 `Data` 目录没合并。**

## 启动方式（最常被忽略的一步）

必须通过 `skse64_loader.exe` 启动。在 MO2/Vortex 里应把它登记为可执行程序，
**从管理器内启动**——否则管理器看不到你的 modlist（MO2 尤其如此，因为 USVFS 只在被它启动的进程里生效）。

## 常见症状

| 症状 | 原因 |
|---|---|
| 游戏根本起不来 / 报"版本不受支持" | SKSE64 与运行时版本不匹配 |
| 能进游戏但 SkyUI 报 Error Code 1 | 用游戏启动器启动了，插件没加载 |
| 某些插件不生效、日志无输出 | Address Library 缺失或版本错 → [Address Library for SKSE Plugins](../01-frameworks/address-library.md) |
| 装了 mod 但进游戏无变化 | 见 [Mod Organizer 2（工具视角）](../03-managers/mo2-tool.md) 的启用/部署检查 |

## 相关

- [Address Library for SKSE Plugins](../01-frameworks/address-library.md)：抗更新的地址映射，几乎所有现代插件都依赖它。
- [CommonLibSSE-NG（插件开发框架）](../01-frameworks/commonlibsse-ng.md)：写插件的开发者框架。
- [Mod Organizer 2（工具视角）](../03-managers/mo2-tool.md)：在 MO2 里正确挂载 SKSE。
- [SKSE 插件开发](../../creation-kit-kb/05-tools/skse-plugin-dev.md)：插件开发的 CK 侧视角。
