from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/next')
def next():
    return 'Its Next Page'


if __name__ == '__main__':
    app.run()
