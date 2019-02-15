from pyquery import PyQuery as pq
import html


#字符串初始化
text='''
<div id="container">
<ul class="list">
<li class="item-0"><a href="link1.html">first item</a></li> 
<li class="item-1"><a href="link2.html">second item</a></li> 
<li class="item-inactive"><a href="link3.html">third item</a></li> 
<li class="item-1"><a href="link4.html">fourth item</a></li> 
<li class="item-0"><a href="link5.html">fifth item</a> 
</ul>
</div>
'''
doc=pq(text)
print(doc)
print(doc('li'))

#url初始化
doc=pq(url='https://cuiqingcai.com')
print(doc('title'))
print(html.unescape(doc('title')))

#文件初始化
# doc=pq(filename='demo.html')


text='''
<div id="container">
<ul class="list">
<li class="item-0"><a href="link1.html">first item</a></li> 
<li class="item-1 active"><a href="link2.html">second item</a></li> 
<li class="item-inactive"><a href="link3.html">third item</a></li> 
<li class="item-1"><a href="link4.html">fourth item</a></li> 
<li class="item-0"><a href="link5.html">fifth item</a> 
</ul>
</div>
'''
doc=pq(text)
print(doc('#container .list li'))
print(type(doc('#container .list li')))

li=doc('.list .item-1.active')
print(li.siblings())

#遍历
print([ (i,i.html(),i.attr("class"),i.text()) for i in li.siblings().items()])

