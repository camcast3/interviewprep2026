import pytest
from codinginterviewprep.twopointers.pair_sum_sorted import pair_sum_sorted


class TestPairSumSorted:
    """Tests for the two-pointer pair sum solution."""

    # Basic functionality tests
    def test_finds_pair_at_ends(self):
        nums = [-5, -2, 3, 4, 6]
        target = 1  # -5 + 6 = 1
        result = pair_sum_sorted(nums, target)
        assert nums[result[0]] + nums[result[1]] == target

    def test_finds_pair_in_middle(self):
        nums = [-5, -2, 3, 4, 6]
        target = 7  # 3 + 4 = 7
        result = pair_sum_sorted(nums, target)
        assert nums[result[0]] + nums[result[1]] == target

    def test_finds_pair_with_duplicates(self):
        nums = [1, 1, 1]
        target = 2  # 1 + 1 = 2
        result = pair_sum_sorted(nums, target)
        assert nums[result[0]] + nums[result[1]] == target

    # Edge cases
    def test_two_element_array(self):
        nums = [1, 4]
        target = 5
        result = pair_sum_sorted(nums, target)
        assert nums[result[0]] + nums[result[1]] == target

    def test_negative_numbers(self):
        nums = [-10, -5, -3, 0, 2]
        target = -8  # -10 + 2 = -8
        result = pair_sum_sorted(nums, target)
        assert nums[result[0]] + nums[result[1]] == target

    def test_no_pair_exists_high(self):
        nums = [1, 2, 3, 4]
        target = 100
        result = pair_sum_sorted(nums, target)
        assert result == []

    def test_no_pair_exists_low(self):
        nums = [1, 2, 3, 4]
        target = -100
        result = pair_sum_sorted(nums, target)
        assert result == []

    def test_no_pair_exists_nums_empty(self):
        nums = []
        target = 50
        result = pair_sum_sorted(nums, target)
        assert result == []
