import urllib.request, re

# bible.asp 전체 텍스트에서 기도 관련 내용 확인
url = 'https://www.duranno.com/qt/view/bible.asp?qtDate=2026-05-30'
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
res = urllib.request.urlopen(req, timeout=5)
html = res.read().decode('euc-kr', errors='replace')

# song, prayer 관련 div 찾기
patterns = [
    ('song', r'class="song[^"]*">([\s\S]*?)</div>'),
    ('pray', r'class="pray[^"]*">([\s\S]*?)</div>'),
    ('prayer', r'class="prayer[^"]*">([\s\S]*?)</div>'),
]
for name, pat in patterns:
    m = re.search(pat, html)
    if m:
        text = re.sub('<[^>]+>', '', m.group(1)).replace('&nbsp;',' ').strip()
        print(f'{name}: {text[:300]}')

# 페이지 내 모든 div class 목록
all_classes = re.findall(r'class="([^"]+)"', html)
print('\nAll classes:', sorted(set(all_classes)))
