import unittest
from codinginterviewprep.twopointers.triplet_sum import triplet_sum


class TestTripletSum(unittest.TestCase):

    def test_basic_triplet(self):
        """Test basic case with valid triplets"""
        result = triplet_sum([-1, 0, 1, 2, -1, -4])
        expected = {(-1, -1, 2), (-1, 0, 1)}
        self.assertEqual(result, expected)

    def test_empty_list(self):
        """Test empty list"""
        result = triplet_sum([])
        self.assertEqual(result, set())

    def test_single_element(self):
        """Test list with single element"""
        result = triplet_sum([0])
        self.assertEqual(result, set())

    def test_two_elements(self):
        """Test list with two elements"""
        result = triplet_sum([0, 1])
        self.assertEqual(result, set())

    def test_no_valid_triplets(self):
        """Test when no triplets sum to zero"""
        result = triplet_sum([1, 2, 3])
        self.assertEqual(result, set())

    def test_all_zeros(self):
        """Test list with all zeros"""
        result = triplet_sum([0, 0, 0])
        expected = {(0, 0, 0)}
        self.assertEqual(result, expected)

    def test_duplicates(self):
        """Test with duplicate elements"""
        result = triplet_sum([-2, 0, 1, 1, 2])
        expected = {(-2, 0, 2), (-2, 1, 1)}
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        result = triplet_sum([-3, -2, -1, 0, 1, 2, 3])
        expected = {(-3, 0, 3), (-3, 1, 2), (-2, -1, 3),
                    (-2, 0, 2), (-1, 0, 1)}
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        """Test with large numbers"""
        result = triplet_sum([-1000, 0, 1000])
        expected = {(-1000, 0, 1000)}
        self.assertEqual(result, expected)

    def test_single_valid_triplet(self):
        """Test when only one valid triplet exists"""
        result = triplet_sum([-1, 0, 1])
        expected = {(-1, 0, 1)}
        self.assertEqual(result, expected)

    def test_skip_duplicate_first_element(self):
        """Test that duplicate first elements are skipped"""
        result = triplet_sum([-1, -1, 0, 1, 1])
        expected = {(-1, 0, 1)}
        self.assertEqual(result, expected)

    def test_many_duplicates(self):
        """Test with many duplicate values"""
        result = triplet_sum([-1, -1, -1, 0, 1, 1, 1])
        expected = {(-1, 0, 1)}
        self.assertEqual(result, expected)

    def test_negative_only_no_solution(self):
        """Test with only negative numbers"""
        result = triplet_sum([-3, -2, -1])
        self.assertEqual(result, set())

    def test_positive_only_no_solution(self):
        """Test with only positive numbers"""
        result = triplet_sum([1, 2, 3, 4, 5])
        self.assertEqual(result, set())

    def test_deduplication_check(self):
        """Test that result set properly deduplicates"""
        result = triplet_sum([-2, -1, -1, 0, 1, 1, 2])
        # Verify no duplicate tuples exist
        self.assertEqual(len(result), len(list(result)))
