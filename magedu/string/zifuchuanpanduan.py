'''
endswith 是否以某个子字符串结尾
startswith 是否以某个子字符串开头
检索的原理与index、find类似，都在在制定的区域内进行检索查询
'''

s = 'i am very very very sorry'
print(s.startswith('very'))
print(s.startswith('very', 5))
print(s.startswith('very', 5, 9))
print(s.endswith('very', 5, 9))
print(s.endswith('very', 5, -1))
# 超范围超界没有关系，只看字符串的最后一位
print(s.endswith('very', 5, 100))

