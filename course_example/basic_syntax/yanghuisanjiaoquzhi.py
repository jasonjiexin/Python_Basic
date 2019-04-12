'''
补零的方法来，零刚好在对位j 和 j-2的值是相同的
'''
pre = [1]
cur = [1]
m = 6
k = 1

# print(pre)

# 分为三个部分：k<m and k!=m ，k==m or k==1，k>m

if k < m and k != 1:
# 要拿到第六层的数据只需要计算到第五层就好了，除了i=1，剩下需要计算四层（m-1）
    for i in range(1, m - 1):
        pre.append(0)
        cur.append(1)
        if i != 1:
            for j in range(1, i // 2 + 1):
                cur[j] = pre[j - 1] + pre[j]
# 当改位置是对称位时才能够执行下边的操作，补全对称位，对称位值相等
                if 2 * j != i:
                    cur[-j - 1] = cur[j]

# 当前的list(cur)变为之前的list(pre),这种写法是Python的一个特性，相当于两个variables相互交换
        cur, pre = pre, cur

    print("yang hui triangle's {}th line {}th num is {}".format(m, k, pre[k - 2] + pre[k - 1]))
# 取头和取尾都是1
elif m == k or k == 1:
    print("yang hui triangle's {}th line {}th num is 1".format(m, k))
else:
    print("k cannot bigger than m!")