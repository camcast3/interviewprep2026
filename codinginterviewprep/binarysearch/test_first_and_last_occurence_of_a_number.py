import unittest
from codinginterviewprep.binarysearch.first_and_last_occurence_of_a_number import first_and_last_occurence_of_a_number


class TestFirstAndLastOccurenceOfANumber(unittest.TestCase):

    def test_example_1(self):
        nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11]
        target = 4

        result = first_and_last_occurence_of_a_number(nums, target)
        self.assertEqual([3, 5], result)
