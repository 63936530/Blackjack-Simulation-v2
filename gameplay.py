from blackjack_hand import BlackJack
import numpy as np

class PlayGame:
    def __init__(self):
        self.hands = {
            'two':2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten': 10,
            'jack': 10,
            'queen': 10,
            'king': 10,
            'ace': {
                'high': 11,
                'low': 1
            }
        }
        self.score = 0
        self.drawn_cards = []
    def game_reset(self):
        if self.score > 21:
            self.score = 0
            self.drawn_cards = []

    def manual_reset(self):
        self.score = 0
        self.draw_cards = []

    def draw_card(self):
        self.card_list = [i for i in self.hands.keys()]
        pick_a_card = np.random.choice(self.card_list)
        return pick_a_card
    
    def card_value(self):
        self.picked_card = self.draw_card()
        if self.picked_card == 'ace':
            if self.score > 10:
                card_value = self.hands[self.picked_card]['low']
            else:
                card_value = self.hands[self.picked_card]['high']
        else:
            card_value = self.hands[self.picked_card]
        self.game_reset()
        self.score += card_value
        self.drawn_cards.append(self.picked_card)