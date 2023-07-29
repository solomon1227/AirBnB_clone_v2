#!/usr/bin/python3
"""
0-hello_route module - host a simple app on local host using flask
"""
from flask import Flask, render_template
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
def c_fun(text):
    """variable ussage in flask"""
    text = text.replace('_', ' ')
    return f'C {escape(text)}'


@app.route("/python/", defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_cool(text):
    """variable ussage in flask"""
    text = text.replace('_', ' ')
    return f'Python {escape(text)}'


@app.route('/number/<int:n>', strict_slashes=False)
def display_num(n):
    """Display a number if only an integer"""
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html(n):
    '''Display html if num is int'''
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
