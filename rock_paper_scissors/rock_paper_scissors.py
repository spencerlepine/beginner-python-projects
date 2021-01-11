import random

def play():
    user = input("(R) for rock, (P) for paper, and (S) for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user ==  computer:
        return 'It\'s a tie!'

    elif iswin(user, computer):
        return 'You won!'
    
    return 'You lost :('

# Helper function
def iswin(player, opponent):
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())