# @author   Lucas Cardoso de Medeiros
# @since    10/06/2022
# @version  1.0

# Blind auction


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bids = {}
finished = False
name = ""
value = 0.0


def find_winner():
    highest = 0.0
    winner = ""
    for element in bids:
        if highest < bids[element]:
            highest = bids[element]
            winner = element
    return winner, highest


print(logo + '\n')

while not finished:
    name = input("What is your name?: ")
    value = round(float(input("What is your bid? $")), 2)
    if value > 0:
        bids[name] = value
    else:
        print("Error, invalid bid value")
    if input("Are there any other bidders? Type 'yes' or 'no'.\n") == 'no':
        finished = True
winner, highest = find_winner()
print(f"\nThe winner is {winner}, with a bid of ${highest}")


