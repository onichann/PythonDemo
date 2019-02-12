import requests,requests.cookies

##文件上传
files={'file':open('favicon.ico','rb')}
r=requests.post('http://httpbin.org/post',files=files)
print(r.text)


##cookies
r=requests.get("https://www.baidu.com")
print(r.cookies)
for key,value in r.cookies.items():
    print(key+"="+value)


headers={
'Cookie':'BAIDUID=A1F6A6F044E557466D45C30683F9A457:FG=1; BIDUPSID=A1F6A6F044E557466D45C30683F9A457; PSTM=1548819344; BD_UPN=12314753; BDUSS=ldDREZtd00yZmY1OTRvWkVpa0ctfkIyUWdJYnp5aHNrQmpaV0luVFRzOHh5NFZjQUFBQUFBJCQAAAAAAAAAAAEAAAC-uE8i7OHfssGm37LG-gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADE-XlwxPl5cU; cflag=13%3A3; ZD_ENTRY=sogou; BD_HOME=1; H_PS_PSSID=1438_21111_28329_26350_28414; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=5; sugstore=0',
'Host':'www.baidu.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

r=requests.get("https://www.baidu.com",headers=headers)
# r.encoding='utf-8'
# with open('my.html','wb') as f:
#     f.write(r.content)
print(r.text)

cookie='BAIDUID=A1F6A6F044E557466D45C30683F9A457:FG=1; BIDUPSID=A1F6A6F044E557466D45C30683F9A457; PSTM=1548819344; BD_UPN=12314753; BDUSS=ldDREZtd00yZmY1OTRvWkVpa0ctfkIyUWdJYnp5aHNrQmpaV0luVFRzOHh5NFZjQUFBQUFBJCQAAAAAAAAAAAEAAAC-uE8i7OHfssGm37LG-gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADE-XlwxPl5cU; cflag=13%3A3; ZD_ENTRY=sogou; BD_HOME=1; H_PS_PSSID=1438_21111_28329_26350_28414; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=5; sugstore=0'
print(cookie.split(";")[0].split("="))
rcj=requests.cookies.RequestsCookieJar()


session=requests.session()
r=session.get('http://httpbin.org/cookies/set/number/123456789')
print(r.text)
r=session.get('http://httpbin.org/cookies')
print(r.text)
session.get()