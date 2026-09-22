---
id: racemenu-presets
title: 预设（.jslot）与分享生态
category: 02-face
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [捏脸, 预设, jslot, 存档, 分享]
aliases: [preset, 捏脸预设, 导入预设, slot 文件, 脸型文件]
source: https://www.nexusmods.com/skyrimspecialedition/mods/19080
summary: .jslot 的结构与存放路径、带雕塑预设的额外 .nif、导出与导入流程，以及"预设应用后脸不对"的常见原因。
---

# 预设（`.jslot`）与分享生态

## 格式：JSON 文本

RaceMenu 发布页明确：**预设改为 JSON 格式，扩展名 `.jslot`**。
旧的二进制 `.slot` 仍能加载，但 CharGen 不再写出这种格式。

结构上每条滑块是一组"滑杆名 + 提供该 morph 的插件 + 数值"：

```json
{
  "name": "ShoulderWidth",
  "keys": [ { "key": "RaceMenuMorphsCBBE.esp", "value": 50 } ]
}
```

> **实用推论**：`keys[].key` 指向**提供 morph 的那个 esp**。
> 所以同一份预设，在 CBBE 身形与 UNP 身形下的可应用程度不同 ——
> 预设是**绑定身形家族**的，跨家族套用只会得到一半生效的结果。

文件里还包含 `weight` 以及 headparts / skinOverrides 等块。
其中 **`skinOverrides` 缺失或条目错误会导致"皮肤油光"类 bug**（社区经验）。

## 存放路径

| 内容 | 路径 |
|---|---|
| 预设文件 | `Data\SKSE\Plugins\CharGen\Presets\` |
| 带雕塑的预设 | 同名 `.nif`（有时带 `.dds`）放在 `Data\SKSE\Plugins\CharGen\`，导入时到 **Sculpt → Import Head** 加载 |
| 控制台导出位置 | `Data\SKSE\Plugins\CharGen\Exported\<PATH>.jslot` |

## 导出与导入

**导出（做自己的预设或随从）**

1. 在 RaceMenu 里捏好脸 → Sculpt 页 **F5 Export head** →
   得到 `Data\SKSE\Plugins\CharGen\<name>.nif` 与 `.dds`；
2. 存预设：`skee preset-save <名字>`。

**导入**

1. `.jslot` 丢进 `CharGen\Presets\`；
2. 游戏内打开捏脸界面，在预设下拉里选；
3. 若预设自带雕塑几何，去 Sculpt 页 **Import Head**。

**应用到 NPC / 随从**：`skee preset-load <名字>` 可加载到 NPC，
但预设负责"滑块值"，**脸部件（head parts）需要单独设置**。

## 导入后"脸不对"的常见原因

| 现象 | 原因 |
|---|---|
| 脸是尖的 / 不像截图 | **High Poly Head 未在 Head 页把 Face part 切到 HPH** |
| 部分特征丢失、纹理紫红 | 预设依赖的**头发/眼/眉/皮肤资源没装** |
| 脸型大体对但眉歪 | 眉毛资源与 HPH 不匹配，缺对应补丁 |
| 皮肤油光 | `skinOverrides` 条目缺失或错误（社区经验） |
| 完全没反应 | SKSE / RaceMenu 版本不符，或 `.jslot` 放错目录 |

## 分享生态

- **Nexus 是主阵地**：搜 "Racemenu preset" 有 **2000+** 结果，多在 Body/Face/Hair 或 Presets 分类。
- 预设作者通常会在要求里列出**所用资源 mod 清单**（皮肤、眼睛、头发、HPH 等）—— **照单装齐是唯一解**。
- **种族匹配的经验规则**（社区经验）：
  - 人类之间（帝国/诺德/布雷顿/红卫）可互用；
  - 精灵之间（高/木/暗）可互用；
  - 兽人、虎人、亚龙人**最好只在同族内用**；
  - COTR 预设需 Charmers of the Reach，UBE 预设需 UBE。
- 其它聚集地：LoversLab（成人向预设多）、Vector Plexus（HPH 相关）、各 Wabbajack modlist 自带预设包。

## 来源

- `.jslot` = JSON、路径、`skee preset-save/load`：RaceMenu 发布页与 changelog —— **一手**
- jslot 结构示例与 "改 json 格式" 的说明：Nexus 论坛 scorrp10 引用 RaceMenu 文案 —— **社区经验（转述一手文案）**
- `skinOverrides` 相关 bug：LoversLab 帖 —— **社区经验**
- 预设数量（2000+）、种族匹配规则、分享习惯：Nexus 论坛 2025 帖 + LoversLab —— **社区经验**
- HPH 预设"脸是尖的"需切 Face part：Nexus 预设页与 HPH 说明 —— **社区经验（多源一致）**
