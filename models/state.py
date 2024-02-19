#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

storageType = getenv('HBNB_TYPE_STORAGE')
class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column('name', String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if storageType == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        @property
        def cities(self):
            """getter function"""
            from models import storage
            my_cities = []
            all_cities = list(storage.all(cls='City').values())
            for city in all_cities:
                if city.state_id == self.id:
                    my_cities.append(city)
            return my_cities
