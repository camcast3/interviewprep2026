import unittest
from codinginterviewprep.twopointers.is_palindrome_valid import is_palindrome_valid


class TestIsPalindromeValid(unittest.TestCase):

    def test_basic_palindrome(self):
        """Test basic palindrome"""
        string = "racecar"
        result = is_palindrome_valid(string)
        self.assertEqual(result, True)

    def test_string_not_palindrome(self):
        """Test string that isn't a palindrome"""
        string = "abc123"
        result = is_palindrome_valid(string)
        self.assertEqual(result, False)

    def test_string_with_spaces_palindrome(self):
        """Test string that is a palindrome but with spaces"""
        string = "a dog a panic in a pagoda"
        result = is_palindrome_valid(string)
        self.assertEqual(result, True)

    def test_string_with_different_cases(self):
        """Test string with different casing"""
        string = "rAceCaR"
        result = is_palindrome_valid(string)
        self.assertEqual(result, True)

    def test_empty_string(self):
        """Test string that is empty"""
        string = ""
        result = is_palindrome_valid(string)
        self.assertEqual(result, True)

    def test_string_with_none_allocated(self):
        """Test string that is None"""
        string = None
        result = is_palindrome_valid(string)
        self.assertEqual(result, False)

    def test_a_single_characters_string(self):
        """Test string with a single character"""
        string = "a"
        result = is_palindrome_valid(string)
        self.assertEqual(result, True)

    def test_a_palindrome_with_two_characters(self):
        """Test string being a palindrome with only 2 characters"""
        string = "aa"
        result = is_palindrome_valid(string)
        self.assertEqual(result, True)

    def test_non_palindrome_with_two_characters(self):
        """Test string with only 2 characters but not a palindrome"""
        string = "ab"
        result = is_palindrome_valid(string)
        self.assertEqual(result, False)

    def test_numeric_palindrome_with_punctuation(self):
        """Test numeric palindrome with punctuation"""
        string = "12.02.2021"
        result = is_palindrome_valid(string)
        self.assertEqual(result, True)

    def test_numeric_but_not_palindrome_with_punctuation(self):
        """Test numeric that isnt a palindrome with punctuation"""
        string = "21.02.2021"
        result = is_palindrome_valid(string)
        self.assertEqual(result, False)
