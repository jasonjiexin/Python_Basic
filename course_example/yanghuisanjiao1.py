#杨辉三角打印四行
triangle = [[1],[1,1]]
#杨辉三角有四行
n = 4
for i in range(2, n):
    pre = triangle[i - 1]
    cur = [1]
    #打印当前列表中除收尾外的元素，逐个循环打印，j的循环是要说明打印的次数，每打印一次列表中多一个元素
    for j in range(0, i - 1):
    #列表中形成元素的规则
        cur.append(pre[0] + pre[1])
    cur.append(1)
    triangle.append(cur)
print(triangle)