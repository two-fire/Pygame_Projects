def insertion_sort(nums):
    # Start on the second element as we assume the first element is sorted
    # 从第二个元素开始，因为我们假设第一个元素已排序
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # And keep a reference of the index of the previous element
        # 并保留前一个元素的索引的引用
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than the item to insert
        # 如果它们大于插入项的项，则将排序段的所有项向前移动
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Insert the item
        nums[j + 1] = item_to_insert


# Verify it works
random_list_of_nums = [9, 1, 15, 28, 6]
insertion_sort(random_list_of_nums)
print(random_list_of_nums)
