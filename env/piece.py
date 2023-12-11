class Piece():
    def __init__(self, shape, x, y):
        self._shape = shape
        self._x = x
        self._y = y

    def rotate(self):
        self._shape = [list(row) for row in zip(*self._shape[::-1])]
        
    def get_shape(self):
        return self._shape
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def move_down(self):
        self._y += 1

    def move_left(self):
        if self._x>0:
            self._x -= 1
        
    def move_right(self):
        if self._x<9:
            self._x += 1