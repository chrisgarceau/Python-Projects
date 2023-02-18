# Deck Class
# Instantiates a new deck by creating all 52 card objects and stores the objects as a list
# Deck is shuffled through a method call using random library shuffle() function
# Deals cards from the deck object using pop method from cards list
from random import shuffle
from card import Card, suits, ranks, values


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

