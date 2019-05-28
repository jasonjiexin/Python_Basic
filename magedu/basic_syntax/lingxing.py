#用负数处理避免了用大数索引，导致关系不好确定并抽象，所以需要体现算法的重要性
#打印菱形
for i in range(-3, 4):
    if i < 0:
        prespace = -i
    else:
        prespace = i
    print(' ' * prespace + '*'*(7 - 2*prespace))


print('1------------'*10)

# 打印闪电
for j in range(-3,  4):
    if j < 0:
        print(' ' * (-j) + '*' * (4+j))
    elif j > 0:
        print(' ' * 3  + '*' * (4-j))
# 隐含条件就是 j = 0
    else:
        print('*' * 7)

print('2------------'*10)
