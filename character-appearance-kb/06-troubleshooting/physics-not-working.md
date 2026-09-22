---
id: physics-not-working
title: 物理不生效（不抖 / 头发穿透）
category: 06-troubleshooting
kind: tutorial
version: 1.0.0
updated: 2026-09-22
tags: [排错, 物理, SMP, CBPC, 骨骼]
aliases: [物理不生效, 不抖, 没物理, 头发穿透, 物理失效, smp 不工作, cbpc 没反应]
source: https://forums.nexusmods.com/topic/3800385-a-guide-to-hdt-smp-usersmodders/
summary: 物理失效的十条检查项（按顺序排列，从版本到身形变体到 dll 顺序），以及"先跑 smp report"这条最高效的诊断路径。
---

# 物理不生效

## 症状分类

| 症状 | 指向 |
|---|---|
| 完全没有任何物理（身体也不抖） | 引擎层问题（SMP/CBPC 未生效） |
| 身体抖、头发不动 | 方案选错（只装了 CBPC）或头发缺 XML |
| 某一件衣服不飘 | 那件衣服缺 XML 或被覆盖 |
| 头发穿过身体 | 碰撞体定义/不匹配 |

## 检查清单（按顺序）

### 1. 先跑 `smp report`

```
smp report warnings
```

FSMP 内置的命令，会**校验整个 load order 的物理 XML 与 `.nif`** 并报告警告。
**这是效率最高的一步** —— 别先逐个 mod 试。

### 2. SKSE 版本对不对

SKSE 与游戏版本不匹配 → 所有 SKSE 插件静默失效 → 物理自然不动。
见 [`../00-overview/version-matrix.md`](../00-overview/version-matrix.md)。

### 3. 装的是不是正确的物理 mod

- 只装 **CBPC** → **头发和衣服永远不会动**（机制限制，不是配置问题）；
- 只装 **SMP** → 身体可能不如 CBPC 自然，但会动；
- 两者都装 → 需要显式配置，否则**互相覆盖**（见第 5 条）。

### 4. XPMSE 是否装了

HDT-SMP / FSMP **只把网格附加到 XPMSE 的 human skeleton**。
装的是别的骨骼 → 物理没有挂点。需要 **XPMSE ≥ 4.6**（带物理骨骼）。

### 5. SMP 与 CBPC 是否在抢插槽

两者默认争同一批骨骼。共存必须：

- 编辑 **`defaultBBPs.xml`** 让 SMP 忽略身体；
- 且把 **`cbp.dll` 改名 `zcbp.dll`**（或 Engine Fixes preload），保证 SMP 先加载。

见 [`../04-physics/physics-overview.md`](../04-physics/physics-overview.md)。

### 6. 身形装的是不是 physics 变体

**这是"装了 FSMP 还是不抖"最常被忽略的一条。**

身形（如 3BA、BHUNP）在 FOMOD 里通常有"带物理"和"不带物理"的选择。
装成不带物理的版本，物理引擎再对也没东西可动。

### 7. 是否在 BodySlide 构建了带物理的身形

选了 physics 变体还不够，还要**构建**。

### 8. 行为补丁跑了吗

FNIS / Nemesis / Pandora 需要跑一次以生成行为文件（CBPC 依赖 FNIS）。

### 9. 旧版 HDT-SMP 的 OpenCL

早期 SMP 需要 **OpenCL 2.0**。"关闭 OpenCL"实际是**切到 CPU 模拟**，不是关掉。

### 10. MCM 里的物理开关

如 3BBB 可以在 CBPC / SMP 之间切换 —— **切错了引擎就会看起来"没物理"**。

## 两条经验性细节（社区）

- **改 CBPC 配置不生效**时，确认：角色体重是 **0 或 100**；
  未被 SMP 覆盖；覆盖式文本配置在 MO2 左栏里位于 CBPC / 身形**之下**。
- **不兼容项**：CBPC 与 *Player Size Adjuster and First Person Camera Height Fix SSE* 不兼容。

## 来源

- `smp report` 命令：FSMP 官方仓库 README / wiki —— **一手**
- "SMP 只附加 XPMSE human skeleton"：HDT-SMP Nexus 页 —— **一手**
- "CBPC 不能管头发和衣服"：LoversLab 帖 —— **社区经验（多帖一致）**
- 检查清单其余项（XPMSE ≥ 4.6、physics 变体、BodySlide 构建、FNIS、OpenCL、
  MCM 开关、体重 0/100、左栏顺序、不兼容项）：
  综合 HDT-SMP 用户/作者指南与 CBPC 专帖 —— **社区经验（多帖一致）**
