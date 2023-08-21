# @author   Lucas Cardoso de Medeiros
# @since    19/08/2023
# @version  1.0

"""Build a website that lists cafes with Wi-Fi and power for remote working.

On day 66, we create an API that serves data on cafes with Wi-Fi and good coffee. Today, you're going to use the data
from that project to build a fully-fledged website to display the information.

Included in this assignment is an SQLite database called cafes.db that lists all the cafe data.

Using this database and what you learnt about REST APIs and web development, create a website that uses this data. It
should display the cafes, but it could also allow people to add new cafes or delete cafes.

For example, this startup in London has a website that does exactly this:

https://laptopfriendly.co/london"""


from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)

API_KEY = "TopSecretAPIKey"


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


def map_to_json(cafe):
    return jsonify(name=cafe.name,
                   map_url=cafe.map_url,
                   img_url=cafe.img_url,
                   location=cafe.location,
                   seats=cafe.seats,
                   has_toilet=cafe.has_toilet,
                   has_wifi=cafe.has_wifi,
                   has_sockets=cafe.has_sockets,
                   can_take_calls=cafe.can_take_calls,
                   coffee_price=cafe.coffee_price)


# HTTP GET - Read Record
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get/<int:id>", methods=["GET"])
def get(id):
    cafe = db.get_or_404(Cafe, id)
    return render_template("cafe.html", cafe=cafe)


@app.route("/random")
def get_random():
    all_cafes = db.session.query(Cafe).all()
    cafe = random.choice(all_cafes)
    return redirect(f"/get/{cafe.id}")


@app.route("/all")
def get_all():
    all_cafes = db.session.query(Cafe).all()
    result = [cafe.to_dict() for cafe in all_cafes]
    return render_template("all.html", cafes=result)


@app.route("/search")
def search():
    query_location = request.args.get("loc")
    cafes = db.session.query(Cafe).filter(Cafe.location.like(f"%{query_location}%"))
    result = [cafe.to_dict() for cafe in cafes]
    if result:
        return render_template("search.html", cafes=result, error=None), 200
    else:
        error_message = "Sorry, we don't have a cafe at that location."
        return render_template("search.html", cafes=None, error=error_message), 404


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_cafe = Cafe(name=request.form.get("name"),
                        map_url=request.form.get("map_url"),
                        img_url=request.form.get("img_url"),
                        location=request.form.get("location"),
                        seats=request.form.get("seats"),
                        has_toilet=bool(request.form.get("has_toilet")),
                        has_wifi=bool(request.form.get("has_wifi")),
                        has_sockets=bool(request.form.get("has_sockets")),
                        can_take_calls=bool(request.form.get("can_take_calls")),
                        coffee_price=request.form.get("coffee_price"))
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(f"/get/{new_cafe.id}")
    return render_template("add.html")


@app.route("/update-price/<int:id>", methods=["GET", "PATCH"])
def update_price(id):
    cafe_to_update = db.get_or_404(Cafe, id)
    if request.method == "PATCH":
        cafe_to_update.coffee_price = request.form.get("new_price")
        db.session.commit()
        return jsonify(response={"success": True, "cafe": cafe_to_update.to_dict()}), 200
    return render_template("update_price.html", cafe=cafe_to_update)


@app.route("/report-closed/<int:id>", methods=["GET", "DELETE"])
def report_closed(id):
    cafe_to_delete = db.get_or_404(Cafe, id)
    if request.method == "DELETE":
        if request.form.get("api_key") == API_KEY:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": True}), 200
        else:
            return jsonify(response={"success": False}), 403
    return render_template("report_closed.html", cafe=cafe_to_delete)


if __name__ == '__main__':
    app.run(debug=True)
