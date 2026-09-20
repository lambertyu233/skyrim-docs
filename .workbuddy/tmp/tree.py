import urllib.request, json, re
u = "https://api.github.com/repos/ersh1/OpenAnimationReplacer/git/trees/main?recursive=1"
req = urllib.request.Request(u, headers={'User-Agent':'x','Accept':'application/vnd.github+json'})
d = json.loads(urllib.request.urlopen(req, timeout=60).read().decode())
paths = [t['path'] for t in d.get('tree',[])]
print("total:", len(paths))
for p in paths:
    if re.search(r'[Aa]ttack|[Ss]tate', p):
        print("  ", p)
