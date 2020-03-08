temp = '搜狗输入法'
print(len(temp))
print('狗的下标:', temp.find('狗'))  #这里返回的是所搜寻字符在字符串中的位置
print('用够替换狗：', temp.replace('狗', '够'))  #这里的replace不会改变原有的字符串
print('原来的字符串不变:', temp)
print('狗' in temp)   #注意in与find的区别in返回的是布尔型find返回的是寻找字符的位置
temp_new = 'Aki Is Me'
print(temp_new.upper())  #注意这里也是不会改变原有的变量
print(temp_new)
print(temp_new.lower())  #与upper一样 不改变原有变量
print(temp_new)
print('----------------------')
List = ['Aki', 'kagura', 'lqc']
print(' ❤  '.join(List), '\n----------------------')  #将列表中的不同字符串连接在一起，并且可以使它们之间插入固定的符号

import pyperclip
pyperclip.copy('Akikagura')