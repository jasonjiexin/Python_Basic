#i为行，j为列
for i in range(1, 10):
    for j in range(1, i+1):
        print(str(j) + 'x' + str(i) + '=' + str(i * j), end='  ') #end='  '   打印的时候不换行
    print('  ') #打印后空格换行

print("1------"*20)

#用制表符\t解决对不齐的问题
for i in range(1, 10):
    for j in range(1, i+1):
        print(str(j) + 'x' + str(i) + '=' + str(i * j) + '\t', end='  ') #\t是在打印的内容前面加空格
    print('  ')

print("2------"*20)

#用i*j的乘积解决对不齐的问题,第一列都空了两个(用空格的方法)
for i in range(1, 10):
    for j in range(1, i+1):
        product = i * j
        if product < 10:
            product = str(product) + '   '
        print(str(j) + 'x' + str(i) + '=' +  str(product) , end='  ') #\t是在打印的内容前面加空格
    print('  ')

print("3------"*20)

#用i*j的乘积解决对不齐的问题,达到等间距（用空格的方法）
for i in range(1, 10):
    for j in range(1, i+1):
#将结果赋值到一个变量中再做操作
        product = i * j
#给结果一位数加一个空格，为了做输出格式对齐
        if j  > 1 and product < 10:
            product = str(product) + ' '
        else:
            product = str(product) #除if条件后的所有条件执行后，两个表达式之间相隔n个空格，n与end后面的空格数保持一致
        print(str(j) + 'x' + str(i) + '=' + product , end='  ') #\t是在打印的内容前面加空格
    print('  ')
print("4------"*20)

#打印乘法口诀的上半部分
for i in range(1, 10):
    print('  ' * 4 * (i - 1), end=' ')  #每段输出前的格式“表达式+空格”
    for j in range(i, 10):
        product = i * j  #乘积先计算出来方便之后格式化代码
        if product < 10:  #用product值来判断结果是否是一位数，一位数才进行补位
            end = '  '
        else:
            end = ' '
        print(str(i) + 'x' + str(j) + '=' + str(product), end=end) #最后决定输出，end具体值赋值给end
    print()
print("5------"*20)

#字符串的处理方式
for i in range(1, 10):
    line = ' '
    for j in range(1, 10):
        if i > j:
            line = '{} {}   {:<4}'.format(' ', ' ', '  ' )
        else:
            line = '{}*{} = {:<4}'.format(i, j, i*j)
        print(line, end=' ')
    print()
print("6------"*20)

#代码是一次一次优化而来的