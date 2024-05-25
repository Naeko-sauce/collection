#元组 即不能被修改的列表
data = (112,6,[1,2,3,4,5],34,63,2522)
index = 0
while index < len(data):
    print(id(data[index]))
    index += 1
hahaha = [1,2,3,4,5]
print(id(hahaha))
data[2] = hahaha
print(data)
index = 0
while index < len(data):
    print(id(data[index]))
    index += 1