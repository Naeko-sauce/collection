with open("1.txe","r+",encoding="utf-8") as f:
    # read 里面的数字可以控制当前读取的内容的字符个数并且是从头开始
    print(f.tell())
    # sekk方法可以控制指针移动
    # offset 移动几个字节
    #whence 移动模式
    #0 默认的模式,按照文件开头作为参照向后移动指定字节数
    #1 按照当前所在位置作为参照向后移动指定字节
    #2 按照文件末尾作为参照向后移动指定字节数
    f.seek(0, 2)
    # tell查看当前指针所在的字节位置
    data = f.read(-1)
    print(data)
    print(f.tell())
    f.write("11111")
