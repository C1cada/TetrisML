import model

class View:
    def __init__(self):
        self.game = model.Game()

    def start_game(self):
        self.game.generate_new_board()
        while True:
            if not self.game.check_overlap():
                self.game.place_current_on_board()
            if not self.game.get_current():
                self.game.choose_and_create_piece()
            self.game.check_clear()
            self.printBoard(self.game.render())
            print("Next move: ")
            move = input()
            if move == "left":
                self.game.move_left()
            elif move == "right":
                self.game.move_right()
            elif move == "down":
                self.game.move_down()
            elif move == "rotate":
                self.game.rotate()

    def printBoard(self, board):
        for row in board:
            print(row)
            
if __name__ == "__main__":
    view = View()
    view.start_game()
           