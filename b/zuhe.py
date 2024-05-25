class p:
    def show(self):
        print("aaaa")

class q:
    def __init__(self,p):
        self.p = p

c = p()
c.show()
