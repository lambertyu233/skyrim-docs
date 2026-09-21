---
id: common-pitfalls
title: 实战常见坑
category: 06-community
version: 1.0.0
updated: 2026-09-21
tags: [社区, 排错, 实战, 性能, 兼容]
source: https://www.nexusmods.com/skyrimspecialedition/mods/86492
summary: 把官方文档散落各处的警告、Nexus 发布页与用户回帖里的高频问题，按「现象 → 原因 → 处理」整理成一份实战清单。
---

# 实战常见坑

本条目把官方 wiki、Nexus 发布页与社区回帖里**反复出现的**问题集中成一条清单，按「现象 → 原因 → 处理」组织。原始出处以官方文档为准；标注「社区」的条目来自用户实测反馈，属于经验而非官方保证。

## 安装与启动

### 黑屏但能听到声音

- **原因**：CS 自 1.2.0 起对**独占全屏**、或**渲染分辨率与显示器分辨率不一致**的配置有问题。
- **处理**：改用**无边框窗口**，并把分辨率设成与显示器一致。Windows 10 创意者更新之后，无边框窗口不再有性能损失。
- **连带**：Display Tweaks 的 `BorderlessUpscale` **明确不受支持**，要性能请用 [Upscaling](https://www.nexusmods.com/skyrimspecialedition/mods/156952)。

### 启动弹「Required DLL <...> was missing」

- **原因**：前置缺失。**最常见的是 `EngineFixes.dll`**。
- **处理**：核对 Nexus 页需求与 [安装指南](../01-installation/installation-guide.md)。注意 Engine Fixes 分两部分：主文件用管理器装，**Preloader 的 `d3dx9_42.dll` 必须手动丢进游戏根目录**。

### 按 END 没打开菜单

- **处理**：若已装 CS，暂停菜单里应有 `Settings > Graphics > Open Community Shaders Menu`，从那里改键（`General > Keybindings`）。若无此项，确认是不是 CS 1.9.0+。仍然不行 → 禁用 overlay（RTSS / Fraps），`Fraps` 直接删，RTSS 对 `SkyrimSE.exe` 禁用。

### 字体/菜单卡顿、滚动一格跳很远

1.8.4 修复过「菜单输入延迟与滚动粒度」。若在旧版遇到，升级即可。

## 着色器与缓存

### 红色报错「Shaders failed to compile」

- **头号原因**：**CS 与附加特性版本混用**，或缓存没重新生成。
- **处理**：只保留「最新 Nexus 版」**或**「单一测试构建」，**绝不混**。然后看游戏内 `Feature Issues` 标签。检查是否还留着已并入核心的旧特性 / 废弃特性，检查是否残留 ENB / Shader Tools（`d3d11.dll`、`d3dcompiler_46e.dll`、Windows 下 `d3dcompiler_47.dll`）。

### 更新后没弹「Compiling Shaders」

- **原因**：磁盘缓存没失效。
- **处理**：手动删缓存。MO2 是 `Overwrite/ShaderCache`，Vortex 是 `<游戏>/Data/ShaderCache`；**顺手删 `UnifiedWaterCache`**。`Shaders` 目录**不要动**。

### 着色器编译卡几小时或直接 CTD

- **处理**：先装/更新 **VC++ Redistributable X64**。弱 CPU 可下调 `Background Compiler Threads` / `Compiler Threads`（`SettingsUser.json`，或首次启动前改 `SettingsDefault.json`）。确认游戏是受支持版本、且用无边框窗口。

### 装了 ENB Light / ENB Particle Lights 类 MOD 却不发光

- **原因**：CS **不支持** ENB Light / ENB Particle Lights。
- **处理**：改用基于 **CS Light** 或 **Light Placer** 的补丁。注意 **Light Limit Fix 的粒子光照只是「向后兼容」性质**，官方推荐的做法已经是直接用 Light Placer 体系。

## 兼容性

### ENB 和 CS 同时装着

- **事实**：两者**不是设计来协同工作的**，做的是同一层次的事。CS **检测到 ENB 会自行禁用**以防崩溃。
- **社区共识**：同时装通常只剩「浪费性能」这一个结果。二选一。
- **例外**：想用 ENB 预设的话，走 **Effects 11**（只支持未加密预设），依然不是同时运行 ENB 本体。

### 装了 Lux 之后性能变差

- **处理**：重装 Lux 时**取消勾选** `optimized` / `split` 网格。**Light Limit Fix 已经取代了这些网格**，留着只会掉性能。另外**不要勾选任何支持粒子光照的选项**，它们与 CS 不兼容。

> Lux 作者本人也确认过：这些网格是为突破引擎灯限而做的，有 LLF 就不需要；但若不用他的网格，记得删掉他对原版网格做的纹理集改动。

### 天气/照明 MOD 之间的冲突

- **规则**：**同一时间只用一款天气 MOD**、**一款室内照明 + 一款室外照明**。
- **已知**：**EVLaS 不要用**，Sky Sync 已完全取代它（装了 EVLaS，Sky Sync 会自动禁用自己）。**Modern Lighting Overhaul 2 高于 1.3.6 的版本与 CS 不兼容**。
- **Window Shadows Ultimate** 与 Window Shadows RT / Lux / ELFX Shadows / Enhanced Lights and FX / Relighting Skyrim (Interiors) / Skyrim is Luminous 互斥。

## 画面异常

### 地形没视差、或者长出「刺」

- **处理**：① 用**带视差的地形纹理**（如 Atlantean Landscapes、Terrain Blending Fix）；视差纹理**必须完整覆盖**，只换一半会导致刺状。② CS 菜单 `Extended Materials` 里勾 `Enable Legacy Terrain`（用 PBR 地形纹理则不需要）。

### 湿润效果出错、有硬边

- **处理**：关闭 `Skyrim.ini` 的 `[Display]` 下动态分辨率（`bEnableAutoDynamicResolution=0`）；NVIDIA 控制面板里「Antialiasing - Transparency」设为**关**。

### 反射看起来不对

- 动态立方体贴图要靠**捕获屏幕内容**来推断环境，**你从没看见过的地方它就是猜的**。想验证某个物体有没有反射，用 [TESTCUBEMAP 测试模式](../04-development/testing-and-debugging.md)。

### 眼睛发亮

- **处理**：装 **Improved Eye**。NPC 需自行补丁，或换用没有该问题的替换包（如 COTR）。

## 性能

### 帧率低于预期

- **预期管理**：画面增强**一定**有代价。叠加的 MOD 越多越慢，这是通例。
- **先怀疑这几项**：Screen Space GI（可关或调 Low）、Effects 11（取决于预设）、Skylighting（低端机可关）、Upscaling（老系统上）。
- **别过度堆纹理**：社区里最贵的错误就是「所有东西都上 8K」。建议大件（山、建筑）用 4K，小件（武器、书）用 2K。
- **看 Profiling 标签**而不是猜。注意 `Utility` 这类开销属于 Bethesda 自身（阴影等），不是 CS 的锅。

### CS 报告的可用显存比实际低（社区反馈）

有用户反馈 CS 报出的可用 VRAM 明显低于显卡实际容量（例如 12 GB 卡显示约 10 GB），官方支持渠道当时也无法给出明确解释。**实践上最有效的做法仍是降低游戏内画质设置与纹理尺寸**（纹理尺寸对显存占用影响最大）。

### 帧生成（Frame Generation）效果不如预期

官方要求写得很明确：

- **只在刷新率 ≥ 120 Hz 时生效**；
- 需要在 **Windowed / Borderless Windowed** 模式下用；
- 建议搭配 **SSE Display Tweaks**（否则高帧率与垂直同步不好控）。

> 另需注意：社区里有把 DLSS 多帧生成（MFG）跑到 Skyrim 上的实验分享，但那是**个人实验构建**，非官方功能；而且 CS 自己的 F10 性能浮层当时**还不能正确显示 3x/4x 的输出帧率**，要看 NVIDIA overlay。

## 环境与平台

### Intel 核显

- **官方不支持**。贡献者欢迎去修，但别期待能跑。

### 游戏版本

- 只支持 **1.6.1170（Steam）/ 1.6.1179（GOG）/ 1.5.97**。**1.6.640、1.7.99、1.7.104 都不行**——其中 1.7.99 / 1.7.104 的不兼容原本计划在 1.9.0 解决。
- 报 `REL/ID.h(223): Failed to open address library file` = 游戏版本不受支持，更新或降级。

### 报 bug 之前请先做「最小设置」

官方 FAQ 的隔离法：只启用 Community Shaders、Nexus 页上 `Additional Features` 列出的那些、以及它们的依赖。MO2 用户新建配置档后 `Ctrl+A` 全禁用再逐个开；Vortex 用户新建配置档只开这些。同时确认 VC++ Redist X64 是最新。

> **跳过这步直接报 bug，大概率被请回去重做。** 这一步同时能省下你自己大量时间。

## 报告问题的正确姿势

- 带上：**截图/录像 + 硬件 + 日志 + 版本号**（内存里不带这些的求助基本会被忽略）。
- 渠道：日常问题 → [官方 Discord](../06-community/community-resources.md)；确认是 bug → GitHub Issue；功能请求 → Discord `#cs-feature-request`，**不要**开 Issue。
- 测试构建的问题**不要**发到 `#support`，回原帖/原线程。

## 相关条目

- [FAQ](../03-reference/faq.md) · [不兼容 MOD 清单](../03-reference/incompatible-mods.md)
- [测试与调试手法](../04-development/testing-and-debugging.md)
- [可信信息源](community-resources.md)
