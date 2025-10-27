# join(可迭代类型)
print(''.join(["1","2","3","4","5","6","7","8","9"]))
print('|'.join(["1","2","3","4","5","6","7","8","9"]))
# 字符串可以索引取值但是不能索引改值
# 切片
# 按照指定位置将某部分取出来
print("dream"[1:3])
# 字符串反转[::1]将整个字符串反转
print("dream"[::-1])
print("dream"[::-2])
# 判断某个值是否在里面
print("d" in "dream")
print("d" in "=ream")
# 去除特殊字符
print("$dre$am$".strip("$"))
# 去除不同方向的特殊字符
print("$dre$am$".rstrip("$"))
print("$dre$am$".lstrip("$"))
# 按照指定的方法将字符串进行分割
m = "dema|aa|dd|ee|ff"
print(m.split("|"))
# 将字符串大小写转换
# 转为大写
ne = "Isss"
print(ne.upper())
# 转换为小写
print(ne.lower())
# 查找某个字符在所在的位置
print(ne.find("s"))
# 统计当前字符在字符串中出现的次数
print("dwwaa".count("a"))
# 填充字符
nee = "derraa"
print(nee.center(len(nee)+3,"$"))
print(nee.startswith("d"), nee.endswith("d"))