numbers = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four'
}
# phone = input('Input number: ')
# output = ''
# for ch in phone:
#     output = output + numbers.get(ch, '!') + ' '
# print(output)
print('Keys in dictionary: ')
for temp in numbers.keys():
    print(temp, end =' ')
print('\nValues in dictionary: ')
for temp in numbers.values():
    print(temp, end = ' ')
print('\nKey to value in dictionary: ')
for temp in numbers.items():
    print(temp, end = ' ')
#三个可以查看字典中元素的函数：keys value items 只限于查看不可修改

spam = list(numbers.items())  #可以将keys value items返回的值变为列表 使用list函数
print('\n')
print(spam, '\n')
numbers.setdefault('5', 'Five')  #setdefault函数 若在字典中已经有key 则返回已有key的值 若没有则添加
print(numbers)