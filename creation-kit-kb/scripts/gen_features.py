#!/usr/bin/env python3
# Data-driven generator for Papyrus script-object reference entries.
# Edit SCRIPTS below, then run: python scripts/gen_features.py
# Produces one .md per script object under 04-scripting/ with uniform frontmatter.
import os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "04-scripting")
BASE = "https://ck.uesp.net/wiki/"
TODAY = datetime.date.today().isoformat()

# Each entry: id, title, page, summary, tags, functions[(name, desc)]
SCRIPTS = [
    {
        "id": "script-object-actor",
        "title": "Actor 脚本对象",
        "page": "Actor Script",
        "summary": "代表游戏中可活动角色（NPC / 生物）的脚本基类，提供属性、装备、战斗、法术等原生函数。",
        "tags": ["papyrus", "script-object", "actor", "native"],
        "functions": [
            ("GetActorValue - Actor", "读取某项 Actor Value（如 Health、Magicka）的当前值。"),
            ("SetActorValue - Actor", "直接设置某项 Actor Value 的当前值。"),
            ("DamageActorValue - Actor", "对某项 Actor Value 造成扣减（不触发永久修改）。"),
            ("RestoreActorValue - Actor", "恢复某项 Actor Value 的已损失部分。"),
            ("EquipItem - Actor", "将指定物品装备到角色身上。"),
            ("UnequipItem - Actor", "卸下角色身上指定物品。"),
            ("AddItem - ObjectReference", "向角色库存添加物品（定义在 ObjectReference，Actor 继承）。"),
            ("AddSpell - Actor", "为角色添加法术或能力（Ability）。"),
            ("RemoveSpell - Actor", "移除角色的法术或能力。"),
            ("StartCombat - Actor", "命令角色与指定目标进入战斗。"),
            ("StopCombat - Actor", "停止角色当前战斗。"),
            ("GetEquippedItemType - Actor", "返回当前右手装备物品的类型枚举。"),
            ("IsDead - Actor", "判断角色是否已死亡。"),
            ("GetLevel - Actor", "返回角色等级。"),
        ],
    },
    {
        "id": "script-object-objectreference",
        "title": "ObjectReference 脚本对象",
        "page": "ObjectReference Script",
        "summary": "游戏世界中所有可放置对象的基类，提供激活、启停、移动、物品、约束等最常用原生函数。",
        "tags": ["papyrus", "script-object", "objectreference", "native"],
        "functions": [
            ("Activate - ObjectReference", "以指定触发者激活该引用对象。"),
            ("Enable - ObjectReference", "启用（显示）对象引用。"),
            ("Disable - ObjectReference", "禁用（隐藏）对象引用。"),
            ("Delete - ObjectReference", "立即删除对象引用。"),
            ("DisableNoWait - ObjectReference", "异步禁用，不等待动画完成。"),
            ("MoveTo - ObjectReference", "将对象移动到另一引用位置。"),
            ("SetPosition - ObjectReference", "直接设置对象的 X/Y/Z 坐标。"),
            ("SetAngle - ObjectReference", "设置对象的旋转角度。"),
            ("AddItem - ObjectReference", "向容器 / 角色添加物品。"),
            ("RemoveItem - ObjectReference", "从容器 / 角色移除物品。"),
            ("GetDistance - ObjectReference", "返回与另一引用的距离。"),
            ("PlayAnimation - ObjectReference", "播放指定动画事件。"),
            ("ApplyHavokImpulse - ObjectReference", "对对象施加物理冲量。"),
            ("BlockActivation - ObjectReference", "暂时阻止对象的激活行为。"),
        ],
    },
    {
        "id": "script-object-game",
        "title": "Game 脚本对象",
        "page": "Game Script",
        "summary": "全局静态（Global）脚本对象，提供存档、时间、天数、玩家控制、工具函数等游戏级 API。",
        "tags": ["papyrus", "script-object", "game", "global", "native"],
        "functions": [
            ("GetPlayer - Game", "返回玩家 Actor 引用。"),
            ("GetForm - Game", "按 Form ID 从当前加载的插件中取回 Form。"),
            ("GetFormFromFile - Game", "按 Form ID 与插件名取回 Form。"),
            ("GetCurrentWeather - Game", "返回当前天气对象。"),
            ("SetGameSettingFloat - Game", "修改 GMST 浮点游戏设置。"),
            ("GetHourOfDay - Game", "返回当前一天中的小时（0-24）。"),
            ("Wait - Game", "游戏等待指定游戏小时数。"),
            ("EnablePlayerControls - Game", "恢复对玩家的控制。"),
            ("DisablePlayerControls - Game", "禁用对玩家的控制。"),
            ("GetPerkPoints - Game", "返回玩家可用 perk 点数。"),
            ("AdvanceSkill - Game", "提升指定技能经验。"),
            ("ShowTitle - Game", "在屏幕上显示标题文字。"),
        ],
    },
    {
        "id": "script-object-debug",
        "title": "Debug 脚本对象",
        "page": "Debug Script",
        "summary": "开发与调试用的全局脚本对象，提供日志输出、相机定位、通知与测试辅助函数。",
        "tags": ["papyrus", "script-object", "debug", "global", "native"],
        "functions": [
            ("Trace - Debug", "向脚本日志输出一条调试信息（最常用）。"),
            ("Notification - Debug", "在屏幕右下角弹出一条玩家可见通知。"),
            ("MessageBox - Debug", "弹出一个带确定的消息框。"),
            ("CenterOnCell - Debug", "将编辑器 / 游戏相机定位到指定单元格。"),
            ("CenterOnCellAndWait - Debug", "定位并等待相机到达目标。"),
            ("OpenUserLog - Debug", "打开 / 创建自定义用户日志文件。"),
            ("CloseUserLog - Debug", "关闭自定义用户日志。"),
            ("DumpAliasData - Debug", "将任务别名数据输出到日志，便于排查。"),
            ("SendAnimationEvent - Debug", "向引用发送动画事件（测试用）。"),
        ],
    },
]


def render(e):
    lines = []
    lines.append("---")
    lines.append(f'id: {e["id"]}')
    lines.append(f'title: {e["title"]}')
    lines.append("category: 04-scripting")
    lines.append("version: 1.0.0")
    lines.append(f"updated: {TODAY}")
    lines.append(f'tags: [{", ".join(e["tags"])}]')
    lines.append(f'source: {BASE + e["page"].replace(" ", "_")}')
    lines.append(f'summary: {e["summary"]}')
    lines.append("status: stable")
    lines.append("kind: reference")
    lines.append("---")
    lines.append("")
    lines.append(f'# {e["title"]}')
    lines.append("")
    lines.append(e["summary"])
    lines.append("")
    lines.append("> 来源：" + BASE + e["page"].replace(" ", "_"))
    lines.append("")
    lines.append("## 概述")
    lines.append("")
    lines.append(
        "本条目汇总该 Papyrus 脚本对象最常用的原生（native）函数。"
        "所有函数均来自游戏引擎暴露，无法在脚本中重写其实现。"
        "完整列表与参数请以官方页面为准。"
    )
    lines.append("")
    lines.append("## 常用函数")
    lines.append("")
    lines.append("| 函数 | 说明 |")
    lines.append("| --- | --- |")
    for name, desc in e["functions"]:
        lines.append(f"| `{name}` | {desc} |")
    lines.append("")
    lines.append("## 使用提示")
    lines.append("")
    lines.append(
        "- 脚本对象即「类」，运行于具体实例（如某个 Actor 或某个箱子）。"
    )
    lines.append("- `Self` 指向调用函数的当前实例；全局对象（Game / Debug）无 Self。")
    lines.append("- 编译与连接请参见同板块的「编译脚本」条目。")
    lines.append("")
    return "\n".join(lines) + "\n"


def main():
    os.makedirs(OUT, exist_ok=True)
    for e in SCRIPTS:
        path = os.path.join(OUT, e["id"] + ".md")
        # newline="\n" —— 资料库约定 LF 换行；默认文本模式在 Windows 上会把 \n 静默转成 CRLF
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(render(e))
        print(f"[GEN] {e['id']}.md  ({len(e['functions'])} functions)")
    print(f"Done: {len(SCRIPTS)} script-object entries.")


if __name__ == "__main__":
    main()
