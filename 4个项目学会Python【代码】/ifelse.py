# if 表达式:
#     代码1
#     代码2
#     代码3
# else:
#     代码4
#     代码5
#     代码6

# 用一个变量记录天气的好坏，如果天气好就打印 出门打篮球
# 否则打印 躺着打游戏
good_weather = False
if good_weather:
    print('出门打篮球')
else:
    print('躺着打游戏')










# if 表达式1:
#     代码1
#     代码2
#     代码3
# elif 表达式2:
#     代码4
#     代码5
#     代码6
# elif 表达式3:
#     代码4
#     代码5
#     代码6
# else:
#     代码7
#     代码8
#     代码9

# 用一个变量记录天气，如果是雪天就打印 雪花飘飘
# 如果是下雨天就打印 下雨天了怎么办
# 如果是大风天或者阴天就打印 嘶
# 否则打印今天是个好日子
weather = '晴天'
if weather == '雪天':
    print('雪花飘飘')
elif weather == '下雨天':
    print('下雨天了怎么办')
elif weather == '大风天' or weather == '阴天':
    print('嘶')
else:
    print('今天是个好日子')











weather = 'rainy'
if weather == 'snow':
    print('雪花飘飘~~')
elif weather == 'rainy':
    print('下雨天了怎么办~~')
print('今天是个好日子~~')





good_weather = 0
hungry = 1
if hungry == 1:
    if good_weather == 1:
        print('我去食堂恰饭')
    else:
        print('我还是恰外卖吧')
else:
    print('恰什么恰，打游戏不香？')