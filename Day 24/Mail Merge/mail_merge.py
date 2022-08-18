# @author   Lucas Cardoso de Medeiros
# @since    29/06/2022
# @version  2.0

# Mail merge script

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".


STARTING_LETTER_PATH = "./Input/Letters/starting_letter.txt"
NAME_LIST_PATH = "./Input/Names/invited_names.txt"

with open(file=STARTING_LETTER_PATH, mode="r") as starting_letter:
    letter_content = starting_letter.read()

with open(file=NAME_LIST_PATH, mode="r") as names_list:
    names = names_list.readlines()
    names = [name.rstrip() for name in names]

for name in names:
    letter = letter_content.replace("[name]", name)
    with open(file=f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(letter)
