#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(string(128), nullable=False)
    cities = relationship(''City), backref='state', cascade='all, delete')
