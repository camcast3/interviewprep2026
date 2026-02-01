import unittest
from codinginterviewprep.hashmapnssets.verify_sudoku_board import verify_sudoku_board


class TestVerifySudokuBoard(unittest.TestCase):

    def test_valid_board(self):
        """Test a valid sudoku board"""
        valid_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.assertTrue(verify_sudoku_board(valid_board))

    def test_duplicate_in_row(self):
        """Test board with duplicate in row"""
        invalid_board = [
            [5, 5, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.assertFalse(verify_sudoku_board(invalid_board))

    def test_duplicate_in_column(self):
        """Test board with duplicate in column"""
        invalid_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [5, 0, 0, 1, 9, 5, 0, 0, 0],  # 5 in column 0
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.assertFalse(verify_sudoku_board(invalid_board))

    def test_duplicate_in_subgrid(self):
        """Test board with duplicate in 3x3 subgrid"""
        invalid_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 5, 1, 9, 5, 0, 0, 0],  # 5 in same subgrid as [0][0]
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.assertFalse(verify_sudoku_board(invalid_board))

    def test_empty_board(self):
        """Test board with all zeros (empty)"""
        empty_board = [[0] * 9 for _ in range(9)]
        self.assertTrue(verify_sudoku_board(empty_board))

    def test_board_with_all_numbers_valid(self):
        """Test fully filled valid sudoku board"""
        full_board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        self.assertTrue(verify_sudoku_board(full_board))

    def test_single_number(self):
        """Test board with only one number"""
        single_board = [[0] * 9 for _ in range(9)]
        single_board[0][0] = 5
        self.assertTrue(verify_sudoku_board(single_board))


if __name__ == '__main__':
    unittest.main()
