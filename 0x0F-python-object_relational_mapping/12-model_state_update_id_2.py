#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
takes 3 arguments: mysql username, mysql password and database name
Change the name of the State where id = 2 to New Mexico
"""

import sys

from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import false
from model_state import Base, State
from sqlalchemy import create_engine


def update_state():
    """ define func """

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)

    found = False

    for state in session.query(State):
        if state.id == 2:
            state.name = 'New Mexico'
            session.commit()
            found = True
            break


if __name__ == '__main__':
    update_state()
