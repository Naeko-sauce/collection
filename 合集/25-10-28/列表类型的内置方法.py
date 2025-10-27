# 1.强制类型转换
# 可以将可迭代类型转换为列表类型
print(list("derma"))
# 列表在强制转换字典的时候默认转换出来的是字典的键
print(list({"n","a","b","c"}))
# 切片
# 列表[起始步长:终止索引:步长]
num = [1,2,3,4,5,6,7,8,9]
print(num[0:3])
# 向列表元素中添加元素追加在结尾
num.append(20)
print(num)
# 插入到指定的索引
num.insert(0,999)
print(num)
# 把两个列表合并
li = [23,44,55,66,77,88]
num.extend(li)
print(num)
# 弹出元素
print(num.pop())
print(num)
print(num.pop(1))
print(num)
# 方式3
del num[0]
print(num)
# 方式4清空列表
num.clear()
print(num)
# 颠倒元素,影响的是原本的列表
num = list(range(1,11))
print(num)
num.reverse()
print(num)
# 自动排序默认是正序
q = [2,4,5,3,1]
print(q.sort())
print(q)