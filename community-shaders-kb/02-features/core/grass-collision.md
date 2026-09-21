---
id: grass-collision
title: Grass Collision 草体碰撞
category: 02-features
kind: core
status: released
version: 1.1.0
updated: 2026-09-21
tags: [草地, 物理, 角色]
aliases: [草体碰撞, 草被踩, grass collision, 草丛互动]
source: https://modding.wiki/en/skyrim/developers/community-shaders/Features-Home/grass-collision
summary: 给草体加上角色碰撞，玩家与 NPC 走过时草会被推开、压弯（1.5.0+ 并入核心）。
---

# Grass Collision 草体碰撞

> 分类：核心特性（1.5.0+ 并入） · 状态：已发布

给草体加上**角色碰撞**，让草在被踩到或被推开时**弯曲**。

## 效果

草现在会与**玩家和 NPC** 碰撞，像被踩到或推挤一样弯折。该效果基于《战神》（God of War）里那套交互式风与植被的技术（官方附了该技术演示视频）。

## 为什么这项功能值得注意

在 CS 之前，「走过草地会分开」是 ENB 阵营的招牌效果之一；Grass Collision 把它带进了 CS，并且因为是在引擎层实现，**不依赖 ENB 的注入式后处理**。在[官方功能对照矩阵](../../00-overview/feature-matrix.md)中，CS / ENB / CS VR 都有、ENB VR 没有。

## 相关条目

- [Grass Lighting 草体光照](grass-lighting.md)
- [Grass Optimizations 草优化](../additional/grass-optimizations.md)（附加特性，重写草渲染）

## 贡献者

- doodlum：主要贡献者
- Nukem：游戏着色器与渲染的原始逆向
- Jonahex：逆向、最早的着色器缓存与协助
- Maxsu：那套「复杂到我看不懂」的碰撞函数
- Ersh：协助
- alandtse

---
*本条目依据官方功能页精修整理；如与官方页面不一致，以官方为准。*
