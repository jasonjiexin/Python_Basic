#-*- coding: UTF-8 -*-
#输入n个数，求每次输入后的算术平均数
n = 0
sum = 0
while True:
    i = input('>>>')
    if i == 'quit':
        break
    n += 1
    sum += int(i)
    avg = sum//n
    print(avg)