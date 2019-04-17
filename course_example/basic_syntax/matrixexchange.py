'''
M=N（方阵）矩阵元素转换
'''
# 写法1
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
count = 0
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if i < j:
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
            count += 1
print(matrix)
print(count)
print('---------'*50)


# 写法2 ，交换部分用到封装和解构
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
count = 0
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if i < j:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            count += 1
print(matrix)
print(count)
print('---------'*50)


# 写法3，不用enumerate方法
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
matrix_len = len(matrix)
print(matrix_len)
count = 0
for i in range(matrix_len):
    for j in range(matrix_len):
        if i < j:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            count += 1
print(matrix)
print(count)
print('---------'*50)