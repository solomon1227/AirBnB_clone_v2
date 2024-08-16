#!/usr/bin/python3
"""
    Sript that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.amenity import Amenity
import os
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Method to filter places and states"""
    states = sorted(storage.all('State').values(), key=lambda x:x.name)
    cities = sorted(storage.all('City').values(), key=lambda x:x.name)
    places = sorted(storage.all('Place').values(), key=lambda x:x.name)
    amenities = sorted(storage.all('Amenity').values(), key=lambda x:x.name)
    users = storage.all('User').values()
    return render_template('100-hbnb.html', states=states, 
                           cities=cities, places=places,
                           amenities=amenities, users=users)


@app.teardown_appcontext
def handle_teardown(self):
    """
        method to handle teardown
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
