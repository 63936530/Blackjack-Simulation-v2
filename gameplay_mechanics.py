#Building the basic version of the game
# 1. Draw a card
# 2. Continue drawing cards until the hand limit was met.
from blackjack_hand import BlackJack
import numpy as np

class PlayHand(BlackJack):
    def __init__(self):
        self.hand = super().card_hands()
        self.hand_list = [i for i in self.hand.keys()]

    def draw_card(self):
        card = np.random.choice(self.hand_list)
        if card == 'ace':
            if self.score > 10:
                return self.hand[card]['low']
            else:
                return self.hand[card]['high']
        else:
            return self.hand[card]

    def restart(self):
        self.score = 0

    def play_hand(self, limit):
        self.score = 0
        while True:
            self.score += self.draw_card()
            if self.score > 21 or self.score >= limit:
                break
        return self.score
        self.restart()
