def register():
    print("用户注册功能")
    username, password = get_user_info()
   
    # 校验用户是否存在
def login():
    print("用户登录功能")
    username, password = get_user_info()
def get_user_info():
    username = input("请输入用户名:").strip()
    password = input("请输入密码:").strip()
    return username, password
def read(file="data.text", mode="r", encoding="utf-8",data=None):
    if mode == "r":
        # 声明一个空字典
        data = {}
        # 如果是第一次注册他是没有data.text文件的，所以要加异常处理
        try:
            with open(file=file, mode=mode, encoding=encoding) as f:
                data = f.read()
        except Exception as e:
            print(e)
            print("文件不存在，可能是第一次注册")
        return data
    else:
        try:
            u = []
            for user_info in data.values():
                u.append("|".join([str(value) for value in user_info.values()]) + '\n')
            with open(file=file, mode=mode, encoding=encoding) as f:
                data = f.writelines(u)
        except Exception as e:
            print(e)
            data = ""


        
nm = '''
功能菜单
1. 用户注册
2. 用户登录

'''
# 做一个功能字典
func_dict = {
    "1": register,
    "2": login
}
w = True
i = 0
# 启动登录注册成功
while w:
    print(nm)
    func_id = input("请输入功能编号:").strip()
    if func_id not in func_dict.keys():
        print("功能编号输入错误，请重新输入")
        i += 1
        if i > 3:
            print("输入错误次数过多，退出程序")
            w = False
        continue
    fun = func_dict.get(func_id)
    print(fun)
    flag , msg = fun()
    if flag:
        print(msg)
        break
    else:
        print(msg)
        continue