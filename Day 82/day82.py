# @author   Lucas Cardoso de Medeiros
# @since    15/08/2023
# @version  1.0

""" You will use what you've learnt to create a text-based (command line) program that takes any String input and
converts it into Morse Code."""

import re
import sys


def create_dict():
    return {'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----',
            ' ': ' '}


def convert_to_morse_code(string_to_convert):
    if not string_to_convert.isalnum():
        string_to_convert = re.sub('[^A-Za-z0-9]+', '', string_to_convert)
    code = create_dict()
    string_morse = ""
    try:
        for char in string_to_convert:
            string_morse += code[char] + ' '
    except KeyError:
        print("[Error] Invalid characters found")
    return string_morse


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("[Error] Usage: python day82.py {string_to_convert}")
        exit(-1)

    print(convert_to_morse_code(sys.argv[1].upper()))
