numbers = [1,4,7,2,4]
numbers.append(100)  #向列表中添加元素 默认在末尾
numbers.insert(0,1000)  #向固定位置添加元素
numbers.remove(1000)  #移除列表中的某个元素，一次只可以删除一个值
numbers.pop()  #用于删除列表中的最后一项
index_number = numbers.index(7)  #返回所搜寻值的下标   建议使用 exist = 7 in numbers 这样若是不存在则返回false而不会报错
number = numbers.count(1)  #返回列表中某元素的个数
numbers2 = numbers.copy()  #进行复制，返回列表，这里复制的不是引用，因此如果改变复制后的列表，以前的旧列表不会被改变
numbers.clear()  #用于清除列表中的所有的元素

numbers = [2,2,4,4,5,6,7,8,8,9]
new_numbers = []
for number in numbers:
    if number not in new_numbers:     #非常好的一种思维
        new_numbers.append(number)
print(new_numbers)

spam = [[1,2,3], [4,5,6], [7,8.9]]
print(spam[1][2])  #列表中可以添加列表，类似于二位数组？
print(spam[-1][-2])  #注意列表可以使用负数的下标，这点与其他语言不同

spam[0:2]  #列表的切片，从第一个整数的值开始到第二个整数，但不会包含第二个整数所代表的量，其结果是一个新列表
spam2 = spam = spam[0:2]   #列表的连接使用的是加号

numbers_new = numbers  #此处复制给numbers_new的是列表的引用，而不是列表值本身