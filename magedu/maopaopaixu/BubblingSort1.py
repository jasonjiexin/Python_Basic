num_list = [
    [1, 9, 8, 5, 6, 7, 4, 3, 2],
    [1, 2, 3, 4, 5, 6, 7, 9, 8],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
]
nums = num_list[1]
print(nums)
length = len(nums)
count_swap = 0
count = 0
'''优化算法：每一趟数据的比较中如果有数据的交换则认为是数据还没有排序结束，如果没有数据交换表示数据已经排序完成可以跳出了，目标是避免一个列表的排序
已经完成，但是根据规则循环的趟数为length，每一趟数据比较的次数都是-1的'''
for i in range(length):
    flag = False
    for j in range(length - i - 1):
        count += 1
        if nums[j] > nums[j+1]:
            tmp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = tmp
            flag = True
            count_swap += 1

    if not flag:
        break
print(nums,  count_swap, count)

'''count 为遍历次数，最差的排序情况是需要的列表与实际的列表完全相反，最好的排序情况是需要的列表和实际的列表尽可能的相同，
最多的遍历情况计算公式：1、2........n-1的和(n(n-1)/2), 最少的遍历情况是n-1'''