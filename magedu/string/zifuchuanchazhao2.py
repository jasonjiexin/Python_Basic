'''
index与rindex 都是在字符串中找元素并返回索引，
index与rindex 找不到都会报错
原理：
现在锁定查找的区间然后再进行检索并返回索引值，类型为int
index() 从左往右找，rindex() 从右往左找
'''

s = "i am very very very sorry"
print(s.index('very'))
print(s.index('very',5))
# index查找不到元素的时候报错
# print(s.index('very',6,13))
print(s.index('very',10))
print(s.rindex('very',10))
print(s.rindex('very',10,15))
#返回字符串的长度，即字符的个数
print(s.__len__())
#找不到元素报错
#print(s.rindex('very',-10,-15))