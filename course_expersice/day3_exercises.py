#-*- coding:utf-8-*-#


print("----------------1----------------")
#打印一个正方形
while True:
    for i in range(1, 11):
        if i == 1:
            print('*' * 21)
        elif i == 10:
            print('*' * 21)
        else:
            print('*' + ' ' * 19 + '*')
    break
print("---------------------------------")


print("----------------2----------------")
#求100以内所以奇数的和，方法一
sum = 0
for i in range(1, 100, 2):
    sum += i
else:
    print(sum)

#方案二,该方法在处理数据的时候会比方法一慢一些
sum = 0
for i in range(1, 100):
    if i % 2 != 0:
        sum += i
else:
    print(sum)
print("---------------------------------")

print("----------------3----------------")
# 判断分支练习
num = int(input(">>>>>>"))
if num > 90:
    print('A')
elif 80 <= num <= 89:
    print('B')
elif 70 <= num <= 79:
    print('C')
elif 60 <= num <= 69:
    print('D')
else:
    print('E')
print("---------------------------------")

print("----------------4-----------------")
# 求1到5阶乘的和,方法一
sum1 = 0
jc = 1
n = 5
for j in range(5, 0, -1):
    for i in range(n, 0, -1):
        jc *= i
    n -= 1
    sum1 += jc
    jc = 1
else:
    print(sum1)

#方法二：运用到算法优化的点
nums = 1
x = 0
for n in range(1, 6):
    nums *= n
    x += nums
else:
    print(x)
print("---------------------------------")

print("----------------5-----------------")
#判断一个数是否是质数，首先这个数要大于1，并且只能被1和本身整除
num1 = int(input(">>>>>>"))
if num1 == 2:
    print(str(num1)+"是质数")
else:
    for a in range(2, num1):
        if num1 % a == 0:
             print(str(num1)+"不是质数")
             break
#利用for循环的else语句不打印else中的语句
    else:
        print(str(num1)+"是质数")
print("---------------------------------")