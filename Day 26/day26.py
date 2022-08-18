# @author   Lucas Cardoso de Medeiros
# @since    01/07/2022
# @version  1.0

# NATO Alphabet Project

import pandas


# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
word = ""
while word != "EXIT":
    word = input("Enter a word: ").upper().replace(' ', '')
    letters = [letter for letter in word]
    nato_list = [value for (key, value) in nato_dict.items() if key in letters]
    print(nato_list)
