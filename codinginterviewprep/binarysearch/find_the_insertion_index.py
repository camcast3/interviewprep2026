def find_the_insertion_index(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity; O(1)
    """

    length = len(nums)

    left = 0
    right = length

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1

        elif nums[mid] >= target:
            right = mid

    return left
