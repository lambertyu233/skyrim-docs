---
id: version-matrix
title: 版本对照表（游戏 ↔ SKSE ↔ RaceMenu ↔ 物理）
category: 00-overview
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [总览, 版本, 对照, 兼容性]
aliases: [version matrix, 版本对照, 哪个版本, 1170 对应, skse 版本对应, 版本不匹配]
source: https://www.nexusmods.com/skyrimspecialedition/mods/30379
summary: 以游戏版本为主键，列出 SKSE64 / RaceMenu / Faster HDT-SMP 的对应版本，并给出"版本错配会有什么症状"。
---

# 版本对照表

**这是整个领域第一大坑**：SKSE64、RaceMenu、FSMP 都是原生 DLL 插件，
它们的版本与**游戏可执行文件版本**强绑定。Steam 一次自动更新就能让整套失效。

## 以游戏版本为主键

| 游戏版本 | SKSE64 | RaceMenu | Faster HDT-SMP |
|---|---|---|---|
| **1.6.1170 / 1179（当前 AE，Steam / GOG）** | **2.2.6** | **0.4.19.16 及以上**（0.4.20.0 亦可） | 最新 4.x，FOMOD 里选 **1.6.1170.0** |
| 1.6.1130 | 2.2.6 | 0.4.19.15+ | — |
| 1.6.640 | 2.2.2 | 0.4.19.13+ | 选 1.6.640 档 |
| 1.6.659（GOG） | 2.2.2 | 0.4.19.14+ | — |
| 1.6.353 | 2.1.5 | 0.4.19.x 相应版本 | 选 1.6.353 档 |
| 1.5.97（pre-AE 长期版本） | 2.0.20 | 0.4.19.12 及以下一支 | 选 1.5.97 档 |
| VR | SKSEVR 2.0.12 | — | 选 VR 档 |

> RaceMenu 的 changelog 里，"Support for Game Version 1.6.1170" 出现在 **0.4.19.16**。
> 官方 Files 页的主文件标注 SKSE64 **2.2.6** 或更高。

## Community Shaders 的口径可作旁证

同一台机器上，其他原生插件对"支持哪些游戏版本"的态度更严格：
`community-shaders-kb` 记录 CS 只支持 **1.6.1170 / 1.6.1179 / 1.5.97**，
明确**不支持 1.6.640 / 1.7.99 / 1.7.104**。这说明"版本敏感"不是个别 mod 的怪癖，
而是这套引擎生态的系统性特征 —— **装任何原生插件前，先确认自己的游戏版本号**。

## 怎么查自己的游戏版本

- Steam 版：右键游戏 → 属性 → 已安装文件，或看游戏目录里 `SkyrimSE.exe` 的详细信息；
- 更可靠的办法是看 **SKSE 启动日志**或 `Documents/My Games/Skyrim Special Edition/SKSE/` 下的插件日志，
  它们会打印运行时版本。

## 版本错配的症状对照

| 错配 | 症状 |
|---|---|
| SKSE 与游戏不匹配 | 游戏起不来，或**所有 SKSE 插件静默失效**（菜单没有、滑块没有） |
| RaceMenu 与 SKSE/游戏不匹配 | 进游戏后捏脸界面是原版的，RaceMenu 全套功能消失 |
| FSMP 选错游戏版本档 | 物理不生效，或开局 CTD |
| Address Library 装了 SE 版给 AE 用 | 依赖它的 DLL 插件全部失效（地址不通用） |

**推论**：遇到"某个功能整体不见"，第一件事永远是核对版本，而不是去翻冲突。

## 来源

- SKSE64 版本与安装说明：`https://www.nexusmods.com/skyrimspecialedition/mods/30379` + Nexus 官方 wiki —— **一手**
- RaceMenu changelog（0.4.19.16 对应 1.6.1170）：`https://www.nexusmods.com/skyrimspecialedition/mods/19080?tab=files` —— **一手**
- Faster HDT-SMP FOMOD 档位与游戏版本对应：`https://www.nexusmods.com/skyrimspecialedition/mods/57339` 文件页 —— **一手**
- Address Library：`https://www.nexusmods.com/skyrimspecialedition/mods/32444` —— **一手**
- 1.6.640 / 1.7.9x 不被 CS 支持：见本工作区 `community-shaders-kb/01-installation/` —— **一手（CS 官方）**

> ⚠️ **时效提醒**：本表随上游发版变化。表内 `updated` 距今较远时，请以各 mod 的 Files 页为准。
