class mySingleton:
    __obg = None
    __in = True
    def __new__(cls, *args, **kwargs):
        if cls.__obg == None:
            cls.__obg = object.__new__(cls)
            return cls.__obg
    def __init__(self,nm):
        if mySingleton.__in:
            print("a")
            self.nm=nm
            mySingleton.__in = False

a = mySingleton("a")
print(a)
b = mySingleton("b")
print(b)