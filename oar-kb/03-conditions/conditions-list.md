---
id: conditions-list
title: 条件全清单（按用途分组 + 引入版本）
category: 03-conditions
kind: reference
version: 1.0.0
updated: 2026-09-21
tags: [OAR, 条件, 清单, 速查, 版本]
source: https://www.nexusmods.com/skyrimspecialedition/mods/92109
summary: OAR 注册的全部条件速查表，按逻辑/装备/身份/战斗/移动/环境/坐骑/目标/数值/场景分组，并标注每个条件的引入版本。已用源码逐条核对完整性。
---

# 条件全清单（按用途分组 + 引入版本）

> **完整性核对**：本页清单由 Nexus 描述页整理，并与本体源码 `src/Conditions.h` 中注册的条件名**逐条比对**——源码共注册 **125** 个名字（含 `! INVALID !`、`! DEPRECATED !` 两个内部占位与 `OR/AND/XOR/TARGET/PLAYER/MOUNT/PRESET` 等容器），官方描述页**无遗漏**。
> 来源：本库对 `github.com/ersh1/OpenAnimationReplacer` 的 `src/Conditions.h` 核对结果（2026-09-21）。

## 一、逻辑与容器

| 条件 | 引入 | 说明 |
| --- | --- | --- |
| **AND** | — | 所有子条件都为真 |
| **OR** | — | 任一子条件为真 |
| **XOR** | 2.1.0 | **仅一个**子条件为真（异或） |
| **TARGET** | 1.3.0 | 子条件全为真，但**改为对"当前目标"求值** |
| **PLAYER** | 1.3.0 | 子条件全为真，但**改为对玩家求值** |
| **MOUNT** | 2.2.0 | 子条件全为真，但**改为对坐骑求值** |
| **PRESET** | 2.2.0 | 就地求值 replacer mod 中定义的**条件预设** |
| **IsForm** | — | ref 与指定 form 匹配 |
| **IsReplacerEnabled** | — | 某指定名称的 replacer 子模组是否启用（**留空**则检查该 replacer 内是否有任何子模组启用） |

> 外层条件列表**本身就是一个 AND**；OR/AND 等组合条件可**无限嵌套**。详见 [容器条件](condition-containers.md)。

## 二、装备与武器

| 条件 | 引入 | 说明 |
| --- | --- | --- |
| **IsEquipped** | — | 右手/左手装备了指定 form（带"左手"布尔组件） |
| **IsEquippedType** | — | 右手/左手装备了指定类型的物品 |
| **IsEquippedHasKeyword** | — | 右手/左手装备的物品带指定关键字 |
| **IsEquippedPower** | — | 威能槽（power）装备了指定法术（= DAR 的 `IsEquippedShout` 的真实语义） |
| **IsEquippedShout** | — | 装备了指定龙吼 |
| **IsWorn** | — | 任意槽位装备了指定 form |
| **IsWornHasKeyword** | — | 任意槽位装备的物品带指定关键字 |
| **IsWornInSlot** | 3.0.0 | 指定槽位装备了物品 |
| **IsWornInSlotHasKeyword** | — | 指定槽位装备的物品带指定关键字 |
| **IsEquippedHasEnchantment** | 2.2.0 | 右手/左手的物品带指定附魔 |
| **IsEquippedHasEnchantmentWithKeyword** | 2.2.0 | 右手/左手物品的附魔带指定关键字 |
| **HasBoundWeaponEquipped** | 3.2.0 | 右手/左手装备了**召唤武器**（bound weapon） |
| **EquippedObjectWeight** | 1.2.0 | 右手/左手所持物品的重量与数值比较 |
| **IsWeaponDrawn** | — | 已拔出武器 |
| **IsBlocking** | 1.1.0 | 正在格挡 |

## 三、身份、种族与关系

| 条件 | 引入 | 说明 |
| --- | --- | --- |
| **IsFemale** | — | 女性 |
| **IsChild** | — | 儿童 |
| **IsUnique** | — | 被标记为唯一（unique） |
| **IsActorBase** | — | ref 的 actor base 是指定 form |
| **IsRace** | — | 种族是指定种族 |
| **IsClass** | — | 职业是指定职业 |
| **IsCombatStyle** | — | 战斗风格是指定风格 |
| **IsVoiceType** | — | 声音类型是指定类型 |
| **IsPlayerTeammate** | — | 是玩家的队友 |
| **IsGuard** | 2.3.0 | 是守卫 |
| **IsGhost** | 3.0.0 | 处于 ghost（无敌）状态（**与游戏里的"鬼魂"无关**） |
| **IsSummoned** | 2.2.0 | 是召唤生物 |
| **HasPerk** | — | 拥有指定 perk |
| **HasSpell** | — | 拥有指定法术或龙吼 |
| **IsInFaction** | — | 属于指定派系 |
| **FactionRank** | — | 派系等级与数值比较 |

## 四、动作与战斗状态

| 条件 | 引入 | 说明 |
| --- | --- | --- |
| **IsAttacking** | — | 正在攻击（**注意：整段弓攻击过程都为真**） |
| **IsRunning** | — | 正在跑 |
| **IsSneaking** | — | 正在潜行 |
| **IsSprinting** | — | 正在冲刺 |
| **IsInAir** | — | 在空中 |
| **IsInCombat** | — | 处于战斗状态 |
| **IsSwimming** | 3.0.0 | 正在游泳 |
| **IsAboveWater** | 3.0.0 | 位于水面上方（若垂直下落会落进水里） |
| **IsStaggered** | 3.1.0 | 正在踉跄 |
| **AttackState** | 1.3.0 | 攻击状态（有弓/施法等专用枚举） |
| **IsAttackTypeKeyword** | 2.2.0 | 本次攻击类型等于指定关键字 |
| **IsAttackTypeFlag** | 2.2.0 | 本次攻击带有指定 flag |
| **LifeState** | 2.1.0 | 生命状态 |
| **SitSleepState** | 2.1.0 | 坐/睡状态 |
| **CastingSpell** | 3.1.0 | 正在用指定释放源施放法术 |
| **CurrentCastingType** | 1.2.0 | 指定释放源的当前释放类型 |
| **CurrentDeliveryType** | 1.2.0 | 指定释放源的当前投递类型 |
| **IsTalking** | 1.2.0 | 正在说话（自言自语或对话） |
| **IsGreetingPlayer** | 1.2.0 | 正在向玩家打招呼 |
| **IsDoingFavor** | 1.2.0 | 被玩家要求去做某事 |
| **CrimeGold** | — | 当前赏金与数值比较 |
| **IsTrespassing** | 2.3.0 | 正在非法闯入 |
| **IsOverEncumbered** | 2.3.0 | 超负重 |
| **InventoryWeight** | 3.0.0 | 总背包重量或当前负重百分比与数值比较 |
| **IdleTime** | 2.3.0 | 已闲置时间与数值比较 |

## 五、移动与物理

| 条件 | 引入 | 说明 |
| --- | --- | --- |
| **IsMovementDirection** | — | 正朝指定方向移动 |
| **MovementSpeed** | — | 指定类型的移动速度与数值比较 |
| **CurrentMovementSpeed** | — | 当前移动速度与数值比较 |
| **MovementSurfaceAngle** | 2.2.0 | 所踩地面的坡度角与数值比较 |
| **IsOnStairs** | 2.3.0 | 在楼梯上（**注意：游戏里并非所有楼梯都被标记为楼梯**） |
| **SurfaceMaterial** | 2.3.0 | 所站地面带有指定材质 ID |
| **FallDistance** | 1.1.0 | 当前下落距离与数值比较 |
| **FallDamage** | 1.1.0 | 若此刻落地会造成的坠落伤害与数值比较 |
| **CurrentRotationSpeed** | 1.2.0 | 当前旋转速度与数值比较 |
| **Scale** | — | ref 的缩放与数值比较 |
| **Height** | — | actor 的高度与数值比较 |
| **Weight** | — | actor 的体重与数值比较 |
| **SubmergeLevel** | — | 入水深度（0–1）与数值比较 |

## 六、环境、位置与时间

| 条件 | 引入 | 说明 |
| --- | --- | --- |
| **IsInInterior** | — | 在室内单元格 |
| **IsInLocation** | — | 在指定 location 内 |
| **LocationHasKeyword** | 2.0.0 | 当前 location 带指定关键字 |
| **LocationCleared** | 2.2.0 | 当前 location 已清除 |
| **IsParentCell** | — | 当前所在是指定单元格 |
| **IsWorldSpace** | — | 当前所在是指定世界空间 |
| **HasRefType** | — | 带有指定 LocRefType |
| **CurrentWeather** | — | 当前天气为指定天气（TESWeather，或 BGSListForm 天气列表） |
| **CurrentWeatherHasFlag** | 1.2.0 | 当前天气启用了指定 flag |
| **CurrentGameTime** | — | 当前游戏时间与指定时间比较 |
| **LightLevel** | 2.0.0 | 该 ref 当前受到的光照强度与数值比较 |
| **WindSpeed** | — | 当前天气风速与数值比较 |
| **WindAngleDifference** | — | 当前天气风向与 ref 朝向的夹角与数值比较 |
| **IsMenuOpen** | 1.3.0 | 指定菜单当前是否打开 |
| **IsQuestStageDone** | 1.2.0 | 指定任务的指定阶段已完成 |

## 七、坐骑与家具

| 条件 | 引入 | 说明 |
| --- | --- | --- |
| **IsOnMount** | 1.1.0 | 正骑在坐骑上 |
| **IsRiding** | 1.1.0 | 正骑在指定 form 上 |
| **IsRidingHasKeyword** | 1.1.0 | 正骑的 form 带指定关键字 |
| **IsBeingRidden** | 1.1.0 | 正被别人骑乘 |
| **IsBeingRiddenBy** | 1.1.0 | 正被指定 form 骑乘 |
| **CurrentFurniture** | 1.1.0 | 正占用指定家具 |
| **CurrentFurnitureHasKeyword** | 1.1.0 | 正占用的家具带指定关键字 |

## 八、目标、行为包与侦测

| 条件 | 引入 | 说明 |
| --- | --- | --- |
| **HasTarget** | 1.1.0 | 拥有指定类型的目标 |
| **CurrentTargetDistance** | 1.1.0 | 与当前目标的距离与数值比较 |
| **CurrentTargetRelationship** | 1.1.0 | 与当前目标的关系与数值比较 |
| **CurrentTargetRelativeAngle** | 1.2.0 | 与当前目标的相对夹角 |
| **CurrentTargetLineOfSight** | 1.2.0 | 当前目标是否在自己的视线内（或反之） |
| **IsCombatState** | 1.1.0 | 当前战斗状态匹配给定状态 |
| **IsCombatSearching** | 2.3.0 | 正在战斗中搜索目标 |
| **IsCrimeSearching** | 2.3.0 | 正在搜索罪犯 |
| **IsCurrentPackage** | — | 当前运行的包是指定包 |
| **CurrentPackageType** | 1.1.0 | 当前行为包的过程类型（3.0.0 由 `CurrentPackageProcedureType` 改名） |

## 九、数值、魔法与物品

| 条件 | 引入 | 说明 |
| --- | --- | --- |
| **CompareValues** | — | 比较两个值（可为静态值、全局变量引用、Actor Value、行为图变量） |
| **Level** | — | actor 等级与数值比较 |
| **Random** | — | 生成随机数与数值比较（可指定随机数的 min/max） |
| **HasKeyword** | — | 带指定关键字 |
| **HasMagicEffect** | — | 正受指定法术效果影响（可选只检查**激活中**的效果） |
| **HasMagicEffectWithKeyword** | — | 正受带指定关键字的法术效果影响（同样可选只查激活中） |
| **MagicEffectElapsedTime** | 3.0.0 | 受指定法术效果影响的时长与数值比较 |
| **InventoryCount** | 1.1.0 | 指定物品的背包数量与数值比较 |
| **InventoryCountHasKeyword** | 1.2.0 | 带指定关键字的物品总数量与数值比较 |
| **HasGraphVariable** | — | 拥有指定行为图变量（**只能判存在，不能读值**） |

## 十、场景

| 条件 | 引入 | 说明 |
| --- | --- | --- |
| **IsInScene** | 1.2.0 | 正处于某个 scene 中 |
| **IsInSpecifiedScene** | 1.2.0 | 正处于指定的 scene 中 |
| **IsScenePlaying** | 1.2.0 | 指定 scene 正在播放 |

## 不存在于 OAR 本体的条件（易被文档误传）

| 名字 | 事实 |
| --- | --- |
| **`IsPlayer`** | **OAR 本体没有这个条件**（源码 125 个注册名里没有）。想判"是玩家"用 `IsForm` + Player（`Skyrim.esm` 的 `0x00000007`）或 `IsActorBase` + `Player`；想判"对玩家求值"用容器条件 **`PLAYER`**。详见 [Detection Plugin 勘误](../06-plugins/detection-plugin.md)。 |
| **`IsEquippedRight` / `IsEquippedLeft` / `IsEquippedRightType` / `IsEquippedLeftType` / `IsEquippedRightHasKeyword` / `IsEquippedLeftHasKeyword` / `ValueEqualTo` / `IsActorValueEqualTo` / `IsFactionRankEqualTo` / `IsLevelLessThan` / `CurrentGameTimeLessThan` … | DAR 时代的名字，已被**改名或合并**，见 [DAR 旧条件对照](dar-condition-renames.md)。旧 mod 仍能被正确读取，但你在编辑器里看到的是新名字。 |

## 相关

- [条件系统总览](conditions-overview.md)
- [容器条件](condition-containers.md)
- [DAR 旧条件改名/合并对照](dar-condition-renames.md)
- [Detection Plugin（额外条件）](../06-plugins/detection-plugin.md)
