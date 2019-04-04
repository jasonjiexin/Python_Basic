lst = ['张','王','理','于']
lst1 = ['王','以','核','丘']

f_name = lst.__len__()
s_name = lst1.__len__()

count = 0

r
print("")
print("======================="*10)


# 上下文字正序组合
for i in range(f_name):
    for j in range(s_name):
     print(lst[i] + lst1[j], end=" ")
     count += 1
     if count > 6:
         print(' ')
         count = 0

print("")
print("======================="*10)

# 上下文字逆序组合
count = 0
for i in range(f_name):
    for j in range(s_name):
     print(lst1[j] + lst[i], end=" ")
     count += 1
     if count > 6:
         print(' ')
         count = 0