#!/usr/bin/python3
"""
    Sript that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
import os
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """Method to filter places and states"""
    states = sorted(storage.all('State').values(), key=lambda x:x.name)
    cities = sorted(storage.all('City').values(), key=lambda x:x.name)
    amenities = sorted(storage.all('Amenity').values(), key=lambda x:x.name)
    return render_template('10-hbnb_filters.html', states=states, 
                           cities=cities, amenities=amenities)


@app.teardown_appcontext
def handle_teardown(self):
    """
        method to handle teardown
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
