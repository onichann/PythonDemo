import http.cookiejar,urllib.request,urllib.error,socket

cookie=http.cookiejar.CookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('https://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)

############
filename='cookies_txt'
cookie=http.cookiejar.MozillaCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.baidu.com')
cookie.save(ignore_discard=False, ignore_expires=False)

cookie=http.cookiejar.MozillaCookieJar()
cookie.load('cookies_txt')
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
try:
    response=opener.open('http://www.baidu.com')
except urllib.error.URLError as e:
    print(e.reason)
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')
print(response.read().decode('utf-8'))
