import random


class TicTacToe:
    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    turn = random.choice(['X', 'O'])
    winner = None

    def print_board(self):
        for row in self.board:
            print(row)

    def display_winner(self):
        print(f'{self.winner} wins!')

    def change_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def check_winner(self):
        # row checking
        for row in self.board:
            if row[0] == "X" and row[1] == "X" and row[2] == "X":
                print("X wins!")
                self.winner = "X"
            elif row[0] == "O" and row[1] == "O" and row[2] == "O":
                print("O wins!")
                self.winner = "O"

        # column checking
        if (self.board[0][0] == "X" and self.board[1][0] == "X" and self.board[2][0] == "X") or (self.board[0][1] == "X" and self.board[1][1] == "X" and self.board[2][1] == "X") or (self.board[0][2] == "X" and self.board[1][2] == "X" and self.board[2][2] == "X"):
            print("X wins!")
            self.winner = "X"
        if (self.board[0][0] == "O" and self.board[1][0] == "O" and self.board[2][0] == "O") or (self.board[0][1] == "O" and self.board[1][1] == "O" and self.board[2][1] == "O") or (self.board[0][2] == "O" and self.board[1][2] == "O" and self.board[2][2] == "O"):
            print("O wins!")
            self.winner = "O"

        # diagonal checking
        if (self.board[0][0] == "X" and self.board[1][1] == "X" and self.board[2][2] == "X") or (self.board[0][2] == "X" and self.board[1][1] == "X" and self.board[2][0] == "X"):
            print("X wins!")
            self.winner = "X"
        if (self.board[0][0] == "O" and self.board[1][1] == "O" and self.board[2][2] == "O") or (self.board[0][2] == "O" and self.board[1][1] == "O" and self.board[2][0] == "O"):
            print("O wins!")
            self.winner = "O"

    def check_if_draw(self):
        # check if - is in any spaces
        if (self.board[0][0] != "-" and self.board[0][1] != '-' and self.board[0][2] != '-') and (self.board[1][0] != '-' and self.board[1][1] != '-' and self.board[1][2] != '-') and (self.board[2][0] != '-' and self.board[2][1] != '-' and self.board[2][2] != '-'):
            print("Draw!")
            self.winner = "Draw!"

    def play_turn(self):
        while self.winner is None:
            usr_input = int(
                input(f"{self.turn}'s turn. Pick a spot from 1-9: "))
            if usr_input >= 1 and usr_input <= 9:
                if usr_input >= 1 and usr_input <= 3:
                    if self.board[0][usr_input - 1] == "-":
                        self.board[0][usr_input - 1] = self.turn
                        self.print_board()
                        self.check_winner()
                        self.check_if_draw()
                        self.change_turn()
                    else:
                        print("Spot is taken.")
                if usr_input >= 4 and usr_input <= 6:
                    if self.board[1][usr_input - 4] == "-":
                        self.board[1][usr_input - 4] = self.turn
                        self.print_board()
                        self.check_winner()
                        self.check_if_draw()
                        self.change_turn()
                    else:
                        print("Spot is taken.")
                if usr_input >= 7 and usr_input <= 9:
                    if self.board[2][usr_input - 7] == "-":
                        self.board[2][usr_input - 7] = self.turn
                        self.print_board()
                        self.check_winner()
                        self.check_if_draw()
                        self.change_turn()
                    else:
                        print("Spot is taken.")
            else:
                print("Invalid spot.")

    def play(self):
        self.print_board()
        self.play_turn()


game = TicTacToe()
game.play()
