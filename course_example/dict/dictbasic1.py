# 缺省字典（defaultdict）

from collections import defaultdict

d1 = {}
d2 = defaultdict(list)  # 这里的list实际上是，list（），空列表

# 不用defaultdict() 的字典，需要提前判断k是否是在字典中，如果不在先需要给该k赋值一个空的列表，才能保证后续的数值存入字典中
for k in "abcde":
    for v in range(5):
        if k not in d1.keys():  # 判断k是否在字典中
            d1[k] = []  # 如果不在赋值为空的列表
        d1[k].append(v)  # 逐步开始加元素
print(d1)

# d2 为缺省字典，已经确定了字典的值为空list，不需要判断后再给某键的值赋值空列表
for k in 'mnopq':
    for v in range(3):
        d2[k].append(v)
print(d2)

# OrderedDict 字典
from collections import OrderedDict
import random

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
print(d)  # 字典输出的时候顺序随机

keys = list(d.keys())  # 转换为有序的列表
print(keys)

print("------------" * 8)

# 以下三次输出的顺序应该是一致的
random.shuffle(keys)  # 对keys再进行一次随机数，避免发生偶然状况（keys与字典中的key顺序一致）
print(keys)

od = OrderedDict()  # 创建 OrderedDict 对象

for key in keys:
    od[key] = d[key]  # d[key]的值赋给od[key],od[key] 记录字典的顺序

print(od)
print(od.keys())