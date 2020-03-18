import requests
from bs4 import BeautifulSoup

url = 'https://python123.io/ws/demo.html'

r = requests.get(url)

demo = r.text
soup = BeautifulSoup(demo, 'html.parser')

"""
for child in soup.body.children: # 遍历儿子节点
    print(child)
"""

for child in soup.body.descendants: # 遍历所有的子孙节点
    print(child.name)

# for child in soup.body.descendants: # 遍历所有的子孙节点
#     print(child)