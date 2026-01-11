def largest_container_slow(heights):
    """
    n = len(heights)
    Time complexity: O((n - 1) log (n - 1))
    Space complexity: O(1)
    """
    left = 0
    max_water = 0
    right = left + 1

    while left != len(heights) - 1:
        current_water = min(heights[left], heights[right]) * (right - left)

        max_water = max(max_water, current_water)

        if right + 1 > len(heights) - 1:
            left += 1
            right = left + 1

        else:
            right += 1

    return max_water


def largest_container(heights):
    """
    n = len(heights)
    Time complexity: O(n)
    Space complexity: O(1)
    """
    left = 0
    max_water = 0
    right = len(heights) - 1

    while left < right:
        current_water = min(heights[left], heights[right]) * (right - left)

        max_water = max(max_water, current_water)

        if heights[left] < heights[right]:
            left += 1

        elif heights[left] > heights[right]:
            right -= 1

        else:
            left += 1
            right -= 1

        # print('Water ', max_water, '\n')
        # print('Left ', left, '\n')
        # print('Right ', right, '\n')

    return max_water


def main():
    heights_list = [
        [2, 7, 8, 3, 7, 6],
        [],
        [1],
        [0, 1, 0],
        [3, 3, 3, 3],
        [1, 2, 3],
        [3, 2, 1]
    ]

    for heights in heights_list:
        water = largest_container(heights)
        print(heights, '-> Water', water)


if __name__ == '__main__':
    main()
