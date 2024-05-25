# 定义函数
# def 函数名(参数1, 参数2, ..., 参数n):
#     业务代码
# def add(number1:int, number2:int=3)->int:
#     return number1+number2
#
# # 调用（使用）函数
# # 函数名(参数1, 参数2, ..., 参数n)
# result= add('6')
# print(result)







# 定义一个函数，该函数能够判断一个数是不是水仙花数
# 如果是水仙花数则返回True，否则返回False
# 153=1*1*1+5*5*5+3*3*3

def is_iris(number:int)->bool:
    if number > 999 or number < 100:
        return False
    gewei = number%10
    shiwei = number//10%10
    baiwei = number//10//10%10
    if gewei**3 + shiwei**3 + baiwei**3 == number:
        return True
    return False

print(is_iris(153))

