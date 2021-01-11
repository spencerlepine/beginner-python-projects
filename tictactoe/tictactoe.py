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
        print(f"There is a diagonal winner: {board[5]}")
        return True

    return False

# Check if the board is full
def board_full(board):
        return not ' ' in board

# Check if user can play here
def valid_turn(board, spot):
    return spot >= 1 and spot <= 9 and board[spot-1] == ' '

def which_letter(board):
    choices = ['X', 'O']
    return choices[board.count(' ') % 2]

def play(board):
    print_board(board)

    if check_winner(board):
        return
    elif board_full(board):
        print("This round is a draw")
        return
    else:
        letter = which_letter(board)

        user_spot = int(input(f"${letter}'s turn: Which spot would you like to fill? (1-9): "))
        while not valid_turn(board, user_spot):
            user_spot = int(input(f"${letter}'s turn: Please choose a valid spot (1-9): "))  

        # Fill in valid spot
        board[user_spot-1] = letter

        play(board)

       
play(board)
