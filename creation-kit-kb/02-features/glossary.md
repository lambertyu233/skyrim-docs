---
id: glossary
title: 术语表
category: 02-features
version: 1.0.0
updated: 2026-09-20
tags: [glossary, terms, form, reference, cell, navmesh]
source: https://ck.uesp.net/wiki/Glossary
summary: MOD 开发高频术语速查——Form、Form ID、引用、Cell、Worldspace、Navmesh、Load Order、BSA 等。
status: stable
kind: reference
---

# 术语表

MOD 开发中的高频术语。完整术语见官方 [Glossary](https://ck.uesp.net/wiki/Glossary)。

## 数据与记录

- **Form**：编辑器中的任意数据对象（武器、法术、NPC、单元格等），均有唯一标识。
- **Form ID**：Form 的唯一编号，由「加载顺序索引 + 对象编号」组成（如 `00012345`）。
- **Record**：插件中以 Form ID 存储的一条记录。
- **Master (.esm) / Plugin (.esp)**：主文件与插件，详见[插件格式](01-installation/data-files.md)。
- **Load Order**：插件加载顺序，后者覆盖前者。

## 世界与布局

- **Cell（单元格）**：世界被切分的基本空间单元，室内/室外均如此。
- **Worldspace（世界空间）**：由若干 Cell 组成的可游玩区域（如天际大陆、某地下城）。
- **Reference（引用）**：某 Form 在世界中放置的「实例」；一个 Form 可有多个引用。
- **Navmesh（导航网格）**：定义 AI 可行走区域的三角网格。
- **LOD**（Level of Detail）：远景简化模型/贴图，提升性能。

## 资源与打包

- **BSA**（Bethesda Archive）：资源归档文件，存放网格/贴图/声音。
- **NIF**：Skyrim 的 3D 模型格式（由 Blender 等工具导出）。
- **DDS**：贴图格式。

## 脚本相关

- **Papyrus**：CK 内置的面向对象脚本语言。
- **Script Object（脚本对象）**：Papyrus 中的「类」，如 Actor、ObjectReference、Game、Debug。
- **Event（事件）**：游戏运行时触发、可被脚本响应的信号（如 OnActivate）。
- **Property（属性）**：脚本对外暴露的可配置变量。

## 相关条目

- [编辑器界面](editor-interface.md)
- [Papyrus 语言要素](04-scripting/papyrus-language.md)

> 来源：[UESP Glossary](https://ck.uesp.net/wiki/Glossary)
