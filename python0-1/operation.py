#!/usr/bin/env python
# coding: utf-8

# In[9]:


'''
加、减、乘、除
'''
num1 = 10     #第一个整数变量
num2 = 3      #第二个整数变量
count = num1+ num2     # 两个变量的和
print('加法和为:%d'%(count))

print('减法差为:%d'%(num1 - num2))   #减法

print('乘法积为:%d'%(num1 * num2))   #乘法

print('除法和为:%d'%(num1 / (num2 + 2))) #除法

result = (num1 + num2)*(num1-num2)/7-3 #混合运算
print('混合运算:%d'%(result))


# In[11]:


'''
取模、幂、取整除
'''

x = 5
y = 3
print(x % y)   #取模
print(x // y)   #整除
print(x ** y)   #幂


# In[1]:


'''
浮点数
'''
print(10.0/3)    #该浮点数就是一个近似的结果

# 计算公式中如果有一个浮点数，结果也一定是浮点数
print(10*2 + 0.1)
print(1.1+0.9)
print(4.0/2.0)


# In[6]:


'''
复数
'''

print((1-2j)) # 复数的表示
print((1-2j)*(2-3j)) #复数的乘法

print((1-2j).real)   #显示实部
print((1-2j).imag)  #显示虚部


# In[11]:


'''
布尔值
'''
print(True)  #True 必须大写
# print(true) 错误的写法

print(True and True)
print(True or False)
print(not False)


# In[1]:


'''
二进制、及二进制运算
'''
print(0b1110)   #输出十进制
print(bin(14))    #十进制转换为二进制
print(bin(97))


# In[13]:


'''
比较运算符-整数
'''

age1,age2,age3=10,9,0o12

#比较值都是boolean 值
print(age1 == age3) #十进制和八进制数字进行比较，现将八进制转化为十进制再进行比较
print(age1 == age2)
print(False == True) #boolean值进行比较
print(3 == 3.0) #整数和浮点数之间的运算比较
print(5-2j == 5+2j)  #复数之间的比较
print(0b01101110 == 0b01101111) #二进制之间的比较


# In[18]:


'''
比较运算符-整数
'''

age1,age2,age3=10,9,0o12

print(age1 != age2)  #不等于
print(age1 >= age2) #大于等于
print(age1 <= age2) #小于等于
print(age1 > age2) #大于
print(age1 < age2) #小于


# In[24]:


'''
比较运算符-字符串
'''

print('a' == 'b')   #字符串之间的比较是ascii码之间的比较
print('ab'== 'ab')
print('a' == 1)
# print('a' > 1)   TypeError: unorderable types: str() > int(),不同类型之间是不能够相互比较大小的


# In[28]:


'''
比较运算符-优先级
'''
print(5+1>5 and True)  #运算优先级，先算数学运算符，然后再算比较运算符，最后算逻辑运算符
print((5+1)*2>5 and True)

