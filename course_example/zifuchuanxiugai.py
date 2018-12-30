'''
字符串代替replace、strip
'''
# replace
s2 = 'www.jasonworkshop.com'
# 将字符串中的w用p代替
print(s2.replace('w', 'p'))
# 将字符串中的w用p代替，只代替两次
print(s2.replace('w', 'p', 2))
print(s2.replace('www', 'com'))

#strip
s3 = '\r  \n  \t  hello world  \n   \t'
print(s3)
#strip 从头和尾部去除空字符
print(s3.strip())

#去除字符是从两头往中间找，指定的字符顺序没有要求，如制定r、y，至于哪个在前哪个在后就不是很重要了。
#制定的字符要是在两头没有只是在字符串的中间有，那么不能够去除与该字符相同的字符
s4 = "i am very very very sorry"
print(s4)
print(s4.strip('r  y'))
print(s4.strip('ry'))
print(s4.strip('ryso ryeiam'))
print('==================')
#注意i 与am 之间的空格，如果没有空格是匹配不到该字符的
print(s4.strip("i am ve"))
print(s4.strip("vei am"))

#从左开始抵消字符
print(s4.lstrip('i am'))
#从右开始抵消字符
print(s4.rstrip('ry'))