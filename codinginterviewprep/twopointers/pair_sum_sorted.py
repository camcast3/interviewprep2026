def pair_sum_sorted(nums, target):
    """
    Find a pair of indices in a sorted array that sum to the target.

    Where n = len(nums)

    Time Complexity: O(n)
      - Edge case check: O(1)
      - Two-pointer traversal: O(n) - left pointer moves right, right pointer moves left
      - Each comparison and pointer movement: O(1)
      - Worst case: pointers traverse entire array without finding pair
      - Total: O(n)

    Space Complexity: O(1)
      - Only uses two pointer variables (left_pointer_index, right_pointer_index)
      - No additional data structures
      - Return array is constant size [index1, index2]
      - Total: O(1) - constant auxiliary space
    """
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
