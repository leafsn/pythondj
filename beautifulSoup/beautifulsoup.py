# coding: utf-8
# @Time    : 2019/5/10 11:50
# @Author  : xianj
# @Email   : starnc@126.com
# @File    : beautifulsoup.py
# @Software: PyCharm
from pytz import unicode

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc)
# 输出整个页面
print(soup.prettify())
# 标题标签内容
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id = 'link3'))

# 找到所有<a>标签的链接
for link in soup.find_all('a'):
    print(link.get('href'))

# 获取所有的文字内容
print(soup.get_text())

# soup = BeautifulSoup(open('index.html'))
soup = BeautifulSoup('<b class="boldest"> Extremely bold</b>')
tag = soup.b
print(tag, type(tag))

# 获取标签的名字
print(tag.name)

# 改变标签的name
tag.name = 'blockquote'
print(tag)

# 获取tag的属性
print(tag['class'])
# 获取所有属性, 返回一个字典
print(tag.attrs)

# tag 的属性操作跟字典一样，添加删除修改
# 修改class
tag['class'] = 'verybold'
# 添加id
tag['id'] = 1
print(tag)

del tag['class']
del tag['id']
print(tag)

# print(tag['class'])
print(tag.get('class'))

## 多值属性
css_soup = BeautifulSoup('<p class="body strikeout"></p>')
print(css_soup.p['class'])

css_soup1 = BeautifulSoup('<p class="body"> </p>')
print(css_soup1.p['class'])

## 看起来是多值属性，但不是多值属性的，返回字符串
id_soup3 = BeautifulSoup('<p id="my id"></p>')
print(id_soup3.p['id'])

rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
print(rel_soup.a['rel'])

# 将tag转换成字符串是，多值属性合并为一个值
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)

# xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
# print(xml_soup.p['class'])

print(tag.string)
print(type(tag.string))

# 转换为Unicode字符串
unicode_string = unicode(tag.string)
print(unicode_string)

## 替换tag中的字符串 replace_with
tag.string.replace_with('No longer bold')
print(tag)

print(soup.name)

# 注释
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup)
comment = soup.b.string
print(type(comment))

# 提取的注释文本
print(comment)

print(soup.b.prettify())

from bs4 import CData
cdata = CData('A CDATA block')
comment.replace_with(cdata)
print(soup.b.prettify())

soup = BeautifulSoup(html_doc)
## 遍历文档树 tag的name
print(soup.head)
print(soup.name)

print(soup.body.b)

# 通过点取属性的方式只能获得当前名字的第一个tag
print(soup.a)
print(soup.find_all('a'))

# 将tag的子节点以列表的方式输出   contents, 仅包含直接子节点
head_tag = soup.head
print(head_tag)

print(
    head_tag.contents
)

title_tag = head_tag.contents[0]
print(title_tag)
print(
    title_tag.contents
)

print(soup.contents[0].name)

text = title_tag.contents[0]
# print(text.contents)


for child in title_tag.children:
    print(child)

print(head_tag.contents)

print('-----------')
### descendants 可以对所有的tag的子孙节点进行递归循环
for child in head_tag.descendants:
    print(child)

print(len(list(soup.children)))
print(len(list(soup.descendants)))

print(soup)
print('---------------')
# string
print(title_tag.string)

# 单个子节点，可以使用.string打印出来，如果有多个子节点就无法确定就打印不出来
print(soup.html.string)

# 如果tag中包含多个字符串，可以使用.strings来循环获取
for string in soup.strings:
    print(repr(string))

# 使用.stripped_strings可以去除多余空白内容
for string in soup.stripped_strings:
    print(repr(string))


## 父节点 .praent
# 通过.parent属性来获取某个元素的父节点
title_tag = soup.title
print(title_tag)
print(title_tag.parent)

# 字符串也有父节点
print(title_tag.string.parent)

# 文档的顶层节点的父节点是BeautifulSoup对象
html_tag = soup.html
print(type(html_tag.parent))

# soup的父节点是None
print(soup.parent)

link = soup.a
print(link)
# 通过元素的.parents属性可以递归得到元素的所有父辈节点，
# 遍历了<a>标签到根节点的所有节点
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

# 兄弟节点
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>")
print(sibling_soup.prettify())

# .next_sibling 和 .previous_sibling查询兄弟节点
# 下一个兄弟节点
print(sibling_soup.b.next_sibling)
# 上一个兄弟节点
print(sibling_soup.c.previous_sibling)

# b标签没有上一个兄弟节点，返回None
print(sibling_soup.b.previous_sibling)
# c标签没有下一个兄弟节点，返回None
print(sibling_soup.c.next_sibling)

print(sibling_soup.b.string)

print(sibling_soup.b.string.next_sibling)
## 实际标签之间都是顿号或空格或换行符
for sibling in soup.a.next_siblings:
    print(repr(sibling))

for sibling in soup.find(id='link3').previous_siblings:
    print((repr(sibling)))

## .next_element 和 .previous_element 指向解析的上一个对象或下一个对象
soup = BeautifulSoup(html_doc)
last_a_tag = soup.find('a', id='link3')
print(last_a_tag)

print(soup)
print(last_a_tag.next_sibling)

print(last_a_tag.next_element)

# 解析对象的上一个
print(last_a_tag.previous_element)
print(last_a_tag.previous_element.next_element)

# .next_elements 和 .previous_elements的迭代器就可以向前或向后解析内容
for element in last_a_tag.next_elements:
    print(repr(element))

# 字符串
print(soup.find_all('b'))

# 正则表达事
import re
for tag in soup.find_all(re.compile('^b')):
    print(tag.name)

for tag in soup.find_all(re.compile('t')):
    print(tag.name)
# 列表
print(soup.find_all(['a', 'b']))

# True 可以匹配任何值，下面代码查找到所有的tag，但是不会返回字符串节点

for tag in soup.find_all(True):
    print(tag.name)
print('----------------')
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

print(soup.find_all(has_class_but_no_id))

print('-----------------')
from bs4 import NavigableString
def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))

for tag in soup.find_all(surrounded_by_strings):
    print(tag.name)

# find_all()
print(soup.find_all('title'))
print(soup.find_all('p', 'title'))

print(soup.find_all('a'))
print(soup.find_all(id='link2'))
# 正则
import re
print(soup.find(text=re.compile('sisters')))
print(soup.find_all(href=re.compile('elsie'), id='link1'))

# data-属性
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
data_soup.find_all(attrs={'data-foo': 'value'})

### 按css搜索  class_ 来搜索
print(soup.find_all('a', class_='sister'))

print(soup.find_all(class_= re.compile('itl')))

def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6

print(soup.find_all(class_ = has_six_characters))
print('------------------')
css_soup = BeautifulSoup('<p class="body strikeout"></p>')
print(css_soup.find_all("p", class_="strikeout"))

print(css_soup.find_all("p", class_="body"))
print(css_soup)
# 搜索class属性是可以通过css值完全匹配,完全匹配如果css类名的顺序与实际不符，将搜索不到结果
print(css_soup.find_all('p', class_='body strikeout'))
print(soup.find_all('a', attrs={'class': 'sister'}))

## text参数 可以搜索文档中的字符串内容，与name参数可选值一样，text参数接受字符串，正则，列表，True
print(soup.find_all(text='Elsie'))

print(soup.find_all(text=['Tillie', 'Elsie', 'Lacie']))
print(soup.find_all(text=re.compile('Dormouse')))

def is_the_only_string_within_a_tag(s):
    "Return True if this string is the only child of its parent tag."
    return (s == s.parent.string)

print(soup.find_all(text=is_the_only_string_within_a_tag))

print(soup.find_all('a', text='Elsie'))

# limit参数 限制返回的数量
soup.find_all('a', limit=2)

# recursive参数  recursive=True 只搜索tag的直系子节点
print(soup.html.find_all('title'))
print(soup.html.find_all('title', recursive=False))

## find_all 的简写，像调用find_all 一样调用tag对象
print(soup.find_all('a'))
print(soup('a'))

## find方法  只取一个,findall返回列表，find返回结果
print(soup.find_all('title', limit=1))
print(soup.find('title'))

# find方法的简写形式
print(soup.head.title)
print(soup.find('head').find('title'))

# find_parents() 和 find_parent() 搜索从父辈节点和子孙节点开始
a_string = soup.find(text='Lacie')
print(a_string)

print(a_string.find_parents('a'))
print(a_string.find_parents('p', class_='title'))

# find_next_siblings() 和find_next_sibling()兄弟节点搜索
first_link = soup.a
print(first_link)

# 查找后面符合条件的标签节点
print(first_link.find_next_siblings('a'))

# p标签的下一个p标签
first_story_paragraph = soup.find('p', 'story')
print(first_story_paragraph.find_next_sibling('p'))

# find_all_next() 和 find_next， 返回向前兄弟节点符合符合条件所有节点和返回第一个节点
print(first_link.find_all_next(text=True))
print(first_link.find_next('p'))

# find_all_previous() 和 find_previous() 向后符合条件的兄弟节点
print(first_link.find_all_previous('p'))
print(first_link.find_previous)

# css选择器 .select()方法中传入字符串参数，即可使用css选择器的语法找到tag
print(soup.select('title'))
# print(soup.select('p nth-of-type(3)'))
print('-------------------')

# 通过tag逐层查找
print(soup.select('body a'))
print(soup.select('html head title'))

# 查找某个tag标签下的直接子标签
print(soup.select('head > title'))
print(soup.select('p > a'))
print(soup.select('p > a:nth-of-type(2)'))
print(soup.select('p > #link1'))
print(soup.select('body > a'))

# 查找兄弟节点标签
print(soup.select('#link1~.sister'))
print(soup.select('#link1 + .sister'))

# 通过css的类名查找
print(soup.select('.sister'))
print(soup.select('[class~=sister]'))

# 通过id查找
print(soup.select('#link1'))
print(soup.select('a#link2'))

# 通过某个属性查找
print(soup.select('a[href]'))

# 通过属性的值来查找
print(soup.select('a[href="http://example.com/elsie"]'))











