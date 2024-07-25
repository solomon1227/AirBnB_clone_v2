#!/usr/bin/python3
'''Start flask web application'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''Start minimal Flask web application:'''

    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    '''Routing function for /hbnb'''

    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
