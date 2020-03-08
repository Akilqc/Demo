import os
import pprint
from pathlib import Path
import time
path_root = Path(r'C:\Users\Lenovo\Desktop')
path2 = path_root / 'Pixiv'
print('path_root: ', path_root)
print('path2: ', path2, '\n------------------------------')


# #生成以及删除文件夹
# path3 = Path('文件操作')
# print('path3的路径：', path3)
# path3.mkdir()  #创建文件夹 注意是文件夹
# time.sleep(5)
# path3.rmdir()  #删除文件夹


#遍历某一指定path下的文件
path4 = Path()
print('path4的当前工作目录：', path4)
for file in path4.glob('*'):        #这里的glob函数生成了一个迭代器，用于迭代指定path中的任意文件，*代表任意文件以及文件夹，可以更改文件扩展名来指定某一类定的文件
    pprint.pprint(file)
print('\n\n------------------------------')
path = Path.cwd()
print('path的当前工作目录：', path)
for file in path.glob('*.py'):
    pprint.pprint(file)


#使用os来提取绝对路径和相对路径，分离目录与基本名称
print('\n\n------------------------------\n', os.path.abspath(path2))
print(os.path.relpath(path2,path_root))                  #从后一个参数到前一个参数的相对路径
print(os.path.split(path2))             #用于分离目录名称以及基本名称


#读写文件
f = open('test.txt', 'a')         #'a'代表添加，不会覆盖原有文字   'w'代表覆写，会删除原有的文字重新进行编写
f.write('\nyou never see me again')
f.close()
f = open('test.txt')

print(f.read())