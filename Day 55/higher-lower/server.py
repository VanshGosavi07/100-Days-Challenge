import random

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1 style='text-align:center'>Guess a number between 0 and 9</h1>" \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="its image" style="margin-left:40%">'


number = random.randint(0, 10)


@app.route('/guess/<int:num>')
def guess(num):
    if num > number:
        return f"<h1 style='text-align:center'>{num} is too greater</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif num == number:
        return f"<h1 style='text-align:center'>You found correct number {num}</h1>" \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    else:
        return f"<h1 style='text-align:center'>{num} is too low</h1>" \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)
