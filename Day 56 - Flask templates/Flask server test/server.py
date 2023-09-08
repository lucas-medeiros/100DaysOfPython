# @author   Lucas Cardoso de Medeiros
# @since    21/12/2022
# @version  1.0

# Flask server with files


from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
