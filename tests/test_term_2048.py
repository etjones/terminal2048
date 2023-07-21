import unittest
from terminal2048.term_2048 import move, merge_tiles, GameAction

class TestMoveFunction(unittest.TestCase):

    def test_move_down(self):
        board = [
            [2, 2, 0, 4],
            [0, 0, 0, 4],
            [4, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        expected_board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [2, 0, 0, 0],
            [4, 2, 0, 8]
        ]
        expected_score = 8

        actual_board, actual_score = move(board, GameAction.DOWN)
        self.assertEqual(actual_board, expected_board)
        self.assertEqual(actual_score, expected_score)

    def test_move_up(self):
        board = [
            [2, 2, 0, 4],
            [0, 0, 0, 4],
            [4, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        expected_board = [
            [2, 2, 0, 8],
            [4, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        expected_score = 8
        actual_board, actual_score = move(board, GameAction.UP)
        self.assertEqual(actual_board, expected_board)
        self.assertEqual(actual_score, expected_score)

    def test_move_left(self):
        board = [
            [2, 2, 0, 4],
            [0, 0, 0, 4],
            [4, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        expected_board = [
            [4, 4, 0, 0],
            [4, 0, 0, 0],
            [4, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        expected_score = 4
        actual_board, actual_score = move(board, GameAction.LEFT)
        self.assertEqual(actual_board, expected_board)
        self.assertEqual(actual_score, expected_score)

    def test_move_right(self):
        board = [
            [2, 2, 0, 4],
            [0, 0, 0, 4],
            [4, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        expected_board = [
            [0, 0, 4, 4],
            [0, 0, 0, 4],
            [0, 0, 0, 4],
            [0, 0, 0, 0]
        ]

        expected_score = 4
        actual_board, actual_score = move(board, GameAction.RIGHT)
        self.assertEqual(actual_board, expected_board)
        self.assertEqual(actual_score, expected_score)

class TestMergeFunction(unittest.TestCase):
    def test_merge(self):
        rows = [
            [2, 2, 0, 4],
            [2, 0, 0, 2],
            [4, 4, 2, 2], 
        ]
        expected_rows = [
            ([4, 4, 0, 0], 4),
            ([4, 0, 0, 0], 4),
            ([8, 4, 0, 0], 12),
        ]
        for row, (expected_row, expected_score) in zip(rows, expected_rows):
            actual_row, score = merge_tiles(row)

            self.assertEqual(actual_row, expected_row)
            self.assertEqual(score, expected_score)


if __name__ == "__main__":
    unittest.main()
