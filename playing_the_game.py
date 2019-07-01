from gameplay import PlayGame

class Player:
    def __init__(self, amount):
        self.game = PlayGame()
        self.amount = amount
    
    def add_money(self, value):
        self.amount += value

    def take_money(self, value):
        self.amount -= value

class Dealer:
    def __init__(self):
        self.game = PlayGame()

