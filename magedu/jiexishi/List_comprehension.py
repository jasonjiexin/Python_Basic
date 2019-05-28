#!/usr/bin/env python
# coding: utf-8
# jason
# ## 解析式

# 作用：解析式和生成器都是python特有的两个特性，他们能够帮助优化程序，大大减少代码的数量.

# ### 1.生成一个列表，列表0~9，对每一个元素自增1后求平方返回新的列表

# In[31]:


# 一般的写法

lst1 = list(range(10))
lst2 = []

for i in range(10):
    lst1[i] += 1
    square_num = lst1[i]**2
    lst2.append(square_num)
print(lst2)
print(lst1)


# In[32]:


# 根据规律简化代码

lst1 = list(range(10))
lst2 = []

for i in lst1:
    lst2.append((i+1)**2)
    
print(lst2)


# In[33]:


# 解析式写法
lst1 =list(range(10))
lst2 = [(i+1)**2 for i in lst1]

print(lst1)
print(lst2)


#  **注：能用列表解析式就用列表解释式，这种写法更加python**

# **注：[ 返回值 for 元素 in 可迭代对象 [if条件] ]**
# 

# ### 2.获取10 以内的偶数，比较执行效率

# In[34]:


#  普通写法
even = []
for x in range(10):
    if x % 2 == 0:
        even.append(x)

print(even)

# 列表解析式写法
even = []
even = [x for x in range(10) if x % 2 == 0]
print(even)   # print 没有返回值


even = []
even = [print(x) for x in range(10) if x % 2 == 0] # print((x) 是没有返回值的
print(even)   # print 没有返回值


# ### 3. 获取20以内的偶数，并且打印3的倍数. 获取20以内的偶数，并且打印不是3的倍数.

# In[35]:



even = [i for i in range(20) if i % 2 == 0 or i % 3==0]
print(even)

even = [i for i in range(20) if i % 2 == 0 or  not i % 3==0]
print(even)


# ### 4.获取20以内能被2整除也能被3整除的数字

# 
# 注：语法2
# [ expr for item in iterable if cond1 if cond2 ]
# 等价于
# ret = []
# for item in iterable:
#       if cond1:
#             if cond2:
#                   ret.append(expr)              

# In[36]:


# 一下两种表达方式表达的逻辑是一致的，and等于两个if
even = [i for i in range(20) if i % 2 == 0 and  i %3 == 0]
print(even)

even = [i for i in range(20) if i % 2 == 0 if i %3 == 0]
print(even)


#  [expr for i in iterable1 for j in iterable2]
#  等价于
#  ret = []
#  for i in iterable1:
#     for j in iterable2:
#         ret.append(expr)

# In[37]:


# tuple 嵌套在列表中
[(x,y) for x in 'abcde' for y in range(3)]
# 字典嵌套在列表中
[{x,y} for x in 'abcde' for y in range(3)]
# 列表嵌套在列表中
[[x,y] for x in 'abcde' for y in range(3)]


# In[38]:


# 以下三种方法表达的意义结果一致
# 每个 for 都做好 if 判断
[(i,j) for i in range(7) if i>4 for j in range(20,25) if j >23]
# 先写for，之后再做判断
[(i,j) for i in range(7) for j in range(20,25) if i>4 if j > 23]
# 先写for，之后再判断，if cond1 and cond2   等同于 if cond1 if cond2
[(i,j) for i in range(7) for j in range(20,25) if i>4 and j>23]


# ### 5.返回1-10平方的列表

# In[39]:


[i**2 for i in range(10)]


# ### 6.有一个列表lst=[1,4,9,16,2,5,10,15],生成一个新列表，要求新列表元素是lst相邻2项的和

# In[40]:


lst = [1,4,9,16,2,5,10,15]
lst_length = len(lst)
[lst[i]+lst[i+1] for i in range(lst_length-1)]


# ### 7.打印九九乘法表

# In[41]:


["{}*{}={}".format(i,j,i*j) for i in range(1,10) for j in range(1,10) if i<=j]


# In[3]:


# 'String1'.join('String2'),九九乘法表的横向构造
# 列表套列表的方式实现
print('\n'.join([' '.join(['%s*%s=%-3s' %(x,y,y*x) for x in range(1,y+1)]) for y in range(1,10)]))


# In[1]:


# ()'\n' if i==j else ' '),三目运算符的写法
[print('{}*{}={:<3}{}'.format(j,i,j*i,'\n' if i==j else ' '),end="") for i in range(1,10) for j in range(1,10)]


# ### 8.生成如下格式的ID号，“0001.abadicddws”

# In[18]:


import random

#代码拆解
bytes(range(97,123)).decode() # 获取 26个英文字母
[random.choice(bytes(range(97,123)).decode())] # 在26个英文字母中随机获取一个字符 
# 在26个英文字母中随机获取一个字符 ，取10次，但是获取后的格式不是需要的 ['b', 't', 'q', 'z', 'i', 'd', 'o', 'k', 'o', 'g']
[random.choice(bytes(range(97,123)).decode()) for _ in range(10)] 
# 用 join() 函数格式化字符串
(''.join([random.choice(bytes(range(97,123)).decode()) for _ in range(10)]))
# 这种写法只是关注次数，但是每一次的值并不关心
# for _ in range(10)

# {:04} 四位有效数字，不够用0填充,系统默认就是右对齐
['{:04}.{}'.format(n,''.join([random.choice(bytes(range(97,123)).decode()) for _ in range(10)])) for n in range(1,101)]


# In[24]:


import random
# 生成随机数random函数有很多的方法
chr(random.randint(97,122))

['{:04}.{}'.format(i,"".join([chr(random.randint(97,122)) for _ in range(10)]))for i in range(1,101)]

