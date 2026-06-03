import urllib.request, re

for path in ['pray', 'prayer', 'bibleprayer']:
    url = f'https://www.duranno.com/qt/view/{path}.asp?qtDate=2026-05-30'
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=4)
        html = res.read().decode('euc-kr', errors='replace')
        t = re.sub('<[^>]+>', ' ', html)
        t = re.sub(r'\s+', ' ', t).strip()
        print(f'{path}: OK, len={len(html)}')
        print(t[100:400])
        print('---')
    except Exception as e:
        print(f'{path}: {e}')

# bible.asp 에서 song 다음 섹션이 기도인지 확인
url2 = 'https://www.duranno.com/qt/view/bible.asp?qtDate=2026-05-30'
req2 = urllib.request.Request(url2, headers={'User-Agent':'Mozilla/5.0'})
res2 = urllib.request.urlopen(req2, timeout=4)
html2 = res2.read().decode('euc-kr', errors='replace')
# song box 이후 내용 확인
song_end = html2.find('</div>', html2.find('class="song box"'))
print('\nAfter song box:')
t2 = re.sub('<[^>]+>', ' ', html2[song_end:song_end+800])
t2 = re.sub(r'\s+', ' ', t2).strip()
print(t2[:400])
