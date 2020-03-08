class Animal:
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run_dog(self):
        print('Dog is running')

class Cat(Animal):
    def run(self):
        print('Cat is running')   #子类中的同名函数会覆盖掉父类

class Monkey(Animal):
    def run(self):
        print('Monkey is running')


def is_animal(animal):   #多态化，传入的只要是animal类就可以使用函数，并且与之相匹配
    animal.run()


class_animal = Animal()
dog = Dog()
cat = Cat()
monkey = Monkey()
dog.run()
dog.run_dog()
cat.run()
print('----------------')
is_animal(dog)
is_animal(cat)
is_animal(monkey)