#!/usr/bin/python3
""" defines City class """
from relationship_state import Base, State
from sqlalchemy import String, Integer, Column, ForeignKey


class City(Base):
    """ City class """
    __tablename__ = "cities"

    id = Column(
            Integer, primary_key=True,
            nullable=False, unique=True,
            autoincrement=True
            )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
