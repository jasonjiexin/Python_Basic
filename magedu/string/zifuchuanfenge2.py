'''
partition 按照分割符将字符串分隔成两部分，并且保留分割符
'''
s1 = "i 'm a super student"
print(s1)
print(s1.partition('s'))
print(s1.partition('stu'))
print(s1.partition(' '))

#当遍历字符串后没有找到分割符，返回头和两个空元素的三元组
print(s1.partition('abc'))

# 从字符串最后一个字符开始遍历，找分隔符
print(s1.rpartition('s'))