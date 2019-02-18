from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="drrrajifiea"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup=BeautifulSoup(html,'lxml')
print(soup.prettify())

print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)

#获取名称
print(soup.title.name)

#获取属性
print(soup.p.attrs,soup.p.attrs['name'])

print(soup.p['name'])

#获取内容
print(soup.p.string)

#嵌套
print(soup.head.title.string)

#关联选择 子节点、子孙节点

print(soup.p.contents) #子节点
print(soup.p.descendants) #所有子孙节点
for child in soup.p.descendants:
    print(child)

print(soup.a.parent)#父节点
print('------------')
print(soup.a.parents)#祖先节点
for child in soup.p.parents:
    print(child)

#兄弟节点
print(soup.a.next_sibling)
print(soup.a.previous_sibling)
print(list(enumerate(soup.a.next_siblings)))
print(type(list(enumerate(soup.a.previous_siblings))[0][1]))

#soup.find() soup.select()
