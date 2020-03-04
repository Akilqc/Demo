def spam(number):
    try:
        return 44 / number
    except ZeroDivisionError:
        print("It's a valid number")

print(spam(2))
print(spam(0))  #注意这里print的是None
print(spam(22))
#try函数和except函数，如果在try字句中的代码导致了一个错误，就立即跳入except进行执行
#同时需要注意，如果try子语句中有多个语句，一旦其中一个导致了错误，就会立马转入except，不执行后面的剩余语句


def spam2(number):
    return 44 / number

try:
    print(spam2(2))
    print(spam2(0))  #这一句没有被执行
    print(spam2(22))  #这一句也没有被执行
except ZeroDivisionError:
    print("Ti's a balid number")