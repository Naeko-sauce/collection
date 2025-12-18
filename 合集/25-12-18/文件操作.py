# 打开文件的两种语法

# 操作模式分为三种
# r模式 read :读取文件数据
# w模式 write : 写入文件模式
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