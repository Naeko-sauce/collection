# 马上双11了，假设某宝有活动，满400减50，如果有无门槛券则先使用无门槛券再执行满减政策。
# 现在你有购物车有10000块钱的商品，你有200.3块钱的无门槛券。打印出你双11要花多少钱能
# 清空购物车。

# 优惠后到底要花多少钱 = 10000 - (200.3 + (10000-200.3)//400*50)
# 优惠 = 无门槛+满减 = 200.3+ 满减
# 满减 = (10000-200.3)//400*50
print(10000 - (200.3 + (10000-200.3)//400*50))

# 解：设 yuanshijiage = 10000 wmk=200.3 man=400 jian=50
#       result = yuanshijiage - (wmk+(yuanshijiage-wmk)//man*jian)
# 赋值
yuanshijiage = 10000
wmk = 200.3
man=400
jian=50
result = yuanshijiage - (wmk+(yuanshijiage-wmk)//man*jian)
print(result)
result = '你干嘛'
print(result)



#变量名的最低规范
# 1.变量名中只能出现字母 数字 下划线
# 2.变量名的第一个字符不能是数字
_1vw50kfc = 50

#变量名常用的两种规范
#1.驼峰命名规范：变量名由一堆单词组成，第一个单词的首字母小写，其余单词的首字母大写
myWifeName = 'Shady'

#2.类ruby命名规范：变量名由一堆单词组成，单词之间用下划线连接，单词首字母小写
my_wife_name = 'Shady'

myWifeName = 'Shady'
myWifeName = 'Shady'
myWifeName = 'Shady'
my_wife_name = 'Shady'
my_wife_name = 'Shady'
my_wife_name = 'Shady'
myWifeName = 'Shady'













