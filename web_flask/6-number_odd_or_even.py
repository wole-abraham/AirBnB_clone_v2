#!/usr/bin/python3
""" Pyhton script that uses flask routes"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    return f"C {text.replace('_', ' ')}"


@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number():
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_temp(n):
    return render_template('6-number_odd_or_even.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_oe(n):
    if n % 2 == 0:
        result = f'{n} is even'
    else:
        result = f'{n} is odd'
    return render_template('6-number_odd_or_even.html', n=n, result=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
