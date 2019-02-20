import requests
import urllib.request
import urllib.parse
from urllib.request import BaseHandler
import http.client
import json

###########
# response = urllib.request.urlopen('http://116.228.152.154:9898/workmanage/login.action')
# data=bytes(urllib.parse.urlencode({'type': '我'}),encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read().decode('utf-8'))
# print(type(response))
# print(response.getheaders())
# print(response.getheader('Server'))
# print(response)

data=bytes(json.dumps({'type': '我1'}),encoding='utf8')
request=urllib.request.Request('http://httpbin.org/post',data=data,method="POST")
# request=urllib.request.Request('https://www.baidu.com',data=data,method="POST")
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
request.add_header('Content-Type','application/json')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))


