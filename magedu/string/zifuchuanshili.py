'''
简单版
不过滤,字符有重复的统计
1.判断数字为几位数
2.打印每一位数字及其重复的次数
3.一次打印每一位数字，顺序：个、十、百、千、万.........
'''

# 输入的数字是几位数,先去除空白字符，左边开头的0
m = input('>>>').strip().lstrip('0')
print("这是{}位数".format(len(m)))

# 打印每一位数字并统计该数字出现的次数
for i in range(len(m)):
    print("{}' s count = {}".format(m[i], m.count(m[i])))

# 依次打印每一位数字，顺序个、十、百、千、万
for j in range(len(m)):
    n = m[-j-1]
    print(n)

print(m)

