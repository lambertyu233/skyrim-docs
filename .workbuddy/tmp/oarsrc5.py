import urllib.request, re

def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=90).read().decode('utf-8', 'replace')

cc = get('https://raw.githubusercontent.com/ersh1/OpenAnimationReplacer/main/src/Conditions.cpp')
lines = cc.split('\n')

# find each GetEnumMap definition and the class it belongs to
for i, l in enumerate(lines):
    if 'GetEnumMap()' in l and '{' in l:
        # walk back to find the enclosing '::GetEnumMap'
        for j in range(i, max(0, i - 40), -1):
            if '::GetEnumMap' in lines[j]:
                owner = lines[j].strip()
                break
        else:
            owner = '(?) ' + lines[max(0, i - 1)].strip()
        body = '\n'.join(lines[i:i + 45])
        nums = re.findall(r'enumMap\[(-?\d+)\]\s*=\s*"([^"]+)"', body)
        print('### %s' % owner)
        print('   ', ', '.join('%s=%s' % (a, b) for a, b in nums) if nums else '(no numeric map)')
        print()
