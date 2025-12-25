for i in range(10):
    try:
        print(1 / 0)
        print("1")
    except (ZeroDivisionError, TypeError) as e:
        print(e)
    else:
        if i == 2:
            raise ValueError("参数不能为2")
    finally:
        print("不管有没有异常都会走入finally")
