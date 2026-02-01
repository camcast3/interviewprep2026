def solution(s):
    """
    Your task is to write a Python function that takes in a string and identifies all the 
    consecutive groups of identical characters within it, with the analysis starting from the 
    end of the string rather than from its beginning. A group is defined as a segment of the 
    text where the same character is repeated consecutively.

    Your function should return a list of tuples. Each tuple will consist of the repeating 
    character and the number of its repetitions. For instance, if the input string is 
    "aaabbcccdde", the function should output: [('e', 1), ('d', 2), ('c', 3), ('b', 2), ('a', 3)].

    Time Complexity: O(n) - single pass through the string
    Space Complexity: O(n) - result list stores up to n characters
    """
    result = []
    i = len(s) - 1

    while i >= 0:
        current_char = s[i]
        count = 0

        while i >= 0 and s[i] == current_char:
            count += 1
            i -= 1

        result.append((current_char, count))

    return result
    pass
