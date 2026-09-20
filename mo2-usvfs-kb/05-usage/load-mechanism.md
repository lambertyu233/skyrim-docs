---
id: load-mechanism
title: 加载机制与 Steam App ID
category: 05-usage
version: 1.0.0
updated: 2026-09-20
tags: [使用, 加载机制, Steam AppID, proxy dll, 排错]
source: https://stepmodifications.org/wiki/Guide:Mod_Organizer
summary: 默认用 Mod Organizer 加载机制；Script Extender 与 Proxy DLL 各有代价；Steam App ID 决定游戏与工具能否正确启动。
kind: reference
---

# 加载机制与 Steam App ID

## Load Mechanism（Settings → Workarounds）

决定 MO 以何种方式作用于游戏。**若默认机制不出问题，就不要改。**

| 机制 | 行为与代价 |
| --- | --- |
| **Mod Organizer**（默认） | 游戏经 MO 启动时被 hook，加载你的 mod。**推荐默认使用**。Skyrim 用它效果最好。 |
| **Script Extender** | 经游戏的脚本扩展加载器把 MO 作为插件加载。代价：**经 MO 安装的脚本扩展插件不会生效**，必须手动装进 Data；且**游戏一更新 SE 就失效，MO 也随之失效**。Oblivion 用它效果最好。 |
| **Proxy DLL** | 以 DLL 应用扩展方式加载 MO，属于"比较大的 hack"，**应尽最大努力避免**。用它还必须**每次游戏更新后至少启动一次 MO**。 |

### Proxy DLL 出问题后的修复

现象：用了 proxy-dll 之后 MO/Skyrim 不工作了。按以下步骤**逐条照做**：

1. 先在 MO 里**停用** proxy-dll 加载，然后关闭 MO。
2. 看游戏目录里 `steam_api.dll` 的大小：
   - 若约 **116 KB** → 删除 `steam_api_orig.dll`；
   - 若约 **11 KB** → 删除 `steam_api.dll`，然后把 `steam_api_orig.dll` 改名为 `steam_api.dll`。
3. 两种情况下你最终都应得到：一个约 116 KB 的 `steam_api.dll`，且**没有**第二个叫 `steam_api*` 的文件。
4. 重新启动 MO，再重新启用 proxy-dll。

## Steam App ID

- MO 会按所管游戏**自动填入** Steam App ID：

| 游戏 | App ID |
| --- | --- |
| Skyrim | 72850 |
| Fallout NV | 22380 |
| Fallout 3 | 22300 |
| Oblivion | 22330 |

- 只有游戏或某个 Steam 工具启动不正确时才需要调整（**很罕见**）。
- 获取正确 App ID 的方法：
  1. 打开 Steam → `Library`；
  2. 右键该游戏 → `Properties`；
  3. `General` 标签页点 `CREATE DESKTOP SHORTCUT`，提示处选 OK；
  4. 在桌面上右键该快捷方式 → `Properties`；
  5. `URL` 字段形如 `steam://rungameid/202480`，那个数字就是 Steam App ID（此例为 Creation Kit）。

### 补充说明

- **Fallout 3 年度版（GOTY）的 App ID 是 22370**——若你用该版本，这可能解决 Fallout 3 的崩溃问题。
- **Skyrim Creation Kit 的 App ID 是 202480**。若没在 `Configure Executables` 里勾选 `Overwrite Steam AppID` 并填 202480，**CK 将看不到你的 mod**。

> 相关：[设置页参考](settings-tabs.md)、[配置第三方程序与快捷方式](third-party-executables.md)（Overwrite Steam AppID 字段）、[常用工具配置配方](tool-recipes.md)（SKSE 的加载机制相关注意）。
