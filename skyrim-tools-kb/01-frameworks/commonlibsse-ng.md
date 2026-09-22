---
id: commonlibsse-ng
title: CommonLibSSE-NG（插件开发框架）
category: 01-frameworks
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [开发, SKSE, 框架, C++, 插件开发]
aliases: [CommonLibSSE, 插件框架, SKSE plugin dev, C++ 写插件, 编译插件]
source: https://github.com/CharmedBaryon/CommonLibSSE-NG
summary: 现代 SKSE 插件的事实标准开发框架：一套代码同时支持 SE / AE / VR 多个运行时，把反汇编工作封装成类型安全的 C++ API。
---

# CommonLibSSE-NG

## 是什么

`CommonLibSSE-NG` 是 `CommonLibSSE` 的下一代分支（NG = Next Generation），
提供游戏内部类、函数与数据结构的 C++ 封装。插件作者写：

```cpp
// 概念示意：通过 RE:: 命名空间访问游戏内部对象
auto* player = RE::PlayerCharacter::GetSingleton();
```

而不是直接算地址、写裸指针。**一套源码可编译出覆盖 SE / AE / VR 多运行时**的插件，
这是它与老 `CommonLibSSE`（单一运行时分支）最主要的区别。

## 配套工程实践

| 环节 | 用什么 |
|---|---|
| 依赖管理 | **vcpkg**（官方 `vcpkg.json`），或 CMake + submodule |
| 构建 | CMake + Visual Studio 2022（Desktop development with C++） |
| 地址解析 | **Address Library**（NG 默认依赖，见 [Address Library for SKSE Plugins](../01-frameworks/address-library.md)） |
| 插件模板 | CharmedBaryon 的 `Sample Plugin Template` |
| 崩溃日志 | **Crash Logger SSE 同时发布 PDB 支持**，配合符号可读性大增（见 [Crash Logger SSE](../09-diagnostics/crash-logger-sse.md)） |

## 什么时候需要它

- 你要写/改一个 SKSE 插件（`.dll`）。
- 你要**编译**别人开源的插件源码（不少作者的 CI 依赖它）。
- 你要读懂崩溃日志里的 `RE::` 符号。

**不需要**它的场景：只是装 mod、做补丁、改模型贴图。这时它与你无关。

## 代价与注意

- 需要完整 C++ 工具链，环境搭建是主要门槛（CMake / vcpkg / MSVC 三者版本都敏感）。
- 上游会跟游戏更新持续变动，**插件作者需要主动 rebase**；
  这也是"某插件在 1.6.1170 上还没更新"这类说法的根源。
- 与 `Address Library` 的关系常被误解：NG 不是它的替代品，而是**消费者**。

## 相关

- [Address Library for SKSE Plugins](../01-frameworks/address-library.md)
- [SKSE64（Skyrim Script Extender）](../01-frameworks/skse64.md)
- [Crash Logger SSE](../09-diagnostics/crash-logger-sse.md)（PDB 与符号）
- [SKSE 插件开发](../../creation-kit-kb/05-tools/skse-plugin-dev.md)
