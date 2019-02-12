import requests
import re
import urllib.error

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

try:
    r = requests.get("https://www.zhihu.com/explore",headers=headers)
except Exception as e:
    print(e)
print(r.status_code)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)


r=requests.get("https://github.com/favicon.ico")
with open('favicon.ico','wb') as f:
    f.write(r.content)


data={'name':'wutong'}
r=requests.post('http://httpbin.org/post',data=data)
print(r.text)

