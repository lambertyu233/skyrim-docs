---
id: papyrus-compiler-decompiler
title: Papyrus 编译器与反编译
category: 08-creation
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [脚本, Papyrus, 编译, 反编译, 工具]
aliases: [Papyrus 编译器, Champollion, pex 反编译, 反编译脚本, papyrus compiler, psc pex]
source: https://ck.uesp.net/wiki/Compiling_Scripts
summary: `.psc` 源码 → `.pex` 编译产物是单向的；读别人的 mod 需要反编译器（Champollion），写自己的 mod 用官方编译器或社区替代品。
---

# Papyrus 编译器与反编译

## 一个必须先纠正的预期

Papyrus 的编译是**单向、有损**的流程：

```
.psc（源码） ──编译──▶ .pex（游戏读的字节码）
.pex ──反编译──▶ 近似源码（变量名/注释/部分结构会丢）
```

所以**反编译出来的代码不能直接当源码用**，只能用来"读懂逻辑"。
反编译质量取决于工具对字节码版本的覆盖度。

## 编译（写 mod）

| 方式 | 说明 |
|---|---|
| **CK 自带编译器** | 官方路径，随 CK 分发；命令行形式为 `PapyrusCompiler.exe` |
| **CK 界面内编译** | 编辑脚本后由 CK 触发 |
| 社区替代实现 | 现存若干重写版编译器，用于无 CK 环境或自动化构建；**挑活跃的分支** |

编译要点：

- 需要 `-import` 指向游戏的 `Data\Scripts\Source`（否则找不到父类）。
- 编译产物 `.pex` 必须进 `Data\Scripts\`，源码 `.psc` 建议一起分发（便于他人阅读）。
- **`.pex` 是二进制，版本敏感**——目标游戏的脚本版本不匹配时加载失败。

## 反编译（读别人）

**Champollion** 是社区长期使用的 Papyrus 反编译器（把 `.pex` 还原成可读源码）。
它的价值：

- 搞清某个 mod 到底做了什么（比读描述可靠）；
- 判断某个脚本是否依赖某个前置；
- 移植/汉化时定位字符串来源。

> 用反编译代码做什么都要看授权：**读**通常没问题，**再分发**受原 mod 的 permissions 约束。

## 与本工作区其他库的关系

- Papyrus 语言本身（类型、状态、事件、函数）→ [Papyrus 脚本](../../creation-kit-kb/04-scripting/)（9 条）
- 脚本的**调试与日志** → [Papyrus 日志与脚本排错](../09-diagnostics/papyrus-logging.md)
- 脚本**性能**问题（延迟尖峰） → [Papyrus Tweaks NG](../09-diagnostics/papyrus-tweaks-ng.md)
- 脚本能力扩展（新函数） → [powerofthree's Papyrus Extender](../01-frameworks/po3-papyrus-extender.md)

## 相关

- [Creation Kit（官方创作工具）](../08-creation/creation-kit.md)
- [编辑器插件（写脚本/配置的外围工具）](../08-creation/editor-plugins.md)（在编辑器里写脚本更舒服）
- [编译脚本（Papyrus Compiler）](../../creation-kit-kb/04-scripting/compiling-scripts.md)
