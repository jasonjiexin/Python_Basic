'''
查找字符串，查到后返回字符串的首字符的索引，
如果没有查到就返回-1
指定查找的区域是前闭后开的，查找包含开始索引，不包含结束的索引
原理：
先看区间是什么，再在区间里进行查找
find()指定区间从左往右找,rfind()指定区间内从右往左找
'''
s = "i am very very very sorry";
# 查询子串，在指定区间内从左至右找
print(s.find("very"))

# 从索引5开始（包括索引5）进行查找
print(s.find("very",5))
print(s.find("very",6))

# 指定区间[6,13)，在这个区间内查找子字符串，查不到返回-1
print(s.find("very",6,13))  #如果是（6,14）就找到了

print("--------------------")
# 指定区间索引10至最后，在这个区间内查找子字符串，指定区间内从右往左找
print(s.rfind('very', 10))
print(s.find('very', 10))
print(s.rfind('very', 5))
print(s.rfind('very', 10, 15))
print(s.rfind('very', -10, -1))
print(s.rfind('very',  -1))