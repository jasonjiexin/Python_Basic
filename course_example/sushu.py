#100以内的素数

import math
n = 100
#给定一个空list
lst = []
#从2-100之间循环取数，
for x in range(2, n):
#一个数字如果能够被一个素数整除那么它就是合数，需要用n来除以所有list中的素数，合数一定可以分解为几个质数的乘积
    for i in lst:
        if x % i == 0:
            break
    else:
        print(x)
        lst.append(x)
#测试性能需要将print语句注释掉
#print(lst)

print("--------------------------")
lst1 = [2]
#所有的偶数都能够被2整除所以0-100之间的取数只取奇数就能够实现了
for n in range(3, 100, 2):
    for i1 in lst1:
        if n % i1 == 0:
            break
    else:
        print(n)
        lst1.append(n)

#验证两个列表的值是否一致
print(lst == lst1)

print("--------------------------")
#规则：如果一个数能够被从2开始到自己的平方根的正整数整除，就是合数
n1 = 100
lst2 = []
for v in range(2, n1):
    for i2 in range(2, math.ceil(math.sqrt(v))): #math.ceil开方取整
        if v % i2 == 0:
            break
    else:
        print(v)
        lst2.append(v)
print(lst2)