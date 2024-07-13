import datetime
import random

import requests
from flask import Flask, render_template

app = Flask('__name__')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/guess/<name>')
def guesses(name):
    response = requests.get(url=f"https://api.agify.io/?name={name}")
    response.raise_for_status()
    contents = response.json()
    names = contents['name']
    ages = contents['age']
    response = requests.get(url=f"https://api.genderize.io/?name={name}")
    response.raise_for_status()
    genders = response.json()["gender"]
    return render_template("index.html", name=names, gender=genders, age=ages)


@app.route('/blog')
def blogs():
    response = requests.get(url="https://api.npoint.io/beed84b243f025b8b61c")
    response.raise_for_status()
    content = response.json()
    return render_template("blog.html", post=content)


if __name__ == '__main__':
    app.run(debug=True)
