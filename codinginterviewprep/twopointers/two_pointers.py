# Leet Code Easy
def is_valid_palindrome_retry(string: str) -> bool:
    """
    Time Complexity O(log n) where n is the length of the array
    Space Complexity O(1)
    """

    length = len(string)

    left = 0
    right = length - 1

    while left < right:

        while left < right and not string[left].isalnum():
            left += 1

        while left < right and not string[right].isalnum():
            right -= 1

        if string[left] != string[right]:
            return False

        left += 1
        right -= 1

    return True


print(is_valid_palindrome_retry(string="racecar"))
print(is_valid_palindrome_retry(string="cb"))
print(is_valid_palindrome_retry(string="cbc"))
print(is_valid_palindrome_retry(string="c!bc"))


def pair_sum_sorted_retry(nums: list[int], target: int) -> list[int]:
    """
    Time Complexity O(log n) where n is the length of the nums list
    Space Complexity O(m) where m is the length of the number of index in the nums array that add up to the  
    """
    left = 0
    right = len(nums) - 1

    result = []

    while left < right:

        while (nums[right] + nums[left]) < target:
            left += 1

        while (nums[right] + nums[left]) > target:
            right -= 1

        if nums[right] + nums[left] == target:
            result.append([left, right])

        left += 1
        right -= 1

    return result


print(pair_sum_sorted_retry(nums=[-5, -2, 3, 4, 6], target=7))
print(pair_sum_sorted_retry(nums=[1], target=2))
print(pair_sum_sorted_retry(nums=[], target=2))

# def
