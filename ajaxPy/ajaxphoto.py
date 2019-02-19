import requests
import urllib.parse
import os
import re

save_path=r'e:\\python爬虫\\photos\\'
url = 'https://www.toutiao.com/api/search/content/?'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
params = {
    'aid': 24,
    'offset': 0,
    'format': 'json',
    'keyword': '美女',
    'autoload': 'true',
    'count': 20,
    'en_qc': 1,
    'cur_tab': 1,
    'from': 'search_tab',
    'pd': 'synthesis'
}

def getPages(offset=0):
    params['offset']=offset
    try:
        resp=requests.get(url+urllib.parse.urlencode(params),headers=headers)
        if resp.status_code==requests.codes.ok:
            return resp.json()
    except Exception as e:
        print('error:'+e.args.__str__())

def parseJson(json):
    if json:
        datas=json.get('data')
        for data in datas:
            title=data.get('title')
            image_list=data.get('image_list')
            yield {
                'title':title,
                'image_list':image_list
            }

def save_image(data):
    ''' {title:str,'image_list':list<dict<>>}'''
    if(not data.get('title')):
        return
    if not os.path.exists(save_path+data.get('title')):
        os.makedirs(save_path+data.get('title'))

    for image in data.get('image_list'):
        url=image.get('url')
        print('url:'+url)
        if 'pgc-image/' not in url:
            continue
        result=re.search('pgc-image/(.*?)$',url)
        print(result.group(1))
        file_path='{0}{1}\\{2}.jpg'.format(save_path,data.get('title'),result.group(1))
        try:
            resp=requests.get(url)
            with open(file_path,'wb') as file_obj:
                file_obj.write(resp.content)
            print('已下载图片：'+file_path)
        except Exception as e:
            print('下载失败图片：'+file_path)

if __name__ == '__main__':
    for i in range(0,3):
        json=getPages(i*20)
        for data in parseJson(json):
            if(data):
                save_image(data)
