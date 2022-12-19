# @author   Lucas Cardoso de Medeiros
# @since    14/06/2022
# @version  1.0

# Number guessing game

import random

logo = """
   _____                       _   _                                  _               
  / ____|                     | | | |                                | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
"""

difficulty_levels = {
    "easy": 10,
    "medium": 7,
    "hard": 5
}


def set_difficulty():
    """Set game difficulty and returns the random_number os attempts"""
    difficulty = input("Choose a difficulty. Type 'easy', 'medium' or 'hard': ")
    if difficulty not in difficulty_levels:
        print("Error. Invalid difficulty. Selected easy instead")
        difficulty = "easy"
    return difficulty_levels[difficulty]


def random_number():
    """Returns a random random_number between 1 and 100"""
    return random.randint(1, 100)


def game():
    """Main game logic"""
    print("\n" + logo + "\nWelcome to the NUmber Guessing Game!\n")
    print("I'm thinking of a random_number between 1 and 100.")

    attempts = set_difficulty()
    number = random_number()

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess the random_number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}\n")
            return
        elif guess > number:
            print("Too high.\nGuess again.")
        else:
            print("Too low.\nGuess again.")
        attempts -= 1

    print(f"You lost! The answer was {number}\n")
    return


if __name__ == '__main__':
    while input("Do you want to play the 'Number Guessing Game'? Type 'y' or 'n': ") == 'y':
        game()
