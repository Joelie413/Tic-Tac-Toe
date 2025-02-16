def display_board(board):

    print('   |   |')
    print(' '+ board[1] + ' | ' +board[2]+ ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' +board[4] + ' | ' +board[5]+ ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' +board[7] + ' | ' +board[8]+ ' | ' + board[9])
    print('   |   |')

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, Would you like to be X or O?').upper()
        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')
    
def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or #top row win
    (board[4] == mark and board[5] == mark and board[6] == mark) or #middle row win
    (board[7] == mark and board[8] == mark and board[9] == mark) or #bottom row win 
    (board[1] == mark and board[5] == mark and board[9] == mark) or #top right down diagonal win
    (board[3] == mark and board[5] == mark and board[7] == mark) or #top left down diagonal win
    (board[1] == mark and board[4] == mark and board[7] == mark) or #right down win
    (board[2] == mark and board[5] == mark and board[8] == mark) or #middle down win
    (board[3] == mark and board[6] == mark and board[9] == mark)) #left down win

import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board,position):

    return board[position] == ' '

def full_board_check(board):
    for i in range(1,11):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9)'))
    
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')



print('Welcome to Tic-Tac-Toe')

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play?')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)

            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Congratulations, Player 1! You win!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                else:
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)

            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('Congratulations, Player 2! You win!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                else:
                    turn = 'Player 1'
    if not replay():
        break