#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""


from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """lists all State objects from the database hbtn_0e_6_usa"""
    lh = "localhost"
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.format(
            u, p, lh, d))
    result = engine.execute("select * from {} ORDER BY states.id".format(
            "states"))

    for row in result:
        print("{}: {}".format(row[0], row[1]))
