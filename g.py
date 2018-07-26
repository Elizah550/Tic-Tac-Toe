from copy import deepcopy
import random

def display_board(test_board):
    game_board = {'r1':[' ','|',' ','|',' '],'r2':[' ','|',' ','|',' '] , 'r3':[' ','|',' ','|',' ']}
    line_break = '----------'
    board = deepcopy(test_board)
    board.pop(0)
    for r in game_board.values():
        r[0] = board[0]
        board.pop(0)
        r[2] = board[0]
        board.pop(0)
        r[4] = board[0]
        board.pop(0)
    for i in game_board.values():
        print(' '.join(i)+'\n'+line_break)
    print('\n'*5    )

def player_input():
    correct_reply = False
    while not correct_reply:
        player_1 = input('what charachter do you want? (O or X)')
        if(player_1 == 'X' or player_1 == 'O'):
            if player_1 == 'X':
                player_2 = 'O'
            else:
                player_2 = 'X'
            print('player1 is {player_1}')
            print('player1 is {player_2}')
            start = input('would you like to start (yes / no)')
            correct_reply = start =='yes'
    player_data = {'p1':player_1,'p2':player_2}
    return player_data


def place_marker(board, marker, position):
    board[position] = marker    

def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[7] == board[8] == board[9] == mark:
        return True
    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[3] == board[6] == board[9] == mark:
        return True
    elif board[1] == board[5] == board[9] == mark:
        return True
    elif board[3] == board[5] == board[7] == mark:
        return True
    else:
        return False

def choose_first():
    turn = random.randint(1,2)
    if(turn ==1):
        print('player1 will go first')
    else:
        print('player2 will go first')

def space_check(board, position):
    return board[position] == ' '

def is_full(board):
    return all(i!=' ' for i in board)

def is_draw(board):
    return True == is_full(board) and (False == win_check(board,'X') and False == win_check(board,'Y'))#when the board is full and nobody has won. 

def game_status(board):
    return False == is_draw(board) and  (False == win_check(board,'X') and False == win_check(board,'Y'))  #not a draw and no one has won the game    

def full_board_check(board):
    return all(i!=' ' for i in board)

def player_choice(board):
    place = int(input('where would you like to place'))
    if  space_check(board,place):
        return place
    else:
        print('THIS PLACE IS ALREADY TAKEN!!')

def replay():
    replay = input('would you like to play again (yes or no)')
    return replay == 'yes'
        


print('Welcome to Tic Tac Toe!')
while True:
    # Set the game up here
    d=player_input()
    choose_first()
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    while game_status(board):
        display_board(board)
        # Player 1 Turn
        p1 = int(input('player1 enter position :'))
        place_marker(board,d['p1'],p1)       
        display_board(board)
        
        # checking for draw or who won
        
        if win_check(board,d['p1']):
            print('player1 WINS!!')
            break
        elif win_check(board,d['p2']):
            print('player2 WINS!!')
            break
        elif is_draw(board):
            print('Draw match!!')
            break
        # Player2's turn.
        
        p2 = int(input('player2 enter position :'))
        place_marker(board,d['p2'],p2)       
        display_board(board)
        
        # checking for draw or who won
        
        if win_check(board,d['p1']):
            print('player1 WINS!!')
            beak
        elif win_check(board,d['p2']):
            print('player2 WINS!!')
            break
        elif is_draw(board):
            print('Draw match!!')
            break
        
            #pass

    if not replay():
        break
        
