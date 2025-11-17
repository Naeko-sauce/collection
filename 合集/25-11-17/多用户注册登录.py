mu = '''
    功能1
    功能2
    退出3
'''
m = {}
while True:
    print(mu)
    fun_id = input("输入功能").strip()
    if not fun_id.isdigit():
        print("布什数字")
        continue
    fun_id = int(fun_id)
    if fun_id not in [1, 2, 3]:
        print("当前功能不存在")
        continue
    if fun_id == 1:
        print("注册")
        name =  input("用户").strip()
        password = input("密码").strip()
        if m.get(name):
            print("当前用户存在",name)
            continue
        m [name] = {
            'name': name,
            'password': password,
        }
        print("当前用户注册成功")
    elif fun_id == 2:
        print("登路")



