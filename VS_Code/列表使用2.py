# spam = ['Aki', 'Kagura','Lqc']
# for index in range(len(spam)):  #常常使用len函数在循环中控制循环次数，或者用于标明下标，range(len())这样的写法将会遍历某列表的所有下标
#     print(f'Index {index} in spam is: {spam[index]}')
import copy
spam = [[1,2], [3,4], [5,6]]
spam2 = copy.deepcopy(spam)  #copy和deepcopy的区别需要注意 见收藏夹
print(spam)
print(spam2)