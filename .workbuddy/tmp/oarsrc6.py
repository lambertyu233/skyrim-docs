import urllib.request, re

def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=90).read().decode('utf-8', 'replace')

cc = get('https://raw.githubusercontent.com/ersh1/OpenAnimationReplacer/main/src/Conditions.cpp')
lines = cc.split('\n')
for i, l in enumerate(lines):
    if '::GetEnumMap' in l:
        owner = l.strip()
        body = '\n'.join(lines[i:i + 50])
        nums = re.findall(r'enumMap\[(-?\d+)\]\s*=\s*"([^"]+)"', body)
        print('### %s' % owner)
        print('   ', ', '.join('%s=%s' % (a, b) for a, b in nums) if nums else '(no numeric map)')
