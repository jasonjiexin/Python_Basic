#!/usr/bin/env python
# coding: utf-8

# In[22]:


# datetime 标准库 ，命名空间
import datetime

# 返回当前时间
to = datetime.datetime.today()  # datetime 是命名空间，datetime是类，today（）是方法，返回的是一个对象
print(to)
print(type(to))

# 返回的是当前的时间，没有时区值情况下today() 与 now() 返回的值相同
no = datetime.datetime.now()
print(no)
print(type(no))

#计算机统一时间
uo = datetime.datetime.utcnow()
print(uo)
print(type(uo))

# 时间戳时间，格林威治时间
to = uo.timestamp()
print(to)
print(type(to))

# 格林威治时间转换成datetime类的对象
fo = datetime.datetime.fromtimestamp(to)
print(fo)
print(type(fo))


# In[42]:


# datetime 标准库 ，命名空间
import datetime

# 构造时间后得到的是一个对象，调用相应的方法
tn = datetime.datetime(2016, 12, 1, 16 ,40, 45,234544)
print(tn)
print(type(tn))

fo = tn.timestamp()  #fo是个对象
print(fo)
print(tn.weekday())   #获取周，周从0开始
print(tn.isoweekday())  #获取周，周从1开始，更符合人定义日期的标准
print(tn.date())    #获取日期
print(tn.time())    #获取时间

print('---------------'*8)

tn1 = tn.replace(2019,5,17)  #更新时间后形成新的时间对象
print(tn1)
print(id(tn1))  #新对象与老对象的地址发生了变化
print(type(tn1)) #tn1 是对象，对象调用方法后依然是对象
print(id(tn))
print(tn1.isocalendar())   #对象调用方法
print(tn.replace(2019,5,17).isocalendar())    #对象调用方法后还是对象，还可以继续调用方法

print('---------------'*8)

print(tn.isocalendar())

print('---------------'*8)


# In[2]:


# 日期格式化
 
import datetime

#类方法
#strptime 不管用什么格式输入，输出的都是 年（四位数）/月/日 时/分 
dt = datetime.datetime.strptime("21/06/11 16:30", "%d/%y/%m %H:%M")   # 生成时间对象,Y表示四位数的年份2006，y表示两位数的年份
print(dt)
print(type(dt))

print('---------------'*8)

#对象方法
dt1 = dt.strftime("%Y-%m-%d %H:%M:%S")  #m、d 都是小写
print(dt1)
print(type(dt1))   

# dt1 是一个字符串
print(id(dt))
print(id(dt1))

print('---------------'*8)

dt2 ="{0:%Y}/{0:%m}/{0:%d} {0:%H}::{0:%M}::{0:%S}".format(dt)
print(dt2)
print(type(dt2))

dt3 = "{}/{}/{}".format(dt.year,dt.month,dt.day)
print(dt3)


# In[74]:


# timedelta 对象
import datetime

#构造函数一,构造timedelta 对象用于计算
h = datetime.timedelta(hours=24)
print(h)
print(type(h))

# 构造函数二
year = datetime.timedelta(days=365)
print(year)
print(year.total_seconds())  #365 天经过了多少秒

#datetime对象  减去 timedelta对象 是 datetime对象 
# datetime2 = datetime1 - timedelta
# datetime2 = datetime1 + timedelta
# timedelta = datetime1 - datetime2

time_now = datetime.datetime.now()
time_delta = time_now - h
print(time_delta)
print(type(time_delta))

print('---------------'*8)

time_now = datetime.datetime.now()
time_delta1 = time_now + year    #year 是已经构造好的 timedelta 对象 
print(time_delta1)
print(type(time_delta1))


# In[72]:


# timedelta 对象
import datetime

h = datetime.datetime.now()
print(h)

# 冒泡排序
num_list = [[1,9,8,5,6,7,4,3,2], [1,2,3,4,5,6,7,8,9]]
nums = num_list[0]
print(nums)
length = len(nums)
print(length)
count_swap = 0
count = 0
#bubble sort
#i 为趟数
for i in range(length):
    #j为前后两个元素的编号
    for j in range(length - i -1): #length - i -1 表示每一趟少比较一次，如果不减1列表会超界
        count += 1 #计数的常规做法，意思为比较次数
        if nums[j] > nums[j +1]:
            #数值交换
            tmp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = tmp
            count_swap += 1 #计数常规做法，意思为交换次数
print(nums,  count_swap, count)
            
        
h1 = datetime.datetime.now()

time_delta = h1 - h  # datetime 对象 减去 datetime对象 是 timedelta对象
print(time_delta)
print(time_delta.total_seconds()) #返回时间差的总秒数
print(type(time_delta))

