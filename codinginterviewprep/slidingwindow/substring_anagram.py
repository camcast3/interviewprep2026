def substring_anagram(s, t) -> int:
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
