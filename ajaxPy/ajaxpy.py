from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    , 'Referer': 'https://m.weibo.cn/u/2830678474'
    , 'host': 'm.weibo.cn'
    , 'X-Requested-With': 'XMLHttpRequest'
}


def getPage(page=1):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == requests.codes.ok:
            return response.json()
    except Exception as e:
        print('Error:', e.args)


def parseJson(json):
    if (json):
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            print('item:' + str(item))
            if item != None:
                weibo['id'] = item.get('id')
                weibo['attitudes_count'] = item.get('attitudes_count')
                text = item.get('text')
                soup = BeautifulSoup(text, 'lxml')
                text = soup.get_text()
                weibo['text'] = text
            yield weibo


if __name__ == '__main__':
    page_info = []
    for page in range(1, 11):
        json = getPage(page)
        results = parseJson(json)
        for result in results:
            if result:
                page_info.append(result)
    print(page_info)
