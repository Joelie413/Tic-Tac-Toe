def display_board(board):
    print(board[1]+ ' | '+board[2]+ ' | '+board[3])
    print('--|---|---')
    print(board[4]+ ' | '+board[5]+ ' | '+board[6])
    print('--|---|---')
    print(board[7]+ ' | '+board[8]+ ' | '+board[9])

def player_input():

    player1 = ''

    while player1 != 'X' and player1 != 'O':
        player1 = input('Player 1, please pick a marker: X or O').upper()
    if player1 == 'X':
        player2 = 'O'
        print('Player 1 will use X and player 2 will use O')
        return ('X','O')
    if player1 == 'O':
        player2 = 'X'
        print('Player 1 will use O and player 2 will use X')
        return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
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
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def player_choice(board):

    while True:
        position = input("Enter your position (1-9): ")
        if position not in ['1','2','3','4','5','6','7','8','9']:
            print('Sorry, that is not a valid position! Please try again!')
        elif not space_check(board, int(position)):
            print('Sorry, that position is already taken...')
        else:
            return int(position)

def replay():
    return input('Do you want to try again? Enter Yes or No: ').lower().startswith('y')


#---------------------------------------------------------------------------------------------------------------------

print('Welcome to Tic-Tac-Toe!')

while True:

    the_board = [' '] * 10
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first!')

    play_game = input('Its time to play the game! Are you ready? Yes or No').lower()

    if play_game[0] == 'y':
        game_on = True
        print('Tip: The Board is set up 1-9 starting in the top left going to the bottom right.')
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 wins!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 2'


        else:
            turn == 'Player 2'
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 wins!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break



#test_board = ['#','X','O','X','O','X','O','X','O','X']
#test_board_o = ['#','X','O','X','O','X','O','X','O','X'] X wins
#test_board_x = ['#','O','X','O','X','O','X','O','X','O'] O wins
#tie_board = ['#','X','O','X','X','O','O','O','X','X'] tie game


#place_marker(test_board,'$',8)
#display_board(test_board)
    
#(player1_marker,player2_marker) = player_input()







