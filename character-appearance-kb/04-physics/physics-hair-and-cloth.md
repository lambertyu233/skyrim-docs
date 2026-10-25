---
id: physics-hair-and-cloth
title: 物理头发与衣物
category: 04-physics
kind: concept
version: 2.0.0
updated: 2026-10-25
tags: [物理, 头发, 衣服, SMP, 斗篷]
aliases: [物理头发, 物理衣服, hdt 头发, 假发, cloth physics, 斗篷物理, 头发不飘, 头发穿透, 裙子物理, 物理发型, smp detail, smp dumptree, 头发物理怎么装]
source: https://github.com/DaymareOn/hdtSMP64
summary: 头发与衣物物理为什么只能靠 SMP、它们靠 .xml 配置而非骨骼动画工作、挂点（XPMSE 的 hair/头部节点）、smp detail/dumptree/list/report 排查手段，以及常见失败表现与判据。
---

# 物理头发与衣物

> **一句话**：头发和衣物的物理**只能靠 SMP**（实际装 [FSMP](faster-hdt-smp.md)），
> 靠每个 mod 自带的 `.xml` 配置工作——[CBPC](cbpc.md) 在机制上就管不了它们。

## 速览

| 项 | 内容 |
|---|---|
| 唯一方案 | **HDT-SMP / FSMP**（Bullet + 蒙皮网格逐顶点）；CBPC 的球体方案**原理上不可能**处理头发衣物 |
| 配置形态 | 每个物理发型/衣物 mod 自带 `Data/SKSE/Plugins/hdtSkinnedMeshConfigs/*.xml` |
| 挂点 | XPMSE 的头部/发骨节点（`Head` 及额外发骨）；斗篷/裙摆挂躯干节点 |
| 硬依赖 | XPMSE（human skeleton）+ SKSE64；引擎本身不提供任何配置 |
| 关键限制 | NPC 的 facegen 头部件物理有专门约束（见下文）；non-wig 头发在 NPC 上大多需改约束 |
| 诊断工具 | `smp report` / `smp detail` / `smp dumptree` / `smp list` |

要点：

- **引擎不认物品**：FSMP wiki 原话——*"It doesn't provide any xml physics
  configuration file. It doesn't know the difference between a cape and a breast."*
  所以"某件斗篷不飘"通常是**那个 mod 的问题，不是引擎的问题**。
- **没有 XML 就没有物理**——这是"死活不飘"的第一嫌疑，`smp report` 一发定位。
- 头发物理**不是骨骼动画**：BBP/TBBP 时代"写在动画里"的思路在这里不适用，
   SMP 是每帧对蒙皮网格顶点实算。
- 物理发型通常带**碰撞体定义**（与身体/其他头发撞），这才是"不穿透"的来源。

## 前世今生

| 时间 | 事件 | 意义 |
|---|---|---|
| LE 早期 | BBP/TBBP 动画式方案只覆盖身体；头发基本没有物理 | "抖"是回放动画，与头发无关 |
| 2015 前后 | HDT-SMP 早期测试即被描述为 "mesh/bullet based" | 网格级物理首次可行，头发/斗篷进入射程 |
| 2016-2018 | `hdtSkinnedMeshConfigs` XML 体系成为 modder 标准；物理版发型（如 KS Hairdos SMP 碰撞 bodyslides）出现 | 头发物理成为可分发的资产：mesh + XML 一对 |
| 2019-2021 | Karonar1 等 fork 支持 facegen 头部件物理（有限制）、`smp list` 等诊断命令 | NPC 头发物理从"基本不可用"到"可用但有条件" |
| 2021-10 起 | FSMP 成为主线，内置 `smp report` 校验整个 load order | 排错从"逐个试"变成"一键定位" |
| 2026 | FSMP 4.1.1；物理发型/衣物已是主流发行形态 | 生态成熟：新发型默认带 SMP 配置 |

### 它从哪来

头发物理的需求来自"假发不自然"：静态假发在转头、跑动时像头盔。SMP 的逐顶点
蒙皮模拟第一次让头发能随运动实时摆动并与身体碰撞。代价是**每个要动的网格都要有
一份配置**——于是形成了"引擎（FSMP）+ 每 mod 的 XML"的分层生态。

### 中间经历了什么

关键节点是 **facegen 头部件支持**（Karonar1 代）：代码能解析 facegen 文件结构，
head part 物理在 NPC 上"可以工作（有限制）"，不必再手改 facegen 数据。
但限制也来自同一处（见下文「NPC 的专门限制」）。

### 现状

主流发型/衣物 mod 默认发行 SMP 版本；**"没物理"反而成了需要专门检查的状态**。
FSMP 官方 wiki 把话说得很直：分不清斗篷和胸，问题在单个 mod 就去该 mod 的页面找。

配套背景：头发/衣物物理与身体物理的分工见 [physics-overview.md](physics-overview.md)，
引擎与配置格式见 [hdt-smp.md](hdt-smp.md)，命令与排错见
[faster-hdt-smp.md](faster-hdt-smp.md)。

## 它解决什么问题

**没有它之前**：

- 头发是**静态网格**：跑步时头发穿进肩膀、斗篷像木板；
- BBP/TBBP 式"动画驱动"只服务身体部位，且动作生硬、与环境无关；
- HDT-PE 的骨骼级方案对头发这种"整体形变"无能为力。

**SMP 的解法**：

```
物理发型 = 蒙皮网格（.nif，挂 XPMSE 头部节点）
         + XML 配置（hdtSkinnedMeshConfigs/<mod>.xml）
              ├─ 碰撞体（sphere/capsule/triangle）挂到哪些骨
              ├─ 哪些顶点参与模拟、约束多硬
              └─ 重力/阻尼/风力
→ FSMP 每帧用 Bullet 求解 → 顶点位移 → 渲染
```

## 挂点

- 头发通常挂到**头部骨骼（`Head`）及额外发骨**；
- XPMSE 提供相关节点（见 [xpmse-skeleton.md](xpmse-skeleton.md)）；
- 斗篷/裙摆挂躯干相关节点；碰撞体一般包含身体（"头发撞肩膀"就是这么来的）。

### NPC 的专门限制（重要）

给 NPC 换物理发型比给玩家换更容易出问题，限制来自 facegen 数据结构
（Karonar1 README，社区技术文档）：

| 限制 | 说明 |
|---|---|
| 一张脸只用一个 XML | 即使脸由多个物理部件拼成，**每个 face 只能应用一个 XML** |
| `NiStringExtraData` 不自动复制 | facegen 文件不会自动带入物理标记，要么 NifSkope 手改，要么在 `defaultBBPs.xml` 里映射 |
| 未引用骨会被删 | facegen 生成时不被任何网格显体引用的骨会被移除，**不能作为约束的运动骨**——用 NPC head 代替，并按需设参考原点 |
| non-wig 头发大多不工作 | 大多数 HDT 头发作为 non-wig 形态在 NPC 上**不改约束就不工作** |

> 所以"给 NPC 换物理发型不生效"优先考虑：换 wig 形态、检查是否踩了上面四条。
> 这与玩家角色无关——玩家捏人时的 head parts 不走 facegen 预生成路径。

### 给 NPC 换物理发型的实操建议

1. **优先选 wig 形态**的物理发型——non-wig 形态受上表第四条限制；
2. 一个脸只认一个 XML：拼了多个物理部件时，确认最终 facegen 用的是哪份配置；
3. 手改 facegen 用 **NifSkope** 补 `NiStringExtraData`，或在 `defaultBBPs.xml`
   里把某个 head part 映射到配置文件；
4. 约束要挂的骨如果被 facegen 删了，改用 **NPC head** 并设好参考原点；
5. 换完用 `smp detail` 确认该 NPC 的 head part 是否进入引擎追踪列表。

## 排查手段

FSMP 的控制台命令是头发/衣物物理的一手诊断工具：

```
smp report [gear] [warnings]   校验整个 load order 的物理 XML 与 .nif（默认只报错误）
smp detail                     全部被追踪 actor 的详细信息：生效/失效的护甲与 head part
smp dumptree                   导出当前目标 NPC 的整棵节点树到日志
smp list                       精简列表：哪些 NPC 被追踪、按激活状态排序
```

使用路径：

1. **先 `smp report`**：告诉你哪个 mod 的 XML 有警告/错误——比逐个 mod 试高效得多；
2. **`smp detail`**：确认目标 NPC 的头发部件到底有没有被引擎追踪、护甲是否生效；
3. **`smp dumptree`**：把节点树导出到日志，核对挂点骨名是否与 XML 写的一致；
4. **`smp list`**：拥挤场景下确认 NPC 是否因距离/角度被引擎关闭（那会让物理"消失"）。

## 物理与 morph 是两回事（别混）

头发/衣物身上同时存在两套互不相干的系统，排查时先分清症状落在哪套：

| | 物理（本页） | morph（滑块变形） |
|---|---|---|
| 改什么 | 每帧的**顶点位置**（模拟运动） | 相对基准形状的**顶点位移**（改形状） |
| 谁驱动 | FSMP/Bullet + XML | RaceMenu/NiOverride + `.tri` 数据 |
| 症状长什么样 | 不飘、穿模、抽搐、鬼畜 | 衣服与身体对不上、滑块无效 |
| 去哪查 | 本页 + `smp report` | [morph-runtime-vs-bake.md](../03-body/morph-runtime-vs-bake.md) |

> "头发形状不对"是 morph 问题；"头发不动/乱抖"才是物理问题。
> 3BA 的物理骨骼与顶点权重负责抖，morph 数据负责形，互不替代。

## 风力

SMP 的 XML 与 FSMP 菜单都支持风力参数（FSMP 在 ImGui 菜单的 **Wind** 页）：

- 每个物品的 XML 可定义受风影响的程度；
- FSMP 内置原生风实现，可设风力缩放与计算距离截断；
- 第三方风插件（如风气场类 mod）可能与内置风叠加——"风太大/风向诡异"时
  先关一个来源再观察。

## 常见失败表现

| 表现 | 判据 | 处理 |
|---|---|---|
| 头发完全不动 | 只装了 CBPC（机制限制）；或发型没有 XML；或 FSMP 未生效 | 装 FSMP；确认 `hdtSkinnedMeshConfigs` 有对应 XML；跑 `smp report` |
| 某一件斗篷不飘、别的都飘 | 那件物品没有 XML 或被覆盖 | `smp report` 定位；查覆盖关系（[mo2-override-rules.md](../07-workflow/mo2-override-rules.md)） |
| 头发穿过身体 | 碰撞体没定义或不匹配身形 | 检查该发型 XML 的碰撞体定义；换匹配身形的配置 |
| 头发抽搐/抖动异常 | XML 参数问题（刚度/阻尼/时间步） | `smp report` 找警告；调 XML 或换预设 |
| 衣服飘但头发不飘 | 只有衣服带了 XML | 给发型补 SMP 版本/配置 |
| NPC 头发不动、玩家动 | 踩了 facegen 四条限制之一 | 见上文「NPC 的专门限制」 |
| 拥挤城市里 NPC 头发突然静止 | 被引擎的距离/角度剔除关闭（设计行为） | `smp list` 确认；需要就调剔除参数 |
| 开局 CTD | FSMP 版本档选错 | FOMOD 重选游戏版本档（见 [faster-hdt-smp.md](faster-hdt-smp.md)） |
| 物理发色错误 | 附近两个 NPC 用同一发型模型的已知问题 | 等上游修复；暂时避开同发型 NPC 同屏 |
| 头发"飘 but 穿模"到武器/盾牌上 | 该物品的碰撞体没把武器骨纳入（或用了 `no-collide-with-bone`） | 检查 XML 的碰撞骨定义；SMP 支持 `can-collide-with-bone` 显式纳入 |
| `smp reset` 后某件斗篷不恢复 | 已知问题（Artesian Cloaks 类物品，原始三角形网格引用被释放） | 读档规避；等上游修复（见 [faster-hdt-smp.md](faster-hdt-smp.md)） |
| physics 开启但只有玩家生效、NPC 全静止 | 引擎的 NPC 距离/视野剔除把远处角色关了（设计行为，非 bug） | `smp list` 确认；在菜单 Simplification 页调距离/角度阈值 |

## 兼容与冲突

| 关系 | 结论 |
|---|---|
| 与 CBPC | 互补不冲突：CBPC 管身体、SMP 管头发衣物；但两者争身体插槽，需分腔（[physics-overview.md](physics-overview.md)） |
| 与原版 HDT-SMP | 不要与 FSMP 混装 |
| 与 XPMSE | 硬依赖（human skeleton 挂点） |
| 与其他覆盖 mesh 的 mod | 后装的 nif 会覆盖物理网格 ⇒ 静默失效，查覆盖 |
| 与风力 mod | FSMP 有内置风参数（菜单 Wind 页）；第三方风插件可能叠加 |

## 取舍与建议

- **要头发/衣物物理就没有第二条路**：装 FSMP，并接受"每个物品要有 XML"的生态规则；
- **排错纪律**：先 `smp report`，再 `smp detail`，最后才怀疑引擎；
- **给 NPC 换发型**：优先 wig 形态；遇到 facegen 限制先查四条表格，别急着改 XML；
- **性能敏感**：用菜单里的 `Performance.xml` 预设压档，CPU 支持就开 AVX2；
- **别做的**：给香草身体期待头发物理（没有挂点与权重）；同时装原版 SMP 与 FSMP；
  遇到不飘就手改 XML——先用 `smp report` 确认是不是真的缺配置；
- **modder 向**：遵循 SMP Modder Guide 的 XSD/Schematron schema 写配置，
  动态控制物理可用 DynamicHDT Papyrus API（从脚本启停/控制单个系统）。

## 来源

- **"CBPC 不能管头发和衣服，必须有 SMP"**：LoversLab 多帖一致 —— **社区经验（多帖一致）**
- **XML 目录 `hdtSkinnedMeshConfigs`、schema（XSD/Schematron）、`smp report`
  （校验整个 load order）、"引擎不提供任何 XML 配置 / 分不清斗篷和胸"、
  SMP Modder Guide、DynamicHDT Papyrus API**：FSMP 官方仓库 README / wiki —— **一手**
  `https://github.com/DaymareOn/hdtSMP64`
- **`smp detail` / `smp dumptree` / `smp list` 命令**：FSMP-MCM 仓库 README
  （"smp list, smp detail, and smp dumptree"）+ aers/Karonar1 README（`smp list`
  的诞生与"按激活状态排序"）—— **一手（配套项目 + 上游仓库）**
- **挂到 Head 及额外发骨、facegen 头部件四条限制（一脸一 XML、NiStringExtraData
  不复制、未引用骨被删、non-wig 头发需改约束）、物理发色偶发错误**：
  Karonar1 的 hdtSMP64 README —— **社区技术文档（上游维护者自述）**
- **"mesh/bullet based physics"（SMP 早期定性）**：LoversLab 2015 测试帖 ——
  **社区经验（早期用户实测）**
- **物理发型生态形态（如 KS Hairdos SMP 碰撞 bodyslides "setup to support 3BA v2"）**：
  Nexus 73324 描述 —— **一手（依赖页）**（另见 [cbbe-3ba.md](../03-body/cbbe-3ba.md)）
- **失败表现与成因**：综合社区帖归纳 —— **社区经验**
- **FSMP 内置风参数（ImGui 菜单 Wind 页）与距离截断**：FSMP 官方仓库提交记录
  与 wiki —— **一手**
- **"物理负责每帧顶点位置、morph 负责形状位移，两套机制互不替代"**：
  本工作区依据 HDT-SMP 机制与 morph 管线的归纳 —— **本工作区实测（机制归纳）**
