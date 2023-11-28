class GameMachine:
    def __init__(self):
        self.coin = 0

    def inputCoin(self):
        if self.coin < 5:
            self.coin += 1

        elif self.coin >= 5:
            print('ERROR!')

    def playGame(self):
        self.coin -= 1

    def _totalCoin(self):
        print(self.coin)


a = GameMachine()
a.inputCoin()
a.inputCoin()
a.inputCoin()
a.inputCoin()
a.inputCoin()
a.inputCoin()

a._totalCoin()