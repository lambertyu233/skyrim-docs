---
id: cloud-shadows
title: Cloud Shadows 云影
category: 02-features
kind: core
status: released
version: 1.1.0
updated: 2026-09-21
tags: [阴影, 户外, 天气, 体积光]
source: https://modding.wiki/en/skyrim/developers/community-shaders/Features-Home/cloud-shadows
summary: 让云层对世界投射真实阴影的定制技术；与太阳对齐、使用真实云系统而非滚动贴图，且不增加额外 draw call。
---

# Cloud Shadows 云影

> 分类：核心特性（1.8.0+ 并入） · 状态：已发布

云层向世界投射阴影。这是 **ProfJack 与 doodlum 合作开发的定制技术**，不是现成方案。

## 它为什么和别的「云影」不一样

- **与太阳对齐、使用真实的云系统**，而不是一张滚动贴图。所以云把太阳挡住时，玩家会**真的被笼罩进黑暗**。
- **极快的近似算法**：云从**玩家视角**渲染，再反投影（unproject）覆盖整个世界。
- **不增加额外 draw call**：云影贴图是在**渲染立方体贴图反射的过程中顺带产出**的副作用。
- **被体积光复用**：云影同样作用于体积光，**太阳光束（godrays）会被云遮断**。多云天气里云层骤然裂开的瞬间视觉上非常抓眼。

## 相关条目

- [体积光](volumetric-lighting.md)（复用云影做遮挡）
- [官方功能对照矩阵](../../00-overview/feature-matrix.md)（CS / ENB / VR 均有此项）

## 贡献者

ProfJack、doodlum、alandtse。

---
*本条目依据官方功能页精修整理；如与官方页面不一致，以官方为准。*
