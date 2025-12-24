# 打开文件的两种语法

# 操作模式分为三种
# r模式 read :读取文件数据
# with open("1.txt","r",encoding="utf-8") as f:
#     data = f.read()
#     print(data)
# w模式 write : 写入文件模式
# 当前文件不存在的时候会自动创建文件
# w又叫覆盖写模式，每一次写入数据的时候都会将原本内容清空，然后写入新的数据
with open("1.txt","w",encoding="utf-8") as f:
    data = f.write("123")
#a模式 append ：追加文件模式
# 句柄 = open("文件路径","操作模式","编码格式")
# 打开文件
# fp = open("1.text","w",encoding="utf-8")
# # 操作句柄
# # 写入数据
# fp.write("hello world")
# # 关闭文件
# fp.close()
# 方法2使用with关键字自动打开和关闭文件
with open("1.txt","w",encoding="utf-8") as f:
    f.write("bddd")

# + 模式，让原本的模式扩展出新的模式
#a+
#r+ 既能读又能写
#w+ 既能写又能读
#特点也是覆盖写
with open("1.txt","r+",encoding="utf-8") as f:
    # f.write("j2222")
    data = f.read()
    print(data)

# 五b模式：操作二进制数据模式
# 读取二进制数据
with open("2FED4FE15EBA40CF4BC10DA6C215E04F.jpg","rb") as f:
    data =f.read()
    print(data)
# 写入二进制数据，跟据网页的图片连接获取到图片二进制数据保存到本地
with open("w.jpg","wb")as f:
    f.write(data)
