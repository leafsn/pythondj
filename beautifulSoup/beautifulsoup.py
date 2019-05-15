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


# 通过语言设置来查找
multilingual_markup = """
 <p lang="en">Hello</p>
 <p lang="en-us">Howdy, y'all</p>
 <p lang="en-gb">Pip-pip, old fruit</p>
 <p lang="fr">Bonjour mes amis</p>
"""

# mutilinggual_soup = BeautifulSoup(multilingual_markup)
# mutilinggual_soup.select('p[lang|=en]')

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b

# 修改标签名
tag.name = "blockquote"
# 修改class
tag['class'] = 'verybold'
# 添加id
tag['id'] = 1
print(tag)

# 删除class,删除id
del tag['class']
del tag['id']
print(tag)

### 修改.string属性,用当前的内容替代原来的内容
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
tag = soup.a
tag.string = "new link text."
print(tag)

### tag.append方法想tag中添加内容
soup = BeautifulSoup("<a>Foo</a>")
soup.a.append('Bar')
print(soup)
print(soup.a.contents)

# 调用工厂方法BeautiSoup.new_string():
soup = BeautifulSoup("<b></b>")
tag = soup.b
tag.append("Hello")
new_string = soup.new_string(" there")
tag.append(new_string)
print(tag)
print(tag.contents)

# 创建一段注释,传入第二个参数
from bs4 import Comment
new_comment = soup.new_string("Nice to see you.", Comment)
tag.append(new_comment)
print(tag)

print(tag.contents)

# 创建一个tag最好的方法是调用工厂方法 BeautifulSoup.new_tag():
soup = BeautifulSoup("<b></b>")
original_tag = soup.b
# 创建一个新标签a,第一个参数tag名字必填
new_tag = soup.new_tag('a', href='http://www.example.com')
# 将新创建的tag添加到原始标签中
original_tag.append(new_tag)
print(original_tag)

# 添加内容
new_tag.string = 'Link text.'
print(original_tag)

## insert 把元素插入到指定位置
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
tag = soup.a

tag.insert(1, 'but did not endorse ')
print(tag)
print(tag.contents)

# 在当前tag或文本节点之前插入内容
soup = BeautifulSoup('<b>soup</b>')
tag = soup.new_tag('i')
tag.string = 'Dont'
# b的前面插入tag
soup.b.string.insert_before(tag)
print(soup.b)

# 在当前tag或文本节点之后插入内容
soup.b.i.insert_after(soup.new_string(" ever "))
print(soup.b)
print(soup.b.contents)

## 移除当前tag的内容
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
tag = soup.a

tag.clear()
print(tag)

print('---------------------------')
# extract() 将当前tag移除文档树,并作为方法返回
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
a_tag = soup.a

i_tag = soup.i.extract()
print(a_tag)
print(i_tag)
print(soup.find('i'))
print(i_tag.parent)


my_string = i_tag.string.extract()
print(my_string)
print(my_string.parent)
print(i_tag)

## decompose 将当前节点移除文档书并完全销毁
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
a_tag = soup.b
soup.i.decompose()
print(a_tag)


## replace_with 移除文档树某段内容.并用新的tag或文本节点替代它
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
a_tag = soup.a

new_tag = soup.new_tag('b')
new_tag.string = 'example.net'
a_tag.i.replace_with(new_tag)

print(a_tag)

# wrap() 方法可以对指定的tag元素进行包装,并返回包装后的结果
soup = BeautifulSoup("<p>I wish I was bold.</p>")
print(soup.p.string.wrap(soup.new_tag('b')))

print(soup.p.wrap(soup.new_tag('div')))

# 移除tag内所有的tag标签,该方法常被用来进行标记的解包
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
a_tag = soup.a

a_tag.i.unwrap()
a_tag

### 输出,
#格式化输出   prettify
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)

print(soup.prettify())

print(soup.a.prettify())

## 只想得到结果字符串,不重视格式,Unicode 或者 str()

print(str(soup))
print(unicode(soup.a))

# 输出格式  讲特殊字符转换成unicode;
soup = BeautifulSoup("&ldquo;Dammit!&rdquo; he said.")
print(unicode(soup))

print(str(soup))

# 如果只想得到tag中包含的文本内容,那么可以使用get_text()方法,
# 这个方法获取到tag中包含的所有文本内容作为Unicode字符串返回

markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)

print(soup.get_text)
print(soup.i.get_text())

# 可以通过参数指定tag的文本内容的分隔符:
print(soup.get_text('|'))

# 去除文本内容前后的空白
print(soup.get_text('|', strip=True))

# 使用.stripped_strings生成起,获得文本列表后手动处理列表
list = [text for text in soup.stripped_strings]
# print(list)

## 编码
markup = b"<h1>\xed\xe5\xec\xf9</h1>"
soup = BeautifulSoup(markup)
print(soup.h1)

print(soup.original_encoding)

# 指定编码方式
soup = BeautifulSoup(markup, from_encoding="iso-8859-8")
print(soup.h1)

### 通过beautifulsoup输出文档时,输出的UTF-8编码

markup = b'''
<html>
  <head>
    <meta content="text/html; charset=ISO-Latin-1" http-equiv="Content-type" />
  </head>
  <body>
    <p>Sacr\xe9 bleu!</p>
  </body>
</html>
'''

soup = BeautifulSoup(markup)
print(soup.prettify())

# 将编码方式传入prettify()方法中,输出原编码
print((soup.prettify('latin-1')))

# 还可以调用BeautifulSoup对象或任意节点的encode()方法
print(soup.p.encode('latin-1'))
print(soup.p.encode("utf-8"))

# 编码不支持会转换成特殊字符引用
markup = u"<b>\N{SNOWMAN}</b>"
snowman_soup = BeautifulSoup(markup)
tag = snowman_soup.b

print(tag.encode('utf-8'))
print(tag.encode('latin-1'))
print(tag.encode('ascii'))


### 编码自动检测
from bs4 import UnicodeDammit
dammit = UnicodeDammit("Sacr\xc3\xa9 bleu!")
print(dammit.unicode_markup)
print(dammit.original_encoding)


dammit = UnicodeDammit("Sacr\xe9 bleu!", ["latin-1", "iso-8859-1"])
print(dammit.unicode_markup)
print(dammit.original_encoding)

# 智能引号,使用Unicode时,会自能地把引号转换成HTML的特殊字符
markup = b"<p>I just \x93love\x94 Microsoft Word\x92s smart quotes</p>"

print(
    UnicodeDammit(markup, ['windows-1252'], smart_quotes_to='html').unicode_markup
)
print(
    UnicodeDammit(markup, ['windows-1252'], smart_quotes_to='xml').unicode_markup
)

# 把引号转换为ascii码:
print(
    UnicodeDammit(markup, ['windows-1252'], smart_quotes_to='ascii').unicode_markup
)

# 默认情况下,BeautifulSoup把引号转换为Unicode
print(
    UnicodeDammit(markup, ['windows-1252']).unicode_markup
)

# 矛盾的编码
snowmen = (u"\N{SNOWMAN}" * 3)
quote = (u"\N{LEFT DOUBLE QUOTATION MARK}I like snowmen!\N{RIGHT DOUBLE QUOTATION MARK}")
doc = snowmen.encode("utf8") + quote.encode("windows_1252")

print(doc)
print(doc.decode("windows-1252"))

# 使用UnicodeDammit.detwingle()方法把这段字符串转换为UTF-8编码,
# 允许我们同时显示文档中的snowmen和引号,
# 在创建BeautifulSoup或UnicodeDammit对象前,先对文档调用UnicodeDammit.detwingle确保文档编码正确
new_doc = UnicodeDammit.detwingle(doc)
print(new_doc.decode("utf-8"))


## 解析部分文档  SoupStrainer
from bs4 import SoupStrainer

only_a_tags = SoupStrainer('a')
print(only_a_tags)

only_tags_with_id_link2 = SoupStrainer(id ='link2')
print(only_tags_with_id_link2)

def is_short_string(string):
    return len(string) < 10
only_short_strings = SoupStrainer(text=is_short_string)



html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

print(
    BeautifulSoup(html_doc, 'html.parser', parse_only=only_a_tags).prettify()
)

print(
    BeautifulSoup(html_doc, 'html.parser', parse_only=only_tags_with_id_link2).prettify()
)

print(
    BeautifulSoup(html_doc, 'html.parser', parse_only=only_short_strings)
)


soup = BeautifulSoup(html_doc)
print(soup.find_all(only_short_strings))

# 代码诊断
from bs4.diagnose import diagnose
data = open("bad.html").read()
print(diagnose(data))


from urllib.request import urlopen

soup = BeautifulSoup(urlopen('https://blog.csdn.net/weixin_42184707/article/details/80361464'))
print(soup.prettify())

print(soup.find_all('pre'))



