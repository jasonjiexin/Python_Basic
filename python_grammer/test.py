
#-*- coding:utf-8 -*-



for a in range(1, 10):
     for b in range(1, 10):
          print('*'+'  ', end="")
     print()

print("-------------------------------------------------")

for c in range(1, 10):
     for d in range(1, 10):
         if c == 1:
              print('*'+'  ', end="")
         elif c == 2:
              print('*')
     print()