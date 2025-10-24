# 1强制类型转换
# 可以将符合整数类型的字符转换为证书
sr = '33'
print(sr,type(sr))
a=  int(sr)
print(type(a))
# 进制转换
# 二进制
print(bin(999))
# 八进制
print(hex(999))
# 十六进制
print(oct(999))
# 判断当前数据类型
n1 = b"4"
print(n1,type(n1))
# 判断当前数字是否是数字类型
print(n1.isdigit())
# 在python中没有判断当前字符串是否是浮点数的方法
age = input('age')
print(age) if age.isdigit() else print("输入数字")