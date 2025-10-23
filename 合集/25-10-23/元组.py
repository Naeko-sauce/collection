nu = [1,2,3]
print(nu[0])
nu[0] = 4
print(nu[0])
# 元组tuple是一种不可变的序列类型，类似于列表用于存储多个元素
# 元组和列表的主要区别在于元组的元素不能被修改，删除或者添加
# 元组通常用()来声明
q = (1,2,3)
# q[1] = 2
print(q[1])
# 如果在字符串后面加逗号字符串就会变成元组
name = "你",
print(name,type(name))
# 当元组中只有一个元素的时候要加逗号，如果是字符串或者证书类型的时候加上逗号就变成了元组类型
nam = ("你")
print(nam,type(nam))
# 元组按照位置解包
name_ag = ("drea",18)
mi,age = ("dream",18)
print(mi,age)