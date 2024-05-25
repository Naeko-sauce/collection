# 找出列表中的最小值
data = [25, 7, 21, 8, 4, 2, 0, -23, -624, 26, 203,26,26,24,62,636,2,624,62,1]
minvalue = data[0]
index = 1
while index < len(data):
    if data[index] < minvalue:
        minvalue = data[index]
    index += 1
print(minvalue)
