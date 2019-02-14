from lxml import etree

text='''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a><li>
<li class="item-1"><a href="link2.html">second item</a><li>
<li class="item-inactive"><a href="link3.html">third item</a><li>
<li class="item-1"><a href="link4.html">fourth item</a><li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''

html=etree.HTML(text,parser=etree.HTMLParser())
result=etree.tostring(html)
print(result.decode('utf-8'))

#直接读取html文件
# html=etree.parse('./test.html',etree.HTMLParser())
# result=etree.tostring(html)
# print(result.decode('utf-8'))

print(html.xpath('//*'))

print(html.xpath('//li'))

print(html.xpath('//li/a'))

print(html.xpath('//ul//a'))

print(html.xpath('//ul/a'))

print(html.xpath('//a[@href="link4.html"]/../@class'))

print(html.xpath('//a[@href="link4.html"]//..'))

for item in html.xpath('//a[@href="link4.html"]//..'):

    print(etree.tostring(item).decode('utf-8'))

print("-----------")

for item in html.xpath('//a[@href="link4.html"]/../@class'):
    print(item)
    # print(etree.tostring(item).decode('utf-8'))

print("-----------")

for item in html.xpath('//a[@href="link4.html"]/parent::*/@class'):
    print(item)

print(html.xpath('//li[@class="item-0"]/a/text()'))

print(html.xpath('//li/a/@href'))

print("-------------------------")

#匹配多个属性

text='''
<li class="li li-first" name="item" ><a href="link.html">first item</a></li>
'''
html=etree.HTML(text)
print(html.xpath('//li[@class="li"]/a/text()'))
print(html.xpath('//li[contains(@class,"li")]/a/text()'))
print(html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()'))

#按顺序选择
text='''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a><li>
<li class="item-1"><a href="link2.html">second item</a><li>
<li class="item-inactive"><a href="link3.html">third item</a><li>
<li class="item-1"><a href="link4.html">fourth item</a><li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''

html=etree.HTML(text)
print('------------')
print(html.xpath("//li/a/text()"))
print(html.xpath("//li[1]/a/text()"))
print(html.xpath("//li[last()]/a/text()"))

print(html.xpath("//li[position()<5]/a/text()"))

print(html.xpath("//li[position()=2]"))
print(etree.tostring(html.xpath("//li[position()=2]")[0]))

#节点轴选择
#p108
print('-----------')
html.xpath('//li[1]/ancestor::*')#所有祖先节点
html.xpath('//li[1]/ancestor::div')#
html.xpath('//li[1]/attribute::*')#所有属性
html.xpath('//li[1]/child::a[@href="link1.html"]')#直接子节点
html.xpath('//li[1]/descendant::span')#所有子孙节点
print(etree.tostring(html.xpath('//li[1]/following::*[2]')))   #当前节点之后的所有节点
html.xpath('//li[1]/following-sibling::*')#当前节点之后所有同级节点
