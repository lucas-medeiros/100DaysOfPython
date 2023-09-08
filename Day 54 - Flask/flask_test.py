# @author   Lucas Cardoso de Medeiros
# @since    16/12/2022
# @version  1.0

# Flask framework Hello World


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def say_bye():
    return 'Bye!'


if __name__ == "__main__":
    app.debug = True
    app.run()
