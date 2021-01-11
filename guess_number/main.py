import random

def guess(x):
    random_number = random.randint(1, x)

    # Guess can only start greater than 1
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)

        if guess < random_number:
            print("Sorry guess again, too low..")
        elif guess > random_number:
            print("Sorry guess again, too high..")

    print(f"Congrats, you have guessed {random_number}!")

print("Find the computers secret number...")
guess(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if low != high:
            # The bounds will be updated each guess
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C): ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"The computer found your number: {x}")

print("Let the computer guess your secret number")
computer_guess(int(input("Pick a number greater than 0: ")))
