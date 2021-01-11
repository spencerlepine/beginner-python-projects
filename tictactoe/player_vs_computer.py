import random

# Player vs Player Tic Tac Toe

def print_board(board):

    print("\n")
    print(f"   {board[0]} | {board[1]} | {board[2]}")
    print("   ---------")
    print(f"   {board[3]} | {board[4]} | {board[5]}")
    print("   ---------")
    print(f"   {board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Start out with blank board
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Check for a winner
def check_winner(board):
    for i in range(3):
        if board[i] != ' ' and (board[i] == board[i+1]) and (board[i] == board[i+2]):
            print(f"There is a row winner: {board[i]}")
            return True

        if board[i] != ' ' and (board[i] == board[i+3]) and (board[i] == board[i+6]):
            print(f"There is a column winner: {board[i]}")
            return True

    if board[4] != ' ' and ((board[0] == board[4] and board[0] == board[8]) or \
        (board[2] == board[4] and board[2] == board[6])):
        print(f"There is a diagonal winner: {board[4]}")
        return True

    return False

# Check if the board is full
def board_full(board):
        return not ' ' in board

# Check if user can play here
def valid_turn(board, spot):
    return spot >= 0 and spot <= 8 and board[spot] == ' '

def which_letter(board):
    choices = ['X', 'O']
    return choices[(board.count(' ') + 1) % 2]

def computer_choice(board):
    computer_move_count = board.count('X') # Assuming the computer plays X

    if computer_move_count >= 2:
        # Go for a midge
        if board[0] == 'X' and board[2] == 'X':
            if valid_turn(board, 1):
                return 1

        elif board[0] == 'X' and board[6] == 'X':
            if valid_turn(board, 1):
                return 3

        elif (board[0] == 'X' and board[8] == 'X') or (board[2] == 'X' and board[6] == 'X'):
            if valid_turn(board, 4):
                return 4

    else:
        # Go for the corners
        priorities = [0, 2, 6, 8]
        random.shuffle(priorities)

        for i in priorities:
            if valid_turn(board, i):
                return i

    
    # Resort to picking SOMETHING
    for i in range(9):
        if valid_turn(board, i):
            return i

def play(board):
    print_board(board)

    if check_winner(board):
        return
    elif board_full(board):
        print("This round is a draw")
        return
    else:
        letter = which_letter(board)

        if letter == "X":
            # Let the computer decide
            spot = computer_choice(board)
        elif letter == "O":
            # Let the player decide
            spot = int(input(f"${letter}'s turn: Which spot would you like to fill? (1-9): ")) - 1
            while not valid_turn(board, spot):
                spot = int(input(f"${letter}'s turn: Please choose a valid spot (1-9): ")) - 1 

        # Fill in valid spot
        board[spot] = letter

        play(board)

       
play(board)
