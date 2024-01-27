from Guessing_Art import logo
from random import randint
print(logo)

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(answer, guess, turns):
    """Checks answer against guess. Returns the number of turns remaining"""
    if guess > answer:
        print("TOO HIGH")
        return turns - 1
    elif guess < answer:
        print("TOO LOW")
        return turns - 1
    else:
        print(f"You got it correct! The answer was {answer}")

def set_difficulty():
    level = input("Chose a difficulty, type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print("Welcome to the Guessing Game!!")
    print("I'm thinking of a number between 1 - 100")
    answer = randint(1, 100)

    turns = set_difficulty()

    

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number. ")
        guess = int(input("Make a guess: "))
        turns = check_answer(answer, guess, turns)

        if turns == 0:
            print("You have ran out of guess, you lose")
            return

game()