'''
分割字符串
split(sep,maxsplit)
'''
# split (sep, maxsplit)  sep为分割字符串，缺省状态下以空格字符串为分割字符串，maxsplit 分割次数
s1 = "i 'm \ta super student"
print(s1)
# 以下两者区别第一个为sep为缺省的情况下不管字符串中有几个空白字符都会视为分割符并打印的时候不显示，第二种以一个空字符为分割符进行分割字符串，当两个空格连在一起的时候切割后的字符串如下
print(s1.split())
print(s1.split(' '))

# ['i', "'m", '\ta', 'super', '', '', '', 'student'] 切割后发现后面一位还是空格，所有以，''，来进行补位,有几个空格就有几个逗号，中间用''（空字符）填充
s2 = "i 'm \ta super    student"
print(s2.split(' '))

print("----------")
# 按照指定的分隔符分割后分隔符不显示
print(s1.split('s'))
print(s1.split('super'))
# 字符串中super后面有一个空格，当分隔符为super和super+一个空格都是能够匹配进行分隔的，当super+多个空格的时候就不能够进行匹配分隔了
print(s1.split('super  '))

# 按照空格进行分隔，\t不省略
print(s1.split(' '))

# maxsplit 最多分割次数，分割一次将字符串分为两段,如果字符串中没有被切字符串，那么一次都不切
print(s1.split(' ',maxsplit=2))
print(s1.split('\t',maxsplit=2))

# maxsplit = -1 遍历整个字符串
print(s1.split(' ',maxsplit=-1))