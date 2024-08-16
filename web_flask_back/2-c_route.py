#!/usr/bin/python3
"""
0-hello_route module - host a simple app on local host using flask
"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """display Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hbnb_user(text):
    """variable ussage in flask"""
    text = text.replace('_', ' ')
    return f'C {escape(text)}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
