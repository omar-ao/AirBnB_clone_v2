#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Returns greeting"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """display “C ” followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
def python_is_text(text="is cool"):
    """Displays “Python ” followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/python", strict_slashes=False)
def python_is_cool():
    """Displays python is cool"""
    return "Python is cool"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
