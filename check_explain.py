import urllib.request, re

url = 'https://www.duranno.com/qt/view/explain.asp?qtDate=2026-05-30'
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
res = urllib.request.urlopen(req, timeout=5)
html = res.read().decode('euc-kr', errors='replace')
all_classes = re.findall(r'class="([^"]+)"', html)
print('Classes:', sorted(set(all_classes)))

# bible div 내용 추출
m = re.search(r'class="bible">([\s\S]*?)</div>', html)
if m:
    t = re.sub('<[^>]+>', ' ', m.group(1)).replace('&nbsp;',' ')
    t = re.sub(r'\s+', ' ', t).strip()
    print('\nexplain bible content:', t[:500])
