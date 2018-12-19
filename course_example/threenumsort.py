#构造一个用户输入的函数
nums = []
for i in range(3):
    nums.append(int(input('{}:'.format(i))))

if nums[0] > nums[1]:
    if nums[0] > nums[2]:
        if nums[1] < nums[2]:
            i1 = nums[0]
            i2 = nums[2]
            i3 = nums[1]
        else:
            i1 = nums[0]
            i2 = nums[1]
            i3 = nums[2]
    else:
        i1 = nums[2]
        i2 = nums[0]
        i3 = nums[1]
else:
    if nums[0] < nums[2]:
        if nums[1] > nums[2]:
            i1 = nums[1]
            i2 = nums[2]
            i3 = nums[0]
        else:
            i1 = nums[2]
            i2 = nums[1]
            i3 = nums[0]
    else:
        i1 = nums[1]
        i2 = nums[0]
        i3 = nums[2]

print(i1, i2 ,i3)