# @author   Lucas Cardoso de Medeiros
# @since    12/12/2022
# @version  1.0

# Send post requests with Flask


from flask import Flask, render_template, request
import requests

posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    return render_template("login.html", name=request.form['username'], password=request.form['password'])


if __name__ == "__main__":
    app.run(debug=True)
