#!/usr/bin/python3
""" class definition of a State instance """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """ State definition """
    __tablename__ = "states"
    id = Column(
            Integer, primary_key=True,
            unique=True, nullable=False,
            autoincrement=True
            )
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")
