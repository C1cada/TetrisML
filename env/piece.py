class Piece():
    def __init__(self, shape, x, y):
        self._shape = shape
        self._x = x
        self._y = y
        self._empty_space_left = 0
        self._empty_space_right = 0
        self._empty_space_up = 0
        self._empty_space_down = 0

    def calculate_empty_space(self):
        self._empty_space_left = 0
        for col in len(self._shape[0]):
            for row in self._shape:
                if row[col] == 1:
                    break
            else:
                self._empty_space_left += 1
                continue
            break

        self._empty_space_right = 0
        for col in reversed(len(self._shape[0])):
            for row in self._shape:
                if row[col] == 1:
                    break
            else:
                self._empty_space_right += 1
                continue
            break
            

        self._empty_space_up = 0
        for row in self._shape:
            for col in row:
                if col == 1:
                    break
            else:
                self._empty_space_up += 1
                continue
            break

        self._empty_space_down = 0
        for row in reversed(self._shape):
            for col in row:
                if col == 1:
                    break
            else:
                self._empty_space_down += 1
                continue
            break
        
    def rotate(self):
        self._shape = [list(row) for row in zip(*self._shape[::-1])]
        # for row in self._shape:
        #     if row[0] == 1:
        #         self._x += 1
            
        
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