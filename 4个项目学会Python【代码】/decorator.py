#装饰器的本质是一个函数，把被装饰的函数当成参数
import time

def timer(func):
    def inner(*args, **kwargs):
        for d in args:
            print(d)
        start = time.time()
        func(*args, **kwargs)
        print(time.time()-start)
    return inner

@timer
def Test(a, b, c):
    for i in range(100000):
        print(123)

Test(1,2, 3)