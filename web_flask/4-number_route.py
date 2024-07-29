#!/usr/bin/python3
"""Flasks python script """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def page_root():
    return "Hello HBNB"


@app.route("/hbnb")
def page_hbnb():
    return "HBNB"


@app.route("/c/<text>")
def page_txt(text):
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=True)
def page_python(text):
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
