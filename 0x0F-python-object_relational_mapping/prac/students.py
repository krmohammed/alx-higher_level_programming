#!/usr/bin/python3
"""
creates a student table
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Student(Base):
    """
    student table
    """

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    first_name = Column(String(128), nullable=False)
    other_names = Column(String(128), nullable=False)
    programme = Column(String(128), nullable=False)
    gender = Column(String(6), nullable=False)
    hall = Column(String(128))
