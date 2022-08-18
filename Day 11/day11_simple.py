# @author   Lucas Cardoso de Medeiros
# @since    14/06/2022
# @version  1.0

# Blackjack simple version

import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal():
    """Returns a random card"""
    return random.choice(deck)


def get_score(hand):
    """Returns the total score of a given hand"""
    score = sum(hand)
    if score > 21 and 11 in hand:
        score -= 10
    return score


def deal_hand(cards):
    """Return a random full hand, given the first card"""
    hand = cards
    score = 0
    while score < 17:
        hand.append(deal())
        score = get_score(hand)
    return hand


def hit(player_hand, pc_hand):
    """Insert new cards in player's hand while player hits"""
    hit = True
    while hit:
        print(f"\tYour cards: {player_hand}, current score: {get_score(player_hand)}")
        print(f"\tComputer's first card: {pc_hand}, current score: {get_score(pc_hand)}\n")
        if input("Type 'y' to get another card, or 'n' to pass: ") == 'y':
            player_hand.append(deal())
        else:
            hit = False
    return player_hand


def check_win(player_hand, pc_hand):
    """Verify the winner and print the result"""
    player_score = get_score(player_hand)
    pc_score = get_score(pc_hand)
    if player_score == pc_score:
        print("Draw, no one wins!  =/")
    elif pc_score == 21:
        print("Your opponent has a blackjack! You lose! =(")
    elif player_score == 21:
        print("You have a blackjack! You win! =)")
    elif player_score > 21:
        print("You went over. You lose! =(")
    elif pc_score > 21:
        print("Your opponent went over. You win! =)")
    elif player_score > pc_score:
        print("Your score is higher. You win! =)")
    else:
        print("Your score is lower. You lose! =(")


def blackjack():
    """Main game logic"""
    print("\n" + logo + "\n")
    player_hand, pc_hand = [], []
    for i in range(2):
        player_hand.append(deal())
    pc_hand.append(deal())

    player_hand = hit(player_hand, pc_hand)
    pc_hand = deal_hand(pc_hand)

    print(f"\tYour final hand: {player_hand}, final score: {get_score(player_hand)}")
    print(f"\tComputer's final hand: {pc_hand}, final score: {get_score(pc_hand)}\n")

    check_win(player_hand, pc_hand)


if __name__ == '__main__':
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        blackjack()
