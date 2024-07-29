#!/usr/bin/python3
""" script starts a flask server """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def page_root():
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def page_hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def page_text(text):
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_page(text):
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
