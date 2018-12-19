#100以内的素数

import math
n = 100
#给定一个空list
lst = []
#从2-100之间循环取数，
for n in range(2, n):
#一个数字如果能够被一个素数整除那么它就是合数，需要用n来除以所有list中的素数，如果有整除
    for i in lst:
        if n % i == 0:
            break
    else:
        print(n)
        lst.append(n)
#测试性能需要将print语句注释掉
#print(lst)

print("--------------------------")
n = 100
lst1 = [2]
#所有的偶数都能够被2整除所以0-100之间的取数只取奇数就能够实现了
for n in range(3, 100, 2):
    for i in lst1:
        if n % i == 0:
            break
    else:
        print(n)
        lst1.append(n)

#验证两个列表的值是否一致
print(lst == lst1)