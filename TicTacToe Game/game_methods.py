# Displays Tic-Tac-Toe board
def display_board(board):
    print ('{} | {} | {}'.format(board[7], board[8], board[9]))
    print ('--|---|--')
    print (board[4] + ' | ' + board[5] + ' | ' + board[6])
    print ('--|---|--')
    print (board[1] + ' | ' + board[2] + ' | ' + board[3])


# Pre-condition: nan
# Collects user input from player1
# Post-condition: board is returned updated with player1 input
def player1_input(board):
    p1_bool = False
    while not p1_bool:
        p1_index = input('Player 1, enter position to place an X: ')
        if not board[p1_index].isspace():
            print('Position already filled. Try another position.')
        else:
            board[p1_index] = 'X'
            p1_bool = True
    return board


# Pre-condition: nan
# Collects user input from player2
# Post-condition: board is returned updated with player2 input
def player2_input(board):
    p2_bool = False
    while not p2_bool:
        p2_index = input('Player 2, enter position to place an O: ')
        if not board[p2_index].isspace():
            print('Position already filled. Try another position')
        else:
            board[p2_index] = 'O'
            p2_bool = True
    return board


# Pre-condition: none
# Checks if winner exists based on the state of the game board
# Post-condition: If winner exists, boolean winner is then True and a print statement is executed declaring
# player a winner. Else, boolean winner is False and the game continues.
def check_for_winner(board):
    winner = False
    # Horizontal winning scenarios
    s1 = [1, 2, 3]
    s2 = [4, 5, 6]
    s3 = [7, 8, 9]
    # Vertical winning scenarios
    s4 = [1, 4, 7]
    s5 = [2, 5, 8]
    s6 = [3, 6, 9]
    # Diagonal winning scenarios
    s7 = [1, 5, 9]
    s8 = [3, 5, 7]

    if board[s1[0]] == 'X' and board[s1[1]] == 'X' and board[s1[2]] == 'X':
        print '\nPlayer 1 wins!!!'.upper()
        winner = True
    if board[s2[0]] == 'X' and board[s2[1]] == 'X' and board[s2[2]] == 'X':
        print '\nPlayer 1 wins!!!'.upper()
        winner = True
    if board[s3[0]] == 'X' and board[s3[1]] == 'X' and board[s3[2]] == 'X':
        print '\nPlayer 1 wins!!!'.upper()
        winner = True
    if board[s4[0]] == 'X' and board[s4[1]] == 'X' and board[s4[2]] == 'X':
        print '\nPlayer 1 wins!!!'.upper()
        winner = True
    if board[s5[0]] == 'X' and board[s5[1]] == 'X' and board[s5[2]] == 'X':
        print '\nPlayer 1 wins!!!'.upper()
        winner = True
    if board[s6[0]] == 'X' and board[s6[1]] == 'X' and board[s6[2]] == 'X':
        print '\nPlayer 1 wins!!!'.upper()
        winner = True
    if board[s7[0]] == 'X' and board[s7[1]] == 'X' and board[s7[2]] == 'X':
        print '\nPlayer 1 wins!!!'.upper()
        winner = True
    if board[s8[0]] == 'X' and board[s8[1]] == 'X' and board[s8[2]] == 'X':
        print '\nPlayer 1 wins!!!'.upper()
        winner = True

    if board[s1[0]] == 'O' and board[s1[1]] == 'O' and board[s1[2]] == '0':
        print '\nPlayer 2 wins!!!'.upper()
        winner = True
    if board[s2[0]] == '0' and board[s2[1]] == '0' and board[s2[2]] == '0':
        print '\nPlayer 2 wins!!!'.upper()
        winner = True
    if board[s3[0]] == '0' and board[s3[1]] == '0' and board[s3[2]] == '0':
        print '\nPlayer 2 wins!!!'.upper()
        winner = True
    if board[s4[0]] == '0' and board[s4[1]] == '0' and board[s4[2]] == '0':
        print '\nPlayer 2 wins!!!'.upper()
        winner = True
    if board[s5[0]] == '0' and board[s5[1]] == '0' and board[s5[2]] == '0':
        print '\nPlayer 2 wins!!!'.upper()
        winner = True
    if board[s6[0]] == '0' and board[s6[1]] == '0' and board[s6[2]] == '0':
        print '\nPlayer 2 wins!!!'.upper()
        winner = True
    if board[s7[0]] == '0' and board[s7[1]] == '0' and board[s7[2]] == '0':
        print '\nPlayer 2 wins!!!'.upper()
        winner = True
    if board[s8[0]] == '0' and board[s8[1]] == '0' and board[s8[2]] == '0':
        print '\nPlayer 2 wins!!!'.upper()
        winner = True

    return winner

# End of game_methods.py
