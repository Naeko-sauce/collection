n = {1,2,3,4,5,6,7,8,9}
# 添加一个元素
n.add(51)
print(n)
# 添加多个元素
n.update([22,33,44,55,66,77,88])
print(n)
# 删除使用remove
# 删除指定的元素2,使用discard删除的时候如果没有这个元素不会报错
n.discard(22)
print(n)
# 集合弹出元素使用pop不过弹出的是第一个元素
n.pop()
print(n)