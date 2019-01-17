'''
技巧版
过滤字符无重复的统计
1.判断数字为几位数
2.打印每一位数字及其重复的次数
3.一次打印每一位数字，顺序：个、十、百、千、万.........
'''

# 判断输入一个正确的正整数
num = ""
while True:
    # 输入一个整数去除整数头部和尾部的空字符,去除从左边开始的0
    num = input("please input a interger >>>").strip().lstrip('0')
    # 判断是否是十进制的数字0~9，不包括其他的字符
    if num.isdigit():
        break
print("The length of {} is {}.".format(num, len(num)))

print('~' * 20)

# 计算字符串中的每一个字符出现的次数
# 构造10个格子(只需要看0-9数字出现的次因此10个格子够了)，用来实现记录每个数字出现的次数，方便输出
counter = [0] * 10
for i in range(10):
    # 字符串中每一个字符在字符串中出现的次数，赋值给构造的列表中，表示counter[1]中放的是1在字符串中出现的次数，每一次迭代都用一个count
    counter[i] = num.count(str(i))
    # 如果counter[i] 只有0不进行打印，表示没有该数字
    if counter[i]:
        print("The count of {} is {}.".format(i, counter[i]))

print('~' * 20)

# 迭代字符串本身，判断条件过滤掉了重复的打印，意思是当counter[i]等于0的时候代表还没有统计过，要是有大于0的值直接进行下一轮迭代
# 上一个counter[i]的判断条件是从0-9一个个进行统计，统计好把次数放在相应的索引里
counter = [0] * 10
for x in num:
    i = int(x)
    # 避免重复统计计算的问题，当counter[x]有数字的时候代表x出现的次数已经统计过了
    if counter[i] == 0:
        counter[i] = num.count(x)
        print("The count of {} is {}.".format(x, counter[i]))

print('~' * 20)
# 迭代字符串本身
counter = [0] * 10
# 把字符串每个字符取出来，给counter[i]相应的位置+1直到所有的数据过滤一遍
for x in num:
    i = int(x)
    counter[i] += 1

for i in range(len(num)):
# 输出判断，出现过再打印
    if counter[i]:
        print("The count of {} is {}.".format(i,counter[i]))

print('~' * 20)

# 倒序打印,用range函数指定最后一位，并从最后一位开始打印
for i in range(len(num), 0, -1):
    print(num[i - 1], end='     ')
print('\n')
# 使用倒序函数进行打印
for i in reversed(num):
    print(i, end='     ')
print('\n')
# 用range函数确定字符串长度，通过计算拼凑从最后一个索引进行打印
for i in range(len(num)):
    print(num[-i - 1], end='     ')
print('\n')

print('~' * 20)
