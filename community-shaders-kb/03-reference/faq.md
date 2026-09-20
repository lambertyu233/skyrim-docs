---
id: faq
title: 常见问题解答 (FAQ)
category: 03-reference
version: 1.0.0
updated: 2026-09-20
tags: [FAQ, 排错, 兼容, 配置, 错误, 性能]
source: https://modding.wiki/en/skyrim/developers/community-shaders/faq
summary: 覆盖已知问题、安装、兼容性、配置、开发、错误、性能与通用排查的全部 Q&A。
---

# 常见问题解答 (FAQ)

> 内容整理自官方 FAQ（CS 1.8.4 已知问题基线）。新增/修订请同步官方并在 CHANGELOG 记录。

## 已知问题（CS 1.8.4）

- **Effects 11** 当前在 Nexus Mods 不可用，可在 [mod.pub](https://mod.pub/skyrim-se/415-effects-11) 获取。
- **Skyrim SE 1.7.99 / 1.7.104.0** 与 CS 1.8.4 不兼容，将在 1.9.0 支持（测试构建可用）。

## 安装

**Q：最新 CS 在哪？**
A：始终在 [Nexus Mods](https://www.nexusmods.com/skyrimspecialedition/mods/86492)。仅官方构建受支持；第三方构建/分支不受支持。开发构建仅在 Discord 相关线程受支持。Discord 上的 Jiaye/后处理构建非官方、未经审核、非为性能设计。

**Q：为何某些 MOD 标记为 CS Official？**
A：CS 开源（GPL-3.0），任何人可发布自己的版本；仅“CS Official”由官方团队发布、符合质量标准并获官方测试/支持。

**Q：如何安装 CS？**
A：见 [安装指南](../01-installation/installation-guide.md)；从 ENB 迁移见 [ENB 迁移指南](../01-installation/enb-migration.md)。

**Q：如何让游戏更好看？**
A：遵循 [Vanilla 设置指南](../01-installation/vanilla-setup.md)。

**Q：CS MOD 的顺序？**
A：CS 功能应无冲突文件，顺序无关。若有冲突，要么操作有误，要么 MOD 页另有说明。

## 兼容性

**Q：CS 支持 VR 吗？**
A：主版本不再支持 VR。VR 或继续 VR 开发请看 [Open Shaders](https://www.nexusmods.com/skyrimspecialedition/mods/180419)。

**Q：CS 支持 Linux 吗？**
A：团队不官方支持，但 Discord 有活跃 Linux 社区可协助。

**Q：Skyrim 刚更新，CS 需更新！**
A：团队已知并在处理，可暂用 [downgrader](https://www.nexusmods.com/skyrimspecialedition/mods/169962) 降级。Steam 降级后设 `appmanifest_489830.acf` 只读；恢复则取消只读并验证文件。CommonLibSSE、Address Library、Engine Fixes 需先更新。

**Q：哪些功能与新版 CS 不兼容？**
A：见 [不兼容 MOD-版本演进](../03-reference/incompatible-mods.md) 表格——达到对应版本须移除该功能。

**Q：哪些 MOD 与 CS 不兼容？**
A：见 [不兼容 MOD清单](../03-reference/incompatible-mods.md)。切勿绕过 CS 兼容保护。

**Q：用 CS 后哪些 MOD 不再需要？**
A：Capture Warmer、Sky Reflection Fix、Rim Lighting Removed、Splashes of Storms（主观）等已被 CS 集成或覆盖。

**Q：还需要 Lux 分流/优化网格吗？**
A：不需要，安装时取消勾选，否则性能下降。Light Limit Fix 使此类网格无意义。

**Q：会有 DLSS 帧生成 / DLSS 5 / FSR 4 / XeSS 吗？**
A：FSR 4 因需 Vulkan/DX11 不支持（可 OptiScaler 硬改）；DLSSG/XeSS 随 Vulkan 转移研究中；DLSS 5 待 SDK；RTX 40 及更旧不支持 DLSS MFG/5。无路线图。

**Q：CS 会支持某旧 Skyrim 版本吗？**
A：仅计划支持 Steam 最新版与 1.5.97。

**Q：哪些 ENB 预设与 Effects 11 不兼容？**
A：依赖天空散射或 **ENB Worldspace Weatherlists** 的预设不兼容；加密预设须先解密（CS 不帮解密）。例如依赖 Silent Horizons 2 / Universal Core（经 ENB Extender 加密）者：Cabbage、Dawnfire、Kauz、Picta；以及 Picta - Weathers of Anubis - Repainted。

**Q：Effects 11 不支持 DoF / 预通行？**
A：刻意未实现（质量低）。用 ReShade 或原版 DoF。CS 后处理将支持 DoF。

## 配置

**Q：不用 CS 菜单能改设置吗？**
A：能。首次改设置后生成 `SKSE/Plugins/CommunityShaders/SettingsUser.json`（MO2 overwrite 或 Data 夹），可直接编辑。

**Q：按 End 没反应！**
A：若已装 CS，暂停菜单应有 `Settings > Graphics > Open Community Shaders Menu`，从中改键 `General > Keybindings` 并保存。若无此项，确认 CS 1.9.0+ 且装好。仍不开则禁用 overlays（RTSS/Fraps）；删 Fraps，禁 RTSS for `SkyrimSE.exe`。

**Q：菜单全屏，怎么移动？**
A：窗体顶部似浏览器标签可拖拽；若隐藏，点左上高亮处显示标签栏。都不行则删 `CommunityShaders_ImGui.ini`（SKSE/Plugins）。

## 开发

**Q：我有功能请求？**
A：发 `#cs-feature-request` 频道；勿发 GitHub Issues 除非开发者要。

**Q：能加入开发吗？**
A：能。经 [GitHub](https://github.com/community-shaders/skyrim-community-shaders)，读 [贡献指南](https://github.com/community-shaders/skyrim-community-shaders/blob/dev/CONTRIBUTING.md)。可加 Discord `#cs-development-discussion`。AI 辅助可行，未经验证的 vibe coding 不行。

**Q：在哪测开发中功能？**
A：测试构建**不提供常规支持**。新功能在 Discord `#cs-testing` 测试，勿在 `#support` 报问题。常是 AIO，须卸旧 CS/功能且无冲突。反馈回原线程。

## 错误

**Q：`REL/ID.h(223): Failed to open address library file`**
A：SSE 版本不受支持；若过时须更新，否则[降级](../../01-installation/installation-guide.md)。CS 只支持[安装指南](../../01-installation/installation-guide.md)指定版本。

**Q：启动报 “Required DLL <...> was missing, will disable all hooks and features”**
A：检查 [Nexus 页](https://www.nexusmods.com/skyrimspecialedition/mods/86492) 需求与[安装指南](../../01-installation/installation-guide.md)。常见缺 `EngineFixes.dll`。

**Q：功能缺失？“not installed” / “file is missing”？**
A：从 Nexus 下载[附加特性](../02-features/additional)；不在 Nexus 即未发布。高级用户可[测开发版](#开发)。

**Q：Shaders failed to compile！红色错误！**
A：多为 CS 与附加特性版本混用，或缓存未重生。**只用最新 Nexus 或单一测试构建，勿混**。Effects 11 红错若 ENB 相关，确认预设[受支持](#兼容性)；加密者不能载。查看游戏内 `Feature Issues` 标签；检查 MOD 管理器冲突；确认无[废弃特性](#兼容性)且皆新；确认无 ENB/Shader Tools（`d3d11.dll`、`d3dcompiler_46e.dll`、Win 下 `d3dcompiler_47.dll`）。Linux 用 [Fluorine](https://github.com/SulfurNitride/Fluorine-Manager)。

**Q：CS 效果奇怪/坏掉！**
A：① 禁 CS 看问题是否消失；② 清 overwrite 生成文件（不含 Shaders 夹），重启重编译；③ 建[最小设置](#通用排查建议)用二分法定位；④ 检查过期功能；⑤ 读本 FAQ。无解则发 Discord 附截图/硬件/日志；若确认 bug 可建 [GitHub Issue](https://github.com/community-shaders/skyrim-community-shaders/issues)。

**Q：启动黑屏但有声？**
A：1.2.0 起独占全屏或渲染/监视器分辨率不符致问题。用**无边框窗口**且分辨率匹配监视器。Display Tweaks 无边框放大不支持，用 [Upscaling](https://www.nexusmods.com/skyrimspecialedition/mods/156952)。仍疑 overlay（RTSS/Fraps）致问题；删 Fraps，禁 RTSS for `SkyrimSE.exe`。

**Q：着色器编译卡数小时或 CTD**
A：先装/更 [VC Redist X64](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist)。弱 CPU 可减 `Background Compiler Threads`/`Compiler Threads`（改 `SettingsUser.json` 或首跑改 `SettingsDefault.json`）。确认受支持 SSE 版、用无边框窗口。仍者发 Discord 崩溃日志。

**Q：眼睛为什么亮？**
A：用 [Improved Eye](https://www.nexusmods.com/skyrimspecialedition/mods/154829)；NPC 需自补或换不此问题 replacer（如 COTR）。

**Q：地形无视差/刺状！**
A：① 用带视差地形纹（如 [Atlantean Landscapes](https://www.nexusmods.com/skyrimspecialedition/mods/89542)、[Terrain Blending Fix](https://www.nexusmods.com/skyrimspecialedition/mods/88261)），须全覆否则刺状；② CS 菜单 `Extended Materials` 勾 `Enable Legacy Terrain`（PBR 地形纹不需）。

**Q：湿润效果坏、有边、全错**
A：禁 Skyrim.ini [Display] 中动态分辨率：`bEnableAutoDynamicResolution=0`；N 卡控制面板‘Antialiasing - Transparency’设关。

**Q：ENB 预设用 Effects 11 不载！**
A：① 预设[受支持](#兼容性)？② 依 [mod.pub 页](https://mod.pub/skyrim-se/415-effects-11) 装：`enbseries` 夹及 `enbseries.ini` 入根目录（或 Data 经管理器，但推荐手动入根）。

## 性能

**Q：最耗 CS 功能？**
A：Screen Space GI（IL 贵，可禁或调 Low）、Effects 11（依预设）、Upscaling（旧系统）、Skylighting（低端可移）。各异，见 `Profiling` 标签。

**Q：性能浮层 “Utility”/“Other” 高！**
A：`Utility` 系阴影等 Bethesda 类型，清 clutter、调阴影设。通用排：调 ini、避高 draw call MOD、查 CPU（单核）/GPU/VRAM 瓶颈、查 FPS 限、减/移 CS 功能、更低 upscaling。用[最小设置](#通用排查建议)判断 CS 是否主因。

**Q：Load Time Profiler 说 CS 启动慢！**
A：编译/水生缓存时会误报，缓存后另测。

## 通用排查建议

**Q：最小设置（Minimal setup）**
A：若 FAQ 未解，隔离 CS 排冲。仅启：Community Shaders、页上 “Additional Features” 所列者、Nexus “requirements/off-site requirements” 及彼等所需者。MO2 新档 `ctrl+a` 禁再启列者；Vortex 新档启列者。确认 VC Redist X64 最新。

**Q：RenderDoc**
A：报 bug 时开发者或要捕获（1.4.6+ 内建）。须用官方最新或指定测试构建。步骤：① CS 菜单 `RenderDoc` 选 `Enable RenderDoc Capture`；② `Save Settings` 重开游戏；③ 见左上 WARNING（性能降正常）；④ 复现 bug 留屏内；⑤ 菜单 `RenderDoc > Create Capture` 后 `Open Capture Directory`；⑥ 传第三方托管（Discord 不支大文件）回链开发者。毕后取消勾选并保存禁捕获。
