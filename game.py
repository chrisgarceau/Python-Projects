from deck import Deck
from dealer import Dealer
from player import Player

# Player enters both their name and balance
player_name = input('Enter your name: ')
player_money = int(input('Enter your chip balance: '))
player = Player(player_name, player_money)

# Dealer is initialized
dealer = Dealer()

# Game deck is initialized
game_deck = Deck()
game_deck.shuffle()

# Start of game
print('Starting game...')
game_on = True
while game_on:
    curr_game_over = False
    game_deck.shuffle()
    valid_bet = True
    while valid_bet:
        bet = int(input('Enter your bet amount: '))
        if bet <= player.balance:
            player.curr_bet = bet
            player.balance -= bet
            valid_bet = False
            break
        else:
            print('Bet amount exceeds your balance. Try again.')
            valid_bet = True

    print('\n')
    # Deals two cards to the dealer
    dealer.add_card(game_deck.deal_one())
    dealer.add_card(game_deck.deal_one())

    # Deals two cards to the player
    player.add_card(game_deck.deal_one())
    player.add_card(game_deck.deal_one())

    dealer.print_curr_hand()
    player.print_curr_hand()

    #########
    # Player's turn
    player_busted = True
    while player_busted:
        answer = int(input('Hit? -> 1 for Yes, 2 for No: '))
        if answer == 1:
            player.add_card(game_deck.deal_one())
            player.calc_curr_hand_value()
            dealer.print_curr_hand()
            player.print_curr_hand()
            if player.curr_hand_value > 21:
                print('You busted.')
                player.update_balance(False)
                print('Balance: ${}'.format(player.balance))
                print('\n')
                curr_game_over = True
                player_busted = False
        elif answer == 2:
            player.calc_curr_hand_value()
            dealer.print_curr_hand()
            player.print_curr_hand()
            break

    # Dealer's turn
    if not curr_game_over:
        dealer.calc_curr_hand_value()
        while dealer.curr_hand_value < 17:
            dealer.add_card(game_deck.deal_one())
            dealer.calc_curr_hand_value()
            if dealer.curr_hand_value > 21:
                print('House busted. YOU WON!')
                player.update_balance(True)
                print('Balance: ${}'.format(player.balance))
                print('\n')
                dealer.reveal_hand()
                player.print_curr_hand()
                print('Dealer: {}'.format(dealer.curr_hand_value))
                print('Player: {}'.format(player.curr_hand_value))
                curr_game_over = True
                break

    if not curr_game_over:
        if dealer.curr_hand_value == 21 or dealer.curr_hand_value > player.curr_hand_value:
            print('You lost.')
            player.update_balance(False)
            print('Balance: ${}'.format(player.balance))
            print('\n')
            dealer.reveal_hand()
            player.print_curr_hand()
            print('Dealer: {}'.format(dealer.curr_hand_value))
            print('Player: {}'.format(player.curr_hand_value))
        if 21 >= player.curr_hand_value > dealer.curr_hand_value:
            print('YOU WON!')
            player.update_balance(True)
            print('Balance: ${}'.format(player.balance))
            print('\n')
            dealer.reveal_hand()
            player.print_curr_hand()
            print('Dealer: {}'.format(dealer.curr_hand_value))
            print('Player: {}'.format(player.curr_hand_value))

    ##########

    # empty player and dealer cards and add cards back to game_deck
    game_deck.add_cards(player.cards)
    game_deck.add_cards(dealer.cards)
    player.cards = []
    dealer.cards = []
    player.curr_hand_value = 0
    dealer.curr_hand_value = 0

    # Ask if player would like to continue
    if player.balance > 0:
        print('\n')
        play_again = int(input('Would you like to play again? Enter 1 for Yes, 2 for No: '))
        if play_again == 1:
            game_on = True
            continue
        elif play_again == 2:
            print('GAME OVER...')
            game_on = False
    else:
        print('Out of money!')
        print('GAME OVER')
        game_on = False

# End of game logic
