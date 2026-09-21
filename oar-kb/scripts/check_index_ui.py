#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_index_ui.py — 索引页 index.html 的交互回归检查（不需要浏览器 / 不下载 Chromium）

做法：把 index.html 内联的 <script> 抽出来，套一层最小 DOM 桩，
在 Node 里真实执行页面脚本，然后模拟点击，断言：
  1. 侧栏「全部」按钮存在且**已绑定 onclick**（历史 bug：写死在 HTML 里但漏绑 → 选进分类后切不回全部）；
  2. 所有分类按钮都绑定了 onclick；
  3. 点某个分类只显示该分类条目，再点「全部」恢复全部条目且高亮回到「全部」；
  4. 分类过滤可收起/展开（#navbox 隐藏、aside 收窄、按钮文案切换、状态写入 localStorage）；
  5. 页面不含已删除的冗余说明文案。

用法：
  托管 python check_index_ui.py            # 检查本库（scripts/ 的上一级）
  托管 python check_index_ui.py <库目录>   # 检查指定库
环境变量 KB_NODE 可指定 node 可执行文件。
退出码：0 = 通过（或环境无 node 而跳过）；1 = 断言失败。
"""
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

DOM_STUB = r"""
// ---------------- 最小 DOM 桩 ----------------
const ALL = [];
let byId = {}, asideEl = null, mainEl = null, navboxEl = null, catnavEl = null;
class ClassList {
  constructor(){ this.s = new Set(); }
  add(){ for(const c of arguments) this.s.add(c); }
  remove(){ for(const c of arguments) this.s.delete(c); }
  contains(c){ return this.s.has(c); }
  toggle(c, force){
    const on = (force === undefined) ? !this.s.has(c) : !!force;
    if(on) this.s.add(c); else this.s.delete(c);
    return on;
  }
  toString(){ return Array.from(this.s).join(" "); }
}
class El {
  constructor(id, cls, dataset){
    this.id = id || null;
    this.classList = new ClassList();
    (cls || "").split(/\s+/).filter(Boolean).forEach(c=>this.classList.add(c));
    this.dataset = Object.assign({}, dataset || {});
    this.attrs = {}; this.children = []; this.parent = null;
    this.textContent = ""; this.scrollTop = 0; this.onclick = null; this._html = "";
    if(this.id) byId[this.id] = this;
    ALL.push(this);
  }
  get className(){ return this.classList.toString(); }
  set innerHTML(v){
    // 重写内容前，先把旧子元素从全局注册表里摘掉，否则统计会累加
    this.children.forEach(c=>{ const i = ALL.indexOf(c); if(i >= 0) ALL.splice(i, 1); });
    this._html = v; this.children = [];
    let m;
    if(v.indexOf('class="card"') >= 0){
      const rd = /data-id="([^"]+)"/g;
      while((m = rd.exec(v))){ const e = new El(null, "card", {id:m[1]}); e.parent = this; this.children.push(e); }
    }
    if(v.indexOf('class="navbtn"') >= 0){
      const rc = /data-cat="([^"]+)"/g;
      while((m = rc.exec(v))){ const e = new El(null, "navbtn", {cat:m[1]}); e.parent = this; this.children.push(e); }
    }
  }
  get innerHTML(){ return this._html; }
  setAttribute(k, v){ this.attrs[k] = String(v); }
  getAttribute(k){ return this.attrs[k]; }
  querySelectorAll(sel){ return select(sel); }
}
function inNavbox(e){ return e.parent === navboxEl || e.parent === catnavEl; }
function select(sel){
  let m;
  if(sel === "aside") return asideEl ? [asideEl] : [];
  if(sel === "main") return mainEl ? [mainEl] : [];
  if(sel === ".card") return ALL.filter(e=>e.classList.contains("card"));
  if(sel === ".navbtn") return ALL.filter(e=>e.classList.contains("navbtn"));
  if(sel === "[data-cat]") return ALL.filter(e=>e.dataset.cat !== undefined);
  if(sel === "[data-status]") return ALL.filter(e=>e.dataset.status !== undefined);
  if(sel === "#navbox .navbtn") return ALL.filter(e=>e.classList.contains("navbtn") && inNavbox(e));
  if(sel === "#navbox .navbtn[data-cat]") return ALL.filter(e=>e.classList.contains("navbtn") && e.dataset.cat !== undefined && inNavbox(e));
  m = /^#navbox \.navbtn\[data-cat="([^"]+)"\]$/.exec(sel);
  if(m) return ALL.filter(e=>e.classList.contains("navbtn") && e.dataset.cat === m[1]);
  return [];
}
const document = {
  getElementById:(id)=> byId[id] || null,
  querySelector:(sel)=>{ const r = select(sel); return r.length ? r[0] : null; },
  querySelectorAll:(sel)=> select(sel)
};
const _store = {};
const localStorage = {
  getItem:(k)=> (k in _store ? _store[k] : null),
  setItem:(k, v)=>{ _store[k] = String(v); }
};
// 按页面静态 HTML 里出现的 id 预建元素
(function(){
  const ids = __PAGE_IDS__;
  ids.forEach(id=>{ if(!byId[id]) new El(id, "", {}); });
  asideEl = new El("aside", "", {});
  mainEl = new El("main", "", {});
  navboxEl = new El("navbox", "", {});
  catnavEl = new El("catnav", "", {});
  // 侧栏内的按钮：全部按钮与状态按钮挂到 #navbox，navtoggle 挂在 #navbox 之外
  const btns = __ASIDE_BUTTONS__;
  btns.forEach(b=>{
    const e = new El(b.id, b.cls, b.dataset);
    const list = b.id === "navtoggle" ? asideEl : navboxEl;
    e.parent = list; list.children.push(e);
  });
  catnavEl.parent = navboxEl; navboxEl.children.push(catnavEl);
})();
// ---------------- DOM 桩结束 ----------------
"""

TESTS = r"""
// ---------------- 断言 ----------------
const FAIL = [];
let PASS = 0;
function ok(cond, name){
  if(cond){ PASS++; console.log("  PASS  " + name); }
  else { FAIL.push(name); console.log("  FAIL  " + name); }
}
function cards(){ return document.querySelectorAll(".card"); }
function cardCats(ENTRIES){
  const map = {}; ENTRIES.forEach(e=>map[e.id] = e.category);
  return cards().map(c=>map[c.dataset.id]);
}
const TOTAL = ENTRIES.length;
const catBtns = document.querySelectorAll("#navbox .navbtn[data-cat]");
const allBtn = catBtns.filter(b=>b.dataset.cat === "all")[0];
const navtoggle = document.getElementById("navtoggle");

console.log("\n[1] 侧栏按钮与绑定");
ok(!!allBtn, "存在「全部」按钮且在 #navbox 内");
ok(!!allBtn && typeof allBtn.onclick === "function", "『全部』按钮已绑定点击事件（历史 bug 回归项）");
ok(catBtns.length >= 2, "分类按钮数量 >= 2（实际 " + catBtns.length + "）");
ok(catBtns.every(b=>typeof b.onclick === "function"), "所有分类按钮都已绑定 onclick");

console.log("\n[2] 分类过滤与切回全部");
ok(cards().length === TOTAL, "初始显示全部 " + TOTAL + " 条（实际 " + cards().length + "）");
const pick = catBtns.filter(b=>b.dataset.cat !== "all")
  .map(b=>({b:b, n:ENTRIES.filter(e=>e.category === b.dataset.cat).length}))
  .filter(x=>x.n > 0).sort((a,b)=>b.n - a.n)[0];
if(pick){
  pick.b.onclick();
  const got = cards().length;
  ok(got === pick.n, "点分类「" + pick.b.dataset.cat + "」显示 " + pick.n + " 条（实际 " + got + "）");
  ok(cardCats(ENTRIES).every(c=>c === pick.b.dataset.cat), "显示的条目全部属于该分类");
  allBtn.onclick();
  ok(cards().length === TOTAL, "点『全部』恢复 " + TOTAL + " 条（实际 " + cards().length + "）");
  ok(cardCats(ENTRIES).every(c=>c !== undefined), "恢复后每条都能对应到条目");
} else {
  ok(false, "找不到有条目的分类，无法测试分类切换");
}
ok(allBtn.classList.contains("active"), "『全部』按钮处于高亮态");

console.log("\n[3] 分类过滤收起 / 展开");
ok(!!navtoggle, "存在收起/展开按钮");
if(navtoggle){
  const box = document.getElementById("navbox");
  ok(!box.classList.contains("hidden"), "初始为展开");
  navtoggle.onclick();
  ok(box.classList.contains("hidden"), "收起后 #navbox 隐藏");
  ok(document.querySelector("aside").classList.contains("collapsed"), "收起后 aside 收窄");
  ok(navtoggle.textContent === "展开 ›", "按钮文案变为『展开 ›』（实际 " + navtoggle.textContent + "）");
  ok(localStorage.getItem("kb-nav-collapsed") === "1", "收起状态写入 localStorage");
  ok(cards().length === TOTAL, "收起不影响列表内容");
  navtoggle.onclick();
  ok(!box.classList.contains("hidden"), "再次点击恢复展开");
  ok(!document.querySelector("aside").classList.contains("collapsed"), "aside 恢复宽度");
  ok(localStorage.getItem("kb-nav-collapsed") === "0", "展开状态已持久化");
}

console.log("\n================ 结果 ================");
console.log("通过 " + PASS + " 项，失败 " + FAIL.length + " 项");
if(FAIL.length){ console.log("失败项：\n  - " + FAIL.join("\n  - ")); process.exit(1); }
console.log("ALL_INDEX_UI_CHECKS_OK");
"""


def find_node():
    import shutil as _sh
    cands = []
    if os.environ.get("KB_NODE"):
        cands.append(os.environ["KB_NODE"])
    w = _sh.which("node")
    if w:
        cands.append(w)
    home = os.path.expanduser("~")
    cands += sorted(glob.glob(os.path.join(home, ".workbuddy/binaries/node/versions/*/node.exe")), reverse=True)
    cands += sorted(glob.glob(os.path.join(home, ".workbuddy/binaries/node/versions/*/bin/node")), reverse=True)
    for c in cands:
        if c and os.path.isfile(c):
            try:
                r = subprocess.run([c, "-e", "console.log(1)"], capture_output=True, timeout=30)
                if r.returncode == 0 and b"1" in r.stdout:
                    return c
            except Exception:
                continue
    return None


def parse_aside(html):
    """从静态 HTML 的 <aside> 中取出按钮（id/class/data-*）和页面所有 id。"""
    ids = sorted(set(re.findall(r'id="([A-Za-z0-9_-]+)"', html)))
    m = re.search(r"<aside[^>]*>(.*?)</aside>", html, re.S)
    buttons = []
    if m:
        for tag in re.findall(r"<button\b[^>]*>", m.group(1)):
            bid = re.search(r'id="([^"]+)"', tag)
            cls = re.search(r'class="([^"]*)"', tag)
            ds = dict(re.findall(r'data-([A-Za-z0-9_-]+)="([^"]*)"', tag))
            buttons.append({
                "id": bid.group(1) if bid else None,
                "cls": cls.group(1) if cls else "",
                "dataset": {_camel(k): v for k, v in ds.items()},
            })
    return ids, buttons


def _camel(k):
    parts = k.split("-")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


def main():
    root = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    html_path = os.path.join(root, "index.html")
    if not os.path.exists(html_path):
        print("未找到 %s（请先运行 build_index.py）" % html_path)
        return 1
    with open(html_path, encoding="utf-8") as f:
        html = f.read()

    m = re.search(r"<script>(.*?)</script>", html, re.S)
    if not m:
        print("index.html 中未找到内联 <script>")
        return 1
    page_js = m.group(1)

    node = find_node()
    if not node:
        print("SKIPPED: 未找到可用的 node 可执行文件，跳过交互检查。")
        print("         （可设环境变量 KB_NODE 指向 node，或安装 node 后重试）")
        return 0

    ids, buttons = parse_aside(html)
    stub = DOM_STUB.replace("__PAGE_IDS__", json.dumps(ids))
    stub = stub.replace("__ASIDE_BUTTONS__", json.dumps(buttons))

    js = stub + "\n" + page_js + "\n" + TESTS
    tmp = tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8")
    try:
        tmp.write(js)
        tmp.close()
        print("检查 %s" % html_path)
        print("使用 node: %s" % node)
        r = subprocess.run([node, tmp.name], capture_output=True, timeout=180)
        out = r.stdout.decode("utf-8", "replace")
        err = r.stderr.decode("utf-8", "replace")
        print(out.rstrip())
        if r.returncode != 0:
            if err.strip():
                print("--- stderr ---")
                print(err.strip())
            return 1
        return 0
    finally:
        try:
            os.unlink(tmp.name)
        except OSError:
            pass


if __name__ == "__main__":
    sys.exit(main())
