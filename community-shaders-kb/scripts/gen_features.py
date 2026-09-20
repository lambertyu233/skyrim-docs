#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_features.py — 生成 Community Shaders 功能特性条目

设计目标（可维护性）：
- 所有功能以「数据」形式集中在此脚本的 FEATURES 列表中。
- 新增 / 删除 / 修改一个功能，只需编辑 FEATURES，然后重新运行本脚本
  （或运行 build_index.py 仅刷新索引）。
- 每个功能生成独立 markdown 文件（含 frontmatter），可单独增删改查。

运行：managed python gen_features.py
"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_VERSION = "1.0.0"
UPDATED = "2026-09-20"
WIKI = "https://modding.wiki/en/skyrim/developers/community-shaders"

# 每条功能: id, title, kind(核心/附加), status(released/TBA), summary, details, tags, link
FEATURES = [
    # ---------------- 核心特性 (Base CS 自带) ----------------
    dict(id="cloud-shadows", title="Cloud Shadows 云影", kind="core", status="released",
         summary="动态云层阴影投射到广阔地形上。",
         details="让云层在地面投射实时移动的阴影，增强户外场景的真实感与时间感。",
         tags=["阴影", "户外", "天气"], link=f"{WIKI}/Features-Home/cloud-shadows"),
    dict(id="cs-editor", title="CS Editor 编辑器", kind="core", status="released",
         summary="实时天气与 imagespace 编辑器，服务所有 MOD 制作需求。",
         details="为 MOD 作者提供的实时编辑工具，可调整天气与 imagespace 参数。",
         tags=["开发工具", "天气"], link=f"{WIKI}/Features-Home"),
    dict(id="dynamic-cubemaps", title="Dynamic Cubemaps 动态立方体贴图", kind="core", status="released",
         summary="实时反射映射，增强环境反射效果（1.0+ 已并入核心）。",
         details="1.0 版本起并入核心，无需单独安装。提供实时环境反射。",
         tags=["反射", "环境"], link=f"{WIKI}/Features-Home/dynamic-cubemaps"),
    dict(id="extended-materials", title="Extended Materials 扩展材质", kind="core", status="released",
         summary="地形与物体视差（parallax）及其它高级效果，需支持纹理与网格修补。",
         details="开启地形/物体视差等高级材质效果。需要配套的支持 PBR/视差的纹理与网格（PGPatcher 修补）。",
         tags=["材质", "视差"], link=f"{WIKI}/Features-Home/extended-materials"),
    dict(id="extended-translucency", title="Extended Translucency 扩展半透明", kind="core", status="released",
         summary="增强的半透明材质渲染（1.4.7+ 已并入核心）。",
         details="1.4.7 起并入核心。改善玻璃、液体等半透明物体的渲染。",
         tags=["半透明", "材质"], link=f"{WIKI}/Features-Home/extended-translucency"),
    dict(id="grass-collision", title="Grass Collision 草体碰撞", kind="core", status="released",
         summary="真实草体交互与碰撞检测（1.5+ 已并入核心）。",
         details="1.5 起并入核心。让角色与草体产生真实的物理交互。",
         tags=["草地", "物理"], link=f"{WIKI}/Features-Home/grass-collision"),
    dict(id="grass-lighting", title="Grass Lighting 草体光照", kind="core", status="released",
         summary="改进植被光照计算，部分功能需支持的草 MOD（1.5+ 已并入核心）。",
         details="1.5 起并入核心。提升草与植被的光照表现，某些特性需配套草 MOD 支持。",
         tags=["草地", "光照"], link=f"{WIKI}/Features-Home/grass-lighting"),
    dict(id="image-based-lighting", title="Image Based Lighting 基于图像光照", kind="core", status="released",
         summary="用立方体贴图球谐推导的物理化 IBL 替换游戏环境光。",
         details="以 cubemap 球谐（spherical harmonics）推导的基于图像光照替换原版环境光，提升整体光照一致性与真实感。",
         tags=["光照", "IBL"], link=f"{WIKI}/Features-Home"),
    dict(id="interior-sun", title="Interior Sun 室内阳光", kind="core", status="released",
         summary="室内随昼夜变化的进阶阴影投射，需支持的照明 MOD。",
         details="为室内空间带来随时间变化的阴影投射，需要配套支持的照明 MOD。",
         tags=["室内", "阴影", "光照"], link=f"{WIKI}/Features-Home"),
    dict(id="inverse-square-lighting", title="Inverse Square Lighting 平方反比光照", kind="core", status="released",
         summary="物理精确的光照衰减计算，需支持的照明 MOD（1.4.7+ 已并入核心）。",
         details="1.4.7 起并入核心。按平方反比规律计算点光衰减，更符合物理真实，需配套照明 MOD。",
         tags=["光照", "物理"], link=f"{WIKI}/Features-Home/inverse-square-lighting"),
    dict(id="light-limit-fix", title="Light Limit Fix 光源上限修复", kind="core", status="released",
         summary="移除引擎对动态光源数量的限制，视野内可超过 4 个光源（1.4+ 已并入核心）。",
         details="1.4 起并入核心。解除原版引擎动态光源数量限制（阴影投射上限不变）。安装 Lux 时请勿勾选其“optimized”网格，CS LLF 已替代它们。",
         tags=["光照", "性能", "引擎修复"], link=f"{WIKI}/Features-Home/light-limit-fix"),
    dict(id="lod-blending", title="LOD Blending LOD 混合", kind="core", status="released",
         summary="对 LOD 物体与地形的光照特性做精细控制。",
         details="提供 LOD 物体与地形光照特性的微调控制，缓解近景与远景光照差异。",
         tags=["LOD", "光照"], link=f"{WIKI}/Features-Home"),
    dict(id="nrd", title="NRD 实时降噪", kind="core", status="released",
         summary="集成 NVIDIA 实时降噪器，供 SSGI、SSR 等使用。",
         details="NVIDIA Real-Time Denoisers 集成，为屏幕空间全局光照（SSGI）、屏幕空间反射（SSR）等提供降噪。",
         tags=["降噪", "屏幕空间"], link=f"{WIKI}/Features-Home"),
    dict(id="performance-overlay", title="Performance Overlay 性能浮层", kind="core", status="released",
         summary="实时监测帧率、绘制调用与性能指标。",
         details="在游戏内实时显示 FPS、draw calls 及各项性能开销，便于定位瓶颈（见 FAQ 性能章节）。",
         tags=["性能", "监测"], link=f"{WIKI}/Features-Home/performance-overlay"),
    dict(id="remote-control", title="Remote Control 远程控制", kind="core", status="released",
         summary="向外部 devbench 暴露开发者工具，支持 AI 辅助开发。",
         details="将 CS 开发者工具暴露给外部 devbench，便于 AI 辅助开发调试。",
         tags=["开发工具"], link=f"{WIKI}/Features-Home"),
    dict(id="renderdoc", title="RenderDoc 捕获", kind="core", status="released",
         summary="内置 RenderDoc 截图捕获，便于开发调试（1.4.6+）。",
         details="1.4.6 起内置。报 bug 时开发者可能要求提供 RenderDoc 捕获，详见 FAQ 的 RenderDoc 章节。",
         tags=["开发工具", "调试"], link=f"{WIKI}/faq#renderdoc"),
    dict(id="scene-manager", title="Scene Manager 场景管理器", kind="core", status="released",
         summary="按室内/室外、昼夜、天气、地点套用选定 CS 设置。",
         details="可根据不同场景（室内外、时间、天气、位置）自动套用不同的 CS 设置组合。",
         tags=["配置", "场景"], link=f"{WIKI}/Features-Home"),
    dict(id="screen-space-shadows", title="Screen Space Shadows 屏幕空间阴影", kind="core", status="released",
         summary="屏幕空间增强阴影渲染（1.5+ 已并入核心）。",
         details="1.5 起并入核心。在屏幕空间增强阴影质量，替代 ENB 的 Shadow/Detailed Shadow。",
         tags=["阴影", "屏幕空间"], link=f"{WIKI}/Features-Home/screen-space-shadows"),
    dict(id="screenshot", title="Screenshot 截图", kind="core", status="released",
         summary="不卡顿地捕获带 HDR 能力的截图。",
         details="支持 HDR 截图捕获，且不会造成游戏停顿。",
         tags=["截图", "HDR"], link=f"{WIKI}/Features-Home"),
    dict(id="sky-sync", title="Sky Sync 天空同步", kind="core", status="released",
         summary="真实日月沿天空运动（1.7+ 已并入核心）。",
         details="1.7 起并入核心，替代 EVLaS/AELaS。提供真实日月运动轨迹。",
         tags=["天空", "天体"], link=f"{WIKI}/Features-Home/sky-sync"),
    dict(id="subsurface-scattering", title="Subsurface Scattering 次表面散射", kind="core", status="released",
         summary="真实光线穿透半透明材质（如皮肤）（1.5+ 已并入核心）。",
         details="1.5 起并入核心。模拟光线在半透明材质内部的散射，常用于皮肤、树叶、蜡烛等。与双层材质不兼容，但与 glint/fuzz/视差/自发光兼容。",
         tags=["皮肤", "散射", "材质"], link=f"{WIKI}/Features-Home/subsurface-scattering"),
    dict(id="terrain-shadows", title="Terrain Shadows 地形阴影", kind="core", status="released",
         summary="无限距离粗糙地形阴影，游戏内与世界地图均生效（1.4.7+ 已并入核心）。",
         details="1.4.7 起并入核心。提供无限距离的粗糙地形阴影，在游戏内与世界地图上都有效。",
         tags=["地形", "阴影"], link=f"{WIKI}/Features-Home/terrain-shadows"),
    dict(id="true-pbr", title="True PBR 物理渲染", kind="core", status="released",
         summary="支持物理基础渲染，需支持的纹理与网格修补。",
         details="CS 的 PBR 渲染支持，带来更真实光照并可组合视差、SSS、自发光、双层材质等效果。需要 PBR 纹理与网格（PGPatcher）修补。详见 04-development/pbr-for-artists.md。",
         tags=["PBR", "材质", "纹理"], link=f"{WIKI}/true-pbr-home"),
    dict(id="unified-water", title="Unified Water 统一水体", kind="core", status="released",
         summary="将真实水体瓦片延伸到 LOD，消除水 LOD 接缝并改善着色。",
         details="把真实水体瓦片扩展到 LOD 范围，消除远处水体的 LOD 接缝并改善 LOD 中的水着色。",
         tags=["水", "LOD"], link=f"{WIKI}/Features-Home"),
    dict(id="vanilla-fresnel", title="Vanilla Fresnel 原版菲涅尔", kind="core", status="released",
         summary="为非 PBR 材质添加真实环境反射。",
         details="为未启用 PBR 的原版材质补充基于菲涅尔的环境反射，提升反射真实感。",
         tags=["反射", "材质"], link=f"{WIKI}/Features-Home"),
    dict(id="volumetric-lighting", title="Volumetric Lighting 体积光照", kind="core", status="released",
         summary="动态体积光照效果。",
         details="提供动态体积光（如光束、雾中光照）效果。",
         tags=["体积光", "光照"], link=f"{WIKI}/Features-Home"),
    dict(id="volumetric-shadows", title="Volumetric Shadows 体积阴影", kind="core", status="released",
         summary="降采样 VSM 阴影贴图，供粒子、贴花等使用。",
         details="使用降采样的方差阴影贴图（VSM），为粒子、贴花等效果提供阴影。",
         tags=["阴影", "粒子"], link=f"{WIKI}/Features-Home"),
    dict(id="water-effects", title="Water Effects 水特效", kind="core", status="released",
         summary="水的视差与焦散，视差需支持的水 MOD（1.4.7+ 已并入核心）。",
         details="1.4.7 起并入核心。提供水的视差与焦散效果；视差需要支持的 Water MOD。替代 ENB 的 Reflection/Water/Underwater。",
         tags=["水", "焦散", "视差"], link=f"{WIKI}/Features-Home/water-effects"),

    # ---------------- 附加特性 (需单独下载) ----------------
    dict(id="advanced-skin", title="Advanced Skin 进阶皮肤", kind="additional", status="TBA",
         summary="以多种技术增强角色皮肤渲染。[TBA]",
         details="开发中（TBA）。计划用多种技术提升角色皮肤渲染质量。",
         tags=["皮肤", "角色"], link=f"{WIKI}/Features-Home"),
    dict(id="effects-11", title="Effects 11 后处理", kind="additional", status="released",
         summary="通过 FX11 框架支持未加密 ENB 预设。",
         details="支持加载未加密的 ENB 预设（FX11 框架）。详见 ENB 迁移指南。注意：不支持 DoF、天空散射、Prepass；加密预设须先解密。可于 mod.pub 获取。",
         tags=["ENB", "后处理", "预设"], link="https://mod.pub/skyrim-se/415-effects-11"),
    dict(id="exponential-height-fog", title="Exponential Height Fog 指数高度雾", kind="additional", status="released",
         summary="随高度增加密度、更真实的雾效。",
         details="添加随高度指数增长的真实雾效，改善远景雾化表现。",
         tags=["雾", "天气"], link="https://www.nexusmods.com/skyrimspecialedition/mods/180146"),
    dict(id="grass-optimizations", title="Grass Optimizations 草优化", kind="additional", status="released",
         summary="围绕 GPU 驱动剔除与实例化重写草渲染。",
         details="以 GPU 驱动的剔除与实例化重写草地渲染，显著提升草地性能。",
         tags=["草地", "性能"], link="https://www.nexusmods.com/skyrimspecialedition/mods/188628"),
    dict(id="hair-specular", title="Hair Specular 毛发高光", kind="additional", status="released",
         summary="带真实高光的增强毛发渲染。",
         details="为角色毛发提供增强的真实高光。可与 True PBR 的 Marschner 毛发模型互补（后者偏实验性）。",
         tags=["毛发", "高光"], link="https://www.nexusmods.com/skyrimspecialedition/mods/149011"),
    dict(id="hdr-display", title="HDR Display HDR 显示", kind="additional", status="released",
         summary="对支持的显示器输出原生 HDR。",
         details="为支持的显示设备提供原生 HDR 输出。",
         tags=["HDR", "显示"], link="https://www.nexusmods.com/skyrimspecialedition/mods/179371"),
    dict(id="horizon-fix", title="Horizon Fix 地平线修复", kind="additional", status="released",
         summary="改善地平线外观。",
         details="修正/改善游戏地平线的视觉表现。",
         tags=["地平线", "天空"], link="https://www.nexusmods.com/skyrimspecialedition/mods/184607"),
    dict(id="linear-lighting", title="Linear Lighting 线性光照", kind="additional", status="TBA",
         summary="内部色彩空间转换以提升光照计算精度。[TBA]",
         details="开发中（TBA）。在内部做色彩空间转换，提高光照计算精度。",
         tags=["光照", "色彩空间"], link=f"{WIKI}/Features-Home"),
    dict(id="order-independent-transparency", title="Order Independent Transparency 顺序无关透明", kind="additional", status="released",
         summary="正确混合重叠的透明表面。",
         details="以顺序无关透明（OIT）技术正确混合多层重叠的透明表面。",
         tags=["透明", "渲染"], link="https://www.nexusmods.com/skyrimspecialedition/mods/187431"),
    dict(id="post-processing", title="Post Processing 后处理", kind="additional", status="TBA",
         summary="进阶图像特效，Effects 11 的继任者。[TBA]",
         details="开发中（TBA）。进阶图像特效与增强，是 Effects 11 的继任者，将支持 DoF 等 Effects 11 不支持的特性，并充分利用 Linear Lighting 与 HDR Display。",
         tags=["后处理", "ENB替代"], link=f"{WIKI}/Features-Home"),
    dict(id="ssgi", title="SSGI 屏幕空间全局光照", kind="additional", status="released",
         summary="实时间接光照模拟（间接光反弹），开销较高。",
         details="实时屏幕空间全局光照，模拟光线遮挡与反弹带来的间接照明，质量显著高于 ENB SSAO/IL，但性能开销大（可在 Low 档或关闭）。依赖 NRD 降噪。替代 ENB 的 SSAO/IL。",
         tags=["全局光照", "屏幕空间", "性能"], link="https://www.nexusmods.com/skyrimspecialedition/mods/130375"),
    dict(id="screen-space-reflections", title="Screen Space Reflections 屏幕空间反射", kind="additional", status="TBA",
         summary="层级化屏幕空间镜面反射。[TBA]",
         details="开发中（TBA）。层级化（hierarchical）屏幕空间镜面反射。",
         tags=["反射", "屏幕空间"], link=f"{WIKI}/Features-Home"),
    dict(id="skylighting", title="Skylighting 天光遮蔽", kind="additional", status="released",
         summary="模拟大规模世界空间环境光遮蔽（AO）。",
         details="模拟大尺度的世界空间环境光遮蔽，提升遮蔽区域（屋檐下、树荫、建筑内）的真实感，质量高于 ENB 版本。替代 ENB 的 Skylighting。低端机可考虑移除。",
         tags=["环境光遮蔽", "户外"], link="https://www.nexusmods.com/skyrimspecialedition/mods/139352"),
    dict(id="snow-deformation", title="Snow Deformation 积雪形变", kind="additional", status="TBA",
         summary="角色踩过积雪可被压陷并留下持久痕迹。[TBA]",
         details="开发中（TBA）。积雪可被角色/生物踩压变形并留下持久轨迹。",
         tags=["雪", "物理"], link=f"{WIKI}/Features-Home"),
    dict(id="terrain-blending", title="Terrain Blending 地形混合", kind="additional", status="released",
         summary="将地形混合进地形网格，消除接缝。",
         details="把地形混合到地形网格中，减少地形衔接处的硬边/接缝。",
         tags=["地形", "混合"], link="https://www.nexusmods.com/skyrimspecialedition/mods/157076"),
    dict(id="terrain-helper", title="Terrain Helper 地形辅助", kind="additional", status="released",
         summary="为非 PBR 地形 MOD 增加额外纹理层以优化贴图。",
         details="为非 PBR 的景观 MOD 提供额外的纹理层，从而生成更优化的地图。",
         tags=["地形", "纹理"], link="https://www.nexusmods.com/skyrimspecialedition/mods/143149"),
    dict(id="terrain-variation", title="Terrain Variation 地形变化", kind="additional", status="released",
         summary="在不损失质量的前提下打破原版地形平铺问题。",
         details="打破原版地形的重复平铺感，且不带来画质下降。",
         tags=["地形", "平铺"], link="https://www.nexusmods.com/skyrimspecialedition/mods/148123"),
    dict(id="upscaling", title="Upscaling 超分与帧生成", kind="additional", status="released",
         summary="DLSS 4.5/FSR 3.1 超分与 FSR 3.1 帧生成。",
         details="集成超分技术（DLSS 4.5 / FSR 3.1）与 FSR 3.1 帧生成，提升帧率。与 Skyrim Upscaler 冲突，与 Display Tweaks 的 Borderless upscale 不兼容，需无边框窗口。替代 ENB 的抗锯齿/帧生成。",
         tags=["超分", "帧生成", "DLSS", "FSR", "性能"], link="https://www.nexusmods.com/skyrimspecialedition/mods/156952"),
    dict(id="wetness-effects", title="Wetness Effects 湿润特效", kind="additional", status="released",
         summary="动态表面湿润与降雨交互、自定义雨涟漪。",
         details="提供动态表面湿润、降雨交互与自定义雨滴涟漪。注意：需在 Skyrim.ini [Display] 关闭 bEnableAutoDynamicResolution=0；N 卡控制面板将 Antialiasing-Transparency 设为关，否则会出现边缘/错误。",
         tags=["湿润", "雨", "天气"], link="https://www.nexusmods.com/skyrimspecialedition/mods/112739"),
]


def render(f):
    kind_cn = "核心特性" if f["kind"] == "core" else "附加特性"
    status_cn = "已发布" if f["status"] == "released" else "开发中 (TBA)"
    tags_line = ", ".join(f["tags"])
    body = f"""---
id: {f['id']}
title: {f['title']}
category: features
kind: {f['kind']}
status: {f['status']}
version: {KB_VERSION}
updated: {UPDATED}
tags: [{tags_line}]
source: {f['link']}
summary: {f['summary']}
---

# {f['title']}

> 分类：{kind_cn} · 状态：{status_cn}

{f['summary']}

## 说明

{f['details']}

## 维护信息

- 类型：{kind_cn}
- 状态：{status_cn}
- 标签：{tags_line}
- 官方来源：{f['link']}

---
*本条目由 gen_features.py 自动生成，修改请编辑脚本后重跑，或直接在源站更新后同步。*
"""
    return body


def main():
    out_core = os.path.join(BASE, "02-features", "core")
    out_add = os.path.join(BASE, "02-features", "additional")
    count = 0
    for f in FEATURES:
        sub = out_core if f["kind"] == "core" else out_add
        path = os.path.join(sub, f"{f['id']}.md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(render(f))
        count += 1
    print(f"Generated {count} feature entries under 02-features/")


if __name__ == "__main__":
    main()
