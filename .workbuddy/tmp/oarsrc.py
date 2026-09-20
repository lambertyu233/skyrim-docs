import urllib.request, re

files = {
    'Conditions.cpp': 'https://raw.githubusercontent.com/ersh1/OpenAnimationReplacer/main/src/Conditions.cpp',
    'Parsing.cpp': 'https://raw.githubusercontent.com/ersh1/OpenAnimationReplacer/main/src/Parsing.cpp',
    'ReplacerMods.cpp': 'https://raw.githubusercontent.com/ersh1/OpenAnimationReplacer/main/src/ReplacerMods.cpp',
    'Conditions.h': 'https://raw.githubusercontent.com/ersh1/OpenAnimationReplacer/main/src/Conditions.h',
}

texts = {}
for name, url in files.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(req, timeout=60).read().decode('utf-8', 'replace')
        texts[name] = data
        print('OK', name, len(data))
    except Exception as e:
        print('FAIL', name, e)

def show(name, pattern, ctx=3, limit=6):
    t = texts.get(name)
    if not t: return
    lines = t.split('\n')
    hits = [i for i, l in enumerate(lines) if re.search(pattern, l)]
    print('=== %s :: /%s/ -> %d hits' % (name, pattern, len(hits)))
    for i in hits[:limit]:
        print('   --- line %d ---' % (i + 1))
        for l in lines[max(0, i - ctx):i + ctx + 1]:
            print('   |', l)

show('Conditions.cpp', r'GraphVariableBoolEqual', 6, 3)
show('Conditions.cpp', r'IsAttackingCondition', 8, 2)
show('Parsing.cpp', r'GraphVariable|IsActorBase\(', 4, 6)
show('ReplacerMods.cpp', r'GraphVariable|IsEquippedType', 4, 6)
