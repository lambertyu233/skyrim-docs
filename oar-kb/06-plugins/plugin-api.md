---
id: plugin-api
title: SKSE 插件 API 概览
category: 06-plugins
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [OAR, API, SKSE, 插件开发, 扩展]
source: https://github.com/ersh1/OpenAnimationReplacer/tree/main/src/API
summary: OAR 把四个域的 API 以可复制头文件形式公布（Animations / Conditions / Functions / UI），按 InterfaceVersion 请求接口；自定义条件必须在其 PostLoad 之前注册。
---

# SKSE 插件 API 概览

## 为什么有 API

官方原话：

> Open Animation Replacer 有一个 **SKSE 插件 API，让其他插件可以添加新条件**，从而让其他作者能扩展可能性，而不必一切都依赖原作者。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

插件 API 是 **0.8.0** 引入的（作者当时说"现在虽然还用不上，但这是我想在公开发布前备好的重要功能，它已完全可用，我用一个示例插件测试过"），并在 **3.0.0** 随函数系统、**3.1.0**（注释）两次更新过版本。

> 来源：<https://bakemono.app/p/patreon/25643772/81916525>、<https://www.nexusmods.com/skyrimspecialedition/mods/92109>

## 四个 API 域

源码 `src/API/` 下是**可复制到自己项目里**的头文件（注释原文：*"For modders: Copy this file into your own project if you wish to use this API"*）：

| 头文件 | 命名空间 | 接口 | 能干什么 |
| --- | --- | --- | --- |
| `OpenAnimationReplacerAPI-Conditions.h` | `OAR_API::Conditions` | `IConditionsInterface2` | **注册自定义条件** |
| `OpenAnimationReplacerAPI-Functions.h` | `OAR_API::Functions` | `IFunctionsInterface1` | 注册自定义函数 |
| `OpenAnimationReplacerAPI-Animations.h` | `OAR_API::Animations` | `IAnimationsInterface1` | 查询当前替换动画、清理条件状态数据 |
| `OpenAnimationReplacerAPI-UI.h` | `OAR_API::UI` | `IUIInterface2` / `IUIInterface3` | 拿到 OAR 的 ImGui 上下文，把自家 UI 画进 OAR 菜单 |

> 来源：`github.com/ersh1/OpenAnimationReplacer` 的 `src/API/` 目录（本库 2026-09-21 核对）

## 通用调用方式

每个域都导出一个 **`GetAPI(InterfaceVersion = Latest)`** 与一个全局接口指针（如 `g_oarConditionsInterface`），内部走 `_RequestPluginAPI_<域>` 函数指针：

```cpp
// 条件域（头文件里的实际声明）
IConditionsInterface* GetAPI(InterfaceVersion a_interfaceVersion = InterfaceVersion::Latest);
extern OAR_API::Conditions::IConditionsInterface* g_oarConditionsInterface;

// 请求失败返回 nullptr
```

各域的 **`InterfaceVersion` 枚举**（源码事实）：

| 域 | 可用版本 |
| --- | --- |
| Conditions | `V1`（**已不支持**）、`V2`、`V3`，`Latest = V3` |
| Functions | `V1`、`V2`，`Latest = V2` |
| Animations | `V1` |
| UI | `V2`、`V3` |

> 来源：`src/API/OpenAnimationReplacerAPI-*.h`（本库核对）

## 注册自定义条件的标准写法

API 提供了一个辅助模板，**关键在于调用时机**：

```cpp
// 头文件里的原文说明：
// Call it inside SKSEMessagingInterface::kMessage_PostLoad or before!
// It will have no effect otherwise, because after that point Open Animation Replacer
// will have already initialized its map of condition factories.

template <typename T>
APIResult AddCustomCondition();   // 要求 T::CONDITION_NAME
```

返回值为 `APIResult` 枚举：**`OK` / `AlreadyRegistered` / `Invalid` / `Failed`**。

> 来源：`src/API/OpenAnimationReplacerAPI-Conditions.h`

### ⚠️ 调用时机是硬约束

**必须在 `kMessage_PostLoad` 或更早**调用。晚于这个点，OAR 已初始化完条件工厂表，注册**不会有任何效果**——而且**不会报错**。这是插件开发最容易踩的坑。

## 自定义条件能长什么样

一个自定义条件由**一组组件（components）**构成。可用的组件类型（源码枚举）：

| 组件类型 | 含义 |
| --- | --- |
| `kMulti` | 多值（子条件组） |
| `kForm` | 表单引用 |
| `kNumeric` | 数值 |
| `kNiPoint3` | 三维点 |
| `kKeyword` | 关键字 |
| `kText` | 文本 |
| `kBool` | 布尔 |
| `kCondition` | 内嵌条件集 |
| `kCustom` | 自定义 |

另有 **`EssentialState`**（3.0.0 引入，官方变更日志的表述）：

| 值 | 行为 |
| --- | --- |
| `kEssential` | 必需——玩家没装对应插件时**会收到错误提示** |
| `kNonEssential_True` | 非必需——没装插件时**不报错**，条件**返回真** |
| `kNonEssential_False` | 非必需——没装插件时**不报错**，条件**返回假** |

> 来源：官方 3.0.0 变更条目（"Added 'essential state' to custom conditions — if marked as non-essential, the user won't be notified with an error about a missing condition, and the condition will return either true or false depending on the selected option"）

**`EssentialState` 的设计很实用**：让扩展插件的条件可以"优雅降级"——没装扩展 mod 的玩家不会看到一堆报错，动画只是按你选的真/假分支走。

## Animations API 能做什么

```cpp
struct ReplacementAnimationInfo {
    std::string animationPath;   // 被替换后的动画路径
    std::string projectName;     // 行为项目名（DefaultMale / DefaultFemale …）
    std::string variantFilename; // 变体文件名
    std::string subModName;
    std::string modName;
};

// 查询某个 clip generator 当前实际在播的替换动画
virtual ReplacementAnimationInfo GetCurrentReplacementAnimationInfo(RE::hkbClipGenerator*) = 0;
```

这解决了"**别的插件怎么知道 OAR 现在让这个角色播了什么**"的问题——做 HUD、做调试工具、做联动逻辑的插件会用到。

> 来源：`src/API/OpenAnimationReplacerAPI-Animations.h`

## 版本兼容须知

⚠️ **OAR 大版本更新后，自定义条件插件往往需要重新编译：**

- **3.0.0**：「已有实现自定义条件的插件**必须用新的 OAR Condition API 版本重新编译**才能获得这个功能。」（指 essential state）
- **3.1.0**：「已有实现自定义条件的插件必须用新的 OAR Condition API 版本重新编译才能获得这个功能。」（指注释）
- 开发日志也提到过 API 为 Detection Plugin 做过专门修复。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/92109>（3.0.0 / 3.1.0 变更条目）

**实践结论**：如果你用的扩展插件在 OAR 更新后失效，第一反应应该是"去插件页面看有没有更新版本"，而不是回退 OAR。

## 已有的扩展插件

| 插件 | 作者 | 注册了什么 |
| --- | --- | --- |
| [Detection Plugin](detection-plugin.md) | Nonameron | `DETECTS` / `DETECTED_BY` + 3 个检测子条件 |
| [Math Plugin](math-plugin.md) | Ersh（本体作者） | `MathStatement` |
| [IED Conditions](ied-conditions.md) | SlavicPotato | 与 IED / SDS 联动的 6 个条件 |

**Detection Plugin 是"API 好不好用"的最好证明**：它在页面上专门感谢了 Ersh，说「Ersh 提供了子条件的逻辑和易用的 API，还为本 mod 专门修过 API」。

> 来源：<https://www.nexusmods.com/skyrimspecialedition/mods/104806>

## 相关

- [Detection Plugin](detection-plugin.md)
- [Math Plugin](math-plugin.md)
- [IED Conditions](ied-conditions.md)
- [函数系统与 OAR 自定义动画事件](../04-functions/functions-and-events.md)
