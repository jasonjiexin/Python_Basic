#!/usr/bin/env python
# coding: utf-8

# # 生成器

# ### 1.生成器表达式

# In[3]:


# 列表解析式
[x for x in range(10)]


# In[5]:


# 生成器表达式
(x for x in range(10))


# In[7]:


# 列表解析式与生成器表达式嵌套使用
# 生成器一定是可迭代对象
[i for i in (x for x in range(10))]


# In[16]:


# 列表解析式，可以循环迭代
g = ["{:04}".format(i) for i in range(1,11)]

for x in g:
    print(x)
    
print('~~~~~~~~~~~~~~~~~')

for x in g:
     print(x)


# In[18]:


# 生成器表达式，不可以循环迭代
g = ("{:04}".format(i) for i in range(1,11))

next(g)   # 按顺序剔除掉生成器中的元素
next(g)

for x in g:  #  除剔除掉的元素外的所有元素
     print(x)
    
print('~~~~~~~~~~~~~~~~~')

for x in g:   #   使用过的元素就没有了，从头走到尾只能走一遍不能够回头
     print(x)


# In[26]:


#first、second 相加的值是什么？
# 以下表达方式使用了 print（）函数，返回值为none，也就是没有返回值
it = (print('{}'.format(i+1)) for i in range(2))
first = next(it)
print(first)
second = next(it)

val = first + second   #两个none值是不能够相加的,因此会报错


# In[32]:


#first、second 相加的值是什么？
# 以下这种表达val是个字符串，相当于first、second两个字符串的连接
it = ('{}'.format(i+1) for i in range(2))
first = next(it)
second = next(it)

val = first + second
print(val)   #打印是忽略数据类型的
val


# In[1]:


# 当迭代器中的元素被用完后，再进行取值时系统会报错，显示迭代器已停止StopIteration
it = ('{}'.format(i+1) for i in range(2))
first = next(it)
second = next(it)

val = first + second 
next(it)  #next（）中是不具有指针的，但是超界后依然会报错


# In[11]:


it = [x for x in range(10) if x % 2]  # 取奇数
print(it)

it = (x for x in range(10) if x % 2) # x 为整数
first = next(it)
second = next(it)
val = first + second
val


# In[6]:


# 验证生成器表达式的运算速率比列表解析式时间快
get_ipython().run_line_magic('timeit', '(x for x in range(100))')
get_ipython().run_line_magic('timeit', '[x for x in range(100)]')


# ### 2.集合解析式

# In[8]:


{(x,x+1) for x in range(10)}


# In[10]:


# 字典中的元素是要可以hash的，list是不能够hash的值
{[x] for x in range(10)}


# ### 3.字典解析式

# In[12]:


# 返回int，tuple类型的数据值
{x:(x,x+1) for x in range(10)}


# In[14]:


# 返回int，list类型的数据值
{x:[x,x+1] for x in range(10)}


# In[16]:


# 返回tuple，list类型的数据值
{(x,):[x,x+1] for x in range(10)}


# In[19]:


# list类型是不可hash的，所以不能够当做key值
{[x]:[x,x+1] for x in range(10)}


# In[22]:


# 0x41 十六进制数，表示“A”，chr（）将数字转换为字符 
{chr(0x41 + x):x**2 for x in range(10)}


# In[24]:


# 字典类型是一个映射类型，key值相同的时候只显示最后一个数据，前面的都被覆盖了
{str(x):y for x in range(3) for y in range(4)}

