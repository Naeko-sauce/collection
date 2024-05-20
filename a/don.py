# python方法的动态性
class Person:
    def work(self):
        print('Work')
    def sleep(self):
        print('Sleep')

def tru(s):
    print('Tru')
Person.work = tru
p = Person()
p.work()