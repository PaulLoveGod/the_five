import urllib.request, re

url = 'https://www.duranno.com/qt/view/bible.asp?qtDate=2026-05-30'
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
res = urllib.request.urlopen(req)
html = res.read().decode('euc-kr', errors='replace')

# 기도 관련 키워드 검색
keywords = ['오늘의 기도', '중보기도', '기도 제목', 'prayer', 'amen', 'class="pray']
for kw in keywords:
    idx = html.find(kw)
    if idx > 0:
        print('FOUND:', kw)
        print(html[max(0,idx-200):idx+400])
        print('===')

# amen 버튼/섹션 확인
amen_idx = html.find('amen')
if amen_idx > 0:
    print('AMEN:', html[max(0,amen_idx-100):amen_idx+300])
