a = 0
b = 0
salarys = []
while True:
    s = input("请输入员工工资(按q结束)")
    if s.upper() == 'Q':
        print("录入结束")
        break
    if float(s)<0:
        print("录入无效")
        continue
    print("录入成功")
    a +=1
    salarys.append(s)
    b += float(s)
    print("员工数{0}".format(a))
    print(salarys)
    print(b)
