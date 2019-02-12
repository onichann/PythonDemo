from urllib.request import ProxyHandler,build_opener
from urllib.error import URLError

proxy_handler = ProxyHandler({
    # 'http': 'http://127.0.0.1:9743',
    'https': 'https://125.123.139.77:9999'
})
opener=build_opener(proxy_handler)
try:
    response=opener.open("http:www.baidu.com")
    print(response.read().decode('utf-8'))

except URLError as e:
    print(e.reason)