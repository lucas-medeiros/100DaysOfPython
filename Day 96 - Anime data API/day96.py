# @author   Lucas Cardoso de Medeiros
# @since    29/08/2023
# @version  1.0


"""Build a custom website using an API that you find interesting.

Using what you have learnt about HTTP request and REST APIs, in today's project you will build a website that uses
data from a public API. For example, previously we created a rain alert app using a weather API. We also created an
ISS tracker and looking into Bitcoin prices, all using a public API. Today you get to work on an API that you find
interesting and build a service or website based on that API."""

from flask import Flask, render_template
import requests


app = Flask(__name__)

API_BASE_URL = "https://api.jikan.moe/v4"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/anime/<int:show_id>", methods=["GET"])
def get_by_id(show_id):
    response = requests.get(f"{API_BASE_URL}/anime/{show_id}")
    return response.json(), 200


@app.route("/anime/<int:show_id>/full", methods=["GET"])
def get_full_by_id(show_id):
    response = requests.get(f"{API_BASE_URL}/anime/{show_id}/full")
    return response.json(), 200


@app.route("/anime/<int:show_id>/characters", methods=["GET"])
def get_characters(show_id):
    response = requests.get(f"{API_BASE_URL}/anime/{show_id}/characters")
    return response.json(), 200


@app.route("/anime/<int:show_id>/staff", methods=["GET"])
def get_staff(show_id):
    response = requests.get(f"{API_BASE_URL}/anime/{show_id}/staff")
    return response.json(), 200


@app.route("/anime/<int:show_id>/episodes", methods=["GET"])
def get_episodes(show_id):
    response = requests.get(f"{API_BASE_URL}/anime/{show_id}/episodes")
    return response.json(), 200


@app.route("/anime/<int:show_id>/news", methods=["GET"])
def get_news(show_id):
    response = requests.get(f"{API_BASE_URL}/anime/{show_id}/news")
    return response.json(), 200


@app.route("/anime/<int:show_id>/pictures", methods=["GET"])
def get_pictures(show_id):
    response = requests.get(f"{API_BASE_URL}/anime/{show_id}/pictures")
    return response.json(), 200


@app.route("/anime/<int:show_id>/statistics", methods=["GET"])
def get_statistics(show_id):
    response = requests.get(f"{API_BASE_URL}/anime/{show_id}/statistics")
    return response.json(), 200


@app.route("/anime/<int:show_id>/reviews", methods=["GET"])
def get_reviews(show_id):
    response = requests.get(f"{API_BASE_URL}/anime/{show_id}/reviews")
    return response.json(), 200


@app.route("/anime/<int:show_id>/themes", methods=["GET"])
def get_themes(show_id):
    response = requests.get(f"{API_BASE_URL}/anime/{show_id}/themes")
    return response.json(), 200


@app.route("/anime/search/<string:q>", methods=["GET"])
def search_anime(q):
    query = q.replace(" ", "%20")
    response = requests.get(f"{API_BASE_URL}/anime?q={query}&sfw&limit=10&order_by=rank&sort=desc")
    return response.json(), 200


@app.route("/characters/search/<string:q>", methods=["GET"])
def search_character(q):
    query = q.replace(" ", "%20")
    response = requests.get(f"{API_BASE_URL}/characters?q={query}&sfw&limit=10")
    return response.json(), 200


@app.route("/genres/anime", methods=["GET"])
def list_genres():
    response = requests.get(f"{API_BASE_URL}/genres/anime")
    return response.json(), 200


@app.route("/producers/search", methods=["GET"])
def search_producers():
    response = requests.get(f"{API_BASE_URL}/producers?limit=10&order_by=mal_id&sort=asc")
    return response.json(), 200


@app.route("/anime/random", methods=["GET"])
def get_random_anime():
    response = requests.get(f"{API_BASE_URL}/random/anime")
    return response.json(), 200


@app.route("/character/random", methods=["GET"])
def get_random_character():
    response = requests.get(f"{API_BASE_URL}/random/characters")
    return response.json(), 200


@app.route("/recommendations", methods=["GET"])
def get_recent_recommendations():
    response = requests.get(f"{API_BASE_URL}/recommendations/anime")
    return response.json(), 200


@app.route("/season/current", methods=["GET"])
def get_airing_shows():
    response = requests.get(f"{API_BASE_URL}/seasons/now")
    return response.json(), 200


@app.route("/season/upcoming", methods=["GET"])
def get_upcoming_season():
    response = requests.get(f"{API_BASE_URL}/seasons/upcoming")
    return response.json(), 200


if __name__ == '__main__':
    app.run(debug=True)
