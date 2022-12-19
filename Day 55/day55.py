# @author   Lucas Cardoso de Medeiros
# @since    19/12/2022
# @version  1.0

# Flask higher-lower game

import random
from flask import Flask

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1><b>Guess a random_number between 0 and 9</b></h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></img>'


@app.route('/<int:guess>')
def guess(guess):
    if guess > random_number:
        text = 'Too high, try again!'
        link = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
    elif guess < random_number:
        text = 'Too low, try again!'
        link = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
    else:
        text = 'You found me!'
        link = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
    return f'<h1 style="color: red;">{text}</h1><img src="{link}"/>'


if __name__ == "__main__":
    app.debug = True
    app.run()
