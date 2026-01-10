def triplet_sum(nums):
    """
    Find all unique triplets in the array that sum to zero.

    Where n = len(nums)

    Time Complexity: O(n²)
      - Sorting: O(n log n)
      - Outer loop: O(n) iterations
      - Inner pair_sum_all_elements: O(n) per call (on slice of size ~n)
      - Total: O(n log n) + O(n) * O(n) = O(n²)

    Space Complexity: O(n)
      - Sorting: O(log n) recursive stack space (in-place quicksort)
      - Results set: O(n) in worst case (all unique triplets)
      - Slicing nums[a+1:]: O(n) per iteration (creates new list)
      - Pairs set in pair_sum_all_elements: O(n) worst case
      - Total auxiliary: O(n) excluding output
    """
    nums.sort()
    results = set()

    for a in range(len(nums) - 2):
        if nums[a] > 0:
            break

        if a > 0 and nums[a] == nums[a - 1]:
            continue

        target = -nums[a]
        pairs = pair_sum_all_elements(nums[a+1:], target)

        for pair in pairs:
            results.add(tuple(sorted([nums[a]] + list(pair))))

    return results


def pair_sum_all_elements(nums, target):
    """
    Find all unique pairs in the array that sum to the target.

    Where n = len(nums) (the slice passed in)

    Time Complexity: O(n)
      - Two-pointer traversal: O(n) total (left pointer moves right, right moves left)
      - Each set operation: O(1) amortized
      - Total: O(n)

    Space Complexity: O(n)
      - Pairs set: O(n) worst case (stores all valid pairs)
      - No other auxiliary structures
      - Total: O(n) for output only
    """
    if len(nums) <= 1:
        return set()

    pairs = set()
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            pair = tuple(sorted([nums[left], nums[right]]))
            pairs.add(pair)
            left += 1
            right -= 1

        elif sum < target:
            left += 1
        else:
            right -= 1

    return pairs
