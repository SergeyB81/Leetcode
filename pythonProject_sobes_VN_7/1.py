def move_zeros(nums):
    insert_pos = 0

    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1
    return nums

nums = test_list = [1, 2, 3, 0, 0, 4, 0, 5]
print(move_zeros(test_list))


def