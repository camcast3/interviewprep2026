import unittest
from codinginterviewprep.stacks.valid_parenthesis_expression import valid_parenthesis_expression


class TestValidParenthesis(unittest.TestCase):

    def test_example_1(self):
        string = "([]{})"
        result = valid_parenthesis_expression(string)

        self.assertTrue(result)

    def test_example_2(self):
        string = "([]{)})"
        result = valid_parenthesis_expression(string)

        self.assertFalse(result)
