#!/usr/bin/env python
# coding: utf-8

# In[48]:


# 字典的基本格式表示
d0={}
print(d0)
d3=dict()   #用函数定义空集合的方式 ， 通常情况下我们使用符号直接定义空集合d0={}
print(d3)

#用key=name 构造字典
#d4=dict(a=1,b=2,c=3,1='tom')   dict()定义字典的时候key值不能是数字
d4=dict(a=1,b=2,c=3)
print(d4)

#用可迭代对象初始化字典
e=enumerate(range(4))
d5=dict(e)
print(d5)

#用键值对、键值映射来构造字典
d1={'tom': 29}
print(d1)
print(len(d1))

d2={1:'car',2:'bus'}
print(d2)
print(len(d2))

#使用 dict.fromkeys() 函数来构造字典
d6=dict.fromkeys(range(5))   #迭代的的对象只是用来做key
d7=dict.fromkeys(range(5),'jason')
print(d6)
print(d7)


# In[3]:


# 字典的键、值设置要求
d3={1:'car',2:'bus',2:'bus'}
print(d3)
print(len(d3))   #重复元素归为1

d4={1:'car',2:'bus',2:'train'}
print(d4)    # 两个键值相等，只保留最后一个元素
print(len(d4))


# In[56]:


#字典元素的增加
d1={'Tom':2,'Jim':5}
print(d1)

#利用赋值给字典新增元素，d[key]=value
d1['Mike']=8   #字典新增元素，‘Mike’：8,如果key不存在增加新的kv对
print(d1)

d1['Mike']=7   #字典中如果该值存在则对以前的值进行覆盖
print(d1)


# 利用setdefault()增加元素
d1.setdefault('Alice',10)
print(d1)

d1.setdefault('jason')   #当不指定key的value值时，value值默认为None
print(d1)


# In[78]:


#字典的查找

# 字典名+[key],key是什么类型就用什么类型访问
d1=dict(([(1,2,3),{1,3,5,6}],))
print(d1)
print(d1[(1,2,3)])
# print(d1[(1,4,3)]) 没有该值报错keyerror

d2={'red':1,'green':2,'yellow':3}
print(d2['red'])   #打印键值 "red"
#print(d2['color'])   当没有这个键值的时候，显示keyError

# get(key[,default]) 方法
print(d2.get('green'))   #get 获取 “green值”
print(d2.get('color'))    #如果没有该键值，返回None值
print(d2.get('color','black'))  #设置了缺省值后如果没有key，返回缺省值
print(d2)

d3=dict(([(1,3,4),{1,3,5,6}],))
print(d3)
print(d3[(1,3,4)])
# print(d3[(1,4,3)])  没有所谓的key值，报错
print(d2.get(1,50))  #返回默认值，有key值就返回相应的value

#setdefault(key[,default]) 返回key值的value值，如果key值不存在添加kv对，value值为默认值，如果没有default值显示None
f=d3.setdefault(4,400)
print(f)
print(d3)
f1=d3.setdefault(4,401)  #如果default值存在，value值不发生覆盖
print(f1)
print(d3)


# In[86]:


#字典值修改

# 利用赋值修改键值对应的值
d1={'Tom':2,'Jim':5,'Mike':8}
print(d1)
d1['Mike'] = 9
print(d1)
d1['jason'] = 10    # 如果没有该键值，新增键值和值
print(d1)


# 利用update()
# 更新字典里键对应的值，使用字典来更新字典
d2 = {'Tom':10,'Mike':11}
d1.update(d2)
print(d1)
# 新增键值对
d1.update({'jack':12})
print(d1)

d1.update(red=1)
print(d1)
d1.update((('black',2),)) # 二元结构
print(d1)
d1.update(({'blue',13},))
print(d1)


# In[46]:


# 字典元素删除

d1 = {'Tom':10,'Jim':5,'Mike':11,'Jack':12}
print(d1)

# 利用del函数删除，删除对象
del(d1['Jim'])
print(d1)


# 利用pop()方法删除
p1 = d1.pop('Mike')
print(p1)
print(d1)

# 利用popitem()方法删除
d1 = {'Tom':10,'Jim':5,'Mike':11,'Jack':12}
print(d1)
k1,v1 = d1.popitem()  #封装和解封装这里用的比较多
print(k1,v1)
print(d1)

t1 = d1.popitem()
print(t1)    #返回一个元组形式的键值对
type(t1)  #元组类型


# 如果没有值得时候都会报错
# del(d1['Jason'])    KeyError
# p1 = d1.pop('Jason')  KeyError
# t1 = d1.popitem('Jason')   TypeError
# print(d1)
# print(p1)
# print(t1)


# In[64]:


# 引用类型能够就地修改，但是数值类型不能够就地修改
# 引用类型：列表对象是可以修改的，修改后lst的空间地址不会发生变化
lst=[1,2,3]  #新值一定会开辟一个新的空间，修改是在原值上就地修改
print(id(lst))
lst[0]=2
print(id(lst))
lst1=lst
print(id(lst1))

# 数值型值修改变化后，空间地址会发生变化，指向一个新的地址
a=1   
b=2
c=2
print(id(a))
print(id(b))
print(id(c))


# In[103]:


# del（）删除
# del 删除的只是一个标识（变量），但是引用如果还有其他标识在用，则该地址和值还在
# 引用类型有一个引用计数，是可增加和可减少的
a=True
b=[6]
d={'a':1,'b':b,'c':[1,3,5]}  #b为一个引用，c是一个对象，元素就是对象
print(a)
print(b)
print(d)

del a  #删除了数值型值
# print(a)   该表示报错没有定义

del d['c']  #删除对象
print(d)

del b[0]   #修改了b[]列表,b更改后使用该引用类型的值都会发生变化
print(b)
print(d)

c=b  #使用b引用类型
print(c)
del c
# print(c) #删除标识后，c标识报错没有定义
print(b) #c标识被删除后，b标识并没有被影响

del b  #删除标识后
# print(b) b标识报错没有定义
b=d['b']  #d['b']就是最开始的b变量（标识）所代表的引用类型，因为一直有这一个引用存在，所以该引用一直存在，不管删除多少个引用对应的变量
print(b)


# In[2]:


# 字典的遍历

d1={'Tom':1,'Jason':2,'Mary':12,'Frank':4}
print(d1)

# 对key值得遍历
for k in d1:  #默认取key值
    print(k)
for k in d1.keys():
    print(k)
print("---------")
# 对 value值得遍历 ,通过 k值 来获取相应的 value 值
for k in d1:
    print(d1[k])
for k in d1.keys():
    print(d1.get(k))
print("----------")    

for item in d1.keys():
    print(item)
for item in d1.values():
    print(item)


# In[8]:


# 字典的遍历
# keys、values、items 返回的是一个生成器的可迭代对象，不会把函数的结果复制内存中

# 遍历所有的键值对
d1={'Tom':10,'Jim':5,'Mike':11,'Jack':12}
print(d1)

print('------------------------')

for get_L in d1.items():     #循环获取元组
    print(get_L)       #打印获取元组
    
print(d1.items())   #执行d1的 items() 方法
type(d1.items())    #结果是一个功能或方法类

print('------------------------')

for k,v in d1.items():   #循环获取元组,这里运用到解构的知识
    print(k,v)
print(v)

for k,_ in d1.items():   # 解构的另一种写法
    print(k)

print('------------------------')

# 遍历所有的键
    # 利用字典变量循环遍历
for gets in d1:
    print(gets)

print('------------------------')
    
   # 利用keys()方法获取字典键
for get1 in d1.keys():
    print(get1)

print('------------------------')

# 遍历所有的值
    #通过键值遍历
for get_key in d1:
    print(d1[get_key])    #d1[get_key]  访问值
    
print('------------------------')    
    
    #利用values（）方法获取自己值
for get_value in d1.values():
    print(get_value)
    
print('------------------------')


# In[43]:


# 字典的其他操作

# in 成员操作
d1={'Tom':10,'Jim':5,'Mike':11,'Jack':12}
print(d1)

if 'Jim' in d1.keys():
    print('Jim 在键集合内')
else:
    print('Jim 不在键集合内')
    
if 10 in d1.values():
    print('10 在键集合内')
else:
    print('10 不在键集合内')
    
print('-------------------------------')

#clear()  方法  , 删除字典中全部的元素
d2={'OK':1,'莫名其妙':2,222:3}
print(d2)

d2.clear()
print(d2)

print('-------------------------------')

# copy()  方法，复制字典,只复制值不复制引用
d2={'OK':1,'莫名其妙':2,222:3}
d3=d2.copy()       # 复制后是将内容进行复制，而不是引用地址
print(d3)
print(id(d3))         # 复制后的值d3与d2相同，地址不同
print(id(d2))

print('-------------------------------')

# 复制引用和值
d4=d2
print(d4)
print(id(d4))
print(id(d2))    # 两个地址是一样的

print('-------------------------------')

#  更改d2后看d3、d4 的变化
d2['OK']=100
print(d3)   #  d3是只复制了字典的值，值等于原来的值
print(d4)   # d4复制了字典的地址，因此值与d2保持一致


print('-------------------------------')

# fromkeys() 方法
d5={}.fromkeys(['Prel','rule','paper'],1)   #给定键值不给定默认值的情况下，默认值为None
print(d5)


# In[49]:


# 字典嵌套
   #字典嵌入字典
no1={'张三':35.5,'李四':200,'王五':800}
no2={'Tom':99.8,'John':183,'Jim':429}
no3={'阿毛':12,'阿狗':33}
rest={'1号':no1,'2号':no2,'3号':no3}
print(rest) 

print('-------------------------------')

total=0
for get_values in rest.values():
    total=total+sum(get_values.values())
print(total)
print('餐厅今天的营业额:%.2f'%(total))


# In[5]:


'''
案例——记录每天的钓鱼记录
'''
# 每天钓鱼的记录
d_date1={'鲫鱼':[18,10.5],'鲤鱼':[8,6.2],'鲢鱼':[7,4.7]}
d_date2={'草鱼':[2,7.2],'鲫鱼':[3,12],'黑鱼':[6,15]}
d_date3={'乌龟':[1,71],'鲫鱼':[1,9.8],'草鱼':[5,7.2],'黄鱼':[2,40]}

#钓鱼的全部记录，不同日期的记录
# 字典嵌套字典，字典里还可以嵌套列表，为了存储更多的数据
fish_records = {'1月1日':d_date1,'1月2日':d_date2,'1月3日':d_date3}

#变量初始化
nums = 0    #记录钓鱼的总数变量初始化
amount = 0  #记录钓鱼的总金额变量初始化
day=''     #日期变量初始化
day_record = {}   #钓鱼记录变量初始化

for day,day_record in fish_records.items():    #从总记录中把日期和钓鱼记录分别取出来
    print('%s 钓鱼记录为:' % day)      # 打印出每日钓鱼数量的标题
    for name,sub_recods in day_record.items():    #从每日钓鱼记录中把鱼的名称、[数量,单价]取出来
        nums+=sub_recods[0]   #累加钓鱼的总数量
        amount+=sub_recods[0]*sub_recods[1]   #累加钓鱼的总金额
        print('%s数量%d,单价%.2f元'%(name,sub_recods[0],sub_recods[1]))   #打印出每日钓鱼的记录
        
print('钓鱼总数量为%d,总金额为%.2f元'%(nums,amount))   #打印出总记录

