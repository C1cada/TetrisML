import unittest

class TestModel(unittest.TestCase):
    def test_clear_board(self):
        example_board = [[0 for _ in range(10)] for _ in range(20)]
        example_board[19] = [1,1,1,1,1,1,1,1,1,1]
        print(example_board)
        self.assertEqual()

