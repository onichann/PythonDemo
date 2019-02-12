import requests
import re
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
# }
#
# try:
#     r = requests.get("https://www.zhihu.com/explore",headers=headers)
# except requests.RequestException as e:
#     print(e)
# print(r.status_code)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)
# print ([ str(title).replace('\n','')  for title in titles])
#

content ='Hello 123 4567 World_This is a Regex Demo'
print(content)
result=re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
print(result)
print(result.group())
print(result.span())
print(len(result.group()))

result=re.match('^Hello\s(\w+\s\d+)\sWorld',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())

result=re.match('^Hello.+World',content)
print(result)

print("----------")
print("贪婪模式和非贪婪")
result=re.match('^He.*(\d+\s\d+).*Demo$',content)
result=re.match('^He.*?(\d+\s\d+).*Demo$',content)
print(result)
print(result.group(1))


print("-----------")
content='http://weibo.com/comment/kEraCN'
result1=re.match('http.*comment/(.*?)',content)
result2=re.match('http.*comment/(.*)',content)
print('result1',result1.group(1))
print('result2',result2.group(1))


print("------------")
print("---.*匹配换行")
content ='''Hello 123 4567 World_This
          is a Regex Demo'''

result=re.match('^He.*(\d+\s\d+).*Demo$',content,re.S)
result=re.match('^He.*?(\d+\s\d+).*Demo$',content,re.S)
print(result)
print(result.group(1))

print("------------ 转义")
content='(百度)www.baidu.com'
result=re.match('\(百度\)www\.baidu\.com',content)
print(result)

print("----------")
content="f8efa78ga7dg7a8g7"
print(re.sub("\d+",'',content))


