#!/usr/bin/python3
"""Module State"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City, Base


class State(Base):
    """State class definition"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')
