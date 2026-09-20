import urllib.request, re

files = {
    'Conditions.cpp': 'https://raw.githubusercontent.com/ersh1/OpenAnimationReplacer/main/src/Conditions.cpp',
    'Conditions.h': 'https://raw.githubusercontent.com/ersh1/OpenAnimationReplacer/main/src/Conditions.h',
    'Parsing.cpp': 'https://raw.githubusercontent.com/ersh1/OpenAnimationReplacer/main/src/Parsing.cpp',
    'ReplacerMods.cpp': 'https://raw.githubusercontent.com/ersh1/OpenAnimationReplacer/main/src/ReplacerMods.cpp',
}
texts = {}
for name, url in files.items():
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    texts[name] = urllib.request.urlopen(req, timeout=60).read().decode('utf-8', 'replace')

def grep(name, pattern, ctx=3, limit=8, label=''):
    t = texts[name]
    lines = t.split('\n')
    hits = [i for i, l in enumerate(lines) if re.search(pattern, l)]
    print('### %s :: /%s/ %s -> %d hits' % (name, pattern, label, len(hits)))
    for i in hits[:limit]:
        for l in lines[max(0, i - ctx):i + ctx + 1]:
            print('   |', l)
        print('   ...')

grep('Conditions.h', r'GraphVariable', 2, 12)
grep('Conditions.cpp', r'GraphVariableBool', 4, 3)
grep('ReplacerMods.cpp', r'_conditions|GetConditions|legacy|DAR', 3, 8)
grep('Parsing.cpp', r'_conditions|IsSneaking|IsActorBase', 3, 8)
