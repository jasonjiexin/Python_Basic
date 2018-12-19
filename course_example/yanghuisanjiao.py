#当杨辉三角只有三行，构造方法是
triangle = [[1],[1,1]]
n = 3
for i in range(2, n):
    #pre是上一行，上一行是需要通过下标索引进行操作的
    pre = triangle[i - 1]
    #cur是当前行，当前行只是进行数据的添加并没有通过下标索引进行操作,建立当前的列表，首个元素是1
    cur = [1]
    #当前列表中第二个元素是上个列表中两个元素的和
    cur.append(pre[0] + pre[1])
    #当前列表最后一个元素是1，完成当前列表的构建
    cur.append(1)
    #将当前列表添加至杨辉三角列表
    triangle.append(cur)
    print(triangle)


