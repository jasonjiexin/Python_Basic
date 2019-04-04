#if嵌套功能，实现判断一个数字是否是一个正确的成绩
#score = 100

#输入一个分数
score = int(input('score='))
if score < 0:
    print('wrong')
else:
    if score == 0:
        print('egg')
    elif score <= 100:
        print('right')
    else:
        print('too big')
