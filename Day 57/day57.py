# @author   Lucas Cardoso de Medeiros
# @since    21/12/2022
# @version  1.0
# Flask server with files


from flask import Flask
from flask import render_template
from datetime import date
import requests
from post import Post
from requests import HTTPError

AGIFY_URL = "https://api.agify.io"
GENDERIZE_URL = "https://api.genderize.io"
BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/guess/<name>')
def guess(name):
    age = get_prop(AGIFY_URL, name, "age")
    gender = get_prop(GENDERIZE_URL, name, "gender")
    return render_template("guess.html", year=date.today().year, name=name.title(), age=age, gender=gender)


@app.route('/blog')
def blog():
    all_posts = get_blog_posts()
    return render_template("index.html", posts=all_posts)


@app.route('/blog/post/<int:id>')
def get_post(id):
    post = get_blog_post_by_id(id)
    return render_template("post.html", post=post)


def get_blog_posts():
    try:
        response = requests.get(f"{BLOG_URL}")
        response.raise_for_status()
        posts = response.json()
        post_list = []
        for post in posts:
            post_list.append(Post(post["id"], post["title"], post["subtitle"], post["body"]))

        return post_list
    except HTTPError as e:
        print("Error: " + str(e))


def get_blog_post_by_id(id):
    try:
        response = requests.get(f"{BLOG_URL}")
        response.raise_for_status()
        posts = response.json()
        for post in posts:
            if post["id"] == id:
                return Post(post["id"], post["title"], post["subtitle"], post["body"])

        return None
    except HTTPError as e:
        print("Error: " + str(e))


def get_prop(url, name, prop):
    try:
        response = requests.get(f"{url}/?name={name}")
        response.raise_for_status()
        print(response.text)
        data = response.json()
        return data[prop]
    except HTTPError as e:
        print("Error: " + str(e))


if __name__ == "__main__":
    app.debug = True
    app.run()
