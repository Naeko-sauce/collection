sa = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# 只能写入字符串所以要转换
with open("sa.txt","w",encoding="utf-8") as f:
     da = f.write(str(sa))

with open("sa.txt","r",encoding="utf-8") as f:
     da = f.read()

     print(da[0],type(da))