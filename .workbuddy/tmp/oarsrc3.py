import urllib.request, re

base = 'https://raw.githubusercontent.com/ersh1/OpenAnimationReplacer/main/src/'
def get(f):
    req = urllib.request.Request(base + f, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=60).read().decode('utf-8', 'replace')

ch = get('Conditions.h')
cc = get('Conditions.cpp')
pa = get('Parsing.cpp')

names = re.findall(r'GetName\(\) const override \{\s*return\s+"([^"]+)"', ch)
print('=== 全部条件名 (%d) ===' % len(names))
print(', '.join(names))
print()

# graph variable classes: print class block
for m in re.finditer(r'class (\w*GraphVariable\w*)', ch):
    start = m.start()
    block = ch[start:start + 2500]
    print('===== class', m.group(1), '=====')
    for line in block.split('\n')[:45]:
        print('   |', line)
    print()

# Parsing.cpp: ParseConditionsTxt function body
lines = pa.split('\n')
for i, l in enumerate(lines):
    if 'ParseConditionsTxt' in l and ('(' in l) and 'conditionSet' in l and 'Parsing' in l or re.match(r'.*Parsing::ParseConditionsTxt', l):
        print('---- Parsing.cpp line %d: %s' % (i + 1, l))
print()
idx = [i for i, l in enumerate(lines) if 'ConditionSet> Parsing::ParseConditionsTxt' in l or ('ParseConditionsTxt' in l and '{' in l)]
print('candidate defs:', idx)
if idx:
    s = idx[0]
    for l in lines[s:s + 130]:
        print('   |', l)
