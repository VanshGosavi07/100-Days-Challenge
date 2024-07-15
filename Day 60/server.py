from flask import request

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def receive_data():
    name = request.form["name"]
    number = request.form["number"]
    email = request.form["email"]
    return render_template("login.html", name=name, number=number, email=email)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
