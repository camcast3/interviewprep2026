import unittest
from codinginterviewprep.slidingwindow.longest_substring_with_unique_charaters import longest_substring_with_unique_charaters


class TestLongestSubstringWithUniqueCharaters(unittest.TestCase):

    def test_simple_string(self):
        string = "abcba"
        result = longest_substring_with_unique_charaters(string)

        self.assertEqual(3, result)

    def test_case_sensitivity(self):
        string = "AbcBa"
        result = longest_substring_with_unique_charaters(string)

        self.assertEqual(5, result)

    def test_empty_string(self):
        string = ""
        result = longest_substring_with_unique_charaters(string)

        self.assertEqual(0, result)

    def test_one_character_string(self):
        string = "a"
        result = longest_substring_with_unique_charaters(string)

        self.assertEqual(1, result)
