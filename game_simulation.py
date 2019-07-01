# Build a game for the user vs. the dealer.
from gameplay_mechanics import PlayHand

class Dealing(PlayHand):
    def player(self, limit):
        return super().play_hand(limit)
    
    def dealer(self):
        return super().play_hand(17)

class GameOutcome(Dealing):
    def __init__(self):
        super().__init__()
    
    def PlayerWins(self, limit, test=False):
        player = super().player(limit)
        dealer = super().dealer()

        if test:
            print(player, dealer)

        if player > 21:
            return False
        elif dealer > 21:
            return True
        elif player >= dealer:
            return True
        else:
            return False

    def funds_check(self):
        if self.amount <= 0:
            return True
        else:
            return False
    
    def Betting(self, bet, hold):
        if self.funds_check():
            return
        else:
            outcome = self.PlayerWins(hold)
            if outcome:
                self.amount += bet
            else:
                self.amount -= bet
            return self.amount
    
    def double_down(self, bet, hold):
        if self.funds_check():
            return
        else:
            bets = []
            balance = []
            outcome = self.PlayerWins(hold)
            while True:
                balance.append(self.amount)
                bets.append(bet)
                if self.funds_check():
                    break
                self.amount -= bet
                bet *= 2
                if bet > self.amount:
                    break
                outcome = self.PlayerWins(hold)
                if outcome:
                    self.amount += bet
                    break
            return self.amount

    def AddFunds(self, amount):
        self.amount = amount
