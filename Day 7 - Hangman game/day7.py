# @author   Lucas Cardoso de Medeiros
# @since    09/06/2022
# @version  1.0

# Hangman

from hangman_components import word_list, stages, logo
import random


def hint(word, guessed, lives):
    str = "\n"
    for char in word:
        if char in guessed:
            str += char
        else:
            str += '_'
        str += ' '
    print(str)
    print(stages[lives])


def check_win(word, guessed):
    for char in word:
        if char not in guessed:
            return False
    return True


def check_lost(lives):
    if lives > 0:
        return False
    else:
        return True


print(logo)

word = random.choice(word_list)
lives = len(stages) - 1
game_finished = False
guessed = []
letter = ''

print(f"Random word: {word}")

while not game_finished:
    hint(word, guessed, lives)
    letter = input("Guess a letter: ").lower()
    if letter in guessed:
        print(f"You already have guessed the letter '{letter}', try another one")
    else:
        guessed.append(letter)
        if letter in word:
            print(f"Nice guess, the letter '{letter}' is in the word")
            if check_win(word, guessed):
                print("\nCongratulations, you won!")
                game_finished = True
        else:
            print(f"Too bad, the letter '{letter}' isn't in the word, you lose a lives...")
            lives -= 1
            if check_lost(lives):
                print(f"\nGame over, you lost! \nThe word was: '{word}'")
                game_finished = True
hint(word, guessed, lives)
