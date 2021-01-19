def partition(nums, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    # 我们选择中间元素作为枢轴，一些实现选择第一个元素或最后一个元素，
    # 有时中间值变成枢轴，或随机的一个。 还有更多的策略可以选择或创建。
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    # 最终左边小于pivot，右部大于pivot
    while True:
        i += 1
        while nums[i] < pivot: # 找到不小于划分的值
            i += 1

        j -= 1
        while nums[j] > pivot: # 找到不大于划分的值
            j -= 1

        if i >= j: # 直到i>=j一轮结束，返回划分元素的下标
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i] # 交换


def quick_sort(nums):
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high) # 根据划分，左边小，右部大于划分
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


# Verify it works
random_list_of_nums = [22, 5, 1, 18, 99]
quick_sort(random_list_of_nums)
print(random_list_of_nums)
