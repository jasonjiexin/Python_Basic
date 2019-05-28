#-*- coding:utf-8 -*-

#continue跳出
for f in range(10):
    if f%2==0:
        continue
    print(f)
print("--------------1--------------")

#break，1000以内能被7整除的前20个数
count = 0
for i in range(0, 1000, 7):
    print(i)
    count += 1
    if count >= 20:
        break
print("--------------2--------------")

#改为while语句
count1 = 0  #计数器清零
a = 0  #指定边界值
while True:
    print(a)
    a += 7   #部长加7
    count1 += 1
    if count1 >= 20:
        break
print("--------------3--------------")

#输入一个数字，判断它是几位数，并且按照个位、十位、百位等的顺序进行打印
num = int(input("请输入一个五位以内的数字："))
countnum = 0
while True:
    print(num%10)
    num = num // 10
    countnum += 1
    if num == 0:
        break
print("countnum:"+ str(countnum)) #两个相同数据类型的数据才能够相互拼接在一起
print("--------------4--------------")

num1 = int(input("请输入一个五位以内的数字："))
countnum1 = 1
b = 5
while True:
    b -= 1
    divi = num1 / 10**b
    if divi >= 1:
        print(num1 // 10**b)
        num1 = num1 % 10**b
        countnum1 += 1
        if num1 == 0:
            break
    else:
        continue
print("countnum:"+ str(countnum1))
print("--------------5--------------")


s_length = int(input("请输入正方形的边长:"))
for i in range(0, s_length):

    print("*")


print("--------------6--------------")

