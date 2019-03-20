'''
python 的format函数
'''
# {} 代表输出的内容，其中数字定位输出的内容，('zhang', 'xin')整体是元组的第一个元素
print("{0[0]} {0[1]}".format(('zhang','xin')))
print("{0[0]} * {0[1]}".format(('zhang','xin')))
print("{0[1]} * {0[0]}".format(('zhang','xin')))

# {0} 表示将('zhang','xin') 整体输出
print("{0} * {0}".format(('zhang','xin')))


# print("{} * {}".format(('zhang','xin'))) IndexError: tuple index out of range；前面要求展现两个{} {} 元素，后面元素中只有一个元素，应修改为以下方式
print("{} * {}".format('zhang','xin'))

print("{0} * {0}".format(('zhang','xin')[0]))
print("{} * {}".format(('zhang','xin')[0], ('  ', 'com')[1]))

# format 传入的是需要展示的数据，
print('{0}*{1}={2:<2}'.format(3,2,2*3))
# < 是左对齐，
print('{0}*{1}={2:<02}'.format(3,2,2*3))
print('{0}*{1}={2:>02}'.format(3,2,2*3))
print('{0}*{1}={2}'.format(3,2,2*3))
#默认为右对齐
print('{0}*{1}={2:02}'.format(3,2,2*3))

