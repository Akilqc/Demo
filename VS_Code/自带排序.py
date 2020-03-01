numbers = [2,4,3,1,5,8,7,6,9,10]
numbers.sort(reverse=False)  #升序排列
print(numbers)
numbers.sort(reverse=True)  #降序排列
print(numbers)
numbers = [2,4,3,1,5,8,7,6,9,10]
numbers_sort = sorted(numbers,reverse=False)
print(numbers_sort)
print(numbers)

max_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
print(max_num)