from urllib.request import urlopen
from bs4 import BeautifulSoup

# 抓取网页中的a标签,切以href靠头的所有url链接
html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html)
allLinks = bsObj.find_all('a')
print(len(allLinks))

for link in allLinks:
    if 'href' in link.attrs:
        print(link.attrs['href'])
