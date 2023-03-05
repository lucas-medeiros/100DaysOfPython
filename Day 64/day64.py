# @author   Lucas Cardoso de Medeiros
# @since    03/03/2023
# @version  1.0

# My TOP 10 movies Website


from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.exc import IntegrityError
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

API_KEY = "35885e6820bba6e5509cd4dd7197060f"
SEARCH_MOVIE_API_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DETAILS_API_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-movies-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(512), nullable=True)
    img_url = db.Column(db.String(250), nullable=True)


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


with app.app_context():
    db.create_all()

    # """Inserts first movie"""
    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an
    #                 extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with
    #                 the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    # db.session.add(new_movie)
    # db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        parameters = {
            "api_key": API_KEY,
            "query": movie_title
        }
        response = requests.get(url=SEARCH_MOVIE_API_URL, params=parameters)
        response.raise_for_status()
        data = response.json()["results"]
        return render_template('select.html', options=data)
    return render_template('add.html', form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    parameters = {
        "api_key": API_KEY
    }
    response = requests.get(url=f"{MOVIE_DETAILS_API_URL}/{movie_api_id}", params=parameters)
    response.raise_for_status()
    data = response.json()
    try:
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            description=data["overview"],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
        )
        db.session.add(new_movie)
        db.session.commit()
    except IntegrityError:
        print("Record already on database")
        return redirect(url_for('home'))
    return redirect(url_for("rate_movie", id=new_movie.id))


@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    movie_to_delete = Movie.query.get(request.args.get('id'))
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
