import urllib.request, re

def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=90).read().decode('utf-8', 'replace')

cc = get('https://raw.githubusercontent.com/ersh1/OpenAnimationReplacer/main/src/Conditions.cpp')

def body(marker, n=40):
    lines = cc.split('\n')
    for i, l in enumerate(lines):
        if marker in l:
            print('===== %s (line %d) =====' % (marker, i + 1))
            for x in lines[i:i + n]:
                print('   |', x)
            print()
            return
    print('!! not found:', marker)

body('HasGraphVariableCondition::EvaluateImpl', 30)
body('AttackStateCondition', 60)
body('IsWeaponDrawnCondition::EvaluateImpl', 20)

print('=== AttackState enum map ===')
m = re.search(r'GetEnumMap\(\)\s*\{[\s\S]{0,1200}?\n\t\}', cc)
print(m.group(0)[:1200] if m else 'n/a')

# CommonLib Actor::IsAttacking
for url in ['https://raw.githubusercontent.com/alandtse/CommonLibVR/ng/include/RE/A/Actor.h',
            'https://raw.githubusercontent.com/alandtse/CommonLibVR/ng/src/RE/A/Actor.cpp']:
    try:
        t = get(url)
        print('=== %s ===' % url.split('/')[-1])
        for i, l in enumerate(t.split('\n')):
            if 'IsAttacking' in l:
                print('   %d: %s' % (i + 1, l.strip()))
    except Exception as e:
        print('FAIL', url, e)
