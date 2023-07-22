#!/usr/bin/python3
"""
0-hello_route module - host a simple app on local host using flask
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """minimal app defination"""
    return 'Hello HBNB!'
