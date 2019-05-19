# import requests
# import json
#
# url = "http://172.16.15.220:8088/default/app/com.shghtd.tdzf.app.xcsb.xcsb.addXcsb.biz.ext"
#
# payload = "{\"xcsb\":{\"tbbh\":\"S2019050600001\",\"ajly\":\"\",\"bsqd\":\"移动端上报3\",\"szq\":19,\"szz\":19516,\"ytbmj\":96825.86,\"zdmj\":96825.86,\"sbr\":\"许俊\",\"cjsj\":\"2018-01-23\",\"xsqk\":\"\",\"distance\":111}}\n\n"
# headers = {
#     'content-type': "application/json",
#     'cache-control': "no-cache",
#     'postman-token': "6b8b002f-6eb1-d5c6-e1e6-256ad2288276"
#     }
# response=requests.post(url,data=json.dumps(json.loads(payload)) ,headers=headers)
# print(response.text)



import requests

url = "http://localhost:8088/default/app/com.shghtd.tdzf.app.xcsb.xcsb.queryXcsbList.biz.ext"

payload = "{\"param\":{\"pageSize\":20,\"pageIndex\":0,\"sortField\":\"cjsj\",\"sortOrder\":\"desc\",\"queryParam\":{\"xsqk\":\"\",\"tbbh\":\"\",\"szq\":\"\",\"szz\":\"\"}}}\r\n"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "cd4f29e8-b72c-22ec-028a-c4d26b4a4095"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)