import unittest
from env import model

class TestModel(unittest.TestCase):
    def test_clear_board_empty(self):
        expected = [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],]
        example_board = [[0,0,0,0,0],
                         [0,0,0,0,0],
                         [0,0,0,0,0],
                         [0,0,0,0,0],]
        game = model.Game()
        game.add_board(example_board)
        game.clear_rows()
        actual = game.render()
        self.assertEqual(expected, actual)

    def test_clear_board(self):
        expected = [[0,0,0,0,0],
                    [0,1,0,0,0],
                    [0,0,1,0,0],
                    [0,1,0,1,0],]
        example_board = [[0,1,0,0,0],
                         [0,0,1,0,0],
                         [0,1,0,1,0],
                         [1,1,1,1,1],]
        game = model.Game()
        game.add_board(example_board)
        game.clear_rows()
        actual = game.render()
        self.assertEqual(expected, actual)

    def test_clear_board_full(self):
        expected = [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],]
        example_board = [[1,1,1,1,1],
                         [1,1,1,1,1],
                         [1,1,1,1,1],
                         [1,1,1,1,1],]
        game = model.Game()
        game.add_board(example_board)
        game.clear_rows()
        actual = game.render()
        self.assertEqual(expected, actual)

    def test_clear_board_two(self):
        expected = [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,1,0,1,0],]
        example_board = [[0,0,1,0,0],
                         [0,1,0,1,0],
                         [1,1,1,1,1],
                         [1,1,1,1,1],]
        game = model.Game()
        game.add_board(example_board)
        game.clear_rows()
        actual = game.render()
        self.assertEqual(expected, actual)


