---
id: testing-and-debugging
title: 测试与调试手法
category: 04-development
version: 1.0.0
updated: 2026-09-21
tags: [开发, 调试, 测试, ShaderDefines, 性能, 官方]
source: https://github.com/community-shaders/skyrim-community-shaders/wiki
summary: 官方 Developer Wiki 的调试手法：A/B 对比测试、TESTCUBEMAP、Shader Defines（含 LLFDEBUG）、灯光编辑器、性能分析与抓帧。
---

# 测试与调试手法

这些手法全部来自**官方 GitHub Developer Wiki**，官方用户 wiki 上没有。调画质参数时尤其有用——靠肉眼在两次启动之间「记忆对比」几乎必然出错，用 A/B 测试才能看见真实差异。

## A/B 对比测试（Test Interval）

官方内置了一个「按固定间隔在两套设置之间自动切换」的模式，用来客观对比两种视觉效果：

1. 调好第一套设置 → 点 **Save Settings**。这套会写入 `CommunityShadersUSER.json`，界面上显示为 `User Mode`。
2. 改成第二套设置。这套显示为 `Test Mode`。
3. 在 **Advanced** 菜单里找到 `Test Interval` 滑块。
4. 设成任意**非零**值（单位：秒，即每套设置停留多久后切换）。此时会生成新的配置文件 `CommunityShadersTEST.json`；屏幕左上角会出现倒计时，你也可以盯着第 2 步改动的参数，确认它们确实在来回切。
5. 退出：把 `Test Interval` 设回 **0**。第 2 步的设置会保留。
6. 想恢复默认：点 **Load Settings**。

> 实操建议：一次只改**一个**变量（例如只动 Skylighting 强度或 SSGI 的 GI 强度），让 Test Interval 在 3–5 秒间切换，看几轮就能判断差异是否真实存在。

## Dynamic Cubemaps 反射测试模式

想知道某个物体到底有没有吃到动态立方体贴图反射，可以让**几乎任何表面变成满反射面**（瓶子、药水最能看出来）：

1. **Advanced → Shader Defines** 里填入 `TESTCUBEMAP`。
2. 如果开了 Disk Cache，先 **Clear Disk Cache**。
3. 再 **Clear Shader Cache**。
4. 对着物体看，环境会映在物品上。

## Shader Defines：通用调试开关

**Advanced → Shader Defines** 是官方的调试入口，填入预定义字符串即可开启对应调试可视化。已知的两个：

| 定义 | 作用 | 出处 |
|------|------|------|
| `TESTCUBEMAP` | 把表面变成满反射，检验动态立方体贴图 | Developer Wiki |
| `LLFDEBUG` | 开启光照可视化 | Light Limit Fix 功能页 |

### LLFDEBUG：看灯光上限

在 **Advanced → Shader Defines** 加上 `LLFDEBUG` 后，Light Limit Fix 提供 3 种可视化：

- 可视化「灯限是否已达」：达到**严格灯限**（portal-strict lights）时显示**红色**；
- 可视化严格灯数；
- 可视化聚簇（clustered）灯数。

> 官方注明这是**开发者调试功能，不面向正常游戏**。配合它排查「进屋就变暗/闪烁」这类问题很有效。

## Light Editor：实时改灯

**Inverse Square Lighting** 自带一个灯光编辑器（CS 菜单 → Inverse Square Lighting 设置里）。可以实时看改灯的效果，包括开关平方反比、调光色与强度。

两条官方警告：

- **编辑器不面向游戏玩法**。使用期间**不建议存档**，可能引发问题。
- **改动不能直接保存**，只能把数值抄进 xEdit 或 Light Placer 的 JSON 配置。

## 性能分析

- **Performance Overlay**：实时帧率、draw call、各功能耗时。菜单里有 `Profiling` 标签（排查性能先看这里）。概念上要区分 `Utility` / `Other` 这类 Bethesda 自身的开销（阴影等）与 CS 功能自身的开销。
- **Load Time Profiler 会误报**：编译着色器 / 生成水体缓存的那几次启动，它会说 CS 拖慢启动。等缓存生成完再测才是真实值。
- 官方给出的高开销功能候选：**Screen Space GI**（间接光贵，可关或降 Low）、**Effects 11**（取决于预设）、**Upscaling**（在老系统上）、**Skylighting**（低端机可考虑关闭）。但官方强调**因机而异**，务必自己看 Profiling。

## 抓帧（RenderDoc）

CS 1.4.6+ 内建 RenderDoc 支持。报 bug 时开发者常会索要一份捕获：

1. CS 菜单 → `RenderDoc` → 勾选 `Enable RenderDoc Capture`；
2. `Save Settings`，重启游戏；
3. 左上会显示 WARNING（性能下降是正常的）；
4. 复现 bug，把画面留在屏幕上；
5. 菜单 `RenderDoc > Create Capture`，再 `Open Capture Directory`；
6. 传到第三方托管（Discord 传不了大文件），把链接回给开发者；
7. 完成后**取消勾选并保存**，关闭捕获。

## 其他开发者向开关

- **Remote Control**：把开发者工具暴露给外部 `devbench`，用于 **AI 辅助开发**（属核心特性）。
- **CS Editor**：实时天气与 imagespace 编辑器，服务 MOD 制作。
- **pbr 详细日志**：1.8.4 起 PBR 提供一个 verbose log 选项，用来压掉刷屏日志。
- **Feature Issues 标签**：游戏内菜单里有该标签，直接列出功能层面的问题（排「着色器编译失败」时先看它）。

## 缓存操作速查

| 操作 | 什么时候用 |
|------|-----------|
| **Clear Shaders**（UI 右上角） | 改 Shader Defines、做着色器开发与热加载 |
| **Clear Disk Cache** | 改了 Shader Defines、换了 CS 版本、想强制重编译 |
| 手动删 `Data/ShaderCache`（MO2 为 `Overwrite/ShaderCache`） | 更新 CS 后没弹「Compiling Shaders」 |
| 顺手删 `UnifiedWaterCache` | 同上（官方建议「顺手一起删更保险」） |

> 铁律：**只删 `ShaderCache`，绝不删 `Shaders`**。`ShaderCache` 里应当能找到逐层嵌套的 `.pso` / `.vso` 文件，用这个来确认自己没删错目录。详见 [架构与缓存系统](../00-overview/architecture.md)。

## 相关条目

- [架构与缓存系统](../00-overview/architecture.md)
- [FAQ - 通用排查建议](../03-reference/faq.md)
- [贡献指南](contributing.md)
