from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# all_books = []

# Setting the path to your SQLite database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/100 Days Challenge/Day 63/Database/books-collection.db'

# Suppress warning messages about the track modifications feature
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        book_to_update = Book.query.get(id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", current_book=Book.query.filter_by(id=id).first())


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    if request.method == "POST":
        book_to_delete = Book.query.get(id)
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("delete.html", current_book=Book.query.filter_by(id=id).first())


if __name__ == "__main__":
    app.run(debug=True)
