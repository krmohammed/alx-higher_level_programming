#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(State(name='Louisiana'))
    added = session.query(State).filter(State.name == 'Louisiana').first()
    print(added.id)
    session.commit()
