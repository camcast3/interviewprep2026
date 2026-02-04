# Current Implementation is O(n^2)

def substring_anagram_worst(s, t) -> int:
    window_size = len(t)
    string_length = len(s)

    if window_size > string_length:
        return 0

    left = 0
    right = window_size
    output = 0

    while right < string_length + 1:
        if is_anagram(s[left:right].lower(), t.lower()):
            output += 1

        left += 1
        right += 1
    return output


def is_anagram(sub, t) -> bool:
    freq = [0] * 26

    for c in sub.lower():
        freq[ord(c) - ord('a')] += 1
    for c in t.lower():
        freq[ord(c) - ord('a')] -= 1

    return all(v == 0 for v in freq)


def substring_anagram(s, t) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    window_size = len(t)
    string_length = len(s)
    count = 0

    if window_size > string_length:
        return count

    expected_freqs, window_freqs = [0] * 26, [0] * 26
    s = s.lower()
    t = t.lower()

    for c in t:
        expected_freqs[ord(c) - ord('a')] += 1

    left = right = 0

    while right < string_length:
        window_freqs[ord(s[right]) - ord('a')] += 1

        if right - left + 1 == window_size:
            if expected_freqs == window_freqs:
                count += 1

            window_freqs[ord(s[left]) - ord('a')] -= 1
            left += 1

        right += 1

    return count
