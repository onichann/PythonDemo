import requests
import json

ip = "http://192.168.5.116:8088/default/app"
# ip = "http://172.16.15.220:8088/default/app"


# 增加巡查上报记录
def addxcsb():
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
def query_xcsb():
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
def delete_xcsb():
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
def submit_xcsb():
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
def query_xcsbList():
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
            "szz":"",
            "sbr":"",
            "tbbhAndXsqk":"1"
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


def post_job():

    url = ip + "/com.shghtd.tdzf.app.plot.addJob.biz.ext"
    # url="http://httpbin.org/post"

    headers = {
        # 'Content-Type':'application/json',
        'x-requested-with': 'XMLHttpRequest'
    }
    data = {
        "geometry": [[[7945.442130350259,-1105.3057300221099],[6357.9381478980395,-2883.3096090075696],[8792.110490353645,-3348.9773684986067]]],
        "layers": ["44c1e80e1425473d963c5fe1e161ef1f", "ec5cd1a04d914fb296735c1d7a1851df"],
            # "layers": ["2cff71d0d83649f09ab4ed4a38697754", "44c1e80e1425473d963c5fe1e161ef1f", "ec5cd1a04d914fb296735c1d7a1851df"],
        # "layers": ["6d56ed32eed3437896e0ed0e4dd3f67c","4e1f3217d0904570ad6a4bf73222ea5a","ed792411eff6468da48931c0b4cce295"],
        "type": "tdzf",
        "tbbh": 111122225556,
        "userId": "19978"
    }

    try:
        resp = requests.post(url,data={"params":json.dumps(data)},headers=headers)
        if resp.status_code == requests.codes.ok:
            # print(resp.json())
            print(resp.text)
        else:
            print(resp.status_code)
    except Exception as e:
        print(e)


def query_job():
    url = ip + "/com.shghtd.tdzf.app.plot.queryJobResult.biz.ext"
    headers = {
        # 'Content-Type':'application/json',
        'x-requested-with': 'XMLHttpRequest'
    }
    try:
        resp = requests.post(url,data={"tbbh":"1558318059576"},headers=headers)
        if resp.status_code == requests.codes.ok:
            # print(resp.json())
            print(resp.text)
        else:
            print(resp.status_code)
    except Exception as e:
        print(e)


def create_tbbh():
    url=ip+"/com.shghtd.tdzf.app.xcsb.xcsb.createTbbh.biz.ext"
    headers = {

        'x-requested-with': 'XMLHttpRequest'
    }
    param={
        "param":{
            "district":"14",
            "town":"14816",
            "recorder_id":"pd_xj",
            "recorder":"许俊",
            "bid":"1ca452c2f6d246458af97e126f77f9f4"
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

def createTask():
    url=ip+"/com.shghtd.tdzf.app.djfxOptimization.newcomponent.OverAnalysisOptimizationTest.biz.ext"
    headers = {

        'x-requested-with': 'XMLHttpRequest'
    }

    try:
        resp = requests.get(url,headers=headers)
        if resp.status_code == requests.codes.ok:
            # print(resp.json())
            print(resp.text)
        else:
            print(resp.status_code)
    except Exception as e:
        print(e)

def TestTask():
    url=ip+"/com.shghtd.tdzf.app.djfxOptimization.newcomponent.OAOTest.biz.ext"
    headers = {

        'x-requested-with': 'XMLHttpRequest'
    }

    try:
        resp = requests.get(url,headers=headers)
        if resp.status_code == requests.codes.ok:
            # print(resp.json())
            print(resp.text)
        else:
            print(resp.status_code)
    except Exception as e:
        print(e)

# addxcsb()
# query_xcsb()
# delete_xcsb()
# submit_xcsb()
# query_xcsbList()
# post_job()
# query_job()
# create_tbbh()
# createTask()
# TestTask()