# import pprint as pp
import random
import time

# Intro
print('Hello. What is your name?')
name = input()
if name != '':
    print(f"Well, {name} how about a game?")
else:
    print(f"Well, Stranger how about a game?")

time.sleep(2)

# Board Setup
def print_board(board):
    print(f"{board['top-L']}|{board['top-M']}|{board['top-R']}")
    print("-"*5)
    print(f"{board['mid-L']}|{board['mid-M']}|{board['mid-R']}")
    print("-"*5)
    print(f"{board['low-L']}|{board['low-M']}|{board['low-R']}")

def player_condition(board):
    if the_board['top-L'] is the_board['top-M'] is the_board['top-R'] == 'X' or \
        the_board['mid-L'] is the_board['mid-M'] is the_board['mid-R'] == 'X' or \
        the_board['low-L'] is the_board['low-M'] is the_board['low-R'] == 'X':
        # Horizontal win
        return 1
    elif the_board['top-L'] is the_board['mid-L'] is the_board['low-L'] == 'X' or \
        the_board['top-M'] is the_board['mid-M'] is the_board['low-M'] == 'X' or \
        the_board['top-R'] is the_board['mid-R'] is the_board['low-R'] == 'X':
        # Vertical win
        return 1
    elif the_board['top-L'] is the_board['mid-M'] is the_board['low-R'] == 'X' or \
        the_board['top-R'] is the_board['mid-M'] is the_board['low-L'] == 'X':
        # Cross win
        return 1
    else:
        return 0

def cpu_condition(board):
    if the_board['top-L'] is the_board['top-M'] is the_board['top-R'] == 'O' or \
        the_board['mid-L'] is the_board['mid-M'] is the_board['mid-R'] == 'O' or \
        the_board['low-L'] is the_board['low-M'] is the_board['low-R'] == 'O':
        # Horizontal win
        return 1
    elif the_board['top-L'] is the_board['mid-L'] is the_board['low-L'] == 'O' or \
        the_board['top-M'] is the_board['mid-M'] is the_board['low-M'] == 'O' or \
        the_board['top-R'] is the_board['mid-R'] is the_board['low-R'] == 'O':
        # Vertical win
        return 1
    elif the_board['top-L'] is the_board['mid-M'] is the_board['low-R'] == 'O' or \
        the_board['top-R'] is the_board['mid-M'] is the_board['low-L'] == 'O':
        # Cross win
        return 1
    else:
        return 0

the_board = {'top-L':'1', 'top-M':'2', 'top-R':'3', 'mid-L':'4', 'mid-M':'5', 'mid-R':'6', 'low-L':'7', 'low-M':'8', 'low-R':'9'}

board_keys = list(the_board.keys())

selection = list(the_board.values())

print('Your move, please choose a square.')
print_board(the_board)
print(selection)
print(' ')

# Trigger win condition
while True:

    # Player move
    player_stop = 0
    while player_stop != 1:

        # Player check
        try:
            player_input = input()
            board_index = board_keys[int(player_input)-1]
        except ValueError:
            board_index = 0 # When no input is entered, this goes to KeyError

        try:
            if the_board[board_index] not in {'X', 'O'}:
                the_board[board_index] = 'X'
                selection.remove(player_input)
                player_stop += 1 # Break player while loop
            else:
                print('Invalid move, choose again.')
        except KeyError:
            print('Invalid move, choose again.')
        
    winner = player_condition(the_board)
    print_board(the_board)
    print(' ')

    if winner == 1:
        print("You've beaten me!")
        break

    elif len(selection) == 0:
        print('Tie!')
        break

    else:
        # Optional wait
        time.sleep(1)

        # Computer move
        cpu_stop = 0
        while cpu_stop != 1:
            cpu_input = random.choice(selection)
            print(cpu_input)
            cpu_move = board_keys[int(cpu_input)-1]
            if the_board[cpu_move] not in {'X', 'O'}:
                the_board[cpu_move] = 'O'
                selection.remove(cpu_input)
                cpu_stop += 1 # Break cpu while loop
                
            else:
                pass

        winner = cpu_condition(the_board)
        print_board(the_board)
        print(selection)
        print(' ')

        if winner == 1:
            print("Looks like I won!")
            break

        else:
            pass