#!/usr/bin/python3
'''Start flask web application'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''Start minimal Flask web application:'''

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Routing function for /hbnb'''

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''Display C followed by text variable, with _ replaced by Space'''

    text = text.replace('_', ' ')
    return f'C {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
