def solution(s):
    """
    In this task, you need to write a Python function that finds repeating two-character patterns in a string. The function should identify when the same pair of characters appear next to each other in the string and count how many times each pair repeats consecutively.

    The function should return a new string that lists each pair followed by the number of times it repeats consecutively. For example, let's break down the input string "aaabbabbababacab":

    Divide the string into pairs:

    "aa"
    "ab"
    "ba"
    "bb"
    "ab"
    "ab"
    "ac"
    "ab"
    Note the consecutive pairs:

    "ab" appears twice consecutively in the middle.
    Therefore, the output string will be: "aa1ab1ba1bb1ab2ac1ab1".

    Similarly, for the input string "aaababbababaca", the output should be "aa1ab2ba3ca1".
    """
    length = len(s)
    result = ""
    i = 0

    while i < length:
        pair = s[i:i+2]  # Extract 2-character substring
        count = 0

        while i < length and pair == s[i:i+2]:
            count += 1
            i += 2

        result += f"{pair}{count}"

    print(f"Final result: {result}\n")
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("aaabbabbababacab", "aa1ab1ba1bb1ab2ac1ab1"),
        ("aaababbababaca", "aa1ab2ba3ca1"),
    ]

    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = solution(input_str)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status}")
        print(f"  Input:    {input_str}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print()
