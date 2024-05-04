# 导入模块
from house_operation import *
def main():
    """循环显示菜单"""

    while True:
        main_menu()
        key = input("请输入1-6")
        if key in ['1', '2', '3', '4', '5', '6',]:
            if key == '1':
                print("后面处理")
            elif key == '2':
                print("后面处理")
            elif key == '3':
                print("后面处理")
            elif key == '4':
                print("后面处理")
            elif key == '5':
                print("后面处理")
            elif key == '6':
                break


if __name__ == '__main__':
    main()
    print("退出程序")