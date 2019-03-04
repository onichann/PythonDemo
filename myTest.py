import requests
import json
import urllib.parse
import time

url='http://17.16.28.42/serviceTest'
# url='http://httpbin.org/post'
datas={'DABH':'1106-YW0501-2012-0026',
       'serviceCode':'tdgyjnml'}
headers={
    'Content-Type':'application/json; charset=UTF-8',
    # 'Connection':'close'
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0',
    # 'user-agent': 'Apache-HttpClient/4.5.5 (Java/1.8.0_65)',
    # 'x-requested-with': 'XMLHttpRequest',
    'Host':'17.16.8.74'
}
proxies={
    "https":"https://111.176.21.50:9999",
    'http':'http://114.249.116.88:9000'
}

try:
    # print(json.dumps(datas))

    # s=requests.session()
    # req=requests.Request(method='post',url=url,headers=headers,data=datas)
    # prepped=s.prepare_request(req)
    # resp=s.send(prepped)

    resp=requests.post(url,json=datas,headers=headers)
    if resp.status_code==requests.codes.ok:
        # print(resp.json())
        print(resp.text)
    else:
        print(resp.status_code)
except Exception as e:
    print(e)

# 17.16.28.42/DASJ/GY/1106-YW0501-2012-0026/1106-YW0501-2012-0026-001.pdf
#http://17.16.8.74:8999/file/11.pdf