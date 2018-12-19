import math
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


print(math.ceil(math.sqrt(25)))
for i2 in range(2, math.ceil(math.sqrt(25))):
    print(i2)