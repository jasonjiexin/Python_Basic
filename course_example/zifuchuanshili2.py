
num = ""
while True:
    # 输入一个整数去除整数头部和尾部的空字符
    num = input("please input a interger:").strip()
    # 判断是否是十进制的数字0~9，不包括其他的字符
    if num.isdigit():
        break
    else:
        print("Bad number")

counter = [0] * 10
for i in range(10):
    counter[i] = num.count(str(i))
    if counter[i]:
        print(i, counter[i])

# print(num)

