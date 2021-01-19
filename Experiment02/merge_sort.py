def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # We use the list lengths often, so its handy to make variables
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it
            # to the sorted list
            # 我们检查每个列表开头的哪个值较小,如果左侧列表开头的项目较小，则将其添加到排序列表
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # If the item at the beginning of the right list is smaller, add it
            # to the sorted list
            # 如果右边列表开头的项目较小，则添加它到排序列表
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # If we've reached the end of the of the left list, add the elements
        # from the right list
        # 如果我们已到达左侧列表的末尾，请从右侧列表添加元素
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # If we've reached the end of the of the right list, add the elements
        # from the left list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    # If the list is a single element, return it
    if len(nums) <= 1:
        return nums

    # Use floor division to get midpoint, indices must be integers
    mid = len(nums) // 2

    # Sort and merge each half
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Merge the sorted lists into a new one
    return merge(left_list, right_list)


# Verify it works
random_list_of_nums = [120, 45, 176, 250, 68]
random_list_of_nums = merge_sort(random_list_of_nums)
print(random_list_of_nums)

'''
Here merge_sort() function, unlike the previous sorting algorithms, returns a new list that is sorted, rather than sorting the existing list.
Therefore, Merge Sort requires space to create a new list of the same size as the input list
与以前的排序算法不同，此处的merge_sort（）函数将返回已排序的新列表，而不是对现有列表进行排序。
因此，合并排序需要空间来创建与输入列表大小相同的新列表
'''
