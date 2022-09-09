#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the database hbtn_0e_6_usa
takes 3 arguments: mysql username, mysql password and database name
"""

import sys

from sqlalchemy.orm.session import Session
from model_state import Base, State
from sqlalchemy import create_engine


def a_objects():
    """ defining func """

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)

    for state in session.query(State):
        if 'a' in state.name:
            print(f'{state.id}: {state.name}')

if __name__ == '__main__':
    a_objects()
