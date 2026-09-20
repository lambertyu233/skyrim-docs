import urllib.request, json
for u in ["https://api.github.com/repos/ersh1/OpenAnimationReplacer",
          "https://api.github.com/repos/ersh1/OpenAnimationReplacer/branches"]:
    req = urllib.request.Request(u, headers={'User-Agent':'x','Accept':'application/vnd.github+json'})
    print("="*60); print(u)
    try:
        d = json.loads(urllib.request.urlopen(req, timeout=60).read().decode())
        if isinstance(d, list):
            print([b.get('name') for b in d])
        else:
            print("default_branch:", d.get('default_branch'))
    except Exception as e:
        print("FAIL", e)
