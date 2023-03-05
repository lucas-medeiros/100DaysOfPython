# @author   Lucas Cardoso de Medeiros
# @since    03/03/2023
# @version  1.0

# Databases and with SQLite and SQLAlchemy


from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    """Read all DB records"""
    books = db.session.query(Book).all()
    return render_template("index.html", books=books)


@app.route('/add', methods=["GET", "POST"])
def add():
    """Add new Book record on DB table"""
    if request.method == "POST":
        new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=["GET", "POST"])
def edit():
    """Updates book's rating based on Id"""
    if request.method == "POST":
        book_to_update = Book.query.get(request.form["id"])
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_selected = Book.query.get(request.args.get('id'))
    return render_template("edit_rating.html", book=book_selected)


@app.route('/delete', methods=["GET", "POST"])
def delete():
    """Deletes book based on Id"""
    book_to_delete = Book.query.get(request.args.get('id'))
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
