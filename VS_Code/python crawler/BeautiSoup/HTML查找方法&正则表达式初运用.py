from bs4 import BeautifulSoup
import requests
import re  # 正则表达式库

url = 'https://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
# 查找到该url中所有的标签名称并且打印出来
print('按照标签名字来检索：')
for tag in soup.find_all(True):
    print(tag.name)
print('----------')
# 查找该url中所有以b为开头的标签
for tag in soup.find_all(re.compile('b')):
    print(tag.name)
print('----------')
# find_all函数中第二个参数为搜索标签属性值
print(soup.find_all('p', 'course'))
print('----------')

# 同时需要注意，检索标签属性值的时候，必须要与所检索的值完全对应才行，但是可以通过使用正则表达式库来检索部分内容
print('按照标签属性值来检索：')
print(soup.find_all(id = 'link1'))  # 精准搜索出标签含有id = link1属性的那一个
print('----------')
print(soup.find_all(id = 'link'))  # 由于标签中没有属性为id = link的，因此返回一个空列表
print('----------')
print(soup.find_all(id = re.compile("link")))  # 由于使用了正则表达式，因此返回的是含有"link"字段的属性的标签
print('----------')

# find_all方法还可以按照标签中文本的字符串来搜寻
print('按照标签文本中的字符串来检索：')
print(soup.find_all(string = 'Basic Python'))
print('----------')
print(soup.find_all(string = 'Basic'))  # 同样的道理，只可以检索出完全一样的字符串，可以通过加字符串来改进
print('----------')
print(soup.find_all(string = re.compile('python')))  # 加了正则表达式后，可以检索出含有部分字段的文本
