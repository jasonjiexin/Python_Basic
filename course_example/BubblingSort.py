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
