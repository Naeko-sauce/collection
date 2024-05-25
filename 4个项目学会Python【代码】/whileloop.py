#练习1.打印10次 鸡你太美
# 循环 做重复劳动
count = 0
while count < 10:
    print('鸡你太美')
    count += 1



#练习2.计算1+2+3+4+....+99+100
sum = 0
number = 1
while number <= 100:
    sum += number
    number += 1
print(sum)


#练习3.打印1到100以内的所有奇数
#遍历
# 1 2 3 4 5 ....  100
number = 1
while number <= 100:
    if number % 2 == 1:
        print(number)
    number += 1