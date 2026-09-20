# Open Animation Replacer (OAR) 教程文档

> **开源动画替换框架 · 完整使用与配置指南**
>
> 本文整理自两个官方来源：
> - **OAR 本体**（Nexus Mods mod 92109）— 作者 Ersh，当前版本 3.2.1
> - **OAR - Detection Plugin**（Nexus Mods mod 104806）— 作者 Nonameron，OAR 的检测条件扩展插件
>
> 适用版本：Skyrim Special Edition / Anniversary Edition / VR（1.5.97、1.6+ 均可）

---

## 目录

1. [OAR 是什么](#一oar-是什么)
2. [前置需求与安装](#二前置需求与安装)
3. [核心概念：Replacer Mod 与 Submod](#三核心概念replacer-mod-与-submod)
4. [文件结构：动画放在哪、怎么替换](#四文件结构动画放在哪怎么替换)
5. [游戏内编辑器（Shift + O）](#五游戏内编辑器shift--o)
6. [条件（Conditions）完整清单](#六条件conditions完整清单)
7. [子模组附加设置](#七子模组附加设置additional-settings)
8. [动画变体（Variants）](#八动画变体variants)
9. [预设（Presets）](#九预设presets)
10. [函数与事件（Functions）](#十函数与事件functions)
11. [日志与调试](#十一日志与调试)
12. [实验性设置](#十二实验性设置)
13. [常见问题 FAQ](#十三常见问题-faq)
14. [Detection Plugin 检测条件扩展](#十四detection-plugin检测条件扩展mod-104806)
15. [参考来源](#参考来源)

---

## 一、OAR 是什么

**Open Animation Replacer（OAR）** 是由 **Ersh** 开发的 **SKSE 框架插件**，作用是根据**可配置的条件**动态替换游戏中的动画文件。它带有**游戏内编辑器**，完全**向后兼容**旧方案并提供了更多功能，还可被其他 SKSE 插件**扩展**，并且是**开源**的。

一句话概括它的定位：**它取代并继承了 Dynamic Animation Replacer（DAR）**。

### 为什么会有 OAR

- DAR 长期未针对游戏最新版本更新，且为**闭源**——原作者一旦停更，社区无人能接手修补。人们曾因为 DAR 无法适配新补丁，不得不给游戏**降级**才能继续用动画替换 mod。
- 动画作者对动画替换器有许多 DAR 不支持的需求，而闭源意味着**没人能贡献代码**。
- 动态动画替换是一个极强的概念，值得继续迭代开发。

### 与 DAR 的关系（关键澄清）

| 问题 | 答案 |
| --- | --- |
| 是 DAR 的逆向工程改版吗？ | **不是**。除少数"与游戏代码交互且只能有一种实现方式"的部分外，**不包含任何 DAR 代码**，是作者基于自己研究游戏的独立成果。 |
| 能替代 DAR 吗？ | 可以。**本体不兼容** Dynamic Animation Replacer（两者不能同时使用）。 |
| 旧 DAR 动画 mod 还能用吗？ | **完全兼容**。放在 `DynamicAnimationReplacer` 文件夹里的 mod 会被自动读取并按新结构转换，行为与原先一致（"It just works"）。 |
| 支持哪些版本？ | 兼容任何非远古的 Skyrim 版本，包括 **1.5.97、1.6+ 与 VR**。 |
| 支持传奇版（LE）吗？ | **不支持，且作者明确不打算支持**。SE 引擎更稳定、有 CommonLibSSE 等框架，建议直接迁移到 SE。 |

### 核心能力一览

- 基于条件实时**替换动画**（角色状态、装备、环境、天气、时间等）
- **游戏内编辑器**：随时检视/编辑条件与优先级、预览动画、调试
- **动画变体**：随机 / 顺序播放
- **条件预设（PRESET）**：replacer mod 级复用
- **函数/事件系统**：动画开始/结束/自定义事件触发游戏行为
- **日志系统**：动画日志 + 动画事件日志
- **SKSE 插件 API**：其他插件可注册**自定义条件**（Detection Plugin 就是这么来的）
- 主菜单预加载动画、提升动画数量上限、增大 Havok 堆
- 纯 SKSE 实现，**随时安装/卸载，无残留**

---

## 二、前置需求与安装

### 必备前置

| 前置 | 说明 |
| --- | --- |
| **SKSE** | Skyrim Script Extender，必须与你的游戏版本匹配 |
| **Address Library for SKSE Plugins** | SKSE 插件的地址库（VR 用 VR Address Library） |
| **Animation Queue Fix** | **仅当你没有启用**实验性设置"跳过预加载动画"时需要 |
| **Paired Animation Improvements** | 让**配对动画（paired animations）**内部的注释（annotations）正常工作 |

### 兼容性要点

- 与 OAR 不兼容的只有 **Dynamic Animation Replacer 本体**——不要同时装。
- 完全向后兼容所有为 DAR 制作的动画替换 mod。
- 内置 **MergeMapper** 支持。
- 对**任何版本的动画替换 mod**没有特殊要求，装好即用。

### 安装 / 卸载

- 用你惯用的模组管理器（MO2 / Vortex）正常安装即可。
- 由于一切通过 SKSE 实现，插件**对存档与游戏没有持久影响，可以随时安装或卸载**。

### 配置文件位置（重要）

- 插件生成的 `.ini` 位于 `Data\SKSE\Plugins\`（例如 `OpenAnimationReplacer.ini`）。
- **如果你用 MO2**，这些文件默认会落到 **overwrite** 文件夹里。
- **不要删除插件生成的 .ini 文件**——删了设置会重置。

---

## 三、核心概念：Replacer Mod 与 Submod

OAR 用两级结构组织动画替换：

```
OpenAnimationReplacer
├── Replacer mod 1            ← 一个"替换模组"（对应一个 mod 作者的作品）
│      ├── Submod A           ← 子模组：一组动画 + 一份条件配置
│      │      ├── [animation files]
│      │      └── config.json   ← 子模组配置文件（名称/描述/优先级/条件等）
│      ├── Submod B
│      │      ├── [animation files]
│      │      └── config.json
│      └── config.json        ← 替换模组配置文件（名称/描述）
└── Replacer mod 2
       ├── Submod C
       │      ├── [animation files]
       │      └── config.json
       └── config.json
```

- **Replacer mod（替换模组）**：包含一个或多个 submod，外加一份只记录**名称与描述**的 `config.json`。
- **Submod（子模组）**：包含替换动画文件 + 一份 `config.json`，记录子模组的**名称、描述、优先级、条件**及其他功能设置。
- 之所以采用这个结构，是因为大多数动画替换 mod 本身就是"多个文件夹、各自带不同条件和动画"。现在所有子文件夹可以收进一个文件夹，结构更整洁。
- **DAR 遗留 mod** 会被统一归到一个叫 **Legacy** 的 replacer mod 之下，每个 mod 作为一个 submod，名字就是它的文件夹名。

> 💡 **不要手动编辑 .json 文件**。虽然可以，但游戏内编辑器能完成一切，且更简单、更安全——手动改配置极易出错。

---

## 四、文件结构：动画放在哪、怎么替换

### 放置规则

自 **2.0.0** 起，replacer mod 可以放在 `Data\Meshes` 内的**任何位置**。理解方法很简单：

> 把它想象成**用一段 `OpenAnimationReplacer\MyMod\MySubmod\` 插进原始动画路径中**。

例如要替换原本位于 `Data\Meshes\actors\character\animations\male\mt_idle.hkx` 的动画，以下任一位置都合法：

```
Data\Meshes\OpenAnimationReplacer\MyMod\MySubmod\actors\character\animations\male\mt_idle.hkx
Data\Meshes\actors\OpenAnimationReplacer\MyMod\MySubmod\character\animations\male\mt_idle.hkx
Data\Meshes\actors\character\OpenAnimationReplacer\MyMod\MySubmod\animations\male\mt_idle.hkx
```

也就是说：把 `OpenAnimationReplacer\<替换模组名>\<子模组名>\` 这一段插入**原路径的任意位置**，后面保留原始的相对路径即可。

### 关键差异（相对 DAR）

- **优先级不再由文件夹名决定**！文件夹可以**任意命名**。
- 但请**避免使用非英文字符/符号**，它们很可能无法被正确读取。
- **运行中不能物理增删**动画文件或增删 mod 本身——改动只在**重启游戏后生效**。（不过可以在编辑器里**禁用**动画或子模组。）

---

## 五、游戏内编辑器（Shift + O）

默认按 **`Shift + O`** 打开游戏内 UI，检视并编辑所有已安装的 replacer mod。

### 三种模式

| 模式 | 说明 |
| --- | --- |
| **Inspect**（检视） | **只读**，禁用所有编辑功能。 |
| **Author**（作者） | 改动**直接保存进 `config.json`**。这是随 replacer mod 一起分发的**主配置文件**，面向 mod 作者。 |
| **User**（用户） | 生成 **`user.json`**，它会**覆盖 `config.json` 里除子模组名称与描述之外的一切**。用于用户个性化调整（改优先级、改条件、禁动画）而**不动原始文件**。user.json 可安全删除，删掉后自动回退到 config.json。 |

### 实用功能

- **选取目标**：在上方角落用**控制台选中某个 actor**，或**直接输入其 FormID**，即设为"当前求值目标"。
- **条件状态图标**：选中目标后，每个条件都会显示一个**图标**，实时指示其要求当前是否满足；部分条件还会额外显示**当前被检查的值**，便于定位问题。
- **复制/粘贴**：**右键**条件即可复制/粘贴单个条件，或整个条件组。
- **拖放排序**：可以**拖放**条件来**重新排序**。
- **替换列表标签页**：额外标签页按**优先级**列出某个动画的**所有替换**，仅供检视、不可编辑（因为一个 submod 内所有替换动画共享同一套配置）。
- **设置菜单**：包含实验性功能开关。
- **警告 / 错误栏**：
  - 多个 submod **优先级相同** → 显示**警告**
  - 某个 submod 的条件**需要其他插件或更高版本** → 显示**错误**
  - **点击编辑器底部的错误栏**可查看详细信息。

---

## 六、条件（Conditions）完整清单

条件决定"什么时候用这套替换动画"。下表按用途分组，括号内标注引入版本（未标注者为早期版本即已具备）。

### 1. 逻辑与组合

| 条件 | 说明 |
| --- | --- |
| **AND** | 所有子条件都为真 |
| **OR** | 任一子条件为真 |
| **XOR**（2.1.0） | 仅**一个**子条件为真（异或） |
| **IsForm** | ref 与指定 form 匹配 |
| **TARGET**（1.3.0） | 子条件全为真，但**改为对"当前目标"求值** |
| **PLAYER**（1.3.0） | 子条件全为真，但**改为对玩家求值** |
| **MOUNT**（2.2.0） | 子条件全为真，但**改为对坐骑求值** |
| **PRESET**（2.2.0） | 就地求值 replacer mod 中定义的条件预设 |
| **IsReplacerEnabled** | 某指定名称的 replacer 子模组是否启用（留空则检查该 replacer 内是否有任何子模组启用） |

> 外层条件列表本身**就是一个 AND**；OR/AND 等组合条件可**无限嵌套**。

### 2. 装备与武器

| 条件 | 说明 |
| --- | --- |
| **IsEquipped** | 右手/左手装备了指定 form（带"左手"布尔组件） |
| **IsEquippedType** | 右手/左手装备了指定类型的物品 |
| **IsEquippedHasKeyword** | 右手/左手装备的物品带指定关键字 |
| **IsEquippedPower** | 威能槽（power）装备了指定法术（即旧 DAR 的 IsEquippedShout） |
| **IsEquippedShout** | 装备了指定龙吼 |
| **IsWorn** | 任意槽位装备了指定 form |
| **IsWornHasKeyword** | 任意槽位装备的物品带指定关键字 |
| **IsWornInSlot**（3.0.0） | 指定槽位装备了物品 |
| **IsWornInSlotHasKeyword** | 指定槽位装备的物品带指定关键字 |
| **IsEquippedHasEnchantment**（2.2.0） | 右手/左手的物品带指定附魔 |
| **IsEquippedHasEnchantmentWithKeyword**（2.2.0） | 右手/左手物品的附魔带指定关键字 |
| **HasBoundWeaponEquipped**（3.2.0） | 右手/左手装备了**召唤武器**（bound weapon） |
| **EquippedObjectWeight**（1.2.0） | 右手/左手所持物品的重量与数值比较 |
| **IsWeaponDrawn** | 已拔出武器 |
| **IsBlocking**（1.1.0） | 正在格挡 |

### 3. 身份、种族与关系

| 条件 | 说明 |
| --- | --- |
| **IsFemale** | 女性 |
| **IsChild** | 儿童 |
| **IsUnique** | 被标记为唯一（unique） |
| **IsActorBase** | ref 的 actor base 是指定 form |
| **IsRace** | 种族是指定种族 |
| **IsClass** | 职业是指定职业 |
| **IsCombatStyle** | 战斗风格是指定风格 |
| **IsVoiceType** | 声音类型是指定类型 |
| **IsPlayerTeammate** | 是玩家的队友 |
| **IsGuard**（2.3.0） | 是守卫 |
| **IsGhost**（3.0.0） | 处于 ghost（无敌）状态（与游戏里的"鬼魂"无关） |
| **IsSummoned**（2.2.0） | 是召唤生物 |
| **HasPerk** | 拥有指定 perk |
| **HasSpell** | 拥有指定法术或龙吼 |
| **IsInFaction** | 属于指定派系 |
| **FactionRank** | 派系等级与数值比较 |

### 4. 动作与战斗状态

| 条件 | 说明 |
| --- | --- |
| **IsAttacking** | 正在攻击 |
| **IsRunning** | 正在跑 |
| **IsSneaking** | 正在潜行 |
| **IsSprinting** | 正在冲刺 |
| **IsInAir** | 在空中 |
| **IsInCombat** | 处于战斗状态 |
| **IsSwimming**（3.0.0） | 正在游泳 |
| **IsAboveWater**（3.0.0） | 位于水面上方（若垂直下落会落进水里） |
| **IsStaggered**（3.1.0） | 正在踉跄 |
| **AttackState**（1.3.0） | 攻击状态 |
| **IsAttackTypeKeyword**（2.2.0） | 本次攻击类型等于指定关键字 |
| **IsAttackTypeFlag**（2.2.0） | 本次攻击带有指定 flag |
| **LifeState**（2.1.0） | 生命状态 |
| **SitSleepState**（2.1.0） | 坐/睡状态 |
| **CastingSpell**（3.1.0） | 正在用指定释放源施放法术 |
| **CurrentCastingType**（1.2.0） | 指定释放源的当前释放类型 |
| **CurrentDeliveryType**（1.2.0） | 指定释放源的当前投递类型 |
| **IsTalking**（1.2.0） | 正在说话（自言自语或对话） |
| **IsGreetingPlayer**（1.2.0） | 正在向玩家打招呼 |
| **IsDoingFavor**（1.2.0） | 被玩家要求去做某事 |
| **CrimeGold** | 当前赏金与数值比较 |
| **IsTrespassing**（2.3.0） | 正在非法闯入 |
| **IsOverEncumbered**（2.3.0） | 超负重 |
| **InventoryWeight**（3.0.0） | 总背包重量或当前负重百分比与数值比较 |
| **IdleTime**（2.3.0） | 已闲置时间与数值比较 |

### 5. 移动与物理

| 条件 | 说明 |
| --- | --- |
| **IsMovementDirection** | 正朝指定方向移动 |
| **MovementSpeed** | 指定类型的移动速度与数值比较 |
| **CurrentMovementSpeed** | 当前移动速度与数值比较 |
| **MovementSurfaceAngle**（2.2.0） | 所踩地面的坡度角与数值比较 |
| **IsOnStairs**（2.3.0） | 在楼梯上（注意：游戏里并非所有楼梯都被标记为楼梯） |
| **SurfaceMaterial**（2.3.0） | 所站地面带有指定材质 ID |
| **FallDistance**（1.1.0） | 当前下落距离与数值比较 |
| **FallDamage**（1.1.0） | 若此刻落地会造成的坠落伤害与数值比较 |
| **CurrentRotationSpeed**（1.2.0） | 当前旋转速度与数值比较 |
| **Scale** | ref 的缩放与数值比较 |
| **Height** | actor 的高度与数值比较 |
| **Weight** | actor 的体重与数值比较 |
| **SubmergeLevel** | 入水深度（0–1）与数值比较 |

### 6. 环境、位置与时间

| 条件 | 说明 |
| --- | --- |
| **IsInInterior** | 在室内单元格 |
| **IsInLocation** | 在指定 location 内 |
| **LocationHasKeyword**（2.0.0） | 当前 location 带指定关键字 |
| **LocationCleared**（2.2.0） | 当前 location 已清除 |
| **IsParentCell** | 当前所在是指定单元格 |
| **IsWorldSpace** | 当前所在是指定世界空间 |
| **HasRefType** | 带有指定 LocRefType |
| **CurrentWeather** | 当前天气为指定天气（TESWeather，或 BGSListForm 天气列表） |
| **CurrentWeatherHasFlag**（1.2.0） | 当前天气启用了指定 flag |
| **CurrentGameTime** | 当前游戏时间与指定时间比较 |
| **LightLevel**（2.0.0） | 该 ref 当前受到的光照强度与数值比较 |
| **WindSpeed** | 当前天气风速与数值比较 |
| **WindAngleDifference** | 当前天气风向与 ref 朝向的夹角与数值比较 |
| **IsMenuOpen**（1.3.0） | 指定菜单当前是否打开 |
| **IsQuestStageDone**（1.2.0） | 指定任务的指定阶段已完成 |

### 7. 坐骑与家具

| 条件 | 说明 |
| --- | --- |
| **IsOnMount**（1.1.0） | 正骑在坐骑上 |
| **IsRiding**（1.1.0） | 正骑在指定 form 上 |
| **IsRidingHasKeyword**（1.1.0） | 正骑的 form 带指定关键字 |
| **IsBeingRidden**（1.1.0） | 正被别人骑乘 |
| **IsBeingRiddenBy**（1.1.0） | 正被指定 form 骑乘 |
| **CurrentFurniture**（1.1.0） | 正占用指定家具 |
| **CurrentFurnitureHasKeyword**（1.1.0） | 正占用的家具带指定关键字 |

### 8. 目标、行为包与侦测

| 条件 | 说明 |
| --- | --- |
| **HasTarget**（1.1.0） | 拥有指定类型的目标 |
| **CurrentTargetDistance**（1.1.0） | 与当前目标的距离与数值比较 |
| **CurrentTargetRelationship**（1.1.0） | 与当前目标的关系与数值比较 |
| **CurrentTargetRelativeAngle**（1.2.0） | 与当前目标的相对夹角 |
| **CurrentTargetLineOfSight**（1.2.0） | 当前目标是否在自己的视线内（或反之） |
| **IsCombatState**（1.1.0） | 当前战斗状态匹配给定状态 |
| **IsCombatSearching**（2.3.0） | 正在战斗中搜索目标 |
| **IsCrimeSearching**（2.3.0） | 正在搜索罪犯 |
| **IsCurrentPackage** | 当前运行的包是指定包 |
| **CurrentPackageProcedureType**（1.1.0） | 当前行为包的过程类型 |

### 9. 数值、魔法与物品

| 条件 | 说明 |
| --- | --- |
| **CompareValues** | 比较两个值（可为静态值、全局变量引用、Actor Value、行为图变量） |
| **Level** | actor 等级与数值比较 |
| **Random** | 生成随机数与数值比较（可指定随机数的 min/max） |
| **HasKeyword** | 带指定关键字 |
| **HasMagicEffect** | 正受指定法术效果影响（可选只检查**激活中**的效果） |
| **HasMagicEffectWithKeyword** | 正受带指定关键字的法术效果影响（同样可选只查激活中） |
| **MagicEffectElapsedTime**（3.0.0） | 受指定法术效果影响的时长与数值比较 |
| **InventoryCount**（1.1.0） | 指定物品的背包数量与数值比较 |
| **InventoryCountHasKeyword**（1.2.0） | 带指定关键字的物品总数量与数值比较 |
| **HasGraphVariable** | 拥有指定行为图变量 |

### 10. 场景

| 条件 | 说明 |
| --- | --- |
| **IsInScene**（1.2.0） | 正处于某个 scene 中 |
| **IsInSpecifiedScene**（1.2.0） | 正处于指定的 scene 中 |
| **IsScenePlaying**（1.2.0） | 指定 scene 正在播放 |

### 11. DAR 旧条件的改名 / 合并对照

以下你在 DAR 里熟悉的条件**已被合并或重命名**（基于 DAR 的 mod 仍会被正确读取）：

| DAR 旧条件 | OAR 新条件 |
| --- | --- |
| IsEquippedShout | **IsEquippedPower**（DAR 里它实际检查的就是 Power） |
| IsEquippedRight / IsEquippedLeft | **IsEquipped** + "左手"布尔组件 |
| IsEquippedRightType / IsEquippedLeftType | **IsEquippedType** + "左手"布尔组件 |
| IsEquippedRightHasKeyword / IsEquippedLeftHasKeyword | **IsEquippedHasKeyword** + "左手"布尔组件 |
| ValueEqualTo / ValueLessThan / IsActorValueEqualTo / IsActorValueLessThan / IsActorValueBaseEqualTo / IsActorValueBaseLessThan / IsActorValueMaxEqualTo / IsActorValueMaxLessThan / IsActorValuePercentageEqualTo / IsActorValuePercentageLessThan | **CompareValues** |
| IsFactionRankEqualTo / IsFactionRankLessThan | **FactionRank** |
| IsLevelLessThan | **Level** |
| CurrentGameTimeLessThan | **CurrentGameTime** |

> 💡 迁移 DAR mod 到 OAR 时，可以在编辑器**作者模式**下从 Legacy 子模组**导出配置文件**。该文件插件不会读取，但你可以手动把它移到正确结构的新文件夹里，省去重做条件的功夫；编辑器里也有**复制配置到剪贴板**的按钮。同时不妨顺便看看新条件——也许能把条件写得更简洁。

---

## 七、子模组附加设置（Additional Settings）

每个 submod 还可开启以下附加设置：

| 设置 | 作用 |
| --- | --- |
| **Constant polling** | 动画播放期间**持续轮询**所需条件，情况一变就**立即替换**，并在新旧动画间做正确混合。 |
| **保留随机结果（on loop）** | 动画**循环**时保留随机条件的结果。移动类 mod 很有用——避免每走几步就换一次动画。 |
| **共享随机结果** | 在整个 submod 内**共享**随机结果，让整套动画一起随机。 |
| **自定义混合时间** | 动画被打断替换时的混合（blend）时长。 |
| **忽略 No Triggers 标记** | 原版某些动画剪辑带此标记，会**忽略**带触发器的注释事件；开启后该标记被忽略，注释中的动画事件即可正常触发。 |
| **必需项目名称** | 指定行为项目名（如 `DefaultMale` / `DefaultFemale`），让该 submod 只在该项目下加载——这些动画**不计入**该项目的动画数量上限。 |
| **动画文件夹覆盖** | 指定存放动画的文件夹名，让多个 submod **共用同一批动画而不必重复复制**。 |

---

## 八、动画变体（Variants）

自 **1.2.0** 起，一个替换动画可以有**多个变体**——这是做"随机动画"更舒适的方式。

过去做随机变体要用"多个条件相同的 submod + 随机条件"；有了变体，**只需一个 submod，且不需要任何随机条件**。

### 添加方法

在该动画原本应放置的位置，**新建一个子文件夹**，命名为 `_variants_[不含扩展名的动画名]`，把变体文件都放进去。

- 例：为 `mt_idle.hkx` 做变体 → 新建文件夹 `_variants_mt_idle`（放在同一位置），把变体文件放进去。
- **变体文件名随意**，但建议用短名（甚至 `1.hkx`、`2.hkx`），以**避免长路径引发的问题**。

结果就是：原本 `submodFolder/male/mt_idle.hkx`，变成 `submodFolder/male/_variants_mt_idle/1.hkx` 等。

就这样——插件会自动识别，并在该替换动画应播放时**随机挑选**一个变体。

### 权重

可在游戏内编辑器的 submod 替换动画里为每个变体**配置权重**：权重 **2** 的变体播放概率是权重 **1** 的**两倍**。

变体随机同样会**遵循**"循环/回声时保留随机结果"与"共享随机结果"这两个 submod 设置，就像随机条件一样。

### 顺序模式（自 2.2.0）

变体新增 **Sequential（顺序）** 模式：不随机，而是**按顺序依次播放**。此模式下可把某个变体标记为 **"Play once"**——它在本轮序列中不会再播放，即使序列已循环回来。序列数据（下一个变体的索引、"只播一次"的历史）会在该替换动画（或整个动画剪辑）**闲置一小段时间后重置**。

> 记住：变体只是**条件求值之后**的一个可选步骤，唯一区别是——不再是"选中并播放单个替换动画"，而是"从可能的多变体中选一个"。

---

## 九、预设（Presets）

自 **2.2.0** 起，新增 **PRESETS（预设）**。可在 replacer mod 中定义多个预设，然后用专门的 **PRESET 条件**来选用。

适用场景：一个 replacer mod 内的多个 submod 常常**共享完全相同的条件**，只差少数几处（比如武器类型不同）。预设让你只在**一处**创建该条件块，然后在各 submod 中**复用**，从而简化配置、减少重复。

> ⚠️ 预设**不会被复制**进 submod 配置——submod 里只保存预设的**名字**，预设的**实际内容保存在 replacer mod 的 config 中**。

---

## 十、函数与事件（Functions）

submod 可以在**动画开始 / 结束 / 指定事件**触发时执行游戏行为。配合自定义事件名 **`OAR`**（**无需行为补丁**即可被识别），可以做出很灵活的效果。

### 可用函数

| 函数 | 作用 |
| --- | --- |
| **PlaySound** | 在 ref 位置播放声音 |
| **ModActorValue** | 修改某个 Actor Value |
| **SetGraphVariable** | 设置行为图变量 |
| **ModifyGraphVariable**（3.1.0） | 修改行为图变量 |
| **SendAnimEvent** | 发送行为图事件 |
| **CastSpell** | 施放法术 |
| **DispelSpell** | 驱散法术 |
| **SpawnParticle** | 生成粒子 |
| **UnequipSlot** | 卸下指定槽位的物品 |
| **SetPlaybackSpeedMultiplier**（3.2.0） | 设置当前动画剪辑的播放速度倍率 |
| **CONDITION** | 仅在条件为真时，运行其包含的一组函数 |
| **RANDOM** | 从包含的函数组中**随机**运行一个 |
| **ONE** | 从上到下依次尝试运行函数组中的函数，直到第一个成功为止（多与 CONDITION 搭配，或与其他自带内部检查的函数搭配） |
| **FILENAME**（3.1.0） | 仅当当前替换动画文件名匹配时，才运行其包含的函数组 |

### 示例：动画中播放两个声音

想让动画期间播两个声音，给动画加 `OAR.sound1` 和 `OAR.sound2` 两个事件（点号后面的载荷可以是任意文本），然后在 OnTrigger 集合里加两个 **PlaySound** 函数，一个触发于 `OAR.sound1`、另一个触发于 `OAR.sound2`。

---

## 十一、日志与调试

### 动画日志

点主 UI 内的按钮即可开启——**关掉 UI 后，动画日志会继续留在屏幕上**，伴随你游玩。

- 可直接看到**刚刚播放的是哪个动画**，以及**它来自哪里**。
- 在设置菜单里可**自定义要记录哪些动画**（例如缓慢转鼠标产生的动画回声会非常刷屏）。
- 也可**启用写入 SKSE 日志文件**，便于事后分析。

### 动画事件日志（自 2.1.0）

额外提供一个**动画事件日志**，主要给行为（behavior）mod 作者用，会列出被跟踪引用上发生的**所有动画事件**。

---

## 十二、实验性设置

在设置菜单中，有几项**实验性功能**（并非 100% 确定无瑕疵，但实践中表现良好）：

### 1. 提高动画数量上限至每项目 65534

- 默认上限为 **32767**。
- 技术背景：Havok 行为里的动画剪辑用一个 16 位**有符号**整数（int16）表示绑定数组索引，范围 -32768 ~ 32767；而几乎整个负数区间都空闲（只有 -1 作为"未初始化"等特例）。该设置把游戏代码中所有按有符号处理该值的地方都改为按**无符号**（uint16）处理，范围 0 ~ 65535，**-1 仍被保留**，故上限为 **65534**。
- 之所以仍标"实验性"，是因为作者可能漏改了某些位置；而且**很少有人真的会触及 32k 上限**。只有你确实需要（或好奇）时才启用。

### 2. 禁用预加载动画

- 作者个人使用正常，但**部分测试者报告会出现短暂 T-Pose**。
- 好处是**对内存占用影响更小，且完全没有动画加载队列**。
- 已被证明存在一些小问题，**官方不推荐使用此设置**。

---

## 十三、常见问题 FAQ

**Q：能中途安装/卸载吗？**
可以。插件对游戏**无持久影响**，随时装卸都行。

**Q：我的设置重置了！**
别删插件生成的 `.ini` 文件。用 MO2 时它默认落在 **overwrite** 文件夹里。

**Q：我怀疑这 mod 导致了崩溃。**

- 请提供 **.NET Script Framework / Crash Logger** 的崩溃日志——对 SKSE 插件类崩溃非常有用。
- 如果崩溃发生在**主菜单**，试着在 `Data\SKSE\Plugins\OpenAnimationReplacer.ini` 中把 `bLoadDefaultBehaviorsInMainMenu` 设为 `false`。
- 报 bug 时请描述清楚，最好附带**可复现步骤**。

**Q：某些替换动画/ mod 似乎没被插件识别？**

- 检查**完整文件路径是否超过 260 个字符**。若超了，试着改短文件夹名，或把游戏/mod 管理器所在目录往上层目录挪。这是某些 Windows 版本和/或 MO 的已知问题。

**Q：怎么把 DAR mod 迁移到 OAR？**
在编辑器**作者模式**下从 Legacy 子模组导出配置、手动移到新结构；或用"复制到剪贴板"按钮。也建议顺便用新条件简化/改进条件。

**Q：很多重复动画怎么办？**
如果 mod 里包含大量重复动画（用在不同条件的 submod 里），可用"**动画文件夹覆盖**"这一可选设置。

**Q：为什么不能运行时加/删动画？**
物理增删动画文件或 mod 只在**重启游戏后生效**；运行时可以在编辑器里**禁用**动画或 submod。

---

## 十四、Detection Plugin：检测条件扩展（mod 104806）

> **Open Animation Replacer - Detection Plugin**
> 作者：**Nonameron** ｜ 首次发布：2023-11-15 ｜ Nexus mod 104806
> 定位：通过 **OAR 的插件 API** 为 OAR 增加**"侦测"类自定义条件**的 SKSE 插件。

OAR 本身允许其他 SKSE 插件注册自定义条件——Detection Plugin 就是一个典型例子。它把游戏**潜行侦测系统**的结果暴露成动画条件，让动画能对"**谁看见了谁**"做出反应。

### 前置需求

- **Open Animation Replacer**（本体，及 SKSE / Address Library）
- 无需行为补丁；无需 Nemesis/Pandora

### 它新增的条件

| 条件 | 说明 |
| --- | --- |
| **DETECTED_BY** | 若存在一个**满足全部子条件**的 actor **看见了**（侦测到）本 actor，则为真。 |
| **DETECTS** | 若存在一个满足条件的 actor **对本 actor 可见**，则为真。 |

> 二者都是**多条件容器**：内部可嵌套任意子条件（含 OAR 全部原条件），用来筛选"侦测者/被侦测者"的身份。

### 配套的"检测子条件"（只能用在上面两个检测条件内部）

| 子条件 | 说明 | 可调组件 |
| --- | --- | --- |
| **DetectionDistance** | 侦测者与被侦测者之间的**距离**是否满足条件。 | Comparison（比较符）+ Distance（数值） |
| **DetectionRelationship** | 侦测者与被侦测者之间的**关系等级**是否满足条件。 | Comparison + Relationship（**-4 = 死敌 … 4 = 恋人**） |
| **DetectionAngle** | 从 actor 到 target 的**夹角**是否满足条件。 | Swap actor（布尔）、Comparison、Angle in degrees（数值）、**限制只在右侧**、**限制只在左侧** |

- **Swap actor**：为 false 时，角度以"被求值的 actor"为基准；为 true 时，在 DETECTS 下以"被侦测者"为基准、在 DETECTED_BY 下以"侦测者"为基准。
- **左右限制**：两个布尔分开控制，可让动画只在"目标出现在左/右侧"时触发（例如侧身躲闪、背后偷袭类动画）。

### 工作原理与判定规则（了解它才能用好）

- 判定基于游戏原生的**侦测等级**：对目标调用 `RequestDetectionLevel`，**结果 > 0** 才算"被看见"。也就是说，它天然受**视线（LOS）、光照、潜行技能、距离、角度**等原版潜行机制影响。
- 只有那些 **AffectsStealthMeter 的 actor**（即能参与侦测的 NPC）会被当作侦测者；**玩家**会被单独检查。
- 以下对象**被排除**，不会触发：
  - **自己**（target == actor）
  - **已删除 / 已禁用**的 actor
  - **ManakinRace**（人偶/展示用种族）
- 求值成功时，条件的"当前值"字段会显示**侦测者的名字**，方便在编辑器里调试。

### 典型用法示例

- **"被敌人发现"的反应动画**：`DETECTED_BY` 下嵌套子条件筛选侦测者（如 `IsInCombat`、`IsGuard`、`IsRace`），让角色在被特定敌人发现时播放相应动画。
- **潜行接近 / 背后偷袭**：`DETECTS` + `DetectionAngle` 勾选"限制检测到后方/侧面" + `DetectionDistance` 限定距离。
- **危险度分层**：用 `DetectionRelationship` 区分"死敌/敌对/友好"，对敌对者才触发警戒姿态。
- **距离分层**：`DetectionDistance` 做近/中/远三档，配合变体随机。

### 注意事项

- 该插件**必须与 OAR 本体版本匹配**——OAR 更新后，插件可能需同步更新（作者在评论区说明过：OAR 不更新，他就无法先更新）。条件要求的 OAR API 版本：DETECTED_BY / DETECTS / DetectionDistance / DetectionRelationship 需 **2.0.0** 以上；DetectionAngle 需 **2.0.3** 以上。
- 使用前请确认 OAR 与插件都为最新版，否则编辑器会给出"需要更高版本/缺少插件"的错误提示（点击底部错误栏可看详情）。
- 条件在游戏内编辑器的 OAR 条件列表里选择；若找不到某个检测条件，先确认插件已正确安装并生效。

---

## 参考来源

1. **Open Animation Replacer** — Nexus Mods（mod 92109），作者 Ersh
   <https://www.nexusmods.com/skyrimspecialedition/mods/92109>
2. **Open Animation Replacer - Detection Plugin** — Nexus Mods（mod 104806），作者 Nonameron
   <https://www.nexusmods.com/skyrimspecialedition/mods/104806>
3. **OpenAnimationReplacer-DetectionConditions** — 插件源代码（GitHub / matiasmakipelto）
   <https://github.com/matiasmakipelto/OpenAnimationReplacer-DetectionConditions>
4. **OpenAnimationReplacer** — 本体源代码（GitHub / ersh1）
   <https://github.com/ersh1/OpenAnimationReplacer>

> 本文为学习用途的结构化整理，版权归原作者所有。条件名称、版本号、路径等关键信息以官方页面为准。
