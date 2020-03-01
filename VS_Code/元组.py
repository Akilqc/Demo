numbers = (1,2,3)  #元组不可以进行修改

# x = numbers[0]
# y = numbers[1]
# z = numbers[2]

x,y,z = numbers  #unpack 这一行代码所做的事等于上面三行 列表也可以使用

numbers2 = (4,5,6)
numbers3 = numbers + numbers2  #元组可以直接进行拼接
print(numbers3)
del numbers3  #删除某个元组