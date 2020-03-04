def greet(name,weather):  #定义多个函数参数
    print(f"Welcom {name}!")
    print(f"It's a {weather} day.")  #注意函数要先定义才可以调用
print("start")
greet('Akikagura','sunny')
greet('Akikagura',weather='sunny')
greet(weather='rainny',name='Akikagura')  #一般来说调用函数的时候，所传入的变量需要和定义的参数位置相对应
print("end")                              #但是也可以强制改变位置如例所示，同时为了加强易读性，最好写上参数名称
                                          #并且还需要注意，关键字参数总是在位置参数之后
def square(number):
    return number ** number  #函数返回值
print(square(9))