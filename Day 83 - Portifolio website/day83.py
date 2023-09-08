# @author   Lucas Cardoso de Medeiros
# @since    15/08/2023
# @version  1.0

""" Using what you have learnt about web development, build your own portfolio website. This can be designed any way
you want. It's the place to show off your skills and the things you've built. Take inspiration from other developers
but try not to copy their designs. Because this is about showing off what you can do! Use what you've learnt from Day
65 and plan out your website. Think about design, UI, UX, colour schemes, fonts. Don't build the website for other
people, build it to make yourself proud. """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
