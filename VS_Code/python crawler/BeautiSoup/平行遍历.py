import requests
from bs4 import BeautifulSoup

url = 'https://python123.io/ws/demo.html'

r = requests.get(url)

demo = r.text
soup = BeautifulSoup(demo, 'html.parser')

for sibling in soup.a.next_sibling:
    print(sibling)

for sibling in soup.a.previous_sibling:
    print(sibling)