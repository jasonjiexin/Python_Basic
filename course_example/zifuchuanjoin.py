# join 将可迭代对象连接起来，.join(lst)
lst = ['1', '2', '3']
print(lst)
print("\"".join(lst))
print("   ".join(lst))
print("\n".join(lst))

lst = ['1',['a','b'],'3']

# "+" 把不同的字符串连接起来形成新的字符串
lst1 = "i"
lst2 = "am"
lst3 = "jason"
print(lst1 + "   " +  lst2 + "   " + lst3)