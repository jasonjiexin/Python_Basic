#打印菱形
for i in range(-3, 4):
    if i < 0:
        prespace = -i
    else:
        prespace = i
    print('  ' * prespace + '*'*(7 - 2*prespace))


print('-----------------------------------------------')


#打闪电
for j in range(-3,  4):
    if j < 0:
        print('  ' * (-j) + '*' * (4+j))
    elif j > 0:
        print('  ' * 3  + '*' * (4-j))
    else:
        print('*' * 7)


