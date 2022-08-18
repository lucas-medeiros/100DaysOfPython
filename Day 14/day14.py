# @author   Lucas Cardoso de Medeiros
# @since    15/06/2022
# @version  1.0

# Higher or Lower
import random
from includes import logo, vs, data


def random_celeb():
    """Return a random entry from data"""
    return random.choice(data)


def check_correct(a, b, guess):
    """Returns True if guess was correct and False if it was wrong"""
    if guess == 'A' and a['follower_count'] > b['follower_count']:
        return True
    elif guess == 'B' and a['follower_count'] < b['follower_count']:
        return True
    else:
        return False


def game():
    """Main game logic"""
    print(logo)
    correct = True
    score = 0
    a = random_celeb()
    b = a
    while correct:
        while a == b:
            b = random_celeb()

        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.\n")

        guess = input("Who has more followers? Type 'A' or 'B': ")
        if guess != 'A' and guess != 'B':
            print("Error. Invalid input\n")
            return

        correct = check_correct(a, b, guess)
        if correct:
            score += 1
            a = b
            print(f"\nYou're right!. Current score: {score}.\n")

    print(f"\nSorry, that's wrong. Final score: {score}\n")
    return


if __name__ == '__main__':
    while input("Do you want to play a game of Higher or Lower? Type 'y' or 'n': ") == 'y':
        game()
