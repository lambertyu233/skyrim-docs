---
id: presets
title: 条件预设（Presets）
category: 02-structure
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 预设, PRESET, 条件复用]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: 自 2.2.0 起可在 replacer mod 内定义条件预设，用 PRESET 条件在各 submod 里引用；预设内容存在 replacer mod 配置里，submod 只保存预设名字。
---

# 条件预设（Presets）

## 它解决什么问题

自 **2.2.0** 起有一个新功能叫 **PRESETS（预设）**。可以在 replacer mod 里定义多个预设，然后用一个专门的 **`PRESET` 条件**来选用。

这个需求来自 replacer mod 作者：一个 replacer mod 里的多个 submod 常常**共享完全相同的条件**，只差少数几处（比如武器类型不同）。预设就是为这个场景设计的——把那段条件块**只写一次**，然后在各 submod 里**复用**。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## 关键机制：预设**不会被复制**

> 请记住，预设**不会被复制**到 submod 配置里。**唯一被保存的是预设的「名字」。预设的「实际内容」保存在 replacer mod 的配置里。**

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

这个设计有直接后果：

| 后果 | 说明 |
| --- | --- |
| **改一处，全体生效** | 在 replacer mod 级改预设内容，所有引用它的 submod 一起变。这是好事（一处维护）。 |
| **删预设会牵连 submod** | 2.3.6 修过一个 bug：删除一个预设会把**所有**含 `PRESET` 条件的 submod 标成 dirty，而不只是用到该预设的那些。 |
| **分享 mod 时要连 mod 级配置一起给** | 只给 submod 文件夹，引用就断了（因为内容在 mod 级）。 |

> 来源（2.3.6 修复）：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## 用在哪

```
ReplacerMod/
├── config.json          ← 预设定义在这里（mod 级）
├── SubmodA/
│   └── config.json      ← 条件里只写 PRESET("某某预设")
└── SubmodB/
    └── config.json      ← 同样引用同一个预设
```

`PRESET` 条件本身的语义（官方）：*在原地求值 replacer mod 中定义的条件预设*。它属于**容器条件**的一种——见 [容器条件](../03-conditions/condition-containers.md)。

## 什么时候值得用

- 同一个 replacer mod 下有 **3 个以上 submod 共享一长串条件**，只差一两处 → 值得。
- 只有 1–2 个 submod → 直接用 `AND` 写更直观，不必引入间接层。

## 相关

- [容器条件：OR / AND / XOR / TARGET / PLAYER / MOUNT / PRESET](../03-conditions/condition-containers.md)
- [条件全清单](../03-conditions/conditions-list.md)
- [`config.json`、`user.json` 与优先级](config-and-priority.md)
