import urllib.request

for page in ['explain', 'essay']:
    url = f'https://www.duranno.com/qt/view/{page}.asp?qtDate=2026-05-30'
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5)
        html = res.read().decode('euc-kr', errors='replace')
        # class 목록 확인
        import re
        divs = re.findall(r'class="([^"]*(?:pray|bible|qt|content|body)[^"]*)"', html, re.IGNORECASE)
        print(f'=== {page}.asp ===')
        print('Classes:', list(set(divs))[:10])
        # 본문 내용 영역
        for cls in ['content', 'bible', 'qt-content', 'essay']:
            m = re.search(f'class="{cls}">(.*?)</div>', html, re.DOTALL)
            if m:
                text = re.sub('<[^>]+>', '', m.group(1)).strip()[:200]
                print(f'  {cls}:', text)
    except Exception as e:
        print(f'{page}: ERROR - {e}')
