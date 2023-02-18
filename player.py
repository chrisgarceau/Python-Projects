# Player Class

class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.cards = []
        self.curr_hand_value = 0
        self.curr_bet = 0

    def add_card(self, new_card):
        self.cards.append(new_card)

    def update_balance(self, won):
        if won:
            self.balance += self.curr_bet * 2
        else:
            self.balance -= self.curr_bet
        self.curr_bet = 0

    def calc_curr_hand_value(self):
        card_sum = 0
        for card in self.cards:
            card_sum += card.value
        self.curr_hand_value = card_sum

    def print_curr_hand(self):
        if len(self.cards) == 0:
            print('You have no cards.')
        else:
            print('Your hand: ')
            for card in self.cards:
                print(card)
        print('\n')

