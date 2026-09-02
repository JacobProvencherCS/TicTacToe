"""
Todo : comment on utilise les bitboards?
"""


class TicTacToe:

    def __init__(self, player1_name: str = "Player 1", player2_name: str = "Player 2"):
        self.grid = [["." for _ in range(3)] for _ in range(3)]
        self.player1 = player1_name
        self.player2 = player2_name
        self.playerTurn = 1

    def __str__(self):
        return "\n".join(("".join(map(str, line)) for line in self.grid))

    def placeToken(self, player: int, row: int, col: int) -> bool:

        if not (1 > row > 3) and not (1 > col > 3):
            self.grid[row - 1][col - 1] = player
            return True

        return False

    def checkWinner(self) -> bool:
        return False

    def mainloop(self):
        while True:
            print(f"Au tour de {self.playerTurn}")
            colInput = input("Enter a col number (1-3): ")
            rowInput = input("Enter a row number (1-3): ")
            self.placeToken(self.playerTurn, int(rowInput), int(colInput))
            print(self)
            self.playerTurn = self.playerTurn % 2 + 1


if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop()
