import requests
import bs4
from bs4 import BeautifulSoup
import pprint

url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html"
r = requests.get(url)
r.encoding = 'uth-8'
html = r.text
soup = BeautifulSoup(html, "html.parser")
list = []
for tr in soup.find('thead').children:
    if isinstance(tr, bs4.element.Tag):
        temp = tr.find_all('th')
child = temp[4].children
# 获取前四个表头字符串
for i in range(0, (len(temp) - 1)):
    list.append(temp[i].string)

# 获取第五个折叠的字符串
for i in child:
    if isinstance(i, bs4.element.Tag):
        temp_list = i.find_all('option')
for i in range(0, len(temp_list)):
    list.append(temp_list[i].string)

print(list)