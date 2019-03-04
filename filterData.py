import requests
from bs4 import BeautifulSoup

url="http://17.16.28.89/bsp/rest/er/bsp/organ/getAllOrganByStruId.json?struId=rootId"

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

def get_datas():
    try:
        resp=requests.get(url=url,headers=headers)
        if resp.status_code==requests.codes.ok:
            return resp.text
        else:
            print("errorInfo:"+resp.status_code)
    except Exception as e:
        print("error:"+e.args)

def parse_data(text):
    return 1
    # soup = BeautifulSoup(text, 'lxml')
    # print(soup.prettify())

if __name__ == '__main__':
    datas=get_datas()
    print(datas)
    parse_data(datas)