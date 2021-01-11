import random
from words import words
import string

def get_usable_world(_words):
    random_word = random.choice(_words)

    while '-' in random_word or '_' in random_word:
         random_word = random.choice(_words)

    return random_word.upper()

def hangman_art(lives):
    pictures = ["\n      |-----} \n     (^^)   l\n     /| \   l\n    c |  c  l\n     / \    l\n    v   v   l\n            l\n    ________J\n",\
                "\n      |-----} \n     (--)   l\n     /| \   l\n      |     l\n     / \    l\n    v   v   l\n            l\n    ________J\n",\
                "\n      |-----} \n     ('')   l\n     /| \   l\n      |     l\n     / \    l\n            l\n            l\n    ________J\n",\
                "\n      |-----} \n     (oo)   l\n     /| \   l\n      |     l\n            l\n            l\n            l\n    ________J\n",\
                "\n      |-----} \n     (OO)   l\n      |     l\n      |     l\n            l\n            l\n            l\n    ________J\n",\
                "\n      |-----} \n     (XX)   l\n            l\n            l\n            l\n            l\n            l\n    ________J\n"]
    
    return pictures[6-lives]

def hangman():
    word = get_usable_world(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # Give the user the hangman picture
        print(hangman_art(lives))

        # letters used, ['a','b','cd'] -> 'a b cd'
        print(f'Lives: {lives} - ', 'You have used these letters: ', ' '.join(used_letters))

        # Revealed correct letters:
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        # Get the user input
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives-=1

        elif user_letter in used_letters:
            lives-=1
            print('You have already guessed that letter. Please try again')

        else:
            print('Invalid character. Please try again')

    # gets here when the hangman word has been guessed
    if lives == 0:
        print("You killed hangman! Better luck next time..")
    else:
        print(f"You solved for the word {word} and saved hangman!")

if __name__ == '__main__':
    hangman()