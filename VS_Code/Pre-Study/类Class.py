class Person:
    def __init__ (self, name):
        self.__name = name            #构造函数，其中self可以类比C++的this        在内部属性前加上两个下划线，则无法从外部进行访问，成为了私有变量

    def get_name(self):
        print(f'Your name is {self.__name}')

    def set_name(self, new_name):
        self.__name = new_name
        print(f'Name is changed to {self.__name}')


para = Person('Akikagura')
para.get_name()
para.set_name('Akikagura.lqc')