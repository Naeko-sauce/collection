# 设置访问修改权限
class W:
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):
        print(self.__name)
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
e = W(199)
print(e.name)
e.name = 2999
print(e.name)
