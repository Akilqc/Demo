numbers = [1,4,7,2,4]
numbers.append(100)  #向列表中添加元素
numbers.insert(0,1000)  #向固定位置添加元素
numbers.remove(1000)  #移除列表中的某个元素
numbers.pop()  #用于删除列表中的最后一项
index_number = numbers.index(7)  #返回所搜寻值的位置代码   建议使用 exist = 7 in numbers 这样若是不存在则返回false而不会报错
number = numbers.count(1)  #返回列表中某元素的个数
numbers2 = numbers.copy()  #进行复制
numbers.clear()  #用于清除列表中的所有的元素

numbers = [2,2,4,4,5,6,7,8,8,9]
new_numbers = []
for number in numbers:
    if number not in new_numbers:     #非常好的一种思维
        new_numbers.append(number)
print(new_numbers)