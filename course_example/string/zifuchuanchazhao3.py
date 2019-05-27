'''
count 统计指定子字符串在字符串中出现的次数
原理：
与index、find执行过程一致
'''

s = "i am very very very sorry"
print(s.__len__())
print(s.count('very'))
print(s.count('very', 5))
print(s.count('very', 10, 14))