from bs4 import BeautifulSoup
import requests

url = "https://python123.io/ws/demo.html"
r = requests.get(url)
print(r.status_code)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
# print(soup.prettify())
print(soup.b.parent.name)  # 获得标签名为b的父标签名字
tag = soup.a
print(tag.attrs)  # 获得tag的属性，固定返回字典
print(tag)  # 返回某一标签的文本
print(tag.string)  # 返回某一标签的字符串
tag2 = soup.p
print(tag2.attrs)
print(tag2.string)