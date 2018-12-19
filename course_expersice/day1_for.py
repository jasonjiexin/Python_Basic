#-*-coding:utf-8-*-#

#for课堂练习
#range(10)是一个集合，（0，1，2，3，4，5，6，7，8，9）
for i in range(10):
    print(i+1)
print("-------------1---------------")

#list()列表输出
print(list(range(10)))
print(list(range(0, 5)))
print(list(range(0, 5, 2)))
print("------------2----------------")

#()括号中不需要换行符
for a in range(0
        , 11):
    print(10-a)
print("--------------3--------------")


for b in range(10, 0, -1):
    print(b)
print("--------------4--------------")

#continue 跳出当前的该次循环，c%2 打印奇数
for c in range(10):
    if not c%2:
        #continue
        print(c)
print("--------------5--------------")

for d in range(10):
    if d%2==0:
        print(d)
print("--------------6--------------")

for e in range(10):
    if e%2==0:
        continue
        print(e)
print("--------------7--------------")

#与9的代码属于一个意思,9多了一个else
for f in range(10):
    if f%2==0:
        continue
    print(f)
print("--------------8--------------")

for g in range(10):
    if g%2==0:
        continue
    else:
        print(g)
print("--------------9--------------")