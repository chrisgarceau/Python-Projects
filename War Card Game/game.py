import deck, player

# Initializing player one and player two
player_one = player.Player('Chris')
player_two = player.Player('Donny')

# Initializing instance of a new deck
game_deck = deck.Deck()
game_deck.shuffle()
game_deck.shuffle()

# Splitting deck between both players
for i in range(26):
    player_one.add_cards(game_deck.deal_one())
    player_two.add_cards(game_deck.deal_one())

# Printing each player's half deck
print(player_one)
print(player_two)
print(str(player_one.name + "'s card(s): "))
for i in range(26):
    print(player_one.all_cards[i])
print('\n')
print(str(player_two.name + "'s card(s): "))
for i in range(26):
    print(player_two.all_cards[i])
print ('\n')

# Start of game
game_on = True
round_num = 0

print('Starting game...\n')
while game_on:
    round_num += 1
    print('Round {}'.format(round_num))

    if len(player_one.all_cards) == 0:
        print(str(player_two.name), 'wins!')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print(str(player_one.name) + 'wins!')
        game_on = False
        break

    # Start new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False
        else:
            print('WAR!')

            if len(player_one.all_cards) < 5:
                print('{} is unable to declare war'.format(player_one.name))
                print('{} wins!'.format(player_two.name))
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print('{} is unable to declare war'.format(player_two.name))
                print('{} wins!'.format(player_one.name))
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

