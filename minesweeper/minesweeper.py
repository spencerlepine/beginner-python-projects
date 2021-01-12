# Command-line minesweeper game
#@KylieYing (12 beginner python projects - coding course)

import random

# Create board class
class Board:
    def __init__(self, board_size, bomb_count):
        self.board_size = board_size
        self.bomb_count = bomb_count

        # let's create the board
        self.board = self.make_new_board() # plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of which spots are uncovered
        # we'll save a (row, col) tuple in the set
        self.dug = set() # if we dig at 0,0 the set will be ({0,0})

    def make_new_board(self):
        board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]

        bombs_planted = 0
        while bombs_planted < self.bomb_count:
            # Each spot has its own ID
            location = random.randint(0, self.board_size**2 - 1)
            r = location // self.board_size
            c = location % self.board_size
            
            if board[r][c] == '*':
                continue
           
            # A bomb can be planted here
            board[r][c] = '*'
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        for r in range(self.board_size):
            for c in range(self.board_size):
                if self.board[r][c] == None:
                    # Count the surrounding spaces
                    self.board[r][c] = self.get_bomb_count(r, c)

    def get_bomb_count(self, row, col):
        surrounding_bombs = 0

        for r in range(max(0, row - 1), min(self.board_size - 1, (row+1)) + 1):
            for c in range(max(0, col - 1), min(self.board_size - 1, (col+1)) + 1):
                if r == row and c == col:
                    continue
                elif self.board[r][c] == '*':
                    surrounding_bombs += 1

        return surrounding_bombs

    def print_game(self):
        print("   ", end="")
        for c in range(self.board_size):
            if c > 8: 
                print(f" {c+1}|", end="")
            else:
                print(f" {c+1} |", end="")

        print("\n  -----------------------------------------")
        for r in range(self.board_size):
            for c in range(self.board_size):
                if c == 0:
                    if r > 10:
                        print(f"{r}|", end="")
                    else:
                        print(f"{r} |", end="")
            
                thisSpot = ' '

                if (r,c) in self.dug:
                    thisSpot = self.board[r][c]
                    
                print(f" {thisSpot} |", end="")

            print("\n")


    def dig(self, spot_to_dig):
        r = (spot_to_dig // self.board_size)
        c = (spot_to_dig % self.board_size)

        if (r,c) not in self.dug:
            # Mark that we dug here
            self.dug.add((r, c))

            # Step 3a: if the location is a bomb, show game over message
            if self.board[r][c] == '*':
                
                # Uncover the entire board:
                for r in range(self.board_size):
                    for c in range(self.board_size):
                        self.dug.add((r,c))
        
                self.print_game()
                print('Game over!')
                return True # Game over is true

            # Step 3b: if not a bomb, dig recursively until each sqaure is at least next to a bomb
            if self.board[r][c] == 0:
                self.dig_surrounding(r, c)
    
        else:
            print("You already dug there..")

        if self.solved():
            self.print_game()
            print('Congrats, you won!')
            return True
        
        return False
    
    def dig_surrounding(self, row, col):
        for r in range(max(0, row - 1), min(self.board_size - 1, (row+1)) + 1):
            for c in range(max(0, col - 1), min(self.board_size - 1, (col+1)) + 1):
                if self.board[r][c] == '*':
                    return
                elif (r, c) not in self.dug:
                    self.dug.add((r, c))
                    if self.board[r][c] == 0:
                        self.dig_surrounding(r, c)

    def solved(self):
        if (self.board_size**2 - (len(self.dug))) == self.bomb_count:
            return True

def play(board_size=10, bomb_count=10):
    # Step 1: create the board and plant the bombs
    board_obj = Board(board_size, bomb_count)

    # Step 4: repeat 2-3b until there are no more places to dig -> Victory
    game_over = False
    while not game_over:
        # Step 2: show the user the board and ask them where they want to dig
        board_obj.print_game()

        user_dig_choice = -1
        while user_dig_choice < 0 or user_dig_choice > board_size**2:
            try:
                user_dig_choice = int ( input( f"Which spot would you like to dig? (1-{(board_size**2)}) " ) )
            except:
                # Only accept valid int
                continue

        # Try to dig here
        game_over = board_obj.dig(user_dig_choice - 1) # index format

play()