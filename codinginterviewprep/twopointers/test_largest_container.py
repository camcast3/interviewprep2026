import unittest
from codinginterviewprep.twopointers.largest_container import largest_container


class TestLargestContainer(unittest.TestCase):

    def test_base_example(self):
        """Test base example from Problem"""
        heights = [2, 7, 8, 3, 7, 6]
        result = largest_container(heights)
        self.assertEqual(result, 24)
