# 输入的数字是几位数
m = input('>>>').lstrip('0')
print("这是{}位数".format(len(m)))

# 打印每一位数字并统计该数字出现的次数
for i in range(len(m)):
    print("{}' s count = {}".format(m[i], m.count(m[i])))

# 依次打印每一位数字，顺序个、十、百、千、万
for j in range(len(m)):
    n = m[-j-1]
    print(n)

print(m)

