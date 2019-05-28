# 字符串定义
s1 = 'string'
s2 = "string"
s2 = "stringnew"

# 三引号中的内容上格式完全
s3 = '''this's a "string"'''

# 输出内容有换行，并且字符串中的空格也会被原样输出
s4 = 'hello \n      magedu.com'

# 引号中内容原样输出
s5 = r"hello \n      magedu.com"

s6 = 'c:\windows\nt'
s7 = R'c:\windows\nt'

#双斜杠表示原样输出\n
s8 = 'c:\windows\\nt'

sql = '''select * from table_name where name = 'jason' '''

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)
print(s8)
print(sql)
print(sql[4:11])
