import requests
from bs4 import BeautifulSoup

url = 'https://python123.io/ws/demo.html'

r = requests.get(url)

demo = r.text
soup = BeautifulSoup(demo, 'html.parser')

for parent in soup.a.parents:  # 遍历a标签之前的所有标签，包括soup本身，但是soup不存在name信息
    if parent is None:
        print(parent)
    else:
        print(parent.name)