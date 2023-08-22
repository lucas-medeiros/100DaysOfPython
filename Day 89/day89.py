# @author   Lucas Cardoso de Medeiros
# @since    21/08/2023
# @version  1.0

"""Today, you are going to build a to-do list website. This is a rite of passage for any developer.
You can choose the type of to-do list you want to build. It could be as simple as a website where you can list some
items and cross them out. Or as complex as a Kanban-style task list like Trello."""

from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3


def create_db():
    # Connect to the database (creates a new database file if not exists)
    conn = sqlite3.connect("instance/tasks.db")

    # Create a cursor
    cursor = conn.cursor()

    # Create a table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY NOT NULL,
            description TEXT NOT NULL,
            due_date DATETIME,
            is_done INTEGER NOT NULL DEFAULT 0,
            is_favorite INTEGER NOT NULL DEFAULT 0,
            color_tag TEXT NOT NULL DEFAULT "#ffffff",
            "order" INTEGER NOT NULL
        )
    """)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Database created successfully.")


# create_db()

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250), nullable=False)
    due_date = db.Column(db.DateTime, nullable=True)
    is_done = db.Column(db.Boolean, default=False)
    is_favorite = db.Column(db.Boolean, default=False)
    color_tag = db.Column(db.String(10), default="#ffffff")
    order = db.Column(db.Integer, nullable=False, unique=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


def get_next_order():
    last_task = Task.query.order_by(Task.order.desc()).first()
    if last_task:
        return last_task.order + 1
    return 1


@app.route('/')
def home():
    tasks = Task.query.order_by(Task.order).all()
    return render_template('index.html', tasks=tasks)


@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        new_task = Task(description=request.form.get("description"),
                        order=get_next_order())
        db.session.add(new_task)
        db.session.commit()
        return jsonify(response={"success": True, "task": new_task.to_dict()})
    return redirect(url_for("home"))


@app.route("/mark-done/<int:id>", methods=["GET", "POST"])
def mark_done_task(id):
    if request.method == "POST":
        task = db.get_or_404(Task, id)
        task.is_done = not task.is_done
        db.session.commit()
        return jsonify(response={"success": True, "task": task.to_dict()})
    return redirect(url_for("home"))


@app.route("/toggle-favorite/<int:id>", methods=["GET", "POST"])
def toggle_favorite_task(id):
    if request.method == "POST":
        task = db.get_or_404(Task, id)
        task.is_favorite = not task.is_favorite
        db.session.commit()
        return jsonify(response={"success": True, "task": task.to_dict()})
    return redirect(url_for("home"))


@app.route("/update-due-date/<int:id>", methods=["GET", "POST"])
def update_due_date(id):
    if request.method == "POST":
        task = db.get_or_404(Task, id)
        new_due_date = datetime.strptime(request.form.get("new_due_date"), '%Y-%m-%dT%H:%M')
        task.due_date = new_due_date
        db.session.commit()
        return jsonify(response={"success": True, "task": task.to_dict()})
    return redirect(url_for("home"))


@app.route("/update-color-tag/<int:id>", methods=["GET", "POST"])
def update_color_tag(id):
    if request.method == "POST":
        task = db.get_or_404(Task, id)
        task.color_tag = request.form.get("new_color_tag")
        db.session.commit()
        return jsonify(response={"success": True, "task": task.to_dict()})
    return redirect(url_for("home"))


@app.route("/delete/<int:id>", methods=["GET", "DELETE"])
def delete_task(id):
    if request.method == "DELETE":
        task_to_delete = db.get_or_404(Task, id)
        db.session.delete(task_to_delete)
        db.session.commit()
        return jsonify(response={"success": "Task deleted successfully"})
    return redirect(url_for("home"))



if __name__ == '__main__':
    app.run(debug=True)
