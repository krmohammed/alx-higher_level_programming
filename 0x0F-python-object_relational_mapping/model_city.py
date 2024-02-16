#!/usr/bin/python3
"""
class definition for City class
"""
from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base, State


class City(Base):
    """
    city class -> city table
    """
    __tablename__ = 'cities'

    id = Column('id', Integer, unique=True, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer,
                      ForeignKey('states.id'),
                      nullable=False)
