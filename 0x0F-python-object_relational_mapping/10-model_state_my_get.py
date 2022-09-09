#!/usr/bin/python3
"""
prints the State object with the name passed as argument from the database hbtn_0e_6_usa
takes 4 arguments: mysql username, mysql password, database name and state name to search (SQL injection free)
"""

import sys

from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import false
from model_state import Base, State
from sqlalchemy import create_engine


def my_get():
    """ defining func """

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)

    state_name = sys.argv[4]
    found = False

    for state in session.query(State):
            if state.name == state_name:
                print(f'{state.id}')
                found = True
                break
    if found is False:
        print("Not found")

if __name__ == '__main__':
    my_get()
