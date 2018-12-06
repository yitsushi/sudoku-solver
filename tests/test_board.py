import unittest
from sudoku_solver import Board, AmbiguousError

def fixture_path(filename):
    return f'tests/input/{filename}'

class TestBoars(unittest.TestCase):
    def test_vaidate_full_board(self):
        board = Board()

        board.from_file(fixture_path('simple-full-valid'))
        self.assertTrue(board.validate())

    def test_vaidate_full_board_invalid(self):
        board = Board()

        board.from_file(fixture_path('simple-full-not-valid'))
        self.assertFalse(board.validate())

    def test_simple_fill(self):
        board = Board()

        board.from_file(fixture_path('simple-fill'))
        self.assertTrue(board.validate())
        board.solve()
        self.assertTrue(board.validate())
        # Test if it's solved
        self.assertTrue(all([v != '_' for line in board.field() for v in line]))

    def test_medium_fill(self):
        board = Board()

        board.from_file(fixture_path('medium-fill'))
        self.assertTrue(board.validate())
        board.solve()
        self.assertTrue(board.validate())
        # Test if it's solved
        self.assertTrue(all([v != '_' for line in board.field() for v in line]))

    def test_real_0001(self):
        board = Board()

        board.from_file(fixture_path('real-0001'))
        self.assertTrue(board.validate())
        board.solve()
        self.assertTrue(board.validate())
        # Test if it's solved
        self.assertTrue(all([v != '_' for line in board.field() for v in line]))

    def test_ambiguous_raises_error(self):
        board = Board()

        board.from_file(fixture_path('ambiguous'))
        self.assertTrue(board.validate())
        with self.assertRaises(AmbiguousError):
            board.solve()
        pass

if __name__ == '__main__':
    unittest.main()
