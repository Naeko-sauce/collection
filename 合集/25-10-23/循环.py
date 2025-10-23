c = 0
while c < 10:
    c = c + 1
    if c  == 4:
        print("跳出本次循环")
        continue
    elif c == 7:
        print("结束")
        break
    else:
        print(c)
