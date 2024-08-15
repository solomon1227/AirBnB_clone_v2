#!/usr/bin/python3
"""
    Sript that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
import os
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state_list():
    """
        method to render states from storage
    """
    states = sorted(storage.all('State').values(), key=lambda x: x.name)
    return render_template("9-states.html", states=states, id=None)


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """
        method to render states from storage
    """
    states = sorted(storage.all('State').values(), key=lambda x: x.name)
    for state in states:
        if state.id == id:
            cities = sorted(list(state.cities), key=lambda x: x.name)
            return render_template("9-states.html", state=state,
                                   cities=cities, id=id)
    return render_template("9-states.html", id='Not Found')


@app.teardown_appcontext
def handle_teardown(self):
    """
        method to handle teardown
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
