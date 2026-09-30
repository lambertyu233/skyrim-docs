---
id: mco-to-bfco-converter
title: MCO to BFCO Converter——老动作包迁移工具
category: 01-frameworks
kind: tool
version: 1.0.0
updated: 2026-09-30
tags: [转换器, MCO, BFCO, 迁移, hkx, 注释]
aliases: [hkx 转换, 动作包转换, MCO 转 BFCO, converter, 批量转换注释]
source: https://www.nexusmods.com/skyrimspecialedition/mods/119926
summary: Sukezzzzz 的官方级转换工具：批量把 MCO 的 hkx 文件名与注释转成 BFCO 规范；1.2.0 起无需 hkanno64。
---

# MCO to BFCO Converter——老动作包迁移工具

## 一句话

老动作包不用重找：MCO 的 hkx 可以批量转成 BFCO 规范。Nexus 页 [mods/119926](https://www.nexusmods.com/skyrimspecialedition/mods/119926)，作者 Sukezzzzz，v1.2.2（2025-01-02）。

## 官方说明它能干什么【一手源】

1. **重命名文件**：`mco_attack` → `BFCO_Attack`、`mco_powerattack` → `BFCO_PowerAttack`、`mco_weaponart` → `BFCO_PowerAttackComb` 等，让 BFCO 识别。
2. **替换/补写注释**：`PIE.@SGVI|MCO_nextattack|1` → `BFCO_NextIsAttack1`、`MCO_WinOpen` → `BFCO_NextWinStart`、`MCO_WinClose` → `BFCO_DIY_EndLoop`、`MCO_Recovery` → `BFCO_DIY_recovery` 等。
3. **批量导出/更新注释**（batch dump and update the annotations）。

## 限制与注意

- **不要装进 MO2**，放到干净目录单独运行；先备份【一手源，官方 description】。
- ≤1.1.8 版改注释需配合 hkanno64；**≥1.2.0 无需**【一手源】。
- MCO 特有的方向派生注释转换后只能实现 BFCO 的**"伪方向重击"**——BFCO 官方说明转换包的方向重击均属伪方向重击【社区经验，见中文技术资料】。
- BFCO 官方不兼容清单里"Skysa/ABR/MCO"一条原话即："people can easily convert the MCO hkx to BFCO by using MCO To BFCO Converter"——所以这是**官方认可的迁移路径**【一手源】。
