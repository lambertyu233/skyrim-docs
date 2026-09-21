---
id: bsa-management-usage
title: BSA 管理与解包（使用侧）
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, BSA, 解包, Unmanaged, Archive Invalidation]
aliases: [BSA 解包, BSA 管理, 查看 bsa, 解包 bsa]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 勾选 Have MO manage archives 后 BSA 被当作 loose file 参与 mod 优先级；真实 Data 中的 BSA 会以 Unmanaged 前缀参与冲突裁决。
kind: tutorial
---

# BSA 管理与解包（使用侧）

> 底层解析见[BSA 的优先级解析](../03-architecture/bsa-priority-resolution.md)；这里讲操作与影响。

## Archives 标签页

- 若某 mod 的资源装在 BSA 里，会在右窗格 **Archives** 标签页、以该 mod 之名下列出。
- 右键 BSA → `Extract…` 可把内容解包到你指定的任意文件夹。

## Have MO manage archives

勾选后（默认行为）：

- **所有 BSA 都完全等同于 loose file**：其优先级**只取决于 mod 优先级顺序**，与插件优先级顺序（加载顺序）**无关**。
- 在此模式下勾选某个 BSA，**无需 dummy plugin** 即可加载其资源。举例：可以勾选 Skyrim 高清材质包的 BSA 并取消其插件，**省下 3 个插件位**。

取消勾选后：

- 回到游戏内置的"BSA vs loose file"规则：BSA 按**插件加载顺序**加载，且**必须通过 dummy plugin** 加载 BSA。

## Unmanaged mod 与冲突裁决

MO 的 BSA 管理让 **mod 优先级更重要**。为了让冲突裁决正确，MO 会把**真实 Data 目录里所有含 BSA 的 mod/DLC** 也列进左窗格，作为 `Non-MO` mod，并加 **`Unmanaged:`** 前缀。

- 使用经验：**让这些 Non-MO mod 排到尽可能低的优先级，同时保持冲突裁决正确**。
- 一个便捷的判断依据：**观察你的加载顺序**——DLC 以及夹在它们之间的 mod，其顺序一般应与加载顺序大致一致，这样才会用到正确的资源。

### 典型案例

Dragonborn DLC 与 Unofficial Skyrim Patch：

- 若把 `Unofficial Skyrim Patch` 放在 Dragonborn DLC（左窗格显示为 `Unmanaged:`）**之上**，`dragonactorscript.pex` 会错误地覆盖 Dragonborn 版本，导致**无法吸收龙魂**。
- 修复方法：让 `Unofficial Skyrim Patch` 的优先级**低于** Dragonborn。

## 已知限制

- 若报错 `failed to remove limit on archive list!`，这类用户**只能以勾选方式加载约 80 个 BSA**。应对办法：解包部分 BSA，或改为加载对应的 ESP——这样游戏会用默认机制加载该 BSA。

## Archive Invalidation（存档失效）

- Bethesda 游戏默认让 BSA 覆盖 loose file。若你用了 loose file 想盖过原版 BSA 内容，就需要 Archive Invalidation。
- Skyrim 的替代方案是 **Back-date BSAs**（Settings → `Workarounds`）：**跑 Skyrim 且未启用 Archive Invalidation 时，必须勾选它**，否则原版 BSA 可能覆盖你的 loose file，出问题后极难排查。
- 详见[设置页参考](settings-tabs.md)与[加载机制与 Steam App ID](load-mechanism.md)。
