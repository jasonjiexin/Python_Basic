
'''
集合运算-差集
'''

a = {1,2,3,4,5,6}
b = {5,6,8,9,7,1,2}
c = {5,6,7,8}

# 差集：A-(A&B)   等同于   A-B
d = a.difference(b)
e = a - b
print(d)
print(e)

print("------"*7)

print(a)
print(b)
print(c)


'''
集合运算-差集
'''

a = {1,2,3,4,5,6}
b = {5,6,8,9,7,1,2}
c = {5,6,7,8,4}

# d = a.difference_update(b) 这种表达方式是错误的，a.difference_update(b) 这个方法不进行传值，因此d的值为None

# 多集合差集：A-B(A对B的差集),A-(A∩B)-(A∩C), 意思为a集合中的这些元素其他两个元素是没有的
a.difference_update(b,c)
print(a)

print("------"*7)

print(a) #a集合的值已经被修改了
print(b)
print(c)



'''
集合运算-差集
'''

a = {1,2,3,4,5,6}
b = {5,6,8,9,7,1,2}
c = {5,6,7,8}


# 差集：A-(A&B)
a -= c

print(a)

print("------"*7)

print(a) #a集合的值已经被修改了
print(b)
print(c)



'''
集合运算-对称差集
'''
a = {1,2,3,4,5,6}
b = {5,6,8,9,7,1,2}
c = {5,6,7,8,4}

# （A-B）∪（B-A）
# 该函数只能与一个集合求对称差集
d=a.symmetric_difference(b)
print(d)

# 第二种用符号的写法
e=a ^ c
print(e)

print("------"*7)

print(a) 
print(b)
print(c)



'''
集合运算-对称差集
'''

a = {1,2,3,4,5,6}
b = {5,6,8,9,7,1,2}
c = {5,6,7,8,4}

# 求A集合和B集合的对称差集，以修改A集合元素的方式，就地修改
a.symmetric_difference_update(b)
print(a)

#符号的方法表示
b^=c
print(b)

print("------"*7)

print(a)  #A集合发生了变化
print(b) #B集合发生了变化
print(c)



'''
集合运算-对称差集
'''
a = {1,2,3,4,5,6}
b = {1,2,3,4}
c = {1,2,3,4,5,6}
f = {11,22,33}
g=set()

# 判断是否是子集
#d = b.issubset(a)
d = b<=a  #运算符重载的写法，与d = b.issubset(a)相同
print(d)

e=a.issubset(c)
print(e)

# 判断b是否是a的真子集，c是否是a的真子集
print(b < a)
print(c < a)

# 判断a是否是b的真超集
print(a > b)
print(c > a)


# 判断a集合与f集合是否有交集，如果没有返回True
print(a.isdisjoint(f))

#空集是任何集合的真子集
print(g < c)
# print({} <  c)  这种写方法是错误的，因为dict（）与set（）不能一起运算
