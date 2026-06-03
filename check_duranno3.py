import urllib.request, re

# essay.asp 에서 기도 내용 확인
url = 'https://www.duranno.com/qt/view/essay.asp?qtDate=2026-05-30'
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
res = urllib.request.urlopen(req, timeout=5)
html = res.read().decode('euc-kr', errors='replace')

# 전체 텍스트 추출
text = re.sub('<[^>]+>', ' ', html)
text = re.sub(r'\s+', ' ', text).strip()

# 기도 관련 내용 찾기
for kw in ['기도', '묵상', '말씀', '오늘']:
    idx = text.find(kw)
    if idx > 0:
        print(f'"{kw}" found at {idx}:')
        print(text[max(0,idx-50):idx+200])
        print('---')
        break

# 300-1500 글자 범위 출력
print('\n=== 본문 텍스트 샘플 ===')
print(text[200:800])
