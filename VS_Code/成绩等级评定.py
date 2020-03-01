import time
temp = input('成绩等级评定系统\n1、开始录入\n2、退出程序\n')
sel = int(temp)
while 1:
    if sel == 2:
        break
    else:
        time.sleep(1)
        temp = input('请输入成绩：')
        mark = int(temp)
        if mark > 100:
            print('请输入正确成绩！')
            continue
        elif mark >= 90:
            print('成绩评定为A！\n')
        elif mark >= 80:
            print('成绩评定为B！\n')
        elif mark >= 60:
            print('成绩评定为C！\n')
        else:
            print('成绩评定为D！\n')
    time.sleep(1)
    temp = input('1、继续录入\n2、退出程序\n')
    sel = int(temp)
print('程序结束！')