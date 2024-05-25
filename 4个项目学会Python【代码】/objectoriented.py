#面向对象三大特性 封装 继承 多态
#封装：把共性（属性，函数）搞在一起变成个类
#继承：子类继承父类的属性，函数
#多态：同一个名字的函数，拥有不同的效果

#类的属性 vs 对象的属性
#类的属性属于类，并且所有该类的对象都共享这个属性
#对象的属性属于对象  self.xxxx


class Animal:
    burudongwu = True
    def __init__(self, name):
        self.__name = name
        print(self.__name, id(self.__name))

    def __eat(self):
        print('Animal的吃')

    def sound(self):
        pass

    # @classmethod
    def piss(self):
        print('尿尿')

Animal.piss()
# a1 = Animal('旺财')
# a2 = Animal('小白')
# print(id(a1.sound))
# print(id(a2.sound))
#
# class Dog(Animal):
#     def __init__(self):
#         super().__init__('旺财')
#
#     def sound(self):
#         print('汪汪汪')
#
# class Cat(Animal):
#     def __init__(self):
#         super().__init__('旺财')
#
#     def sound(self):
#         print('喵喵喵')
#
# class Bird(Animal):
#     def __init__(self):
#         super().__init__('旺财')
#
#     def sound(self):
#         print('叽叽叽')
#
#
# def makesound(animal):
#     animal.sound()
#
# dog = Dog()
# cat = Cat()
# bird = Bird()
# makesound(dog)
# makesound(cat)





