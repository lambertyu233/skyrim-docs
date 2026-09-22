---
id: install-order
title: 安装次序
category: 07-workflow
kind: tutorial
version: 1.0.0
updated: 2026-09-22
tags: [安装, 次序, 流程, 检查清单]
aliases: [安装顺序, 装 mod 顺序, install order, 先装什么, 步骤]
source: https://stepmodifications.org/wiki/SkyrimSE:0.1.0
summary: 从 SKSE 到物理的推荐安装次序，每一步"装完该验证什么"，以及三条"先做再说"的纪律（只装一个身形、统一预设、先跑一次行为补丁）。
---

# 安装次序

次序错了的代价是**症状深远且难查** —— 覆盖关系一旦定型，后面所有东西都建立其上。

## 推荐次序

```
1. SKSE64（版本必须匹配游戏）
2. Address Library（SE / AE 两套，别装错）
3. SkyUI
4. 其它 SKSE 插件框架（PapyrusUtil / JContainers / MCM Helper / po3 Extender）
5. 骨骼：XPMSE（≥ 4.6）
6. 行为补丁跑一次（FNIS / Nemesis / Pandora）
7. 身形家族（女性：CBBE 系 或 UNP 系，只能选一个；男性身形独立）
8. 皮肤贴图（必须与身形同族）
9. BodySlide and Outfit Studio → 构建身形 + 服装（勾 Build Morphs）
10. RaceMenu（+ High Poly Head，+ EFM/EFA）
11. 脸部件资源（眼 / 眉 / 发 / 须）+ 对应 HPH 补丁
12. 物理：Faster HDT-SMP（和/或 CBPC）→ 按需配置
13. （可选）NPC 身形分配：BodyGen / OBody NG / AutoBody
14. NPC 美化 mod（如装了，注意 FaceGen 对齐）
```

## 每一步"装完该验证什么"

| 步 | 验证 |
|---|---|
| 1 | 用 `skse64_loader.exe` 能启动；`Data/SKSE/Plugins/` 有对应文件 |
| 3 | SkyUI 不报 "SKSE is not functioning properly" |
| 5 | 骨骼文件在 `meshes/actors/character/character assets/` |
| 6 | 行为补丁工具输出无错 |
| 7 | **只有一套**女性身形生效 |
| 9 | **勾了 `Build Morphs`**；构建日志无错误 |
| 10 | 进游戏能打开 RaceMenu 界面，**且能看到身形滑块** |
| 12 | 身体/头发有物理反应 |
| 13 | NPC 身材不再千人一面 |

## 三条纪律

### ① 女性身形只能启用一个

CBBE 与 UNP / BHUNP 互斥。同时启用 = 覆盖关系取决于排序，结果不可预期。

### ② 裸身与服装用同一个预设构建

否则穿模。见 [`../06-troubleshooting/clipping.md`](../06-troubleshooting/clipping.md)。

### ③ 装完身形/骨骼先跑一次行为补丁

FNIS / Nemesis / Pandora 生成行为文件，物理与动画都依赖它。
**顺序上它要早于物理 mod 真正生效。**

## 一个反直觉但重要的建议

> **不要一次装完再一起测。** 每完成一个"层"就进游戏看一眼。
>
> 五层一起装然后出错，你有几十种组合要排除；
> 每层装完就测，出错时嫌疑人只有一个。

## 来源

- 整体次序骨架（SKSE → ADL → SkyUI → 骨骼 → 身形 → 皮肤 → BodySlide → RaceMenu → 物理 → 行为补丁）：
  **社区共识**，与 Nexus 论坛的 CBBE 3BA 安装问答、STEP 指南一致 —— **社区经验（多源一致）**
- 排序原则（master/DLC → 修复 → 框架 → 身形皮肤骨骼 → 服装 → NPC 美化 → 补丁）：
  STEP 官方策划指南 —— **一手（指南）**
  `https://stepmodifications.org/wiki/SkyrimSE:0.1.0`
- "XPMSE ≥ 4.6"、"身形 physics 变体"、"`Build Morphs`"：各 mod 官方说明 —— **一手**
