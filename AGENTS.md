# AGENTS.md — 上古卷轴5 模改工作区

本工作区是一个**结构化知识库**（不是代码仓库）：7 个独立资料库 + 入口索引，
共 242 条目，全部为「每主题一个 Markdown + 统一 frontmatter」。
本文件是 agent 的入口契约：**先看这里，再决定读什么。**

---

## 零、先试这条路（最省事）

**手里是「症状」而不是「主题」时**（"角色摆大字""贴图糊""改了没反应"），
直接读排错索引，它按现象组织并已指向具体条目：

```
01-navigation/troubleshooting-index.md
```

它同时给出每条症状的**最易误判分叉点**——这比"该读哪篇"更值钱。

## 一、检索协议（四步，别跳）

```bash
KB="C:/Users/laptopyu/.workbuddy/binaries/python/versions/3.13.12/python.exe scripts/kb.py"

$KB list                      # 1. 有哪些库、各管什么
$KB toc oar-kb                # 2. 定位到库后，看它的分类地图
$KB find AttackState 条件      # 3. 检索条目，返回 路径 + 别录 + 摘要（不是全文）
$KB show conditions-overview  # 4. 先看元数据 + 标题大纲
$KB read <id>                 #    确认相关才读正文（也可用 Read 工具读路径）
```

**别做的事**（这几条是省 token 的关键）：

- ❌ 不要读 `index.json` / `index.html`。它们内联了每条正文的渲染 HTML
  （oar-kb 单个 296KB），读一个就等于把整个库塞进上下文。
- ❌ 不要为了"了解全貌"通读整个库。700KB 正文 ≈ 全工作区上下文预算。
- ✅ 找**具体事实**用 `grep`（返回 `路径:行号:内容`），找**该读哪篇**用 `find`。
- ✅ `find` 会返回每条命中的**别名（aliases）**——那是这个库里的"俗称表"，
  提问词与标题不一致时靠它命中（例如 `submod priority` → 优先级条目）。

## 二、路由表（问题 → 库）

| 你在处理什么 | 去哪个库 | 常见入口 |
|---|---|---|
| **出故障了，但不知道归谁管** | `01-navigation` | `troubleshooting-index.md` |
| OAR 条件 / `config.json` / submod / 优先级 / 游戏内编辑器 / DAR 迁移 | `oar-kb` | `03-conditions`、`08-practices` |
| FNIS / Nemesis / Pandora 行为补丁、hkx、动画数据库 | `behaviour-engine-kb` | `01-principles`、`06-practices` |
| Community Shaders 功能、ENB 迁移、画质与着色器 | `community-shaders-kb` | `02-features`、`01-installation` |
| Creation Kit、Papyrus 脚本、ESP/编辑器操作 | `creation-kit-kb` | `04-scripting`、`03-game-systems` |
| MO2 / USVFS / 虚拟文件系统 / 冲突覆盖 / 实例管理 | `mo2-usvfs-kb` | `05-usage` |
| 改造某个 mod 动画的实战方法论 | `oar-kb/08-practices/`（原 `OAR/` 目录的内容已并入本库） | 心智模型 + 六步改造法 |
| **捏脸 / 身形 / 骨骼 / 物理 / NPC 身材分配** | `character-appearance-kb` | `02-face`、`03-body`、`04-physics`、`06-troubleshooting` |

跨库问题通常要同时查多个库，别只查一个就下结论。三个高频组合：

- "我的拉弓动画被覆盖了" → `mo2-usvfs-kb`（覆盖规则）+ `oar-kb`（替换逻辑）
- "捏的脸进游戏变黑了" → `character-appearance-kb`（黑脸成因与四种修法）+ `mo2-usvfs-kb`（左栏/右栏不一致）
- "身形装了但滑块不出现" → `character-appearance-kb`（morph 未构建）+ `mo2-usvfs-kb`（构建产物被覆盖）

## 三、证据纪律（本工作区的硬规矩）

1. **引用要落到条目路径**，格式：`oar-kb/03-conditions/conditions-list.md`。
   没写清出处 = 结论不可用。
2. **区分核实层级**：条目里的结论分三类，转述时不要混同——
   - 一手源（源码 / Nexus 官方描述 / 作者日志）→ 可直接采信；
   - 社区经验（论坛帖、他人 `config.json`）→ 标注"社区经验"；
   - 本工作区实测 → 标"本机实测"。
3. **先查 `07-sources/unreliable-sources.md` / `09-sources/`**：库内已逐条记录过
   不可信来源与编造内容（如 CSDN 的 12 处编造、"OAR 有 wiki"、"`IsPlayer` 条件存在"）。
   踩过的坑不要踩第二遍。
4. **版本敏感性**：结论绑定上游版本（OAR 2.3.6 / CS 1.8.x 等）。
   条目 `updated` 距今较远、或用户环境版本不同时，**明说"可能已过期，建议核实"**，
   不要当作现状陈述。

## 四、写回（agent 也要维护这个库）

| 学到的东西 | 写到 |
|---|---|
| 一条可复用的事实 / 做法 | 对应库的条目正文（**改前先读全文，保持 frontmatter 与 `version` 递增**） |
| 一条新症状 / 新分叉点 | `01-navigation/troubleshooting-index.md`（只加索引行，别复制正文） |
| 新人可能用的俗称 / 英文提问词 | 该条目的 `aliases`（**这是提升检索命中最有效的单点改动**） |
| 排查过程中确认的临时结论、路径、命令坑 | `.workbuddy/memory/YYYY-MM-DD.md`（append-only） |
| 长期不变量、项目约定、工具教训 | `.workbuddy/memory/MEMORY.md`（就地更新） |
| 用户明确要求的偏好 | `~/.workbuddy/MEMORY.md` |

### `aliases` 怎么写（检索质量的杠杆）

`tags` 是"这篇属于什么主题"，`aliases` 是"**别人会用什么词来找它**"。
写英文术语、俗称、常见错拼、上级概念词，**别和 tags 重复**（validate 会提示）：

```yaml
tags: [OAR, 条件, 清单, 速查, 版本]
aliases: [conditions, conditions list, 条件列表, 条件速查表, AttackState, IsAttacking]
```

`find` 的加权：id 精确 100 > 别名精确 60 > tag 精确 40 > 别名模糊 26 > tag 模糊 22 > 标题 20 > 摘要 8。
实测：条目标题是「条件全清单」，用英文提 `conditions list` 原本基本淹没，加了别名后排第一。

**全库 241 条已全部补齐 aliases**（2026-09-21 完成 198 条；2026-09-22 新增
`character-appearance-kb` 43 条时已同步，并把与 `tags` 完全重复的项清掉）。**
新增条目请照上面的规则一并写，写完自检「删掉与 tags 同名的项，是否每条还剩 ≥3 个」。
写的时候注意搜索端的两条归一化，能省掉一堆无效别名：

- **空格不敏感**：`find` 会先去掉查询与别名里的所有空白再比对。
  所以 `怎么装mod` / `怎么装 mod` 等价，**别名不用为了兼容空格写法多写几条**。
- **中文长串会做反向包含**：你输入 `光源太多闪烁`（一个词、库里没有完全一样的别名）时，
  会拿库里较短的别名 `光太多闪烁` 去反向匹配加分。**所以中文别名写"更短的核心说法"比写长句更划算**
  —— 长的口语整句既占名额，也容易切不中。
- 最终建议：一条别名 ≈「一个别人真会敲进去的**短查询**」，而不是一句话。

## 五、维护自检

```bash
$KB check                                  # AGENTS.md 是否覆盖全部库（新增库后必跑）
python scripts/sync_scripts.py --check     # 各库的 stock 脚本是否还有分叉
python oar-kb/scripts/validate_kb.py       # 条目结构 + 索引 + 别名规范 + 脚本存在性
python oar-kb/scripts/check_links.py       # 站内相对链接
```

改页面一律改 `scripts/build_index.py` 的模板再重建，**不要手改 `index.html`**。
七个库的脚本与技能 `.workbuddy/skills/build-maintainable-kb/scripts/` 的 stock 版逐字节一致——
改完**必须**跑 `scripts/sync_scripts.py` 推送到全部库，否则会产生
"技能是这行为、库是那行为"的隐性分叉。

> 目录布局约束（踩过坑）：**每个资料库的条目必须放在 `NN-` 前缀的分类子目录里**。
> `build_index.py` 的 `if rel == "."` 会跳过库根层，条目写在根层会被**静默丢掉**
> （构建显示 `0 entries` 却不报错）。根层只放 `manifest.json` / `index.*` / `README.md`。
> 分类目录名**必须带 `NN-` 前缀**，`category` 字段与目录名严格相等。
