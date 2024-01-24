import random
import piece
import copy

class Game:
    def __init__(self):
        self._board = []
        self._score = 0
        self._width = 10
        self._height = 20
        self._current = None
        
    def generate_new_board(self):
        new_board = [[0 for _ in range(self._width)] for _ in range(self._height)]
        self._board = new_board

    def add_board(self, board):
        self._board = board
        self._width = len(board[0])
        self._height = len(board)
    
    def choose_shape(self):
        SHAPES = [
                [[1, 1, 1, 1]],
                [[1, 0, 0],
                 [1, 1, 1]],
                [[0, 0, 1],
                 [1, 1, 1]],
                [[0, 1, 0],
                 [1, 1, 1]],
                [[1, 1], 
                 [1, 1]],
                [[1, 1, 0], 
                 [0, 1, 1]],
                [[0, 1, 1],
                 [1, 1, 0]]]
        return SHAPES[random.randint(0,len(SHAPES)-1)]
    
    def check_overlap(self):
        if not self._current:
            return True
        peice_x = self._current.get_x()
        peice_y = self._current.get_y()
        looking_x = peice_x
        looking_y = peice_y
        shape = self._current.get_shape()

        for shape_row in shape:
            looking_x = peice_x
            for shape_row in shape_row:
                if shape_row == 1 and len(self._board)-1 == looking_y:
                    return False
                elif shape_row == 1 and self._board[looking_y][looking_x] == 1:
                    return False
            looking_y += 1

        return True

    def move_down(self):
        if self._current:
            self._current.move_down()
            self.score_points(1)

    def move_left(self):
        if self._current:
            self._current.move_left()

    def move_right(self):
        if self._current:
            self._current.move_right()

    def rotate(self):
        if self._current:
            self._current.rotate()

    def create_new_piece(self, shape):
        return piece.Piece(shape, int(self._width/2)-1, 0, self._width)
    
    def choose_and_create_piece(self):
        self.set_current(self.create_new_piece(self.choose_shape()))

    def place_piece(self, board, piece):
        peice_x = piece.get_x()
        peice_y = piece.get_y()
        looking_x = peice_x
        looking_y = peice_y
        shape = piece.get_shape()

        for shape_row in shape:
            looking_x = peice_x
            for shape_col in shape_row:
                if shape_col == 1:
                    board[looking_y][looking_x] = 1
                looking_x += 1
            looking_y += 1

        return board
    
    def place_current_on_board(self):
        print("this")
        self.place_piece(self._board, self._current)
        self.clear_current()

    def clear_current(self):
        self._current = None

    def render(self):
        render = copy.deepcopy(self._board)
        if self._current:
            print(self._current.get_x())
            print(self._current.get_y())
            render = self.place_piece(render, self._current)
        return render

    def get_current(self):
        return self._current
    
    def set_current(self, piece):
        self._current = piece

    def clear_rows(self):
        num = 0
        for row in range(len(self._board)-1,-1,-1):
            full = True
            for col in self._board[row]:
                if col == 0:
                    full = False
                    break
            
            if full:
                num += self.move_board_down(row, 0)
        if num > 0:
            print((num-1)*200 + 100)
            self.score_points((num-1)*200 + 100)
    
    def move_board_down(self, full_row, num):
        num += 1
        if full_row-1 < 0:
            self._board[full_row] = [0 for _ in range(self._width)]
            return num
        full = True
        for col in self._board[full_row-1]:
            if col == 0:
                full = False
                break
        if full:
            num = self.move_board_down(full_row-1, num)
        for row in range(full_row,-1,-1):
            if row-1 < 0:
                self._board[row] = [0 for _ in range(self._width)]
            else:
                self._board[row] = self._board[row-1]

        return num

    def score_points(self, amount):
        self._score += amount
