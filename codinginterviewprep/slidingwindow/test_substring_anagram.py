import unittest
from codinginterviewprep.slidingwindow.substring_anagram import substring_anagram


class TestSubstringAnagram(unittest.TestCase):

    def test_example(self):
        s = "caabab"
        target = "aba"

        result = substring_anagram(s, target)
        self.assertEqual(2, result)

    def test_example_at_the_end(self):
        s = "caabab"
        target = "bab"

        result = substring_anagram(s, target)
        self.assertEqual(1, result)

    def test_target_larger_than_string(self):
        s = "caabab"
        target = "caababd"

        result = substring_anagram(s, target)
        self.assertEqual(0, result)

    def test_different_casing(self):
        s = "cAAbab"
        target = "aBa"

        result = substring_anagram(s, target)
        self.assertEqual(2, result)
