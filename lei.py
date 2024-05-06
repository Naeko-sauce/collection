class Student:
    com = "stx"
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    @classmethod
    def printcompany(cls,a,c):
        print(cls.com)
        print(a,c)
    def git(self):
        print(self.com)

Student.printcompany(1,2)
s = Student()
s.git()
