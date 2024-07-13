import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def blogs():
    response = requests.get(url="https://api.npoint.io/beed84b243f025b8b61c")
    response.raise_for_status()
    content = response.json()
    return render_template("index.html", post=content)

@app.route('/post/<int:id_post>')
def show_post(id_post):
    response = requests.get(url="https://api.npoint.io/beed84b243f025b8b61c")
    response.raise_for_status()
    content = response.json()
    return render_template("post.html", post=content,post_id=id_post)

if __name__ == "__main__":
    app.run(debug=True)
