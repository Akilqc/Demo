import re

strr = r'[0-9]\d{5}'
match1 = re.search(strr, 'sss 100089 jjj 100087')  # search方法是对于全部的搜索对象进行搜索
match2 = re.match(strr, 'sss 100089 jjj 100087')  # match方法与search方法最大的不同：match方法从头开始搜索，若第一个没有搜索到，则返回空
print('-------------------------------')
print('search方法返回的类型：', type(match1))
print('match方法返回的类型(匹配失败)：', type(match2))
if match1:
    print(match1.group())
if match2:
    print(match2.group())
else:
    print("匹配失败")
# 但是需要注意的是，search和match方法都只会返回最先匹配到的字符串
print('-------------------------------')
match3 = re.split(strr, "sss 100089 jjj 1000875")
match4 = re.split(strr, "sss 100089 jjj 1000875 kkk 100088", maxsplit = 2)  # maxsplit参数，用于控制分割的个数
print('spilt方法返回的类型：', type(match3))
if match3:
    print(match3)
if match4:
    print(match4)
print('-------------------------------')
match5 = re.findall(strr, "sss 100089 jjj 100087")
print("findall方法返回的类型：", type(match5))
print(match5)
# findall方法与search最大的不同在于，findall方法会返回所有匹配到的值，而不是只返回第一个
print('-------------------------------')
match6 = re.finditer(strr, "sss 100089 jjj 1000875")
print("finditer返回的类型是：", type(match6))
for i in match6:
    print(i.group())
# 注意这里finditer返回的类型是迭代器，使用for循环来遍历迭代器中的元素
print('-------------------------------')
match7 = re.sub(strr, "--zipcode", "sss 100089 jjj 100087")
print("sub方法返回的类型：", type(match7))
print(match7)
print('-------------------------------')
regx = re.compile(strr)
print('compile方法形成的对象的类型：', type(regx))

'''
这里需要注意的是，re库的六种方法可以通过Pattern类型的对象进行调用，
此时其后的正则表达式参数类型变为Pattern，若使用re库进行调用，则类型为AnyStr
'''
print('-------------------------------')
print("match对象中所记录的带匹配字符串：", match1.string)
print("match对象中的匹配时使用的正则表达式：", match1.re)