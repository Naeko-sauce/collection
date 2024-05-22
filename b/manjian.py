def is_iris(number:int) ->bool:
# 计算水仙花数，首先判断这个数字是不是三位数
    if number >999 or number < 100 :
        return False
    # 把他的个位十位百位抽出来乘以3等于他本身就是
    # 思路一把数字变成字符串然后抽出来在转成数字
    number = str(number)
    ge = int(number[2])
    shi = int(number[1])
    bai = int(number[0])
    if ge**3 + shi**3 + bai**3 == int(number):
        return True
    return False
print(is_iris(153))