# //推导式生成元组
b = (x *10 for x in range(5));
c = tuple(b) #用tuple转化为元组才能正常输出
print(c)
e = (x *20 for x in range(3));
print(e.__next__())#调用一次就打印一个如果超出就报错
print(e.__next__())
