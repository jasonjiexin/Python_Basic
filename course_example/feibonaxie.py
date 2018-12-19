#打印斐波那契数列，100以内
print(0)
print(1)
a = 0
b = 1
while True:
    c = a+b
    if c > 100: break
    a = b
    b = c
    print(c)

print('--------------------------1-------------------------------')

#打印斐波那契数列的第101项
i = 1
j = 1
count = 0
while True:
    i, j = j, j+i
    count += 1
    if count ==100:
        break
print(i)

print('--------------------------2-------------------------------')

