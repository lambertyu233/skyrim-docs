#!/usr/bin/env python3
"""
通用 MediaWiki 抓取器（适配 ck.uesp.net / modding.wiki 等任意 MediaWiki 站点）。

为什么需要它（实战踩坑）：
  - 直接用 WebFetch 抓 MediaWiki 页面往往只返回标题，正文抽不到；
  - 用 urllib 默认 User-Agent 访问会被 403。
解法：走 MediaWiki API（action=parse 取 wikitext，或 list=categorymembers 列分类成员），
     UA 设为浏览器串即可正常抓取。

用法：
  python fetch_mediawiki.py --api https://ck.uesp.net/w/api.php "Main_Page"
  python fetch_mediawiki.py --api https://ck.uesp.net/w/api.php --cat "Category:Papyrus"
  python fetch_mediawiki.py --api https://ck.uesp.net/w/api.php --links "Papyrus"
  # 不加 --api 时默认 ck.uesp.net；--api 也可写成 --api=URL
"""
import sys, json, urllib.request, urllib.parse, os

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
OUT = "_raw"


def api(api_url, params):
    params = dict(params)
    params["format"] = "json"
    url = api_url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch_wikitext(api_url, title):
    d = api(api_url, {"action": "parse", "page": title, "prop": "wikitext", "redirects": 1})
    return d["parse"]["wikitext"]["*"]


def category_members(api_url, cat):
    if not cat.startswith("Category:"):
        cat = "Category:" + cat
    members, cmcontinue = [], None
    while True:
        p = {"action": "query", "list": "categorymembers", "cmtitle": cat, "cmlimit": "500"}
        if cmcontinue:
            p["cmcontinue"] = cmcontinue
        d = api(api_url, p)
        for m in d["query"]["categorymembers"]:
            members.append(m["title"])
        cmcontinue = d.get("continue", {}).get("cmcontinue")
        if not cmcontinue:
            break
    return members


def page_links(api_url, title):
    d = api(api_url, {"action": "query", "prop": "links", "titles": title, "pllimit": "500", "redirects": 1})
    links = []
    for p in d["query"]["pages"].values():
        for l in p.get("links", []):
            links.append(l["title"])
    return links


def save(title, text):
    os.makedirs(OUT, exist_ok=True)
    safe = title.replace("/", "_").replace(":", "_")
    path = os.path.join(OUT, safe + ".wiki.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    args = sys.argv[1:]
    api_url = "https://ck.uesp.net/w/api.php"
    mode, target = "page", None
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--api":
            api_url = args[i + 1]; i += 2; continue
        if a.startswith("--api="):
            api_url = a.split("=", 1)[1]; i += 1; continue
        if a == "--cat":
            mode = "cat"; target = args[i + 1]; i += 2; continue
        if a == "--links":
            mode = "links"; target = args[i + 1]; i += 2; continue
        target = a; i += 1
    if mode == "cat":
        mem = category_members(api_url, target)
        print(f"== {target} 成员 ({len(mem)}) ==")
        for t in mem:
            print(t)
    elif mode == "links":
        links = page_links(api_url, target)
        print(f"== {target} 出链 ({len(links)}) ==")
        for t in links:
            print(t)
    else:
        wt = fetch_wikitext(api_url, target)
        p = save(target, wt)
        print(f"[SAVED] {target} -> {p} ({len(wt)} chars)")


if __name__ == "__main__":
    main()
