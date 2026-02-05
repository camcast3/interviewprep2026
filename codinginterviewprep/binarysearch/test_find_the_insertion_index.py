import unittest
from codinginterviewprep.binarysearch.find_the_insertion_index import find_the_insertion_index


class TestFindTheInsertionIndex(unittest.TestCase):

    def test_example_1(self):
        nums = [1, 2, 4, 5, 7, 8, 9]
        target = 6

        result = find_the_insertion_index(nums, target)
        self.assertEqual(4, result)

    def test_example_2(self):
        nums = [1, 2, 4, 5, 7, 8, 9]
        target = 4

        result = find_the_insertion_index(nums, target)
        self.assertEqual(2, result)
