#-*- coding:utf-8 -*-

#当flag值为-10的时候，flag永远没有为0的时候，判断条件永远不为假，因此系统进入死循环中，以下为改造过程
flag = -10
while flag:
    print(flag)
#让每个数字都加上1不断的接近0
    flag += 1