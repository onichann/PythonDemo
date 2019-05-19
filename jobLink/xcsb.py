import requests

ip = "http://tdzfxx:8088/default/app"
# ip = "http://172.16.15.220:8088/default/app"


# 增加巡查上报记录
def addxcsb(ip):
    url = ip + "/com.shghtd.tdzf.app.xcsb.xcsb.addXcsb.biz.ext"
    # url="http://httpbin.org/post"
    headers={
        'Content-Type':'application/json',
        'x-requested-with': 'XMLHttpRequest'
    }
    data = {
                    "xcsbGuid":"4483d1473c644feeb77790e8f952ab13",
                    "tbbh": '112',
                    "ajly": "feaga",
                    "bsqd": "上海2",
                    "szq": "sss",
                    "szz": "ssss",
                    "ytbmj": 12.1,
                    "zdmj": 661,
                    "sbr": "sefie",
                    "cjsj": "2018-01-23",
                    "xsqk": "ssfjiji",
                    "distance":"500"
            }

    try:
        resp = requests.post(url, json={"xcsb":data})
        if resp.status_code == requests.codes.ok:
            # print(resp.json())
            print(resp.text)
        else:
            print(resp.status_code)
    except Exception as e:
        print(e)

# 查询巡查上报单个记录
def query_xcsb(ip):
    url=ip+"/com.shghtd.tdzf.app.xcsb.xcsb.queryXcsbDetail.biz.ext"
    headers = {

        'x-requested-with': 'XMLHttpRequest'
    }
    param={
        "id":"36250062dca74be0ba20b28c02e687f9"
    }

    try:
        resp = requests.get(url,param,headers=headers)
        if resp.status_code == requests.codes.ok:
            # print(resp.json())
            print(resp.text)
        else:
            print(resp.status_code)
    except Exception as e:
        print(e)


# 删除
def delete_xcsb(ip):
    url=ip+"/com.shghtd.tdzf.app.xcsb.xcsb.deleteXcsb.biz.ext"
    headers = {

        'x-requested-with': 'XMLHttpRequest'
    }
    param={
        "id":"464ac8dd0d594e6cb853700baba72e69"
    }

    try:
        resp = requests.get(url,param,headers=headers)
        if resp.status_code == requests.codes.ok:
            # print(resp.json())
            print(resp.text)
        else:
            print(resp.status_code)
    except Exception as e:
        print(e)

# 提交
def submit_xcsb(ip):
    url=ip+"/com.shghtd.tdzf.app.xcsb.xcsb.submitXcsb.biz.ext"
    headers = {

        'x-requested-with': 'XMLHttpRequest'
    }
    param={
        "id":"4483d1473c644feeb77790e8f952ab23"
    }

    try:
        resp = requests.get(url,param,headers=headers)
        if resp.status_code == requests.codes.ok:
            # print(resp.json())
            print(resp.text)
        else:
            print(resp.status_code)
    except Exception as e:
        print(e)


# 查询列表
def query_xcsbList(ip):
    url=ip+"/com.shghtd.tdzf.app.xcsb.xcsb.queryXcsbList.biz.ext"
    headers = {

        'x-requested-with': 'XMLHttpRequest'
    }
    param={
        "pageSize":20,
        "pageIndex":0,
        "sortField":"cjsj",
        "sortOrder":"desc",
        "queryParam":{
            "xsqk":"",
            "tbbh":"",
            "szq":"",
            "szz":""
        }

    }

    try:
        resp = requests.post(url, json=param,headers=headers)
        if resp.status_code == requests.codes.ok:
             print(resp.json())
            # print(resp.text)
        else:
            print(resp.status_code)
    except Exception as e:
        print(e)

# addxcsb(ip)
# query_xcsb(ip)
# delete_xcsb(ip)
# submit_xcsb(ip)
query_xcsbList(ip)