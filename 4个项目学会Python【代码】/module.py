# 实现一个“今天吃啥”的小程序
# “今天吃啥”程序的功能很简单，运行程序后从你喜欢的各种美食中
# 随机挑选一种作为结果打印出来

# 模块 包 库
# import random
from random import shuffle, choice

data = ['辣椒炒肉','水煮鱼','猪肚鸡','兰州拉面','咖喱饭','炒面']
shuffle(data)
print(choice(data))
print(data)

import math
print(math.fabs(-10.123))

import os.path
print(os.path.abspath('./'))



