# @author   Lucas Cardoso de Medeiros
# @since    12/06/2022
# @version  1.0

# Calculator


import math

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def power(a, b):
    return a ** b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
}


if __name__ == '__main__':
    finished = False
    answer, a, b = math.inf, 0.0, 0.0
    op = ''
    while not finished:
        print(logo)
        if answer == math.inf:
            a = float(input("What's the first number? "))
        else:
            print(f"First number: {a}")
        for symbol in operations:
            print(symbol)
        op = input("Pick an operation: ")
        if op not in operations:
            print("Invalid operation\nOperation selected: +")
            op = '+'
        b = float(input("What's the next number? "))
        function = operations[op]
        answer = function(a, b)
        print(f"{a} {op} {b} = {answer}")
        new = input(f"Type 'y' to continue calculating with {answer}, type 'new' to start a new calculation, "
                    "or 'exit' to quit:\n")
        if new == 'exit':
            finished = True
        elif new == 'new':
            answer = math.inf
        else:
            a = answer
