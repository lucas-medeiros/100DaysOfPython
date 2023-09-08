# @author   Lucas Cardoso de Medeiros
# @since    03/06/2022
# @version  1.0

# Rock, Paper and Scissors

# Rules:
# Rock     (0) wins from: Scissors (2) e (3) Lizard
# Paper    (1) wins from: Rock     (0) e (4) Spock
# Scissors (2) wins from: Paper    (1) e (3) Lizard
# Lizard   (3) wins from: Spock    (4) e (1) Paper
# Spock    (4) wins from: Scissors (2) e (0) Rock

# 0 - Rock
# 1 - Paper
# 2 - Scissors
# 3 - Lizard
# 4 - Spock

import random

play = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
win = [
            [2, 3],
            [0, 4],
            [1, 3],
            [1, 4],
            [0, 2]
        ]
players = int(input("How many players? "))
print('''Options:
        0 - Rock
        1 - Paper
        2 - Scissors
        3 - Lizard
        4 - Spock''')
print()
p1 = int(input('Player 1: '))
if players == 1:
    p2 = random.randint(0, 4)
else:
    p2 = int(input('Player 2: '))

if p1 < 0 or p2 < 0 or p1 >= len(play) or p2 >= len(play):
    print('Error')
    exit(-1)

print(f'P1: {play[p1]}')
print(f'P2: {play[p2]}')
print()

if p1 == p2:
    print('DRAW')
else:
    for i in win[p1]:
        if i == p2:
            print('Player 1 wins!')
            exit(1)
    print('Player 2 wins!')
    exit(2)


