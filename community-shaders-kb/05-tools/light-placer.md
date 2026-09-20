---
id: light-placer
title: Light Placer（光照放置器）
category: 05-tools
version: 1.0.0
updated: 2026-09-20
tags: [工具, 光照, JSON, ENB替代]
source: https://modding.wiki/en/skyrim/developers/community-shaders/light-placer-home
summary: 通过 JSON 将可配置的真实光源附加到物体与角色，是 ENB Light 的社区替代。
---

# Light Placer（光照放置器）

**Light Placer** 是一个框架型工具，允许 MOD 作者通过 `.json` 文件把**真实灯泡**附加到各种网格与引用（reference）上。因为灯泡是真实的，它们也影响潜行（stealth）。

## 为什么需要它

- ENB Light 在 CS 中**仅有限支持**（且不再承诺广泛支持）。
- 社区公认的 ENB Light 替代是 **Light Placer**。

## 工作机制

- 它是一个**框架**，自身不做任何事；需要各 MOD 提供 JSON 配置来“附加灯泡”。
- 最流行的附加组件是 **CS Light**：把灯泡附加到许多原本靠 ENB Light 照亮的原版网格，并为一些流行 ENB Light MOD 提供补丁。
- 相比 ENB Light，Light Placer 的补丁**更容易创建**。

## 使用建议

- 安装 Light Placer 时请遵循其说明与前置要求。
- 从 ENB 迁移时：在 MOD 列表中搜索含 “ENB Light” 的项并禁用（注意 MLO2 等未在名称中明示的依赖）。移除后用 Light Placer + CS Light 替代以维持发光。
- 安装任何照明 MOD 前，**先装 Light Placer 与 CS Light**（见 [Vanilla 设置指南](../01-installation/vanilla-setup.md)）。

> 更多细节与 JSON 格式请参考官方 Light Placer 页面与 Discord。
