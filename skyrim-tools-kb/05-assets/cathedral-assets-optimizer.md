---
id: cathedral-assets-optimizer
title: Cathedral Assets Optimizer（CAO）
category: 05-assets
kind: tool
version: 1.0.0
updated: 2026-09-22
tags: [资产, 转换, 优化, LE 到 SE, 贴图, 批量处理]
aliases: [CAO, Cathedral Assets Optimizer, 资产优化, LE 转 SE, 移植, 批量转换, 23316]
source: https://github.com/Guekka/Cathedral-Assets-Optimizer
summary: 批量转换与优化三类资产（贴图/网格/动画）的工具：LE↔SE 移植、BC7 重压缩、降采样、修 mipmap、打包 Bethesda 归档。
---

# Cathedral Assets Optimizer（CAO）

## 官方定位

> *"a tool aiming to automate asset conversion and optimization for several Bethesda games,
> such as Skyrim and Skyrim Special Edition"*（README）

作者 Guekka 自述的主用途：**帮助把 mod 在 Skyrim LE 与 SE 之间"移植"**，
并把 CAO 描述为"被数千人使用"的自动化工具。

## 它处理的三种资产

| 类型 | 能做什么 |
|---|---|
| **Textures（.dds）** | 重压缩（如 BC7）、分辨率降采样、修正/生成 mipmap |
| **Meshes（.nif）** | **LE ↔ SE 格式转换**（几何相同、二进制头不同）、结构优化 |
| **Animations（.hkx）** | LE ↔ SE 转换 |

另外它也能**创建 Bethesda 归档（bsa）**。

## 它**不能**做什么（务必知道）

CAO 转的是**资产格式**。它**不管**：

- Papyrus 脚本的 API 差异；
- 记录结构差异；
- 依赖缺失（前置 mod、字体、shader）；
- 命名路径变化。

所以"用 CAO 转完就能跑"是常见误解——**转完只是第一步**。
（社区总结，一致口径）

## 操作要点

1. 解压到独立目录，**不要放 `Program Files`**。
2. 选游戏模式（Skyrim SE / LE），选**输入文件夹**。
3. 在 Texture / Mesh / Animation 各页配置动作；有备份选项。
4. 跑完把输出**作为一个新 mod** 装进管理器再测试。

典型移植流程：解压 LE mod → CAO 输入该目录 → 输出到 `MyMod-SE` → 作为 mod 安装 → 测试。

## 代价与限制

- **降采样是有损的**：4K → 2K 会丢细节，这是取舍而非免费优化。
- **整包批处理很慢**：几十 GB 的资产量级可能以小时计。
- **设置项很多**，不懂参数时容易配出意外结果。
- 小版本偶有回归问题（社区经验，来自关于 CAO 的综述类文章；建议保留一个已知稳定的版本）。
- 官方 README 明示：**GitHub 上的是在开发中的实验版本，文档可能过时**；
  正式使用请看 **Nexus 发布页**（`skyrimspecialedition/mods/23316`）。

## 前身

**SSE NIF Optimizer** 是它的前身，只做网格优化与 LE→SE 转换。
现在除极特殊情况外，用 CAO 即可。

## 相关

- [NifSkope（NIF 模型编辑器）](../05-assets/nifskope.md)（单个 nif 的精修）
- [BSA / BA2 归档工具](../05-assets/archive-tools.md)（bsa 打包/解包）
- [DDS 与贴图工具链](../05-assets/texture-tools.md)（DDS 与 mipmap 细节）
- [常见错误认知](../12-sources/common-misconceptions.md) 第 14 条
