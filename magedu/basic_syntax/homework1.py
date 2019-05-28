#计算一个圆形的面积和周长
#r = int(input('r='))
# print ('area='+str(3.14*r*r))
# print ('circumference='+str(2*3.14*r))

'''
# 从小到大打印两个数字
a = input('score1=')
b = input('socore2=')
if a<b:
    print(a, b)
else:
    print(b, a)
'''


#输入n个数字计算平均数
n = 0
sum = 0
while True:
    i = input('>>>')
    if i == 'q':
        break
    n += 1
    sum += int(i)
    avg = sum/n
    print(avg)
