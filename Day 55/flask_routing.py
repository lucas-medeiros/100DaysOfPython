# @author   Lucas Cardoso de Medeiros
# @since    19/12/2022
# @version  1.0

# Flask framework Routing


from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center;">Hello, World!</h1>' \
           '<p>This is a paragraph</p>'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return 'Bye!'


@app.route('/username/<name>/<int:random_number>')
def greet(name, number):
    return f"Hello {name}, you are {number} year old!"


if __name__ == "__main__":
    app.debug = True
    app.run()
