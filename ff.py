def f():
    print("1")

f()

class car:
    def __call__(self,a,b):
        print("2")
        self.a=a
        self.b=b

        print(a,b)
c =car()
c(1,2)