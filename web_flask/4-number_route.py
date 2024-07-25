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

@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    '''
    Display "Python" followed by text variable, with _ replaced by Space
        - Default text is "is cool"
    '''

    text = text.replace('_', ' ')

    return f'Python {text}'


@app.route('/number/<int:n>')
def number(n):
    '''Display if n is an integer number only'''

    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
