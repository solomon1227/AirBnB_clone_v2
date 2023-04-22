#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if models.storage_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
    else:
        name = ""

