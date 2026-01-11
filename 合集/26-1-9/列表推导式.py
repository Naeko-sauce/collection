num_list =[ i for i in range(10)]
print(num_list)

def fun(s):
    print("调用函数",s)

fun("kl")
# python的多个参数传递
def fun2(a,*args):
    print("第一个参数",a)
    print("其他参数",args)
fun2(1,2,3,4,5)