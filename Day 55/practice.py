from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>' \
           '<p>My name is Kitty</p>' \
           '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjVpbWFkNXM5dWxyYjloeDZ2bG90MmMxY2Rmb3ZybHR0ZzQzY2pwMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EvYHHSntaIl5m/giphy.gif" width="700" height="450">'


@app.route('/username/<name>/<int:age>')
def username(name, age):
    return f'Hello {name} and i am {age} years old'


@app.route("/bye")
@make_bold
def bye():
    return "bye"


if __name__ == '__main__':
    app.run(debug=True)
