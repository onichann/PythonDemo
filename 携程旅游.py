import requests
from bs4 import BeautifulSoup
import re
import json

def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Upgrade-Insecure-Requests':'1',
        'Cookie':'_abtest_userid=d40c61a1-aa2e-48e5-bbb4-da517e3451c7; gad_city=bfc57e4d16854aac15936b76ba41619a; _ga=GA1.2.1085782229.1550132481; _gid=GA1.2.911463644.1550132481; Session=smartlinkcode=U130709&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4901&SID=130709&OUID=&Expires=1550737280979; MKT_Pagesource=PC; _RF1=116.228.152.154; _RSG=q24jCvyUvjAvPVLVYqmnSB; _RDG=28c439ce1bb8712a91274d23ff86b2385e; _RGUID=ab797bce-4cb4-40b4-b731-c3489f55f679; ASP.NET_SessionSvc=MTAuOC4xODkuNjV8OTA5MHxqaW5xaWFvfGRlZmF1bHR8MTU0NzYzNjAxOTkwOQ; __utma=1.1085782229.1550132481.1550132529.1550132529.1; __utmc=1; __utmz=1.1550132529.1.1.utmcsr=flights.ctrip.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmb=1.1.10.1550132529; bdshare_firstime=1550132533090; _bfa=1.1550128658495.240n1r.1.1550128658495.1550132477627.2.6; _bfs=1.5; _gat=1; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224901%22%2C%22timestamp%22%3A1550132543549%7D%5D; _jzqco=%7C%7C%7C%7C1550132481248%7C1.766066022.1550132481178.1550132536439.1550132543566.1550132536439.1550132543566.undefined.0.0.5.5; __zpspc=9.1.1550132481.1550132543.5%233%7Cwww.sogou.com%7C%7C%7C%7C%23; _bfi=p1%3D290510%26p2%3D290564%26v1%3D6%26v2%3D5; appFloatCnt=5',
        'Connection':'keep-alive',
        'Referer':'http://you.ctrip.com/place/Shanghai2.html'
    }
    proxies = {
        'http': 'http://180.118.77.9:9999'
    }
    # r=requests.get(url,headers=headers,proxies=proxies)
    try:
        r = requests.get(url, headers=headers)
    except requests.RequestException as e:
        return None
    return r.text if (r.status_code == 200) else None

def page_pinglun():
    url='http://you.ctrip.com/destinationsite/TTDSecond/SharedView/AsynCommentView'

def main():
    data=dict()
    url='http://you.ctrip.com/sight/shanghai2/1412255.html'
    html=getHtml(url)
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    print(soup.prettify())
    print('-------------')
    name=soup.find(class_='dest_toptitle detail_tt').find_next(name='div',attrs={'class':'cf'})\
        .find_next(name='div',attrs={'class':'f_left'}).find_next(name='h1').find_next(name='a').string.strip()
    print('name='+name)
    # print(soup.select('.dest_toptitle .cf .f_left a')[0].string)
    data['name']=name
    discription=soup.find_all(name='div',attrs={'class':'toggle_s'})[0].find(name='div').string.strip()
    print('discription='+discription)
    data['discription']=discription
    print(data)
    save(data)
    return None




def save(data):
    if(data):
        print(data)
    with open('xiecheng.txt','w',encoding='utf-8') as file:
        #indent 缩进字符
        json.dump(data,file,ensure_ascii=False,indent=2)

if __name__ == '__main__':
    main()