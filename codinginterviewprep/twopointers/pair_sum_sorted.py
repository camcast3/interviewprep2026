def pair_sum_sorted(nums, target):
    # What happens when nums is an empty array
    if (len(nums) <= 1):
        return ([])

    left_pointer_index = 0
    right_pointer_index = len(nums) - 1

    while True:
        if (left_pointer_index == right_pointer_index):
            break

        sum = nums[left_pointer_index] + nums[right_pointer_index]

        if (sum > target):
            right_pointer_index -= 1

        elif (sum < target):
            left_pointer_index += 1

        elif (sum == target):
            return ([left_pointer_index, right_pointer_index])

    return ([])

# time complexity O(len(nums))
# space complexity O(1)
