# @author   Lucas Cardoso de Medeiros
# @since    13/06/2022
# @version  1.0

# Blackjack

import random

# Achar um jeito melhor de fazer com lista de listas
deck = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

suits = ['♣', '♦', '♥', '♠']


def random_card():
    return random.choice(list(deck))


def hand_score(hand):
    score = 0
    for card in hand:
        score += deck[card]
    if score > 21:
        score = -1
    return score


def pc_hand(pc_cards):
    hand = pc_cards
    score = 0
    while score < 17 and score != -1:
        hand.append(random_card())
        score = hand_score(hand)
    return hand


def check_win(player_hand, pc_hand):
    player_score = hand_score(player_hand)
    pc_score = hand_score(pc_hand)
    if player_score > pc_score:
        return 1
    elif player_score == pc_score:
        return 0
    else:
        return -1


def blackjack():
    player_cards, pc_cards = [], []
    for i in range(2):
        player_cards.append(random_card())
    pc_cards.append(random_card())
    hit = True
    while hit:
        print(f"Your cards: {player_cards}")
        print(f"Computer's first card: {pc_cards}")
        if input("Type 'y' to get another card, or 'n' to pass: ") == 'y':
            player_cards.append(random_card())
        else:
            hit = False
    print(f"Your final hand: {player_cards}")
    pc_cards = pc_hand(pc_cards)
    print(f"Computer's final hand: {pc_cards}")
    win = check_win(player_cards, pc_cards)
    if win == 1:
        print("You win!")
    elif win == 0:
        print("Draw")
    else:
        print("The Computer wins!")


if __name__ == '__main__':
    finished = False
    while not finished:
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'n':
            finished = True
        else:
            blackjack()
