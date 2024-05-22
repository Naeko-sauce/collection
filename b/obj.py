class s:
    def __init__(self):
        print(12312)

    def show(self):
        print(1231)

class b(s):
    def show(self):
        super(s,self).__init__()#调用父类方法
        print(a)
    # def show2(self):

a = s()
c = s()
# a.show()
# c.show()