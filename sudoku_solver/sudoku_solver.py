#@KylieYing (12 beginner python projects - coding course)

# Helper function
def find_next_empty_spot(puzzle):
    # Finds the next row, col thats empty --> 0
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c

    # The board is full         
    return None, None


def is_valid(puzzle, guess, row, col):
    # Blocks surrounding
    block_row, block_col = (row // 3) * 3, (col // 3) * 3
    for r in range(block_row, block_row + 3):
        for c in range(block_col, block_col + 3):
            if puzzle[r][c] == guess:
                return False

    # Check this for row
    for r in range(9):
        if puzzle[r][col] == guess:
            return False

    # Check this col
    for c in range(9):
        if puzzle[row][c] == guess:
            return False

    return True


def print_sudoku(puzzle):
    print("\n")
    for r in range(9):
        for c in range(9):
            print(f" {puzzle[r][c]} ", end="")
        
        print("\n")


def solve_sudoku(puzzle):
    # solve sudoku using a backtracking technique
    # pass in a 2d array for a 9x9 grid
    # return wether the solution exists
    # mutates the list if there is a solution

    # Step 1: choose somehwere on the puzzle to guess
    row, col = find_next_empty_spot(puzzle)

    # Step 1.1: Puzzle is solved, end recursion
    if row is None:
        return True
    
    # Step 2: make the guess
    for guess in range(1, 10):
        # Step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # Step 3.1: if this is valid, then place it on the board
            puzzle[row][col] = guess
            
            # Step 4: recursively call this function
            if solve_sudoku(puzzle):
                return True

        # Step 5: wrong guess, backtrack and try new numbers
        puzzle[row][col] = 0 #reset this value

    # Step 6: after trying every single combination, there is no solution
    return False
    
if __name__ == '__main__':
    example_board = [
        [3, 9, 0,   0, 5, 0,   0, 0, 0],
        [0, 0, 0,   2, 0, 0,   0, 0, 5],
        [0, 0, 0,   7, 1, 9,   0, 8, 0],

        [0, 5, 0,   0, 6, 8,   0, 0, 0],
        [2, 0, 6,   0, 0, 3,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 4],

        [5, 0, 0,   0, 0, 0,   0, 0, 0],
        [6, 7, 0,   1, 0, 5,   0, 4, 0],
        [1, 0, 9,   0, 0, 0,   2, 0, 0]
    ]

    solve_sudoku(example_board)
    print_sudoku(example_board)
