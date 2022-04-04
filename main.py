import random
from re import I


class TicTacToe:
    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    turn = None
    winner = None
    play_against_computer = None
    player_turn_choice = None

    def print_board(self):
        for row in self.board:
            print(row)
        print("\n")

    def display_winner(self):
        print(f'{self.winner} wins!')

    def change_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def print_winner(self):
        if self.play_against_computer:
            if self.player_turn_choice == self.winner:
                return "You win!"
            elif self.player_turn_choice != self.winner:
                return "Computer wins!"
        else:
            return f"{self.winner} wins!"

    def check_winner(self):
        # row checking
        for row in self.board:
            if row[0] == "X" and row[1] == "X" and row[2] == "X":
                self.winner = "X"
                print(self.print_winner())
            elif row[0] == "O" and row[1] == "O" and row[2] == "O":
                self.winner = "O"
                print(self.print_winner())

        # column checking
        if (self.board[0][0] == "X" and self.board[1][0] == "X" and self.board[2][0] == "X") or (self.board[0][1] == "X" and self.board[1][1] == "X" and self.board[2][1] == "X") or (self.board[0][2] == "X" and self.board[1][2] == "X" and self.board[2][2] == "X"):
            self.winner = "X"
            print(self.print_winner())
        if (self.board[0][0] == "O" and self.board[1][0] == "O" and self.board[2][0] == "O") or (self.board[0][1] == "O" and self.board[1][1] == "O" and self.board[2][1] == "O") or (self.board[0][2] == "O" and self.board[1][2] == "O" and self.board[2][2] == "O"):
            self.winner = "O"
            print(self.print_winner())

        # diagonal checking
        if (self.board[0][0] == "X" and self.board[1][1] == "X" and self.board[2][2] == "X") or (self.board[0][2] == "X" and self.board[1][1] == "X" and self.board[2][0] == "X"):
            self.winner = "X"
            print(self.print_winner())
        if (self.board[0][0] == "O" and self.board[1][1] == "O" and self.board[2][2] == "O") or (self.board[0][2] == "O" and self.board[1][1] == "O" and self.board[2][0] == "O"):
            self.winner = "O"
            print(self.print_winner())

    def check_if_draw(self):
        # check if - is in any spaces
        if (self.board[0][0] != "-" and self.board[0][1] != '-' and self.board[0][2] != '-') and (self.board[1][0] != '-' and self.board[1][1] != '-' and self.board[1][2] != '-') and (self.board[2][0] != '-' and self.board[2][1] != '-' and self.board[2][2] != '-'):
            print("Draw!")
            self.winner = "Draw!"

    def play_turn(self):
        while self.winner is None:
            if self.play_against_computer:
                if self.turn != self.player_turn_choice:
                    usr_input = random.randint(1, 9)
                    print('Computer picked: ', usr_input, '\n')
                elif self.turn == self.player_turn_choice:
                    usr_input = int(
                        input(f"{self.turn}'s turn. Pick a spot from 1-9: "))
                    print(f'You picked: {usr_input}\n')
            else:
                usr_input = int(
                    input(f"{self.turn}'s turn. Pick a spot from 1-9: "))
                print(f'{self.turn} picked: {usr_input}\n')
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

    def play(self, play_against_computer):
        if play_against_computer:
            self.play_against_computer = True
            pick_turn = str(input("Pick X or O: ")).upper()
            if pick_turn == "X":
                self.turn = "X"
                self.player_turn_choice = "X"
                print("You are X. AI is O.")
            elif pick_turn == "O":
                self.turn = "O"
                self.player_turn_choice = "O"
                print("You are O. AI is X.")
            else:
                print("Invalid choice.")
            self.print_board()
            self.play_turn()

        else:
            self.turn = random.choice(['X', "O"])
            self.print_board()
            self.play_turn()


if __name__ == "__main__":
    play_against_comp = input(
        "Would you like to play against AI? (y/n): ")
    print('\n')
    if (play_against_comp == "y"):
        game = TicTacToe()
        game.play(True)
    if (play_against_comp == "n"):
        game = TicTacToe()
        game.play(False)
    game = TicTacToe()
