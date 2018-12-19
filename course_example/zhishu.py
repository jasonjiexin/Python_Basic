import datetime

#打印100以内的所有素数
delta = [0, 0]
counts = [0, 0]
start = datetime.datetime.now()
for x in range(2, 100):
    for i in range(2, x):
        if x % i == 0:
            break
    else:     #else是for循环后执行的语句，并不是break后执行的语句
        print(x)
        counts[0] += 1
delta[0] = ((datetime.datetime.now())-start).total_seconds()
print(delta)
print(counts)

print('---------------------------------------------------------------------')

#打印10000以内的所有素数
for x in range(2, 10000):
    for i in range(2, x):
        if x % i == 0:
            break
    else:     #else是for循环后执行的语句，并不是break后执行的语句
        print(x)

#改进打印10000以内的所有素数
for x in range(2, 10000):
    for i in range(2, int(x**0.5)):
        if x % i == 0:
            break
    else:     #else是for循环后执行的语句，并不是break后执行的语句
        print(x)

print('---------------------------------------------------------------------')

#计算算法的时间


upper_limit = 100000
delta = [0, 0]
counts = [0, 0]

start = datetime.datetime.now()
for _ in range(10): #将循环放大观察算法的效率，当不关心变量的具体变化时，变量名可以用下划线表示
    counts[0] = 0
    for x in range(2, upper_limit):
        for i in range(2, int(x ** 0.5)+1):
            if x % i == 0:
                break
        else:
            print(x)
            counts[0] += 1
delta[0] = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(counts)