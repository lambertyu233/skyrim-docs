---
id: upload-steam-workshop
title: 教程：上传到 Steam 创意工坊
category: 06-tutorials
version: 1.0.0
updated: 2026-09-20
tags: [tutorial, steam, workshop, publish, upload, release]
source: https://ck.uesp.net/wiki/Uploading_To_Steam_Workshop
summary: 官方教程——将做好的 MOD 通过 CK 打包并发布到 Steam 创意工坊，含前置检查与限制说明。
status: stable
kind: tutorial
---

# 教程：上传到 Steam 创意工坊

本教程（Bethesda 官方）讲解如何把完成的 MOD 通过 Creation Kit 发布到 **Steam 创意工坊（Steam Workshop）**。

## 发布前检查

- MOD 应已[清理](05-tools/tes5edit.md)（移除 ITM / UDR），减少冲突。
- 资源尽量打包（见 [Archive.exe](02-features/archive-exe.md)），但注意工坊上传对文件组合的**限制**。
- 确认 `.esp` 的 `Author` / `Description` 等元数据填写完整。

## 工坊上传的限制（官方提示）

根据 CK 的自动归档机制，工坊可能**只接受**不包含以下内容的 MOD：

- `.esm` 主文件
- 多个 `.esp` 文件
- 多个文本文档
- 图片文件

因此很多复杂 MOD 无法直接通过 CK 上传；可用 **Archive.exe** 先打包，再视情况分发到各 Skyrim MOD 站点。

## 上传步骤概要

1. 在 CK 中打开要发布的插件。
2. 通过 CK 的「Upload Plugin」/ 归档功能启动上传向导。
3. 填写标题、描述、预览图、标签。
4. 确认依赖（如需要官方主文件）后提交。
5. 在创意工坊页面校验页面信息并设为公开/好友可见。

## 提示

- 首次发布建议先以「私有/好友」测试，确认加载无误再公开。
- 资源打包与版本更新流程，结合 [Archive.exe](02-features/archive-exe.md) 使用更稳妥。

> 来源：[UESP Uploading To Steam Workshop](https://ck.uesp.net/wiki/Uploading_To_Steam_Workshop)
