with open("1.txe","w",encoding="utf-8") as f:
    f.write("hello 你好")

    # split()
    # 的核心用处是按指定规则拆分字符串，将零散的文本转换为可操作的列表数据，其优势在于灵活适配不同分隔符、支持限制分割次数，是文本解析、数据提取、用户输入处理等场景的必备工具。
with open("1.txe","r",encoding="utf-8") as f:
    data = f.read().split(" ")
    print(data)
    # 在
    # Python
    # 中，insert()
    # 是列表（list）类型的内置方法，核心作用是在列表的指定索引位置插入一个元素，且不会覆盖原有元素，原有元素及后续元素会自动向后移位（索引 + 1）。它是灵活调整列表结构、在指定位置添加数据的关键工具。
    data.insert(1,"der")
    print(data)
    # 在
    # Python
    # 中，"".join(data)
    # 里的
    # join()
    # 是字符串（str）类型的内置方法，核心作用是：将一个「可迭代对象」（如列表、元组等）中的所有元素（必须是字符串类型），按照指定的「分隔符字符串」连接成一个全新的字符串。
    # 其中
    # "".join(data)
    # 中的空字符串
    # ""
    # 就是「分隔符」，表示连接时元素之间不添加任何字符，直接拼接。
    data = "".join(data)
    print(data)
with open("1.txe","w",encoding="utf-8") as f:
    f.write(data)