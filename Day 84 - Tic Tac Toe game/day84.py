# @author   Lucas Cardoso de Medeiros
# @since    16/08/2023
# @version  1.0

"""Using what you have learnt about Python programming, you will build a text-based version of the Tic Tac Toe game.
The game should be playable in the command line just like the Blackjack game we created on Day 11 - Blackjack game. It should be a
2-player game, where one person is "X" and the other plays "O"."""

import random

PLAYERS = ['X', 'O']
BOARD = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]


def reset_board():
    """Restart board to original state at the start of the game"""
    global BOARD
    BOARD = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]


def check_win(player_symbol):
    """Check if given player won"""
    # Check rows
    for row in BOARD:
        if all(element == player_symbol for element in row):
            return True

    # Check columns
    for col in range(3):
        if all(BOARD[row][col] == player_symbol for row in range(3)):
            return True

    # Check diagonals
    if all(BOARD[i][i] == player_symbol for i in range(3)) or all(BOARD[i][2 - i] == player_symbol for i in range(3)):
        return True

    return False


def check_draw():
    """Check if game has ended with a draw: all elements in board are 'X' or 'O'"""
    return all(element != '-' for row in BOARD for element in row)


def print_board():
    """Displays current board on the prompt"""
    for row in BOARD:
        print(" | ".join(row))
        print("-" * 11)


def get_ai_move():
    """AI player make a random move on any of the available positions"""
    available_moves = [(row, col) for row in range(len(BOARD)) for col in range(len(BOARD[0]))
                       if BOARD[row][col] not in PLAYERS]
    return random.choice(available_moves)


def get_move(player_symbol, is_ai):
    """Get player move and register on the board"""
    while True:
        print(f"Player {player_symbol} turn")
        if not is_ai:
            row_move = int(input("Enter your row move (0, 1, 2): "))
            column_move = int(input("Enter your column move (0, 1, 2): "))
        else:
            row_move, column_move = get_ai_move()

        if BOARD[row_move][column_move] in PLAYERS:
            print("Invalid move, please enter again...")
        else:
            BOARD[row_move][column_move] = player_symbol
            return


def switch_current_player(current_player):
    """Switch player's turn"""
    if current_player == 'X':
        return 'O'
    else:
        return 'X'


def switch_current_ai(player_count, current_ai):
    """Switch IA flag for current turn"""
    if player_count != 1:
        return False
    return not current_ai


def tic_tac_toe(player_count):
    """Main tic-tac-toe game logic"""
    endgame = False
    current_ai = False
    current_player = 'X'
    reset_board()
    print("\n --- Game Start! ---\n")
    print_board()
    while not endgame:
        get_move(current_player, current_ai)
        print_board()

        if check_win(current_player):
            print(f"Player {current_player} wins!")
            endgame = True
        elif check_draw():
            print(f"It's a draw!")
            endgame = True
        else:
            current_player = switch_current_player(current_player)
            current_ai = switch_current_ai(player_count, current_ai)

    print("\n --- Game Over! ---\n")


if __name__ == '__main__':
    while True:
        if input("Do you want to play a game of tic-tac-toe? Type 'y' or 'n': ") == 'n':
            exit(1)

        tic_tac_toe(int(input("Enter the number of players (1 / 2): ")))
