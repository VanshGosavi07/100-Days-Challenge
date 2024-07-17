# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
#
# cursor = db.cursor()
#
# # cursor.execute(
# #     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUE(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
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


# Ensure app context is pushed
with app.app_context():
    # Create all tables based on defined models
    db.create_all()

    # Add a new book entry to the database
    new_book = Book(id=2, title="ddsfs", author="J. K. Rowling", rating=7.5)
    db.session.add(new_book)
    db.session.commit()
