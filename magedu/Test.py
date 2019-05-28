#计算算法的时间
import datetime

delta = [0, 0]
counts = [0, 0]
start = datetime.datetime.now()
for _ in range(100):
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
