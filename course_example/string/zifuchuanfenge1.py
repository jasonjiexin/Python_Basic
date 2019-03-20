# 字符串分割 split
'''
按照行来切割字符串
keepends 指是否保留行分割符
行分隔符\n, \t\n, \t
'''
print('ab c\n\nde fg\r kl\r\n'.splitlines())

#保留分割符的切分字符串
print('ab c\n\nde fg\r kl\r\n'.splitlines(True))

#不保留分割符的切分字符串
#分割字符串是先遍历整个字符串，先按照分割符分割好字符串，分割符也将被分割出来，最后再决定是否需要显示分割符
print('ab c\n\nde fg\r kl\r\n'.splitlines(False))

s1 = "i 'm   a super student.\n" \
     "you are a super student"
print(s1)
print(s1.splitlines())
print(s1.splitlines(True))