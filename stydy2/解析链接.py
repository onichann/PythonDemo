from urllib import parse,robotparser,request
import datetime

url='http://127.0.0.1:8080/user/1?name=a&year=2'
result=parse.urlparse(url)
print(result)

# parse.urlunparse()
# parse.urlsplit()
# parse.urlunsplit()
# parse.urljoin()
# parse.urlencode()
print(parse.urljoin("http://127.0.0.1:8080/user",'?name=xiaowang'))
# parse.parse_qs()


#name=%E6%88%91
print(parse.urlencode({'name':'我'}))
#name%3D%E6%88%91
print(parse.quote('name=我'))

'''
    robots.txt 
    协议
'''

rfp=robotparser.RobotFileParser()
rfp.set_url("http://www.baidu.com/robots.txt")
rfp.read()
print(datetime.datetime.fromtimestamp(rfp.mtime()))
print(rfp.can_fetch('*','http://www.baidu.com/baidu/w'))

# rfp.parse(request.urlopen("http://www.baidu.com/robots.txt").read().decode("utf-8").split("\r\n"))
# print(rfp.can_fetch('EasouSpider','http://www.baidu.com/baidu1/w'))
