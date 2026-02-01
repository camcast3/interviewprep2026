def two_pair_sum_unsorted(array, target):
    # Time Complexity: O(n) - single pass through the array
    # Space Complexity: O(n) - hash map stores up to n elements
    hash_map = {}
    result = []
    length = len(array)

    for i in range(length):
        x = target - array[i]
        print(x)
        if x in hash_map:
            result.append((hash_map[x], i))
            print("x is seen")
        hash_map[array[i]] = i

    print(hash_map)
    return result
