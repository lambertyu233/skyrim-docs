---
id: settings-persistence
title: 设置持久化：游戏内菜单调的参数存在哪
category: 03-reference
version: 1.1.0
updated: 2026-10-22
tags: [配置, 持久化, 设置, JSON, 菜单, 排错]
aliases: [CS 设置保存位置, 设置文件在哪, SettingsUser, SettingsUser.json, SettingsDefault, CS 配置目录, 菜单参数存哪, 改完设置重启就丢, PostProcessing 预设, SceneManager.json, overwrite, 换存档参数还在吗]
source: https://github.com/community-shaders/skyrim-community-shaders/blob/v1.8.4/src/Utils/FileSystem.cpp
summary: 游戏内菜单（END）调的参数写进 Data/SKSE/Plugins/CommunityShaders/SettingsUser.json，另有默认档、测试档、主题档、Overrides 覆盖档、PostProcessing 预设档与场景档，共 4 层合并优先级；MO2 环境下全部落在 overwrite/，且与存档无关。
---

# 设置持久化：游戏内菜单调的参数存在哪

> 一句话答案：**`Data/SKSE/Plugins/CommunityShaders/SettingsUser.json`**。
> 前提是**必须点菜单右上角的 `Save Settings`**——不点就只在内存里，关游戏即丢（见下文「保存时机」）。

本文路径与文件名以官方仓库 `v1.8.4` / `main` 分支的 `src/Utils/FileSystem.cpp`（`Util::PathHelpers`）为准，属于**一手源**。

## 一张表：菜单上各类东西各存哪

所有路径都相对于**游戏 Data 目录**。MO2 用户对应到 `overwrite/` 下的同名相对路径。

| 存的东西 | 路径 | 说明 |
|---|---|---|
| **你调的功能参数（主体）** | `Data/SKSE/Plugins/CommunityShaders/SettingsUser.json` | `Save Settings` 写的就是它 |
| 默认档（基线） | `Data/SKSE/Plugins/CommunityShaders/SettingsDefault.json` | 缺失时 CS 自动生成（所有 shader 类型默认启用） |
| A/B 测试的 B 套 | `Data/SKSE/Plugins/CommunityShaders/SettingsTest.json` | `Test Interval ≠ 0` 时生成 |
| 主题（配色/字号） | `Data/SKSE/Plugins/CommunityShaders/SettingsTheme.json` | 1.5.0 起 |
| 主题预设文件 | `Data/SKSE/Plugins/CommunityShaders/Themes/` | 1.5.0 起，`*.json` |
| MOD 作者的强制覆盖 | `Data/SKSE/Plugins/CommunityShaders/Overrides/*.json` | 1.4.0 起，见下文 |
| 你对覆盖的修改 | `Data/SKSE/Plugins/CommunityShaders/Overrides/User/<特性名>.user.json` | 1.5.0 起 |
| 已应用覆盖的记录 | `Data/SKSE/Plugins/CommunityShaders/AppliedOverrides.json` | 1.4.0 起，用于清理失效的 `.user` |
| **Post Processing 预设** | `Data/SKSE/Plugins/CommunityShaders/PostProcessing/<预设名>.json` | PP 特性的**预设档**，不是功能参数，见下文 |
| 场景专属设置 | `Data/SKSE/Plugins/CommunityShaders/SceneSettings/InteriorOnly.json` | 1.5.0 起，目前只有「仅室内」一种 |
| **菜单窗口布局**（位置/大小/停靠） | `Data/SKSE/Plugins/CommunityShaders_ImGui.ini` | 注意在**Plugins 根下**，不在 `CommunityShaders\` 夹里 |
| 特性（feature）自身的 ini | `Data/Shaders/Features/<特性名>.ini` | 装没装、版本对不对，**不是**你调的参数 |
| 翻译文件 | `Data/SKSE/Plugins/CommunityShaders/Translations/` | 1.7.0 起 |

> `CommunityShaders_ImGui.ini` 容易和上面的设置 json 搞混：**它只管 ImGui 窗口自己的几何信息**（窗口多大、停靠在哪、标签页位置），**不存任何着色器参数**。菜单卡住/全屏跑不掉时删它能恢复（见 [FAQ](faq.md)），但删它不会丢你的画质设置。

## 加载优先级：4 层合并

CS 不是简单地「读一个文件」，而是按固定顺序叠加（源码注释原文：`LOADING ORDER: Default → User → Overrides → User Overrides`）：

```
SettingsDefault.json  <  SettingsUser.json  <  Overrides/*.json  <  Overrides/User/*.user.json
   默认基线                你的设置              MOD 作者强制值          你对强制的反覆盖
```

要点：

- **User 层只在 USER 模式下叠加**。加载测试档时不会拿你的 USER 档去盖。
- **Overrides 优先级高于你的设置**。这是 MOD 作者「强制某功能必须开/某参数必须是多少」的机制，命名规则是 `<Mod名>_<特性名>.json`，全局覆盖则用 `<Mod名>_Global.json`。
- **`.user.json` 是给你的「逃生口」**：当你确实要改掉某个 MOD 强制的值时，CS 把它写进 `Overrides/User/<特性名>.user.json`，这一层优先级最高，能压过 Overrides。
- 加载时 CS 会比对 Overrides 文件的哈希，自动清掉内容已变的旧 `.user.json`（`CleanupStaleUserOverrides`）。

**实践含义**：如果你在菜单里调了某个参数，重启后又变回原样，先怀疑**它被某个 Overrides 强制覆盖了**，而不是怀疑「没保存」。

## PostProcessing 预设：和功能参数不是一回事

`PostProcessing/` 目录存的是 **PP 特性的「调色方案」快照**，与 `SettingsUser.json` 里的功能参数分工不同：

```
Data/SKSE/Plugins/CommunityShaders/PostProcessing/
├── <预设名>.json          ← 例如 Astral.json、NAT.CS.json
├── ColorGrading/          ← 1.9.x 起按子功能再分目录
├── DoF/
└── ...
```

- **预设是「参数快照」**：把当前 PP 的一整套参数导出成文件，可分享、可导入。
- **`SettingsUser.json` 是「当前状态」**：菜单里实时调的值。
- 两者会互相影响：**加载预设 = 用快照覆盖当前状态**，所以旧预设套到新版 CS 上经常出错（见下文「跨版本不通用」）。
- 官方对预设的态度：预设功能**目前只在实验构建里可用**，正式版不一定有完整支持（见 [版本与支持](../00-overview/version-and-support.md)）。
- **PP 与 Effects 11 互斥**：作者明确「use either Post Processing or Effects 11, not both」，别同时装。

> **实测数据**：某整合包 26.1.20 的 `PostProcessing/Astral.json` 为 41,647 字节，而 `SettingsUser.json` 为 32,430 字节——预设档比主参数档还大，说明预设承载了 PP 的绝大部分调参。**备份时不能只备 SettingsUser.json。**

## 新版（1.9.x / 26.x）配置文件清单明显变长

早期版本（≤ 1.8.x）CS 引用的配置文件约 **8 种**；到 **1.9.x**（含 Jiaye 26.10.3）二进制里引用的已增至约 **21 种**，新增的都是新 feature 的配套档：

| 新增文件 | 属于哪个 feature |
|---|---|
| `SceneManager.json` | Scene Manager（1.9.0 起，按场景切设置） |
| `cs_editor.json` | CS Editor（新编辑器） |
| `Skin.json` / `NewSkin.json` | Advanced Skin（材质编辑） |
| `State.json` | 状态持久化 |
| `Location.json` | 位置相关 |
| `preset.json` / `_active.json` | 预设库 |
| `_locationweather.ini` / `_weatherlist.ini` | 天气列表 |

同时 `CommunityShaders\` 下新增 `Presets/` 与 `UnifiedWaterCache/` 两个目录。

> **升级影响**：这些文件**首次使用对应 feature 时自动生成**，不需要手动创建；但它们和旧版不通用——**跨大版本升级后建议连配置一起重置**，否则新版读到旧结构可能直接卡死。

### 跨版本升级的实测教训（2026-10-22）

一次 26.1.20 → 26.10.3 的升级实测中：

- 旧版引用的配置文件名 8 种 → 新版 21 种
- 新版 `Translations/zh_CN.json` = **356,142 字节**；同代官方 v1.9.1 的为 **161,545 字节**（Jiaye 版翻译更全）
- Feature 数量：26.1.20 = 39、官方 v1.9.1 = 40、Jiaye 26.10.3 = 48
- 旧版有的 `WeatherEditor` / `WeatherPicker` 在新版被移除，改由 `SceneManager` 承担

作者在更新日志里反复强调：*Presets, wherever you get them, are **mostly NOT compatible between versions**.* 跨版本**连预设带设置一起重置**是更稳的做法。

## MO2 环境：全部落 overwrite，与存档无关

MO2 用户的 `Data\` 是**虚拟化**的，所以：

- CS 写的所有配置实际落在 **`<MO2>\overwrite\SKSE\Plugins\CommunityShaders\`**，而不是任何 mod 文件夹里。
- **「我的文档」下不会有 CS 配置目录**——实测确认 `Documents\My Games\Skyrim Special Edition\SKSE\Plugins\CommunityShaders\` 不存在。如果你在那儿找不到文件，不是坏了，就是被 MO2 接管了。
- **参数与存档无关**：`SettingsUser.json` 是**全局配置**，所有存档共用一份。换档、读档都不会丢；反过来，你调好的参数对所有新档也立即生效。

> ⚠️ **MO2 运行时不要手改这些文件**。CS 只在**游戏运行**时写、MO2 在**自己运行**时也可能重写 `overwrite`，两边会互相覆盖。正确顺序：**关游戏 → 关 MO2 → 改文件 → 开 MO2 → 开游戏**。

## 保存时机：只有点按钮才落盘

- 菜单右上角 **`Save Settings`** → 调 `State::Save()`，写 `SettingsUser.json`。
- 菜单右上角 **`Restore Saved Settings`** → 调 `State::Load()`，从磁盘重新读回来（丢弃当前未保存的改动）。
- **关闭游戏时不会自动保存**。源码里 `State::Save()` 的调用点只有菜单按钮、以及首次引导完成时的强制落盘。改完参数直接退 → 下次启动回到上次的值。这是「我明明调了怎么重启就没了」的第一大原因。
- 首次安装后的欢迎界面结束时，CS 会自动落盘一次（免得欢迎页每次都弹）。

## 版本命名分界（重要）

同一个位置，**0.8.x 与 1.0+ 的文件名完全不同**：

| 版本 | 文件名 | 位置 |
|---|---|---|
| **≤ 0.8.x** | `CommunityShaders.json`（默认）、`CommunityShadersUSER.json`（用户）、`CommunityShadersTEST.json`（测试） | `Data/SKSE/Plugins/` **根下**，且没有 `CommunityShaders\` 子夹 |
| **1.0.0 起** | `SettingsDefault.json`、`SettingsUser.json`、`SettingsTest.json` | `Data/SKSE/Plugins/CommunityShaders/` **子夹内** |

两个坑：

1. **官方 GitHub Developer Wiki 的 A/B 测试页至今仍写旧名**（`CommunityShadersUSER.json` / `CommunityShadersTEST.json`）。那是文档没跟上 1.0 的改名，不是你环境出问题。**当前稳定版（1.8.x）以 `SettingsUser.json` 为准。**
2. 1.0 改名后**目录也变了**：旧版文件在 `Plugins\` 根下，新版在 `Plugins\CommunityShaders\` 子夹里。升级后**旧文件不会被自动迁移**，要自己把旧 `CommunityShadersUSER.json` 的内容合并进新 `SettingsUser.json`（注意两者结构不同：旧版是扁平结构，新版顶层分了 `Menu` / `Advanced` / `General` / `Replace Original Shaders` / `Disable at Boot` / 各特性节）。

## 直接手改配置文件

官方 FAQ 明确支持这条路子：「首次改任何设置时会生成 `SettingsUser.json`，你可以直接编辑它」。

- 改完**要重启游戏**才生效（配置只在启动时读一次；游戏内改完也是靠 `Save Settings` 落盘）。
- 改 `SettingsDefault.json` 也能生效，但**不是推荐做法**：CS 更新会重置它，你得每次更新后重改一遍。优先改 `SettingsUser.json`。
- **JSON 格式坏了会导致启动卡死**。症状是进游戏后卡住不动、`SettingsUser.json` 变成 0 字节。官方给的处理：删掉 `SettingsDefault.json` 和 `SettingsUser.json` 让 CS 重建；如果装了 **PrivateProfileRedirector**，确认版本 ≥ 0.6.0（0.5.x 及以下会触发此问题）。
- 排查「着色器编译卡死」时，官方给的临时手段就是改 `SettingsUser.json` 里的 `Background Compiler Threads` / `Compiler Threads` 降低编译线程数（还没生成 user 档就改 `SettingsDefault.json`）。

## 排错速查

| 现象 | 先查这里 |
|---|---|
| 调完参数重启后还原 | ① 是不是忘了点 `Save Settings` ② 参数是不是被 `Overrides/*.json` 强制覆盖 |
| 设置文件变成空/0 字节，游戏卡死 | 删 `SettingsDefault.json` + `SettingsUser.json` 重建；检查 PrivateProfileRedirector ≥ 0.6 |
| 菜单窗口跑到屏幕外/全屏出不来 | 删 `Data/SKSE/Plugins/CommunityShaders_ImGui.ini`（**不会**丢画质设置） |
| 想批量改参数 | 手改 `SettingsUser.json`，改完重启 |
| 想要「装好的样子」和「我自己调的」并存 | 看 `Overrides/` 机制：改用 `.user.json` 覆盖，或删掉 Overrides 文件 |
| 菜单打不开（按 END 无反应） | 见 [FAQ](faq.md)——暂停菜单 `Settings > Graphics > Open Community Shaders Menu`（1.9.0+）、禁 RTSS/Fraps |
| 画面不正常（灰白/过曝） | PP 没设 **tonemapper**（Jiaye 版尤其明显，作者原话 "You have to set at least a tonemapper"） |
| 预设套上去效果怪/报错 | 预设与 CS 版本不匹配，重新下载对应版本的预设或重置 PP 配置 |
| 「我的文档」里找不到配置 | MO2 接管了，去 `<MO2>\overwrite\` 找 |
| 换存档后调参「没了」 | 不会没——配置是全局的；真没了就是没点 `Save Settings` |
| 升级后游戏卡死 | 新版配置结构不兼容旧档 → 连 `SettingsUser.json` + `PostProcessing\*.json` 一起删掉重建 |
| 日志 | `Documents\My Games\Skyrim Special Edition\SKSE\CommunityShaders.log`（SKSE 标准日志目录，官方 CommonLibSSE 约定）——看它打印的加载路径，能直接确认本次实际读的是哪个文件 |

> **读日志确认实际路径**：`CommunityShaders.log` 里会打印 `Loading default settings from: ...` / `Loading user config file (...)` 之类的行，**这是判定「到底加载了哪个文件」最可靠的依据**——比猜路径靠谱。日志用法见 [测试与调试手法](../04-development/testing-and-debugging.md)。

## 相关条目

- [常见问题解答 (FAQ)](faq.md) —— 菜单打不开、设置文件空白等高频问题
- [架构与缓存系统](../00-overview/architecture.md) —— 设置文件与 ShaderCache / Disk Cache 的分工
- [测试与调试手法](../04-development/testing-and-debugging.md) —— A/B 测试（Test Mode 用的是 `SettingsTest.json`）
- [什么是 Community Shaders](../00-overview/what-is-cs.md) —— CS 与 ENB 的配置方式对比（CS 用 json 菜单，ENB 用 `enbseries.ini`）
- [版本与支持策略](../00-overview/version-and-support.md) —— 官方版 vs 实验构建（Jiaye 26.x）的定位差异
- [安装指南](../01-installation/installation-guide.md) —— MO2 下的安装与 overwrite 行为
- [Overwrite 目录（MO2-USVFS）](../../mo2-usvfs-kb/05-usage/overwrite-dir.md) —— 虚拟化写入机制本身
