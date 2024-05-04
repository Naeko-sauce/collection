class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(self.name, self.age)


s = Student('John', 18)
print(s.name, s.age)
s1=Student('John1', 181)
print(s1.name, s1.age)