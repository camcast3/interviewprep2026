def triplet_sum(nums):
    tempArrayList = nums.sort()  # O(len(num) * log len(num))?
    tuple = set()

    a = 0
    b = a + 1
    c = len(nums) - 1

    while True:
        break
    return ([])


def pair_sum_all_elements(nums, target):
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
            return ([nums[left_pointer_index], nums[right_pointer_index]])

    return ([])
