a = [x for x in range(1,20) if x % 2 ==0]
print(a)
s =  input("输入")
s = int(s)
a = [a for a in range(s)]
print(a)
cells = [(row,col) for row,col in zip(range(1,4),range(s))]
print(cells)
# 字典推导式
v = ["a","b","c"]
z = {v:id for v,id in zip(range(1,4),v)}
print(z)