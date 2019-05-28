for i in range(1, 10):
    for j in range(i, 10):
        if i >1:
            print(' ' * 10 * (i - 1), end='  ')
        print(str(i) + 'x' + str(j) + '=' +  str(i * j), end='  ')
    print('  ')