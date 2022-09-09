#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
takes 3 arguments: mysql username, mysql password and database name
"""

import sys

from sqlalchemy.orm.session import Session
from model_state import Base, State
from sqlalchemy import create_engine


def add_state():
    """ defining func """

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)

    state = State(name='Louisiana')
    session.add(state)
    session.commit()

    print(state.id)

if __name__ == '__main__':
    add_state()
