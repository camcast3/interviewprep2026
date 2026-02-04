def longest_substring_with_unique_charaters(s: str) -> int:
    """
    Time Complexity: O(n) due to while loop O(n) + hash set traversal O(1)
    Space Complexity: O(m) the length of the longest substring getting stored in the hash_set
    """
    string_length = len(s)

    if string_length < 1:
        return 0

    if string_length == 1:
        return 1

    hash_set = set()
    max_length = 0
    left = right = 0

    while right < string_length:

        while s[right] in hash_set:
            hash_set.remove(s[left])

            left += 1

        max_length = max(max_length, right - left + 1)
        hash_set.add(s[right])

        right += 1

    return max_length


def longest_substring_with_unique_charaters_brute_force(s: str) -> int:
    """
    Time Complexity: O(n^2) 
    Space Complexity: O(n)
    """
    string_length = len(s)

    if string_length < 1:
        return 0

    if string_length == 1:
        return 1

    left = right = 0
    current_substring = ""
    current_count = 0
    max_count = 0

    while right < string_length:

        if s[right] in current_substring:
            current_count -= 1
            left += 1
        else:
            current_count += 1

        current_substring = s[left:right]
        right += 1
        max_count = max(max_count, current_count)

    return max_count
