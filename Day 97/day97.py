# @author   Lucas Cardoso de Medeiros
# @since    31/08/2023
# @version  1.0


"""An eCommerce website with payment processing.

Using what you have learnt by building the blog website using Flask, you're now going to build your own eCommerce
website. Your website needs to have a working cart and checkout. It should be able to display items for sale and take
real payment from users. It should have login/registration authentication features.
Here is an example website: https://store.waitbutwhy.com/
You should consider using the Stripe API: https://stripe.com/docs/payments/checkout"""


from flask import Flask, render_template, request, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import sqlite3


def create_db():
    # Connect to the database (creates a new database file if not exists)
    conn = sqlite3.connect("instance/ecommerce.db")

    # Create a cursor
    cursor = conn.cursor()

    # Create a table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            name TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS item (
            id INTEGER PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            price NUMERIC(10,2) NOT NULL DEFAULT 0,
            category TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cartItem (
            user_id INTEGER NOT NULL,
            item_id INTEGER NOT NULL,
            PRIMARY KEY (user_id, item_id),
            FOREIGN KEY (user_id) REFERENCES User (id),
            FOREIGN KEY (item_id) REFERENCES Item (id)
        )
    """)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Database created successfully.")


app = Flask(__name__)

app.config['SECRET_KEY'] = '59f8f539-2d86-4e60-ab70-19ef47d694b9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# db.init_app(app)

# LOGIN CONFIGURATION
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLES IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(256))
    cart = db.relationship('Item', secondary='cart_item', backref='users', lazy=True)

    def to_string(self):
        return f"{self.name} <{self.email}>"

    def get_id(self):
        return str(self.id)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    description = db.Column(db.String(2000))
    price = db.Column(db.Integer, nullable=False, default=0)
    category = db.Column(db.String(256))
    users = db.relationship('User', secondary='cart_item', backref='cart_items', lazy=True)


class CartItem(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route('/')
def home():
    items = Item.query.all()
    return render_template("index.html", items=items, logged_in=current_user.is_authenticated)


# noinspection PyArgumentList
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            password = generate_password_hash(request.form.get("password"), method="pbkdf2:sha256", salt_length=8)
            new_user = User(name=request.form['name'],
                            email=request.form['email'],
                            password=password)
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)
            return redirect(url_for("home"))

        except sqlite3.IntegrityError as ex:
            print(ex)
            return render_template("index.html", logged_in=current_user.is_authenticated)

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user:
            if check_password_hash(pwhash=user.password, password=password):  # Log in and authenticate user
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                flash('Email or password incorrect, please try again.')
                return render_template('login.html', logged_in=current_user.is_authenticated), 401
        else:
            flash("That email does not exist, please try again.")
            return render_template('login.html', logged_in=current_user.is_authenticated), 404

    return render_template('login.html', logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/add_item', methods=["GET", "POST"])
@login_required
def add_item():
    if request.method == "POST":
        new_item = Item(name=request.form['name'],
                        description=request.form['description'],
                        price=float(request.form['price']),
                        category=request.form['category'])
        db.session.add(new_item)
        db.session.commit()

        flash('Item added successfully!', 'success')
        return redirect(url_for('home'))

    return render_template("add_item.html", logged_in=current_user.is_authenticated)


@app.route('/add_to_cart/<int:item_id>')
@login_required
def add_to_cart(item_id):
    item = Item.query.get_or_404(item_id)
    current_user.cart_items.append(item)
    db.session.commit()
    flash('Item added to cart!', 'success')
    return redirect(url_for('home'))


@app.route('/cart')
@login_required
def cart():
    return render_template('cart.html', cart_items=current_user.cart_items)


if __name__ == "__main__":
    # create_db()  # First execution only
    app.run(debug=True, port=5001)
