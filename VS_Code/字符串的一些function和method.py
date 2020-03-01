temp = '搜狗输入法'
print(len(temp))
print(temp.find('狗'))  #这里返回的是所搜寻字符在字符串中的位置
print(temp.replace('狗', '够'))  #这里的replace不会改变原有的字符串
print(temp)
print('狗' in temp)   #注意in与find的区别in返回的是布尔型find返回的是寻找字符的位置
temp_new = 'Aki Is Me'
print(temp_new.upper())  #注意这里也是不会改变原有的变量
print(temp_new)
print(temp_new.lower())  #与upper一样 不改变原有变量
print(temp_new)