"""
101
100
011
"""


class TicTacToe:

    def __init__(self):
        self.grid = [["." for m in range(3)] for n in range(3)]

    def __str__(self):
        return "\n".join(("".join(map(str, line)) for line in self.grid))

    def placeToken(self, player: int, row: int, col: int) -> bool:
        if not (1 > row > 3) and not (1 > col > 3):
            self.grid[row - 1][col - 1] = player
            return True
        return False

if __name__ == "__main__":

    game = TicTacToe()
    playerTurn = 1

    while True:
        print(f"Au tour de {playerTurn}")
        colInput = input("Enter a col number (1-3): ")
        rowInput = input("Enter a row number (1-3): ")
        game.placeToken(playerTurn, int(rowInput), int(colInput))
        print(game)
        playerTurn = playerTurn % 2 + 1

