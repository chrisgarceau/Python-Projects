# Class Dealer

class Dealer:
    def __init__(self):
        self.cards = []
        self.curr_hand_value = 0

    def add_card(self, new_card):
        self.cards.append(new_card)

    def print_curr_hand(self):
        if len(self.cards) == 0:
            print('Dealer has no cards.')
        else:
            print("Dealer's hand: ")
            print(self.cards[-1])
            print('{} card(s) hidden.'.format(len(self.cards) - 1))
        print('\n')

    def reveal_hand(self):
        print("Dealer's hand:")
        for card in self.cards:
            print(card)
        print('\n')

    def calc_curr_hand_value(self):
        card_sum = 0
        for card in self.cards:
            card_sum += card.value
        self.curr_hand_value = card_sum

