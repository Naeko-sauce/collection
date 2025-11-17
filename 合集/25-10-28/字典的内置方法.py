# 字典取值方法
g = {"v":"1","w":"2","x":"3","y":"4","z":"5"}
# 使用下标去取如果没有对应的值就会报错
print(g["v"])
# 使用get去取值没有会返回none,并且可以为他指定一个值
print(g.get("a","n"))
# 获取长度
print(len(g))
d = {"a":"1","b":"2","c":"3","d":"4"}
# 遍历新字典添加到旧字典中
for i in d:
    print(i,d[i])
    g[i] = d[i]
print(g)
# 方式一删除字典内的数据
del g["v"]
print(g)
# 方式2弹出
re = g.pop("w")
print(re)
print(g)
# 取出字典中所有的键
print('================================')
print(g.keys(),type(g.keys()))
# 取出字典中所有的值
print(g.values())
# 取出字典中所有的键值对
print(g.items())
print("=========================================")
m = {}
name = input()

m[name] = {
    "a":1,
    "b":name,
    "c":{
        "d":123,
        "e":345,
    }
}
print(m)
print(m.get(name).get("c"))