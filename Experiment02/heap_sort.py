# 调整堆
def heapify(nums, heap_size, root_index):
    # Assume the index of the largest element is the root index
    # 假设最大元素的索引是根索引
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index, and the element is greater
    # than the current largest element, then update the largest element
    # 如果根的左孩子是有效索引，并且元素更大比当前最大元素大，那么更新最大元素
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # Do the same for the right child of the root
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # If the largest element is no longer the root element, swap them
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)
    # Create a Max Heap from the list
    # The 2nd argument of range means we stop at the element before -1 i.e.
    # the first element of the list.
    # The 3rd argument of range means we iterate backwards, reducing the count
    # of i by 1
    # e.g list(range(0, -10, -1))
    # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

    # 从堆的最后一个开始，依次向前进行堆的调整，建立最大堆
    for i in range(n, -1, -1):  # [5,-1)
        heapify(nums, n, i)

    # Move the root of the max heap to the end of
    for i in range(n - 1, 0, -1): # [4,-1)
        # 交换头尾，取出头即为最大值；将剩下四个进行堆调整
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


# Verify it works
random_list_of_nums = [35, 12, 43, 8, 51]
heap_sort(random_list_of_nums)
print(random_list_of_nums)
