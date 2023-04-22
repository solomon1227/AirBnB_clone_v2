#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if models.storage_type == "db":
        __tablename__ = "cities"

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('State.states.id'), nullable=False)
        state = relationship('State', back_populates='cities')
    else:
        name = ""
        state_id = ""

if models.storage_type == "db":
    State.cities = relationship("City", order_by=City.id, back_populates='state')
else:
    @property
    def cities(self):
        """getter for list of city instances related to the state"""
        city_list = []
        all_cities = models.storage.all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list