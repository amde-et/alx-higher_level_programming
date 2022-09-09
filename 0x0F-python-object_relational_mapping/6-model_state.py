#!/usr/bin/python3
"""
using the module SQLAlchemy
connect to a MySQL server running on localhost at port 3306
"""

import sys

from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                                       sys.argv[2], sys.argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)
