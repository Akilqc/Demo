for item in range(1,11,2):  #注意range函数的用法，前两个数字代表界限（注意不包含最后一个数字），最后一个数字代表step，即步长
    print(item)             #for循环可以遍历任何序列的项目，如一个列表或者一个字符串

for item in ['Aki','kagura','lqc']:
    print(item)

print('\n\n')
for x in range(3):
    for y in range(4):
        print(f'({x},{y})')  #循环嵌套
print('\n\n')

numbers = [5,2,5,2,2]
for first_loop in range(1):
    for second_loop in numbers:
        print('X' * second_loop)