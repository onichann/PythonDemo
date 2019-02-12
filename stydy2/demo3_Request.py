import requests
import urllib3

urllib3.disable_warnings()
response=requests.get("https://www.12306.cn",verify=False)
print(response.status_code)

import logging
logging.captureWarnings(True)
response=requests.get("https://www.12306.cn",verify=False)
print(response.status_code)


#指定本地证书
# response=requests.get('https:www.12306.cn',cert=('/xx.cert','/key'))


#代理
proxies={
    'http': 'http://144.255.12.170:9999',
    'https': 'https://116.209.52.12:9999'
}

r=requests.get("http://httpbin.org/get",proxies=proxies)
print(r.text)

#http basic auth
proxies={
    'http':'http://user:password@ip:port/'
}
r=requests.get("http://httpbin.org/get",proxies=proxies)

from requests.auth import  HTTPBasicAuth

r=requests.get("http:localhost:5000",auth=HTTPBasicAuth('username','password'))

r=requests.get("http:localhost:5000",auth=('username','password'))



#sockets
proxies={
    'http':'socks5://user:password@host:port',
    'https':'socks5://user:password@host:port'
}
r=requests.get("http://httpbin.org/get",proxies=proxies)

r=requests.get("http://httpbin.org/get",timeout=10)

#oauth
from requests_oauthlib import OAuth1

url="https:/ip"
auth=OAuth1('xx','xx','xx','xx')
requests.get("url",auth=auth)
# @see https://requests-oauthlib.readthedoc.org

#request
from requests import Request,Session
url='http://httpbin.org/post'
data={
    'name':'germey'
}
headers={
    'User-Agent':''
}
s=Session()
req=Request('POST',url,data=data,headers=headers)
prepped=s.prepare_request(req)
r=s.send(prepped)
print(r.text)