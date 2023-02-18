from game_methods import display_board, check_for_winner, player1_input, player2_input

# Main program
print('Welcome to Tic Tac Toe!')
print('Preparing board...')

game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display_board(game_board)

boxes_filled = 0

while not check_for_winner(game_board):
    player1_input(game_board)
    display_board(game_board)
    boxes_filled += 1
    if check_for_winner(game_board):
        print 'Game over.'.upper()
        break

    player2_input(game_board)
    display_board(game_board)
    boxes_filled += 1
    if check_for_winner(game_board):
        print 'Game over.'.upper()
        break

    elif not check_for_winner(game_board) and boxes_filled == 8:
        print '\nDraw'.upper()
        print 'Game over.'.upper()
        break
