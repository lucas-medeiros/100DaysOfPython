# @author   Lucas Cardoso de Medeiros
# @since    09/06/2022
# @version  1.0

# Random password generator

import random
import string

print("Welcome to the PyPassword Generator")

letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like in your password?\n"))
numbers = int(input("How many numbers would you like in your password?\n"))

symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

for i in range(letters):
    password.append(random.choice(string.ascii_letters))
for i in range(numbers):
    password.append(random.choice(string.digits))
for i in range(symbols):
    password.append(random.choice(symbols_list))

random.shuffle(password)
print(f"Your password is: {''.join(password)}")

