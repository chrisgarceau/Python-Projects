# Player class
# Player will be able to add a single card or multiple cards to their list


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # For multiple card objects
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        # For single card object
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return 'Player {} has {} card(s)'.format(self.name, len(self.all_cards))


