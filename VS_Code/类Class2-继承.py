class Animal:
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run_dog(self):
        print('Dog is running')

class Cat(Animal):
    def run(self):
        print('Cat is running')

class Monkey(Animal):
    def run(self):
        print('Monkey is running')


def is_animal(animal):
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
