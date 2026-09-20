---
id: pbr-for-artists
title: True PBR 美术师与开发者指南
category: 04-development
version: 1.0.0
updated: 2026-09-20
tags: [PBR, 纹理, 网格, 开发, 美术]
source: https://modding.wiki/en/skyrim/developers/community-shaders/true-pbr-home
summary: 面向纹理作者与开发者的 True PBR 完整指南：网格标记、纹理槽位、特殊渲染技法与 MATO。
---

# True PBR 美术师与开发者指南

PBR（物理基础渲染）近似真实材质对光的反应，被多数现代游戏采用。**True PBR** 是 CS 的一部分，优势：

- 比原版/复杂材质更真实的光照，且可组合视差、次表面散射、自发光、双层材质等；
- 可使用广泛可得（含免费）的 PBR 材质；
- 可在 Blender 等标准工具中轻松使用并简单导出；
- 因 PBR 是行业标准，纹理软件皆为之设计，纹理在工具中与在启用 CS 的 Skyrim 中外观一致，无需按 Skyrim 独特亮度/高光盲目修改。

> 使用 PBR 需要 Community Shaders（基础 CS 已含）与 True PBR 纹理包；纹理包无 CS 无法正确渲染（Creation Kit / Outfit Studio / Bodyslide 中也不会正确）。非纹理作者可忽略下文。

## 生成一套 True PBR 纹理（两步）

1. **更新使用这些纹理的网格以启用 PBR**：True PBR 只关心被特定 flag 标记的网格，其余照常渲染。True PBR MOD 因此包含「一组 PBR 纹理 + 标记为 PBR 的网格」，**或**包含告诉 PGPatcher 替换哪些纹理路径、对网格应用哪些值的 JSON（后者更推荐，便于重纹理原版模型或盔甲并允许用户套用到 bodyslide 输出）。
2. **创建 True PBR 纹理**：基础纹理为 albedo（基础色）、normal（DX 格式）、roughness、metallic、ambient occlusion、specular。部分附加特性还需额外纹理（emissive、parallax 等）。

可用 **TruePBR Manager** 将一组 PBR 纹理导出为可用 Skyrim MOD（自动处理通道打包、压缩格式、纹理槽、JSON 与文件夹结构）。

---

## 网格修改（.nif）

### 基础

网格要在 `BSLightingShaderProperty` 中被识别为 PBR，须满足：

- 默认 shader 类型（除非另有说明）；
- `Shader Flags 2` 中设置 `Unused01`（或 PBR）flag；
- 依所用附加特性可能需额外 flag（在各特性小节说明）。

---

## 纹理修改

### 通用纹理（槽位从 1 起）

1. **Base color**：RGB 基础色，A 为不透明度。（sRGB 色彩空间 + DDS flag）
2. **Normal**：RGB 三通道（DX 格式），A 未用。（线性空间 + DDS flag）
3. **Emissive（可选）**：RGB 自发光色，A 未用。（sRGB + DDS flag）
4. **Displacement（可选）**：R 为位移，GBA 未用。（BC4 灰度）
5. 未用。
6. **RMAOS**：R=roughness，G=metallic，B=AO，A=specular。注意 AO：烘焙 AO 纹理所见即所得——黑/0=满 AO，白/255=无 AO。（线性空间 + DDS flag）
7. **Multilayer normal（可选）**：RGB 多层法线，A=roughness（线性）。**Fuzz（可选）**：RGB fuzz 色，A fuzz 权重（sRGB）。
8. **Subsurface（可选）**：RGB 次表面色，A 次表面不透明度（sRGB）。**Multilayer coat（可选）**：RGB 涂层色，A 强度（sRGB）。

**色彩空间规则**：
- 代表游戏中颜色（base color、emissive、fuzz、coat、subsurface 色）→ **sRGB**（部分软件称 gamma 2.2）+ sRGB DDS flag；
- 也可导出线性并保存线性 DDS，但会在人眼最敏感的光谱段损失精度；
- 不代表颜色（normal、displacement、rmaos）→ 始终线性 + 线性 DDS。

### 地形纹理

四叉片（quad）中任一纹理为 PBR，则整个 quad 按 PBR 渲染；若混有原版风格纹理，内部会做转换使其不太违和，但经验法则是**只发布完整地形 MOD**——务必覆盖 DLC（DLC 大量复用基础游戏纹理）。地形 LOD **不会**渲染为 PBR（远景混合）；Dyndolod / xlodgen 会在用户侧由你的 PBR 纹理生成原版风格 LOD 纹理。

---

## 特殊渲染技法

### 次表面散射（Subsurface Scattering）

模拟光在物体内部散射，类似原版 soft lighting 与 back lighting。最适用于树叶、部分织物（旗帜）、蜡烛蜡、龙翼（原版用 back lighting）。注意它始终带 backlighting 效果——玻璃盔甲若开 SSS 会像光穿透角色，务必只在合理处使用。可用烘焙 thickness / transmission 纹理。

参数：
- **Subsurface Color**（替换 Specular Color）：若提供 subsurface 贴图，作为线性乘子。
- **Subsurface Opacity**（替换 Lighting Effect 1）：**越高越弱，越低透光越多**。
- 纹理：槽 8（sRGB）。

与双层材质不兼容；与 glint、fuzz、视差、自发光兼容。

### Fuzz（绒毛）

模拟柔软纤维材质外观（天鹅绒、某些皮毛、桃绒、某些布料）。需：启用 soft lighting flag + multilayer parallax shader 类型；fuzz 纹理入槽 7（fuzz 色 RGB + fuzz 遮罩 A，sRGB）；fuzz color 参数作 fuzz 高光色（无纹理时单独控制，有纹理时作乘子，存前三个 multilayer parallax 参数，建议 [0.08,0.08,0.08] 或 [0.04,0.04,0.04]）；fuzz weight 作遮罩（存第四个参数）。

与双层材质或 glint 不兼容；与 subsurface、视差、自发光兼容。

示例 JSON：
```json
{
    "texture": "clothes\\example", "emissive": false, "parallax": false, "subsurface": false, "specular_level" : 0.04, "subsurface_color": [1,1,1], "roughness_scale" : 1, "subsurface_opacity" : 1, "displacement_scale" : 0,
    "fuzz": { "texture": true, "color": [1.25,1.25,1.25], "weight": 1.0 }
}
```

### 毛发模型（Hair model）

使用 Marschner 毛发模型（模拟 3D 毛发的漫反射、镜面与散射）。CS PBR 毛发着色仍处实验状态。启用：back lighting flag；无需特殊纹理/参数。它是完全不同的着色模型，与任何其它都不兼容；仅对真实 3D 毛发/皮毛有用（原版盔甲上画出来的皮毛不合适）。角色头发请用 CS 的 **Hair Specular** 特性（同技术但更完善）。

### 双层材质（Dual Layer Material）

True PBR 对 Multilayer Parallax 的等价物，用来在常规 PBR 材质上渲染半透明涂层：简单清漆、彩色涂层、涂层法线、层间视差。可用于普通网格（水晶、冰洞壁、stalhrim 盔甲），但**不能用于地形**。与 glint、fuzz、SSS 不兼容；与视差、自发光兼容（辉光来自下层）。

参数（由 MultilayerParallax flag + shader 类型启用）：
- Coat strength（替换 Lighting Effect 1）：涂层贡献 0–1，作涂层强度纹理（槽 8 alpha）乘子；
- Coat roughness（替换 parallax inner layer thickness）：涂层粗糙度，作槽 7 alpha 乘子；
- Coat specular level（替换 parallax refraction scale）：涂层反射率，多数材质 0.04，冰用 0.02；
- EffectLighting flag：启用漫反射贡献（涂层色）；
- SoftLighting：启用层间视差；
- BackLighting：启用涂层自有法线（取槽 7 RGB）。

额外纹理：槽 4 displacement（同常规视差）；槽 7 涂层法线 RGB + 涂层粗糙度 A；槽 8 涂层色 RGB + 涂层强度 A（sRGB）。

（JSON 中 “coat parallax” 即指层间视差。）

### 材质对象（Material Objects / MATO，投影雪、灰等）

MATO 是 ESP/ESM 中的记录。仅带 **single pass** flag 的 MATO 可渲染为 PBR（效果渲染在底层材质之上，贴合其法线与视差）。single pass MATO 与原版 multilayer parallax 及 parallax shader 类型不兼容，但兼容复杂材质。MATO 仅当应用于 PBR 启用表面时才渲染为 PBR。

启用：在插件中设为 single pass，并将同名 editor ID 的 JSON 放入 `data/PBRMaterialObjects`。JSON 中可乘算颜色、高光强度、roughness 缩放，并可选启用 glint 或 fuzz（无纹理时）。

示例 JSON：
```json
{
    "baseColorScale": [0.98, 0.98, 1.0],
    "glintParameters": {
        "densityRandomization": 5.0, "enabled": true,
        "logMicrofacetDensity": 13.0, "microfacetRoughness": 1.0, "screenSpaceScale": 1.0
    },
    "roughness": 0.7, "specularLevel": 0.02
}
```

---

## 纹理创建工作流

- 使用带 PBR 命名 flag 的 [Nifskope（Jonahex 版）](https://github.com/Jonahex) 便于手动改 flag。
- 测试时搭建测试文件夹并配置 **PGtools**（PGPatcher 的 MOD 作者工具，详见 PGPatcher GitHub wiki）以快速批量改动。
- 选正确 specular 强度：多数材质 0.04；雪/冰/水 0.02；钻石 0.16（按 Reflectance F0 列）。
