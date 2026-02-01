import unittest
from codinginterviewprep.hashmapnssets.two_pair_sum_unsorted import two_pair_sum_unsorted


class TestTwoPairSumUnsorted(unittest.TestCase):

    def test_base_example(self):
        """Test base example from Problem"""
        array = [-1, 3, 4, 2]
        target = 3
        result = two_pair_sum_unsorted(array, target)
        self.assertEqual(result, [(0, 2)])

    def test_empty_array(self):
        """Test with empty array"""
        result = two_pair_sum_unsorted([], 5)
        self.assertEqual(result, [])

    def test_single_element(self):
        """Test with single element - no pair possible"""
        result = two_pair_sum_unsorted([5], 10)
        self.assertEqual(result, [])

    def test_no_pair_exists(self):
        """Test when no pair sums to target"""
        result = two_pair_sum_unsorted([1, 2, 3, 4], 100)
        self.assertEqual(result, [])

    def test_negative_numbers(self):
        """Test with negative numbers"""
        result = two_pair_sum_unsorted([-5, -2, 0, 2, 5], 0)
        self.assertIsNotNone(result)

    def test_duplicates(self):
        """Test with duplicate elements"""
        result = two_pair_sum_unsorted([2, 2, 2, 2], 4)
        self.assertIsNotNone(result)

    def test_zero_target(self):
        """Test with target of zero"""
        result = two_pair_sum_unsorted([-3, 0, 3, 1], 0)
        self.assertIsNotNone(result)

    def test_large_numbers(self):
        """Test with large numbers"""
        result = two_pair_sum_unsorted([1000000, 2000000, 3000000], 3000000)
        self.assertEqual(result, [(0, 1)])

    def test_two_elements_exact_match(self):
        """Test with exactly two elements that match"""
        result = two_pair_sum_unsorted([1, 2], 3)
        self.assertEqual(result, [(0, 1)])

    def test_negative_target(self):
        """Test with negative target"""
        result = two_pair_sum_unsorted([-10, -5, 0, 5, 10], -5)
        self.assertEqual(result, [(1, 2), (0, 3)])
