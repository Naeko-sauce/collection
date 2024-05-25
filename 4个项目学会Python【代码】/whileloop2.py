# 计算1!-2!+3!-4!+...+49!-50!
# 循环  4！=1*2*3*4  6！=1*2*3*4*5*6
#      判断当前数字是不是偶数
#         循环
#         - 数字的阶乘
#     否则
#         循环
#         + 数字的阶乘

# sum = 0
# number = 1
# while number <= 50:
#     result = 1
#     i = 1
#     while i <= number:
#         result *= i
#         i += 1
#     if number % 2 == 0:
#         sum -= result
#     else:
#         sum += result
#     number += 1
# print(sum)



#输出100以内的所有素数（素数就是只能被1和本身整除的正整数，例如3，5，7，11）
#循环从2看到100(遍历)
#    判断当前看到的数是不是素数（循环）
#       打印当前看到的数
# break 跳出当前循环
# continue 提前结束本次循环


number = 2
while number <= 100:
    i = 2
    is_prime = True
    while i < number:
        if number % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(number)
    number += 1














