# @author   Lucas Cardoso de Medeiros
# @since    10/06/2022
# @version  1.0

# Caesar cipher

import string


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = [char for char in string.ascii_lowercase]


def chiper(word, shift, encode):
    encoded = ""
    for char in word:
        if char not in alphabet:
            encoded += char
        else:
            if encode:
                new_letter = alphabet.index(char) + shift
                if new_letter >= len(alphabet):
                    new_letter -= len(alphabet)
            else:
                new_letter = alphabet.index(char) - shift
                if new_letter < 0:
                    new_letter += len(alphabet)
            encoded += alphabet[new_letter]
    return encoded


print(logo)
game_finished = False
mode, message, end_game = "", "", ""
shift = 0
while not game_finished:
    mode = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n")
    message = input("Type your message:\n")
    shift = int(input("Enter the shift number\n"))
    print(f"Here's the {mode}d result: {chiper(message, shift, mode == 'encode')}")
    if input("Type 'yes' if you want to go again. Otherwise type 'no'\n") != "yes":
        game_finished = True
print("Goodbye!")

