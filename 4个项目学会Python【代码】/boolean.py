#真 对(True) 假 错(False)
shadyYYDS = False
print(shadyYYDS)
#大于(>) 小于(<) 等于(==) 大于等于(>=) 小于等于(<=) 不等于(!=)

print(233!=222)




#并且(and) 或者(or) 非(not)
# 本质
# x and y  ===> 如果x是False那么表达式的结果是x，否则是y
# x or y  ===> 如果x是False那么表达式的结果是y，否则是x
# not x ===> 如果x是False那么表达式的结果是True，否则是False

# 表示0 表示空 表示没有
print(not 3)


# 更好理解的版本（前提：两边都是bool值）
# and：只有两边都是True时，表达式的结果才是True，否则是False
# or： 只有两边都是False时，表达式的结果才是False，否则是True
# not：结果取反
print(not True)

#优先级:not > and > or
#                                   True
print(not True and True or False and False or True)
#                           False
print((not True and True or False) and (False or True))

