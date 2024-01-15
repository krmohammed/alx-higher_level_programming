#!/usr/bin/python3
"""
contains the class definition of a State and an instance
Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """
    State class mapping to a `states` table
    """
    __tablename__ = 'states'

    id = Column(
            'id', Integer,
            primary_key=True, nullable=False,
            autoincrement=True
            )
    name = Column('name', String(128), nullable=False)