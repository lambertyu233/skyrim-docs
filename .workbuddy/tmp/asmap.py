import urllib.request, re
urls = [
 "https://raw.githubusercontent.com/ersh1/OpenAnimationReplacer/main/src/Conditions/Conditions/AttackStateCondition.h",
 "https://raw.githubusercontent.com/ersh1/OpenAnimationReplacer/main/src/Conditions/Conditions/AttackStateCondition.cpp",
]
for u in urls:
    try:
        d = urllib.request.urlopen(u, timeout=30).read().decode('utf-8', 'ignore')
    except Exception as e:
        print("FAIL", u, e); continue
    print("="*70); print(u, len(d))
    print(d)
