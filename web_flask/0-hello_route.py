#!/usr/bin/python3
""" script that starts a flash application """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "<p>Hello HBNB!</p>"
