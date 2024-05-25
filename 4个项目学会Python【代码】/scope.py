#作用域 范围 前缀
#全局作用域 不管在这个代码文件的哪个地方都有机会访问到
#局部作用域 在代码块里面的变量
#访问一个变量 局部作用域->全局作用域
a = 11  #全局.a
b = 21  #全局.b
def testfunc():
    global a
    a = 10    #全局.a=10
    b = 20    #局部.b
    return a, b #局部.a #局部.b
c, d = testfunc()
print(a, b, c, d) #全局.a #全局.b