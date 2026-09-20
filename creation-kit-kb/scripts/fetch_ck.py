#!/usr/bin/env python3
# Fetch pages from the UESP Creation Kit MediaWiki API.
# Usage: python fetch_ck.py <PageTitle> [PageTitle2 ...]
# Saves raw wikitext to ../_raw/<PageTitle>.wiki.txt and prints a preview.
import urllib.request, urllib.parse, json, sys, os

API = "https://ck.uesp.net/w/api.php"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_raw")

def fetch_wikitext(title):
    params = {
        "action": "parse",
        "page": title,
        "prop": "wikitext",
        "format": "json",
        "redirects": 1,
    }
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    data = urllib.request.urlopen(req, timeout=40).read()
    j = json.loads(data)
    if "error" in j:
        return None, j["error"]
    wt = j["parse"]["wikitext"]["*"]
    return wt, None

def fetch_category_members(cat, limit=200):
    members = []
    cont = {}
    while len(members) < limit:
        params = {
            "action": "query",
            "list": "categorymembers",
            "cmtitle": cat,
            "cmlimit": 200,
            "format": "json",
        }
        params.update(cont)
        url = API + "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        data = urllib.request.urlopen(req, timeout=40).read()
        j = json.loads(data)
        for m in j["query"]["categorymembers"]:
            members.append(m["title"])
        if "continue" not in j:
            break
        cont = j["continue"]
    return members

def main():
    os.makedirs(OUT, exist_ok=True)
    args = sys.argv[1:]
    quiet = False
    if args and args[0] == "--quiet":
        quiet = True
        args = args[1:]
    if not args:
        print("No args. Use: fetch_ck.py [--quiet] <Title> ...  OR  fetch_ck.py --cat <Category>")
        return
    if args[0] == "--cat":
        cat = args[1] if args[1].startswith("Category:") else "Category:" + args[1]
        members = fetch_category_members(cat)
        print(f"== {cat} members ({len(members)}) ==")
        for t in members:
            print(t)
        return
    for title in args:
        wt, err = fetch_wikitext(title)
        if err:
            print(f"[ERROR] {title}: {err}")
            continue
        safe = title.replace("/", "_").replace(":", "_")
        path = os.path.join(OUT, safe + ".wiki.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(wt)
        if not quiet:
            print(f"[SAVED] {title} -> {path}  ({len(wt)} chars)")
            lines = [l for l in wt.splitlines() if l.strip()]
            print("  PREVIEW:")
            for l in lines[:25]:
                print("   |", l[:120])
        else:
            print(f"[SAVED] {title} ({len(wt)} chars)")

if __name__ == "__main__":
    main()
