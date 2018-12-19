#杨辉三角变式方法一
triangle = []
n = 6
for i in range(n):
    # row代表着行1，从行0（第一行）就开始进行计算，所有的行都是通过计算得到的
    row = [1]
    triangle.append(row)
    if i == 0:
        continue
    for j in range(i - 1):
        #根据下行是上行衍变而来的原则，通过双下标指定相应的元素进行运算
        row.append(triangle[i-1][j] + triangle[i-1][j+1])
    row.append(1)
print(triangle)