'''
集合的初始化
'''
# 创建空的集合
s = set()  #创建空集合的方法
s4 = {}   #创建过程中集合已经变成了字典

s1=set(range(5))
s2=set(list(range(10)))
s5={9,10,11}   #定义了一个集合
s6={(1,2),3,'a'}
# s7={[1],(1,),1} 其中有list类型，list不能hashable
s8={(1,2),2,None,"abc"} #这些数据类型都是不可变的
s9={"abc",b"abc"}  #这些数据类型都是不可变的

print(s, type(s))
print(s1, type(s1))
print(s2, type(s2))
print(s4, type(s4))
print(s5, type(s5))
print(s6,type(s6))
print(s8,type(s8))
print(s9,type(s9))
# print(s7,type(s7))



'''
集合的初始化
'''
# 如下两种表达方式表面上看起来是列表，但是set这种表达方式是将list值传给set而不是直接用list作为set的元素，
# 所以s12=set(list(range(4))) 与 s13=set([0,1,2,3])是可以初始化成功的

#s10={[0,1,2,3]} 报错
# s11={list(range(4))} 报错
s12=set(list(range(4)))
s13=set([0,1,2,3])

# print(s10,type(s10))
# print(s11,type(s11))
print(s12,type(s12))
print(s13,type(s13))


'''
集合的新增
'''
s=set(range(10))
print(s)

# set中增加一个元素
s.add(10)
print(s)

# set中增加的元素已经存在，不重复
s.add(10)
print (s)

#add是增加一个元素到set中，这里新增了一个tuple元素（66,67）
s4=(66,67)
s.add(s4)
print (s)

# update函数中的元素是可迭代的类型
s1={20,21} #set
s2=[31,32]  #list
s3=(51,52) #tuple
s.update({11,12,13,2})
s.update(s1)
s.update(s2)
s.update(s3)
print(s)


'''
集合删除
'''
s=set(range(10))
print(s)

# 移除set中的一个元素

s.remove(1)
print(s)

# 当没有元素的时候报错，KeyError
# s.remove(11)
# print(s)

# 当s中没有被需要的删除的元素时，什么都不做
s.discard(11)
print(s)

#每次任意删除集合中的一个元素
for i in range(5):
    s.pop()
print(s)

# 删除后剩下一个空的集合set（）
s.clear()
print(s)


