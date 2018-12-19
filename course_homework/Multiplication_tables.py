#-*- coding: UTF-8 -*-
#乘法口诀表,方法一
#主要思路：为从行进行打印，然后将不符合要求的去掉
for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
          print (str(j)+'*'+ str(i) +'='+str(i * j), end="  ")
        else:
            break
    print('\n')

print("----------------------------------------")

#方法二
#主要思路：按照行进行打印，按照列来限制打印的列
for a in range(1, 10):
    for b in range(1, a+1):
        print(str(b)+'*'+str(a)+'='+str(b*a), end="  ")
    print()