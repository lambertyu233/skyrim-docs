---
id: common-misconceptions
title: 常见错误认知
category: 12-sources
kind: reference
version: 1.0.0
updated: 2026-09-22
tags: [来源, 辨析, 误区, 纠错]
aliases: [谣言, 错误认知, myth, 常见错误, 是不是真的]
source: https://wiki.nexusmods.com/
summary: 工具话题上反复出现的错误认知，逐条给出「错在哪 + 正解出处」，避免把社区口口相传的说法当成事实。
---

# 常见错误认知

每条格式：**误解** → 为什么错 → 正解。

## 一、启动与加载

1. **"装完 SKSE64 就能用普通启动器进游戏。"**
   错。SKSE 的 DLL 由 `skse64_loader.exe` 注入；走 Steam/`SkyrimSE.exe` 启动时**插件全部不加载**，
   SkyUI 会报 Error Code 1。→ [SKSE64（Skyrim Script Extender）](../01-frameworks/skse64.md)（来源：Nexus Mods Wiki SKSE64 安装指南）

2. **"SKSE64 用最新版就行。"**
   错。必须与 `SkyrimSE.exe` 的**精确运行时版本**对应（1.5.97 → 2.0.20；1.6.1170 → 2.2.6，Steam）。
   用"最新版"是装错版本最常见的来源。→ [SKSE64（Skyrim Script Extender）](../01-frameworks/skse64.md)

3. **"Address Library 装哪个版本无所谓。"**
   错。SE（1.5.97）与 AE（1.6+）是两份不同文件，混装会导致插件**静默不加载**。
   → [Address Library for SKSE Plugins](../01-frameworks/address-library.md)

4. **"Crash Logger 和 Trainwreck 一起装更保险。"**
   错。两者都装会互相干扰，**只能保留一个**。（来源：Phostwood Crash Log Analyzer 官方站提示）
   → [Crash Logger SSE](../09-diagnostics/crash-logger-sse.md)

## 二、排序与冲突

5. **"LOOT 排完序就没有冲突了。"**
   错。LOOT 只决定**插件加载顺序**（记录级覆盖的先后），**不消解记录级冲突**——
   两个 mod 改同一条记录时，仍是后加载者全胜，需要 xEdit 做补丁。
   （来源：LOOT 官方 "Introduction To Load Orders"）→ [LOOT（插件排序）](../04-loadorder/loot.md)

6. **"插件上限是 255，没救了。"**
   不完全对。255 是**常规 .esp/.esm** 的上限；Skyrim SE/VR 里 **ESL 还可额外加载 4096 个**。
   优先 ESL 化而不是合并。（来源：LOOT 官方文档）→ [ESL 化（突破 255 插件上限）](../04-loadorder/esl-flagging.md)

7. **"zMerge 是合并插件的标准工具，可以放心用。"**
   过时。zMerge 自 2021-08 起**未再更新**（zEdit 最后一版 v0.6.7 为 2022-11），
   含脚本 / MCM / 导航网格 / facegen 的插件合并后极易出隐性问题；
   现代做法是先 ESL 化，其次才考虑合并。→ [zEdit / zMerge（插件合并，已停滞）](../04-loadorder/zedit-zmerge.md)

8. **"清理 mod 里的脏编辑总是好事。"**
   危险。**只清官方 master**（`Update.esm`、`Dawnguard.esm` 等）。
   第三方 mod 里的"脏"记录常常是作者的有意设计，清掉会造成缺件。
   → [脏编辑与清理（ITM / UDR）](../04-loadorder/dirty-edits-cleaning.md)

9. **"手动 Apply Filter for Cleaning 更可控，自动清理不安全。"**
   反了。xEdit 4.0.2 起**三个手动清理函数已废弃**，官方口径统一走 Quick Auto Clean；
   且在 Skyrim SE 上它会把 group 与主记录标脏后保存，以避免早年版清理 `Dawnguard.esm` 后
   灵魂石冢部分 worldspace 不加载的老问题。（来源：xEdit `whatsnew.md`）→ [xEdit / SSEEdit（记录编辑器与冲突检测）](../04-loadorder/xedit.md)

## 三、安装与卸载

10. **"禁用 mod 就等于卸载干净了。"**
    错。Papyrus 脚本实例会**留在存档**里；SKSE 插件的数据还写在 `.skse` cosave 里。
    要清需要 FallrimTools/ReSaver，而且它也只清理 Papyrus 堆的一部分（Change Form、
    cosave 内容它**刻意不动**）。→ [FallrimTools / ReSaver（存档清理）](../09-diagnostics/fallrimtools-resaver.md)

11. **"MO2 会把文件复制进游戏目录，所以游戏目录会变大。"**
    错。MO2 用 USVFS 在进程内虚拟化，**游戏目录保持干净**；
    Vortex 才是真的把文件部署（硬链接/复制）进游戏目录。→ [Mod Organizer 2（工具视角）](../03-managers/mo2-tool.md)

12. **"整合包（Wabbajack list）可以装了再往上面加 mod。"**
    技术上可以，但**不在支持范围**：list 的描述、补丁与排序都是针对固定集合做的，
    加 mod 后出的问题作者不背。→ [Wabbajack（整合包一键安装）](../03-managers/wabbajack.md)

## 四、资产与生成

13. **"NifSkope 最新版就是官方 dev7。"**
    过时。官方 `niftools/nifskope` 分支停在 2018（dev7）；**社区在用的是 fo76utils 的 dev11**
    （支持到 Starfield）。→ [NifSkope（NIF 模型编辑器）](../05-assets/nifskope.md)

14. **"CAO 能把 LE mod 转成 SE mod。"**
    半对。它转换的是**资产格式**（nif / hkx / dds 的二进制头与压缩）。
    脚本、记录结构、Papyrus 函数差异它一概不管——**转完不一定能跑**。
    → [Cathedral Assets Optimizer（CAO）](../05-assets/cathedral-assets-optimizer.md)

15. **"跑一次 DynDOLOD 就够了。"**
    错。DynDOLOD 依赖 xLODGen 先出地形 LOD，且**每次改动影响外景物体的 mod 都要重跑**。
    另外版本匹配是硬要求：`DynDOLOD Resources` 不能低于 standalone 版本。
    → [DynDOLOD（物体与树木远景）](../06-lod/dyndolod.md)

16. **"生成工具出来的东西可以放进 Overwrite 里不管。"**
    不推荐。产物应各建独立的"输出 mod"（如 `xLODGen Output` / `TexGen Output` / `DynDOLOD Output`）
    并排在 mod 列表末尾，这样重跑与回退都可控。→ [xLODGen（地形 LOD 生成）](../06-lod/xlodgen.md)

## 五、语音与音频

17. **"把 `.wav` 放进 `Sound\Voice\` 就能听到配音。"**
    错。游戏读 `.fuz`（内嵌 xwm + lip），需要 Yakitori 之类工具打包，
    且 lip 要用 FaceFXWrapper 从 wav 生成。→ [配音制作完整链路（wav → lip → fuz）](../10-audio/lip-fuz-workflow.md)

18. **"lip 文件是按音频波形算出来的。"**
    不对。FaceFXWrapper 的输入是**文本 + 音频**（Fonix 数据做音素→口型映射），
    所以文本与音频节奏不一致时，口型会明显不同步。→ [FaceFXWrapper（生成口型 .lip）](../10-audio/facefxwrapper.md)
