from itertools import batched


class TicTacToe:

    def __init__(self):
        self.gameState = 0
        self.players = [0, 0]
        self.wOutcomes = [0b111_000_000,
                          0b000_111_000,
                          0b000_000_111,
                          0b100_100_100,
                          0b010_010_010,
                          0b001_001_001,
                          0b100_010_001,
                          0b001_010_100]

        self.playerTurn = 0
        self.winner = None
        self.dico = {0: 'O', 1: 'X'}

    def __str__(self):
        string = '.........'
        for k, v in self.dico.items():
            string = ''.join(v if bit == '1' else dot for dot, bit in zip(string, f"{self.players[k]:09b}"))
        return "\n".join(''.join(e for e in line) for line in list(batched(string, n=3)))

    def __bool__(self):
        for i, player in enumerate(self.players):
            for wOutcome in self.wOutcomes:
                if wOutcome & player == wOutcome:
                    self.winner = self.dico[i]
                    return True
        return False

    def __call__(self):

        while not self:
            print(self)
            user_input = input(
                f"Joueur {self.dico[self.playerTurn]}, entre une position ({", ".join(str(n + 1) for n in self.getPositionsLeft())}): ")
            self.placeToken(self.playerTurn, int(user_input))
            self.playerTurn ^= 1

        print(self)
        print(f"Le joueur {self.winner} gagne!")

    def updateGameState(self):
        self.gameState = self.players[0] & self.players[0]

    def placeToken(self, player: int, position: int) -> bool:
        if player in [0, 1] and position in self.getPositionsLeft():
            self.players[player] |= pow(2, 9 - position)
            self.updateGameState()
            return True
        return False

    def getPositionsLeft(self):
        return [i for i in range(9) if not self.gameState & (1 << i)]


if __name__ == "__main__":
    game = TicTacToe()
    game()
