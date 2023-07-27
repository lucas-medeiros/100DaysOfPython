# @author   Lucas Cardoso de Medeiros
# @since    25/07/2023
# @version  1.0

# RESTFUL API - London Cafes


from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)

API_KEY = "TopSecretAPIKey"


# Cafe TABLE Configuration
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


def get_json(cafe):
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


@app.route("/random")
def get_random_cafe():
    all_cafes = db.session.query(Cafe).all()
    cafe = random.choice(all_cafes)
    return get_json(cafe)


@app.route("/all")
def get_all_cafes():
    all_cafes = db.session.query(Cafe).all()
    result = [cafe.to_dict() for cafe in all_cafes]
    return jsonify(cafes=result)


@app.route("/search")
def search_cafe():
    query_location = request.args.get("loc")
    cafes = db.session.query(Cafe).filter(Cafe.location.like(f"%{query_location}%"))
    result = [cafe.to_dict() for cafe in cafes]
    if result:
        return jsonify(cafes=result)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


# HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add_cafe():
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
        return jsonify(response={"success": "Successfully added new Cafe", "cafe": new_cafe.to_dict()}), 200


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:id>", methods=["GET", "PATCH"])
def update_price(id):
    if request.method == "PATCH":
        cafe_to_update = db.get_or_404(Cafe, id)
        cafe_to_update.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price", "cafe": cafe_to_update.to_dict()}), 200


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:id>", methods=["GET", "DELETE"])
def report_closed(id):
    if request.args.get("api_key") == API_KEY:
        cafe_to_delete = db.get_or_404(Cafe, id)
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the closed Cafe"}), 200
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct API key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
