def first_and_last_occurence_of_a_number(nums: list[int], target: int) -> list[int]:

    lower_bound_index = lower_bound_search(nums, target)
    upper_bound_index = upper_bound_search(nums, target)

    return [lower_bound_index, upper_bound_index]


def lower_bound_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums)

    while left < right:

        mid = (right + left) // 2

        if nums[mid] > target:
            right = mid - 1

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid

    return left


def upper_bound_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums)

    while left < right:

        mid = (right + left) // 2 + 1

        if nums[mid] > target:
            right = mid - 1

        elif nums[mid] < target:
            left = mid + 1

        else:
            left = mid

    return right
