import requests, re, time


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    proxies = {
        'http': 'http://180.118.77.9:9999'
    }
    # r=requests.get(url,headers=headers,proxies=proxies)
    r = requests.get(url, headers=headers)
    return r.text if (r.status_code == 200) else None


if __name__ == '__main__':
    url = 'http://maoyan.com/board/4'
    url = "https://dianying.taobao.com/showList.htm?spm=a1z21.3046609.t1.1.32c0112a0zIzCb&n_s=new"
    html = get_page(url)
    print(html)
    pattern = re.compile('<span class="bt-l">(.*?)</span>[\s\S]*?<span class="bt-r">(.*?)</span>[\s\S]*?<div class="movie-card-list">([\s\S]*?)</div>')
    # pattern = re.compile('<span class="bt-l">(.*?)</span>', re.S)
    # pattern = re.compile('<span class="bt-r">(\d*\.\d*)</span>', re.S)
    # pattern = re.compile('<div class="movie-card-list">(.*?)</div>', re.S)

    lists = re.findall(pattern, html)


    # for i in lists:
    #     print(str(i).strip().replace(' ',''))
    print(lists)
    print("----")
    print(lists[0][2])
    print("----")
    print(re.sub("\n*\s*",'',lists[0][2]))
    # for name,score,text in lists[0]:
    #     print(text)
